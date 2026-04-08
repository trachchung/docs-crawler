# System Design Interview Guide: Crypto Payment Systems

This guide prepares you to design a crypto payment system from scratch in an interview setting. It draws from real-world patterns observed across Mesh Connect, NodeRails, Payram, and TrySpeed.

---

## Part 1: If You're Asked "Design a Crypto Payment System"

### Step 1: Clarify Requirements (2-3 minutes)

Ask these questions before designing:

1. **Who are the users?** Merchants accepting crypto, or consumers paying with crypto, or both?
2. **Custody model?** Do we hold funds (custodial), use escrow (non-custodial), or let merchants self-host?
3. **Which blockchains?** EVM-only? Bitcoin? Lightning Network? Multi-chain?
4. **Payment types?** One-time only, or also recurring/subscriptions?
5. **Settlement speed?** Instant (Lightning), or can we have a lockup period (escrow)?
6. **Scale?** Transactions per second, number of merchants, geographic distribution?
7. **Compliance?** KYC/KYB requirements? Travel Rule? Jurisdiction restrictions?

### Step 2: High-Level Architecture (5 minutes)

Draw the core components:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│ Merchant API  │────▶│ Payment      │────▶│ Blockchain       │
│ (REST)        │     │ Orchestrator │     │ Monitor          │
└──────┬───────┘     └──────┬───────┘     └──────┬───────────┘
       │                    │                     │
       ▼                    ▼                     ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────────┐
│ Webhook       │     │ Checkout UI  │     │ Wallet Service   │
│ Dispatcher    │     │ (Hosted)     │     │ (HD Derivation)  │
└──────────────┘     └──────────────┘     └──────────────────┘
```

**Key components to mention:**
- **API Gateway**: REST API for merchants (authentication, rate limiting, versioning)
- **Payment Orchestrator**: State machine for payment lifecycle
- **Blockchain Monitor**: Listens to RPC nodes for incoming transactions, tracks confirmations
- **Wallet Service**: HD wallet derivation for customer deposit addresses (explain BIP-32/44)
- **Webhook Dispatcher**: At-least-once delivery with HMAC signing and retry
- **Hosted Checkout**: Payment page with QR codes, amount display, TTL countdown

### Step 3: Deep Dive into Key Components (15-20 minutes)

Pick 2-3 areas to go deep based on interviewer interest:

---

## Part 2: Deep Dive Topics

### Topic A: Payment State Machine

**Draw this state machine and explain each transition:**

```
CREATED
  │
  ▼
PENDING (awaiting blockchain confirmation)
  │
  ├──▶ CONFIRMED (N confirmations reached)
  │       │
  │       ├──▶ SETTLED (funds in merchant wallet)
  │       │
  │       ├──▶ REFUNDED (merchant-initiated)
  │       │
  │       └──▶ DISPUTED (if escrow model)
  │                ├──▶ DISPUTE_WON (merchant keeps funds)
  │                └──▶ DISPUTE_LOST (funds returned to customer)
  │
  ├──▶ EXPIRED (TTL elapsed, no payment received)
  │
  └──▶ CANCELLED (merchant cancelled)
```

**Key design decisions to discuss:**
- When should we fulfill the order? At CONFIRMED, not SETTLED (NodeRails pattern)
- How many confirmations? BTC: 6, ETH: 12, Lightning: instant (Payram's approach)
- What about partial payments? Track cumulative received vs. required (TrySpeed pattern)
- What about overpayments? Explicit OVER_FILLED state (Payram pattern)

### Topic B: Webhook Reliability

**Design a reliable webhook system:**

```
Payment Event → Event Queue (Kafka/SQS) → Webhook Worker → Merchant Endpoint
                                              │
                                              ├── Success (200 OK) → Done
                                              │
                                              └── Failure → Retry Queue
                                                    │
                                                    ├── Exponential backoff
                                                    ├── Max retries (e.g., 10)
                                                    └── Dead letter queue
```

**Key patterns from the 4 systems:**
- **HMAC signing**: All 4 systems sign webhooks. Use `HMAC-SHA256(secret, raw_body)`. NodeRails adds a timestamp header for replay protection.
- **Idempotency**: Mesh sends `EventId` (business event, use for dedup) and `Id` (delivery attempt, changes on retry). Consumer must dedup on `EventId`.
- **Response SLA**: Mesh requires <200ms response, retries otherwise. This prevents slow consumers from blocking the queue.
- **Raw body verification**: The HMAC is over raw bytes, not parsed JSON. Middleware that parses the body before verification breaks the signature (NodeRails explicitly warns about this).

### Topic C: Address Generation at Scale

**HD Wallet Derivation (Payram pattern):**

```
Master Seed
  │
  ▼
