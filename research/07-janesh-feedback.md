# Janesh's Feedback — Answered

---

## 1. Go deeper into real payment flows

**NodeRails (most complete flow):**
User hits checkout → wallet connects → signs ERC-20 permit → funds pull into escrow contract → `payment.captured` webhook fires (merchant fulfills here) → 7-day timelock → no dispute → escrow releases to merchant wallet → `payment.settled`. Two separate signals: capture = "safe to ship," settled = "money in your bank."

**Payram (self-hosted flow):**
Merchant calls `POST /payment` → gets `reference_id` + hosted URL → customer picks coin/network → system assigns a permanent HD-derived deposit address → customer pushes crypto → blockchain engine detects via RPC polling → fires "Payment Detected" webhook → waits for N confirmations (6 for BTC, 12 for ETH) → `FILLED` → fires "Payment Confirmed" webhook. Settlement is a separate SmartSweep cycle: deposit wallets → sweep contract → cold wallet.

**Key insight:** Payment confirmation and settlement are always decoupled. Confirmation = "we saw the money." Settlement = "money is where it needs to be." Every production system separates these because they happen at different times and can fail independently.

---

## 2. Transaction mapping & state management

**NodeRails' PaymentIntent is the canonical answer.** Every entry point (checkout session, invoice, subscription, payment link) eventually creates one PaymentIntent. That's your source of truth. States:

```
CREATED → AUTHORIZED → CAPTURED → SETTLED
                    ↘ CANCELLED
                              ↘ REFUNDED
                              ↘ DISPUTED → DISPUTE_RESOLVED | DISPUTE_LOST
```

Consistency rule: state transitions are forward-only, one owner per transition. `AUTHORIZED` → `CAPTURED` is triggered by the escrow contract (not the API server). `CAPTURED` → `SETTLED` is triggered by timelock expiry (not a human). No state can be skipped.

**Payram handles partial states explicitly:** `PARTIALLY_FILLED` and `OVER_FILLED` are first-class states, not edge cases. If a customer sends 80% of the amount, the payment sits at `PARTIALLY_FILLED` — it doesn't fail, it doesn't retry, it waits. The merchant decides what to do.

**TrySpeed layers state machines:** The Payment object goes `paid` on any funds received. The Checkout Session only goes `paid` when cumulative received >= total. Two objects, two state machines, one payment. The session is the consistency boundary, not the individual payment.

---

## 3. Idempotency and reliability patterns

**Three real implementations:**

**Mesh Connect** — Client-supplied `transactionId` in `transferOptions`. This is the merchant's idempotency key. Mesh also sends `EventId` (business event) vs `Id` (delivery attempt) on webhooks. You dedup on `EventId`. If you dedup on `Id`, retries create duplicates.

**NodeRails** — SDK-level idempotency key on any mutation:
```typescript
noderails.paymentIntents.create(params, { idempotencyKey: 'order_456' })
```
Same key = same response, no second resource created. Server stores the response keyed by `(apiKey, idempotencyKey)` and replays it.

**TrySpeed** — Fail-fast on concurrent debits. If a cashback withdrawal is processing, a simultaneous transfer on the same account rejects immediately (not queued). Failed withdrawals atomically reverse: balance + network fees restored. No partial states.

**The pattern:** Idempotency keys on writes. Dedup keys on webhook consumption. Atomic reversal on failure. That's it.

---

## 4. Blockchain-specific edge cases

**Confirmations:** Not all confirmations are equal. Payram requires 6 for BTC (~60 min), 12 for ETH (~3 min). TrySpeed's Lightning is instant (no confirmations — off-chain). The confirmation count is a probability threshold: "how unlikely is a reorg that would undo this transaction?"

**Reorgs:** A blockchain reorg means confirmed blocks get replaced by a longer chain. Your "confirmed" transaction disappears. Defense: don't mark a payment as final until N confirmations deep. N is chain-specific. For Bitcoin, 6 blocks means an attacker needs >50% of hash power sustained for an hour — economically infeasible for most payment amounts.

**Delayed transactions:** Payram's blockchain engine polls RPC nodes. If the node is behind or down, deposits aren't detected. The "Last Block Processed" metric in the dashboard tells you if the listener is stalled. Fallback: `GET /payment-status/{ref}` polling endpoint so merchants aren't solely dependent on webhooks.

