# Design Patterns & System Design Concepts

This document extracts the design patterns from all 4 payment systems, organized by system design concept. Use these as talking points in your interview — each pattern comes with a real-world implementation example.

---

## 1. Authentication & Authorization Patterns

### API Key with Typed Prefixes (NodeRails, TrySpeed)
```
nr_live_sk_abc123   →  environment=live, type=secret
nr_test_pk_xyz789   →  environment=test, type=public
wsec_xxxxxxxxx      →  webhook signing secret
pi_l7sygu3xYQukjvzS →  payment intent resource
```
**Why it matters**: Resource type is identifiable from the ID alone. Debugging, logging, and access control all benefit. This is a Stripe innovation adopted industry-wide.

**Interview angle**: "How would you design your ID scheme?" → Typed prefixes with environment namespacing prevent cross-environment mistakes and make logs instantly readable.

### Dual API Key Model (All 4 systems)
Every system separates server-side secrets from client-safe keys:

| System | Server Key | Client Key |
|--------|-----------|------------|
| Mesh | X-Client-Secret | X-Client-Id (in linkToken) |
| NodeRails | `nr_*_sk_*` | `nr_*_pk_*` |
| Payram | API-Key (server) | N/A |
| TrySpeed | Secret key | Publishable key |

**Interview angle**: "How do you handle authentication for both server and client components?" → Split key architecture. Server keys never leave the backend; client keys are safe for frontend embedding with limited permissions.

### Session Token as Self-Contained Config (Mesh Connect)
The `linkToken` carries the entire session configuration (destination addresses, amounts, allowed tokens, fees) in a base64-encoded payload. The Mesh backend can verify it without database lookups.

**Interview angle**: "How would you design a stateless session system?" → JWT-like approach where the token IS the state. Enables horizontal scaling without session stickiness. Trade-off: token size grows with configuration complexity.

### OAuth-Style Permission Grants (TrySpeed WooCommerce)
The "Connect Speed" flow: merchant authenticates → Speed presents permission scope list → restricted keys generated on approval. Keys are scoped to the granted permissions.

**Interview angle**: "How do you handle third-party integrations?" → OAuth-style flows are more secure than manual API key copy-paste because keys are scoped, auditable, and rotatable.

---

## 2. Payment State Machines

### Linear State Machine (Payram)
```
OPEN → FILLED | PARTIALLY_FILLED | OVER_FILLED | CANCELLED
```
Simplest model. No intermediate states. Customer pushes funds, system detects and confirms.

### Rich State Machine with Escrow (NodeRails)
```
CREATED → AUTHORIZED → CAPTURED → SETTLED
                    ↘ CANCELLED
                              ↘ REFUNDED
                              ↘ DISPUTED → DISPUTE_RESOLVED | DISPUTE_LOST
```
Most complex. Mirrors real-world financial flows with authorization, capture, and dispute resolution.

### Layered State Machines (TrySpeed)
Four concurrent state machines, each at a different abstraction level:
```
Payment:          unpaid → paid | expired | cancelled
Checkout Session: active → paid | deactivated
Checkout Link:    active → paid | deactivated  (one-time)
Payment Link:     active → deactivated         (never "paid")
```

**Interview angle**: "Design a payment state machine." → Start with the simplest (Payram), then layer on complexity. Discuss: What happens with partial payments? Disputes? Expiry? Each state must have clear entry/exit conditions and exactly one owner responsible for transitions.

### Key State Machine Design Principles (from all 4)
1. **Terminal states must be truly terminal**: `SETTLED`, `CANCELLED`, `DISPUTE_LOST` have no outgoing transitions
2. **Every transition must be auditable**: Webhook fired, timestamp recorded
3. **Distinguish "action signal" from "final state"**: NodeRails captures at `CAPTURED` (action signal) but settles at `SETTLED` (final state). Merchants fulfill on action signal, not final state.
4. **Partial payments need explicit states**: Payram's `PARTIALLY_FILLED` vs. TrySpeed's "track cumulative received" are two different approaches.