Master Extended Public Key (xPub)
  │
  ├── m/44'/60'/0'/0/0  →  Customer A's ETH address
  ├── m/44'/60'/0'/0/1  →  Customer B's ETH address
  ├── m/44'/60'/0'/0/2  →  Customer C's ETH address
  └── ... (unlimited, deterministic)
```

**Key points:**
- xPub can generate addresses without the private key being online
- Addresses are permanent per customer (no re-auth needed for repeat payments)
- Blockchain Family abstraction: same address works across EVM chains (ETH, Base, Polygon)
- Non-EVM chains (Bitcoin, Tron) need separate derivation paths

### Topic D: Exchange Rate Management

**The volatility problem:**
- Customer sees $100, exchange rate = 1 BTC = $50,000, so 0.002 BTC
- While customer fumbles with wallet, BTC drops to $49,000
- 0.002 BTC is now worth $98 — merchant loses $2

**Solutions from the 4 systems:**
- **TTL-based rate lock** (TrySpeed): Lock rate for 600 seconds. Auto-refresh on expiry.
- **Stablecoin preference**: NodeRails + Payram focus on USDC/USDT to avoid volatility entirely.
- **SmartFunding conversion** (Mesh): Convert at execution time using the exchange's real-time rate.

### Topic E: Fund Consolidation (The "Thousand Wallets" Problem)

**The problem**: If you have 10,000 customers, you have 10,000 deposit addresses, each with a small balance. How do you consolidate?

**Three approaches from the 4 systems:**

1. **Smart Contract Sweep (Payram)**: Deploy a sweep contract that can pull from multiple addresses in one transaction. Triggers: amount threshold, address count, or time elapsed. Hot wallet pays gas.

2. **Smart Contract Escrow (NodeRails)**: Funds go to a shared escrow contract, not individual addresses. No consolidation needed — escrow releases directly to merchant.

3. **Custodial Pooling (TrySpeed)**: Speed receives all Lightning payments at their node. No address-level fragmentation — it's all in Speed's balance.

### Topic F: Multi-Chain Architecture

**How to support multiple blockchains:**

```
┌─────────────────────────────────────────┐
│ Unified Payment API                      │
│  POST /payments { chain, token, amount } │
└────────────────┬────────────────────────┘
                 │
    ┌────────────┼────────────┬────────────┐
    ▼            ▼            ▼            ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│ EVM    │ │ Bitcoin │ │ Tron   │ │ Solana │