**Manual deposit attribution (Mesh):** 15-minute window to match an incoming on-chain transfer to a session. Criteria: correct token + correct network + correct address + within window. If the customer sends after the window closes, the funds arrive at the address but aren't attributed to a payment. This is a real operational edge case — Mesh explicitly doesn't guarantee attribution outside the window.

**TTL and rate drift (TrySpeed):** Fiat-denominated sessions lock the exchange rate for 600 seconds. After expiry, the checkout session auto-generates a new invoice with a fresh rate. If the customer paid the old invoice amount after TTL expiry, they've underpaid relative to the new rate. The session tracks cumulative received vs. current required amount.

---

## 5. System design thinking: source of truth, data flow, failure ownership

**Source of truth by system:**

| System | Source of truth | Why |
|--------|----------------|-----|
| NodeRails | Smart contract (on-chain) | Escrow state is immutable and verifiable by anyone |
| Payram | Blockchain + PostgreSQL | Blockchain for fund existence, DB for payment-to-customer mapping |
| TrySpeed | Speed's internal ledger | Custodial model — their balance DB is authoritative |
| Mesh | Exchange API response + webhook | Mesh relays — the exchange is the actual source of truth |

**Failure ownership:**
- Blockchain monitor goes down → payments aren't detected → **the platform owns this** (Payram mitigates with "Last Block Processed" metric)
- Webhook delivery fails → merchant doesn't know about payment → **the platform owns retry**, merchant owns polling fallback
- Customer sends wrong amount → **nobody "owns" this** — it's a state (`PARTIALLY_FILLED`) that requires merchant decision
- Escrow contract has a bug → **catastrophic, unrecoverable** — this is why NodeRails' escrow is the highest-risk component and must be audited

**Consistency guarantees:**
- NodeRails: eventual consistency between API state and on-chain state. The API reads from its DB; the DB is updated by an on-chain event listener. Lag between on-chain event and API reflection is the consistency window.
- Payram: same pattern — blockchain engine writes to Postgres, API reads from Postgres. If the engine crashes mid-write, you have a payment on-chain that's not in the DB. Recovery: re-scan blockchain from last processed block.

---

## 6. Practical implementation, not just concepts

**Smallest useful system you could build:**
1. HD wallet derivation (generate deposit addresses from a single seed — BIP-32 library)
2. RPC poller (call `eth_getBlockByNumber` in a loop, scan for transfers to your addresses)
3. State machine (OPEN → DETECTED → CONFIRMED, persisted in Postgres)
4. Webhook dispatcher (POST to merchant URL with HMAC signature, retry on failure)

That's Payram in 4 components. No smart contracts, no Lightning, no SDK. Just: generate address → watch blockchain → update state → notify merchant.

**What makes it production-grade:**
- Confirmation threshold before marking CONFIRMED (not just 1 block)
- Idempotent webhook consumption (EventId-based dedup)
- Block re-scanning on restart (pick up from last processed block, not current)
- Amount tolerance (handle PARTIALLY_FILLED, OVER_FILLED, not just exact match)

---

## 7. Reconciliation and settlement

**Reconciliation = "does my internal state match external reality?"**

Two sources to reconcile:
1. **Internal DB** — what we think happened (payment records, states, amounts)
2. **Blockchain** — what actually happened (transactions, balances, confirmations)

**Payram's approach:** The blockchain engine continuously scans blocks via RPC. Each deposit wallet's on-chain balance is compared against the expected balance from internal records. Discrepancy = reconciliation alert. The SmartSweep dashboard shows swept vs. un-swept balances per address — this IS the reconciliation view.

**NodeRails' approach:** The escrow contract is the reconciliation layer. Internal state says "CAPTURED" → verify escrow contract holds the funds. Internal state says "SETTLED" → verify escrow released to merchant address. Any mismatch between API state and on-chain state is a critical alert.

**Mesh's approach:** `GET /v1/transfers/managed/mesh` returns historical transfers for audit. Compare this against webhook events received. Missing webhook = delivery failure (retry or manual reconciliation). The `TransactionId` (merchant's ID) links Mesh records to the merchant's internal order system.

**Settlement flow (Payram, most explicit):**
```
Deposit detected → Confirmations reached → FILLED in DB
                                              ↓
SmartSweep trigger fires → Sweep contract executes → Funds in cold wallet
                                              ↓
Merchant withdraws from cold wallet → Converts to fiat (external) → Done
```

Three separate events: confirmation, sweep, and withdrawal. Each can fail independently. Each needs its own reconciliation check. The system is only fully settled when funds are in the cold wallet — everything before that is "confirmed but not settled."