---

## 3. Webhook & Event System Design

### HMAC Signature Verification (All 4)
```
Mesh:      Base64(HMAC-SHA256(secret, payload))  →  X-Mesh-Signature-256
NodeRails: HMAC(secret, raw_body + timestamp)     →  x-noderails-signature + x-noderails-timestamp
TrySpeed:  HMAC with wsec_ signing secret
Payram:    API-Key header match (simplest)
```

**Critical implementation detail (NodeRails)**: Webhook endpoint MUST receive raw body (`express.raw()`), not parsed JSON. HMAC is computed over the raw bytes. This is a common interview pitfall.

### Idempotency Keys for Webhook Delivery (Mesh Connect)
Mesh sends two IDs per webhook:
- `EventId`: Business event identifier (idempotency key)
- `Id`: Delivery attempt identifier (changes on retry)

Merchants must dedup on `EventId`, not `Id`. If they dedup on `Id`, retries are processed as new events.

**Interview angle**: "How do you handle webhook reliability?" → At-least-once delivery + idempotency keys. The consumer must be idempotent. Discuss: retry backoff, dead letter queues, delivery SLAs (Mesh requires <200ms response).

### Dual Notification Pattern (Mesh Connect)
Two parallel channels:
1. **Client-side**: `onTransferFinished` callback fires immediately (for UX)
2. **Server-side**: Webhook POST fires asynchronously (source of truth)

**Why both**: User might close the browser before the transfer completes. The webhook still reaches the server. Client-side events are for UX feedback only; never use them for order fulfillment.

**Interview angle**: "What if the user closes the browser mid-payment?" → Dual notification solves this. The webhook is the source of truth. Client-side events are optional UX optimizations.

### Event Catalog Design (NodeRails vs. Payram)
NodeRails: 12+ granular events (`payment.authorized`, `payment.captured`, `payment.settled`, `invoice.sent`, `subscription.renewed`, etc.)
Payram: 3 events (`Payment Page Rendered`, `Payment Detected`, `Payment Confirmed`)

**Trade-off**: More events = more integration flexibility but more complexity. Fewer events = simpler but less visibility.

---

## 4. Fund Flow Patterns

### Broker/Relay Model (Mesh Connect)
```
User's Exchange Account → (Mesh orchestrates) → Merchant's Address
```
Mesh never holds funds. It calls exchange APIs or deep-links wallets to initiate transfers. Pure orchestration layer.

### Smart Contract Escrow (NodeRails)
```
Customer Wallet → Escrow Contract → (timelock) → Merchant Wallet
                                  → (dispute)  → Customer Wallet
```
Trustless custody. The escrow contract is the neutral third party. Neither NodeRails nor the merchant controls the funds during the lockup period.

### Push-to-Address + Sweep (Payram)
```
Customer → Deposit Address → (SmartSweep) → Cold Wallet
                                ↑
                          Hot Wallet (gas)
```
Customer pushes directly. No smart contract escrow — the deposit address is merchant-controlled (HD-derived from master account). SmartSweep consolidates.

### Custodial Receive + Account Balance (TrySpeed)
```
Customer → Speed's Lightning Node → Merchant's Speed Account Balance
                                  → (Transfer/Withdrawal) → External Wallet
```
Speed receives and holds. Merchant withdraws or transfers internally.

**Interview angle**: "What are the trust models for payment processing?" → Walk through all four: relay (Mesh), escrow (NodeRails), self-custody (Payram), custodial (TrySpeed). Each has different regulatory, security, and UX implications.

---

## 5. Multi-Tenancy Patterns

### Sub-Client Hierarchy (Mesh Connect)
```
Platform (Mesh) → Client (merchant) → Sub-Client (merchant's customer)
```
Designed for PSPs (Payment Service Providers) who white-label Mesh. Token isolation ensures cross-merchant/cross-sub-client data separation.