│ Adapter│ │ Adapter │ │ Adapter│ │ Adapter│
│        │ │         │ │        │ │        │
│ • RPC  │ │ • UTXO  │ │ • RPC  │ │ • RPC  │
│ • ERC20│ │ • BIP32 │ │ • TRC20│ │ • SPL  │
│ • Permit│ │ • No SC │ │ • SC   │ │ • Token│
└────────┘ └─────────┘ └────────┘ └────────┘
```

**Key design decisions:**
- **Chain families** (Payram): Group chains that share address space. Reduces complexity.
- **Token identification**: `SYMBOL-chainId` format (NodeRails) ensures USDC-on-Base vs. USDC-on-Ethereum are distinct.
- **Bitcoin is always special**: No smart contracts, UTXO model, separate mobile signing flow (Payram). Every multi-chain system treats Bitcoin as a special case.

### Topic G: Custody Models (Critical Interview Topic)

| Model | Example | Trust | Regulatory | Settlement |
|-------|---------|-------|-----------|------------|
| **Relay/Broker** | Mesh Connect | Mesh never touches funds | Minimal (no custody) | Instant |
| **Non-custodial Escrow** | NodeRails | Smart contract holds | Minimal (code is law) | After timelock |
| **Self-custodial** | Payram | Merchant controls everything | Merchant's responsibility | After sweep |
| **Custodial** | TrySpeed | Platform holds funds | Maximum (money transmitter) | Instant (internal) |

**What to say in interview**: "The custody model is the most important architectural decision. It determines regulatory requirements, trust assumptions, settlement speed, and failure modes. Let me walk through four approaches..."

---

## Part 3: Common Interview Questions & How to Answer

### Q: "How would you handle a payment where the user sends less than the required amount?"

**Answer using Payram + TrySpeed patterns:**
- Track cumulative received amount vs. required amount
- States: `PARTIALLY_FILLED` (Payram) or keep session `active` (TrySpeed)
- Options: (a) wait for more funds, (b) allow merchant to accept partial, (c) refund
- Lightning doesn't support partial payments (BOLT11 invoices are exact-amount)
- On-chain supports partial payments naturally

### Q: "How would you design recurring crypto payments?"

**Answer using NodeRails pattern:**
- Initial checkout captures wallet authorization (ERC-20 allowance or EIP-2612 permit)
- Store authorization: `permitSignature`, `permitDeadline`, `approvedAllowance`
- At each billing cycle: auto-generate invoice, auto-pull using stored authorization
- Retry logic for failed captures: `captureRetryCount` / `maxCaptureRetries`
- Grace period before marking subscription as past-due
- Key challenge: allowance exhaustion (need to prompt customer to re-authorize)

### Q: "How would you secure private keys?"

**Answer using Payram's SmartSweep pattern:**
- Don't keep private keys on the server at all
- Deploy smart contracts that hard-code the destination (cold wallet)
- After deployment, take the key offline
- Fund movement happens via contract calls, not key operations
- Hot wallet (gas station) only holds native tokens for gas fees — minimal risk
- AES-256 encryption for any keys that must be stored

### Q: "How would you design the webhook system?"

**Answer combining all 4 systems' patterns:**
1. **Sign all payloads**: HMAC-SHA256 with per-endpoint secret. Include timestamp for replay protection.
2. **Idempotency**: Include a business-event ID (not delivery-attempt ID) for consumer dedup.
3. **At-least-once delivery**: Retry on non-2xx responses with exponential backoff.
4. **Response SLA**: Enforce timeout (e.g., 200ms). Slow consumers don't block the queue.
5. **Dead letter queue**: After max retries, store for manual inspection.
6. **Polling fallback**: Provide a `GET /transfers` endpoint for reconciliation when webhooks fail.
7. **Raw body verification**: Compute HMAC over raw bytes, not parsed JSON.

### Q: "What's your approach to multi-tenancy?"

**Answer using all 4 patterns:**
- **Sub-client hierarchy** (Mesh): Platform → Merchant → Sub-merchant. Best for PSPs.
- **App-scoped** (NodeRails): Each merchant has multiple Apps with isolated keys/webhooks. Best for multi-product companies.
- **Project-based** (Payram): Shared infrastructure, isolated API keys and branding. Best for multi-brand merchants.
- **Account-level** (TrySpeed): Simple 1:1 mapping. Best for single-brand merchants.

Key principle: "Tenancy boundaries should align with isolation requirements. If tenants need separate billing, they need separate accounts. If they only need separate branding, projects/apps suffice."

### Q: "How would you handle exchange rate volatility?"

**Answer combining TrySpeed + Mesh patterns:**
- Lock the exchange rate for a TTL window (TrySpeed: 600s for fiat, 1 year for crypto)
- Auto-regenerate the invoice with a fresh rate when TTL expires
- For stablecoins (USDC/USDT), TTL can be very long — no volatility concern
- Alternative: use SmartFunding (Mesh) to convert at execution time
- Design decision: who bears the rate risk during TTL? The merchant (if rate drops) or the customer (if rate rises)?

### Q: "Design a payment system that works even when some components fail."

**Answer using Mesh's graceful degradation:**
- Primary path: automated exchange integration (highest conversion)
- Fallback 1: QR code with manual deposit + blockchain monitoring (works without exchange integration)
- Fallback 2: Static deposit address with manual reconciliation (works without blockchain monitoring)
- Dual notification: client-side callback + server-side webhook (handles browser close)
- Polling API as webhook fallback (handles webhook delivery failures)

---

## Part 4: Architecture Trade-off Cheat Sheet

Use this to quickly reason about trade-offs:

| Decision | Option A | Option B | When to pick A | When to pick B |
|----------|----------|----------|---------------|---------------|
| Custody | Non-custodial (escrow) | Custodial | Regulatory concerns, trust issues | Speed of settlement, simplicity |
| Deployment | SaaS (hosted) | Self-hosted | Ease of operation | Data sovereignty, control |
| Settlement | Instant (Lightning) | Escrow + timelock | Microtransactions, trust | Dispute protection needed |
| State machine | Simple (3-4 states) | Rich (8+ states) | MVP, simple payments | Subscriptions, disputes, refunds |
| Multi-chain | Chain families | Per-chain isolation | EVM chains with shared addresses | Heterogeneous chains |
| Webhook delivery | At-least-once + idempotency | Exactly-once (with coordination) | Simpler, more reliable | Lower consumer complexity |
| Rate management | TTL lock + auto-refresh | Real-time conversion | Checkout flows | Instant payments |
| Key management | Smart contract sweep (keyless) | Server-side key with HSM | Security-first | Simplicity, legacy systems |
| Multi-tenancy | Hierarchy (platform → client → sub-client) | Flat accounts | PSP/marketplace model | Direct merchant model |
| API design | Stripe-like (familiar) | Domain-specific | Developer adoption speed | Unique domain requirements |

---

## Part 5: Numbers to Know

| Metric | Value | Source |
|--------|-------|--------|
| Bitcoin confirmation target | 6 blocks (~60 min) | Payram |
| Ethereum confirmation target | 12 blocks (~3 min) | Payram |
| Lightning settlement | Instant (milliseconds) | TrySpeed |
| Escrow timelock default | 7 days (604,800 seconds) | NodeRails |
| Dispute window default | 1 day (86,400 seconds) | NodeRails |
| Exchange rate TTL (fiat) | 600 seconds (10 min) | TrySpeed |
| Webhook response SLA | <200ms | Mesh Connect |
| Manual deposit attribution window | 15 minutes | Mesh Connect |
| Payram payout auto-approve limit | $500 per transaction | Payram |
| Payram hourly payout limit | $5,000 | Payram |
| Payram daily payout limit | $10,000 | Payram |
| TrySpeed max transfer destinations | 25 per checkout session | TrySpeed |
| TrySpeed cashback fee cap | 100 SATS | TrySpeed |
| NodeRails pagination max | 100 per page | NodeRails |
| Mesh Connect supported integrations | 300+ exchanges/wallets | Mesh Connect |
| NodeRails production chains | 6 EVM chains | NodeRails |
| Payram supported chains | 5 (ETH, Base, Polygon, Tron, BTC) | Payram |
| TrySpeed supported networks | 5 (LN, BTC, ETH, Tron, Solana) | TrySpeed |

---

## Part 6: Vocabulary for Interview

| Term | Definition | Which System |
|------|-----------|-------------|
| **PaymentIntent** | The universal payment tracking object | NodeRails |
| **linkToken** | Self-contained session config token | Mesh Connect |
| **SmartFunding** | Auto-conversion of user's holdings to merchant's preferred token | Mesh Connect |
| **SmartSweep** | Keyless fund consolidation via smart contracts | Payram |
| **MMT (Mesh Managed Tokens)** | Encrypted credential vault for exchange auth tokens | Mesh Connect |
| **BOLT11** | Lightning Network invoice standard (encoded as QR) | TrySpeed |
| **LNURL** | Pull-payment protocol layered on Lightning | TrySpeed |
| **HTLC** | Hash Time-Locked Contract (Lightning routing mechanism) | TrySpeed |
| **HD Wallet** | Hierarchical Deterministic wallet (BIP-32/44) | Payram |
| **EIP-2612** | ERC-20 permit standard (gasless approval) | NodeRails |
| **EIP-7702** | Account abstraction for EOAs | NodeRails |
| **Blockchain Family** | Group of chains sharing address space | Payram |
| **Cold Wallet** | Secure offline settlement address | Payram |
| **Hot Wallet / Gas Station** | Online wallet holding native tokens for gas fees | Payram |
| **Sweep Contract** | Smart contract that consolidates funds to cold wallet | Payram |
| **Timelock** | Escrow hold period before funds release | NodeRails |
| **Dispute Window** | Period during which customer can contest a captured payment | NodeRails |
| **Broker Adapter** | Integration layer translating unified API to exchange-specific protocol | Mesh Connect |
| **TTL (Time to Live)** | Duration an exchange rate quote is valid | TrySpeed |