### App-Scoped Tenancy (NodeRails)
```
Merchant Account → App 1 (keys, webhooks, chains)
                → App 2 (separate keys, webhooks, chains)
```
Each App is a fully isolated namespace within the merchant's account.

### Project-Based Tenancy (Payram)
```
Organization → Project 1 (brand A, API keys, webhooks)
             → Project 2 (brand B, separate API keys)
             → (shared wallet balances)
```
Projects share wallet infrastructure but have isolated API keys and branding.

### Account-Level Tenancy (TrySpeed)
```
Speed Platform → Merchant Account (keys, branding, domains)
```
One account = one merchant. Multi-brand achieved via custom domain configuration.

**Interview angle**: "How would you design multi-tenancy?" → Start with the isolation requirements: Do tenants share infrastructure? Do they need separate billing? Separate data? Mesh's 3-level hierarchy handles the PSP use case; NodeRails' App model handles the multi-product merchant.

---

## 6. Exchange Rate & TTL Management

### Rate Lock with Auto-Refresh (TrySpeed)
- Fiat sessions: 600-second TTL (10 min), auto-regenerate invoice with fresh rate on expiry
- Crypto sessions: 1-year TTL (no rate conversion needed)
- Checkout sessions handle TTL transparently; raw payments don't auto-refresh

### Amount Locking at linkToken Creation (Mesh Connect)
Amount is fixed when the `linkToken` is generated. If the token is used much later, the exchange rate may have drifted. SmartFunding handles conversion at execution time.

**Interview angle**: "How do you handle exchange rate volatility?" → TTL-based rate locks. Too short = bad UX (customer sees price change mid-checkout). Too long = merchant bears exchange rate risk. TrySpeed's 10-minute default is a reasonable balance.

---

## 7. HD Wallet Derivation (Payram)

### Hierarchical Deterministic (HD) Wallet Pattern
```
Master Account (xPub)
  ├── Deposit Address 1 (customer A, ETH_Family)
  ├── Deposit Address 2 (customer B, ETH_Family)
  ├── Deposit Address 3 (customer C, ETH_Family)
  └── ... (unlimited, deterministic, no key exposure)
```

From a single master key, generate unlimited unique customer addresses. Each address is permanent and collision-resistant. The master account's xPub is sufficient for address generation — the private key doesn't need to be online.

**Interview angle**: "How do you generate unique payment addresses at scale?" → HD wallets (BIP-32/44). Explain: deterministic derivation from a single seed, no database lookup needed for address generation, addresses are permanent per customer.

---

## 8. Smart Contract as Authorization Boundary (Payram)

### Keyless Sweep Pattern
```
Deploy Phase: Master Account Private Key → Deploy Sweep Contract (cold wallet hard-coded)
              (key can be taken offline after deployment)

Sweep Phase:  Hot Wallet → Calls Sweep Contract → Funds move to Cold Wallet
              (no private key needed — contract enforces destination)
```

The sweep contract acts as a programmable authorization gate. It only sends to the pre-specified cold wallet. This eliminates the need for server-side private key exposure.

**Interview angle**: "How do you secure fund movement in a payment system?" → Smart contracts as authorization boundaries. The contract enforces the invariant (funds can only go to cold wallet), removing the human/server from the trust model.

---

## 9. Layered Abstraction Pattern (TrySpeed)

### Payment Instrument Hierarchy
```
Raw Payment      — Full control, no lifecycle management
  ↑
Checkout Session — Adds: TTL auto-renewal, partial payment tracking, customer data collection
  ↑
Checkout Link    — Adds: No-code creation, one-time use, hosted page
  ↑
Payment Link     — Adds: Reusability (spawns new session per visit)
```

Each layer adds exactly one concern on top of the layer below. Developers choose their entry point based on how much lifecycle management they want to handle themselves.

**Interview angle**: "How do you design an API for both simple and complex use cases?" → Layered abstractions. Raw primitives for advanced users, high-level wrappers for simple use cases. Each layer composes the one below. Same principle as Stripe's Payment Intent → Checkout Session → Payment Link hierarchy.

---

## 10. Graceful Degradation Pattern (Mesh Connect)

### Fallback Chain
```
Primary: User authenticates with exchange → Transfer via exchange API
  ↓ (exchange not supported or auth fails)
Fallback: QR code / manual deposit → Blockchain monitoring → Attribution
  ↓ (15-minute window for blockchain attribution)
Final: Payment page with address for manual transfer
```

Every payment session has a built-in fallback. Even if the automated path fails, the customer can still complete the payment manually.

**Interview angle**: "How do you handle partial system failures?" → Graceful degradation. Design primary and fallback paths. Mesh's approach ensures 100% of customers can complete payment, even when specific integrations fail.

---

## 11. Marketplace Split Payment Pattern (TrySpeed)

### Percentage-Based Auto-Distribution
```json
{
  "transfers": [
    { "destination": "acct_platform", "percentage": 10 },
    { "destination": "acct_seller_1", "percentage": 60 },
    { "destination": "acct_seller_2", "percentage": 30 }
  ]
}
```
Up to 25 destinations. Percentages must sum to ≤100%. Split happens atomically at payment time.

**Interview angle**: "How would you design payment splitting for a marketplace?" → Define splits at checkout creation time, execute atomically. Discuss: what if a destination account is closed? What about refunds on split payments? What's the max fan-out?

---

## 12. Subscription Authorization Storage (NodeRails)

### Wallet Authorization for Recurring Pulls
```
First Payment: Customer signs ERC-20 permit or native approval
  → authorizationMethod, permitSignature, permitDeadline, permitNonce stored
  → approvedAllowance recorded

Subsequent Payments: System auto-pulls using stored authorization
  → No customer interaction needed
  → captureRetryCount tracks failed attempts
  → pastDueSince tracks dunning state
```

This is the crypto equivalent of "card on file." The authorization is an on-chain permission (ERC-20 allowance or EIP-2612 permit) stored by NodeRails and reused for each billing cycle.

**Interview angle**: "How do recurring payments work in crypto?" → Unlike cards where a network handles recurring pulls, crypto requires explicit on-chain authorization. NodeRails stores the permit/allowance and pulls against it. Discuss: What happens when the allowance is exhausted? What about token approvals on different chains?

---

## 13. Blockchain Family Abstraction (Payram)

### Chain Grouping for Address Reuse
```
ETH_Family: Ethereum + Base + Polygon  →  Same address across all three
TRX_Family: Tron                       →  Separate address format
BTC_Family: Bitcoin                    →  Separate address format
```

Chains that share address space are grouped into families. One master account, one deposit address, one sweep contract covers the entire family.

**Interview angle**: "How do you handle multi-chain support?" → Chain families are a pragmatic grouping. EVM chains share address space, so one address works across Ethereum/Base/Polygon. Non-EVM chains (Tron, Bitcoin) need separate address derivation. This reduces customer confusion and simplifies wallet management.

---

## 14. Concurrency Control Patterns

### Serialized Account Debits (TrySpeed)
```
Thread 1: Cashback withdrawal processing → account locked
Thread 2: Transfer request → IMMEDIATE FAIL (not queued)
```
Fail-fast, not queue-and-wait. Prevents double-spend at the cost of availability.

### Payout Approval Workflow (Payram)
```
Non-admin: OTP verification → pending-approval → Admin approves → processing
Admin: Auto-approve up to $500 → hourly limit $5,000 → daily limit $10,000
```
Human-in-the-loop for high-value operations. Multi-step approval chain.

**Interview angle**: "How do you prevent double-spending?" → TrySpeed uses pessimistic locking (fail-fast). NodeRails uses escrow contracts (smart contract enforces single-spend). Payram uses approval workflows. Each approach trades off availability for safety differently.
