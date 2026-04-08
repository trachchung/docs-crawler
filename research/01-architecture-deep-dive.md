# Architecture Deep Dive: 4 Crypto Payment Systems

## Table of Contents
- [Mesh Connect](#mesh-connect)
- [NodeRails](#noderails)
- [Payram](#payram)
- [TrySpeed](#tryspeed)

---

## Mesh Connect

### What It Is
A global crypto payments **aggregation network** that connects 300+ exchanges, wallets, and payment providers. Mesh doesn't process payments directly — it brokers connections between the user's existing crypto accounts and the merchant's destination address.

### Architectural Model: Backend-for-Frontend (BFF) + Drop-in iframe UI

```
┌─────────────────────────────────────────────────────────────────────┐
│ Merchant Backend                                                     │
│  POST /api/v1/linktoken  (X-Client-Id + X-Client-Secret)           │
│  → Returns: linkToken (base64-encoded session config)                │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ linkToken
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Merchant Frontend (SDK: Web/iOS/Android/React Native/Flutter)        │
│  meshLink.openLink(linkToken) → renders iframe modal                 │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Mesh Link UI (Mesh-hosted iframe)                                    │
│  • Integration catalog (300+ brokers)                                │
│  • Credential validation + MFA handling                              │
│  • Asset selection, amount entry, transfer preview                   │
│  • SmartFunding (auto-conversion of user holdings)                   │
│  • Wallet deep-links for DeFi                                        │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
┌──────────────────────┐  ┌──────────────────────────────┐
│ CEX Path              │  │ DeFi/Self-Custody Path        │
│ Mesh calls exchange   │  │ Deep-link to wallet app       │
│ API server-to-server  │  │ User signs & broadcasts       │
│ with user's authToken │  │ on-chain                      │
└──────────────────────┘  └──────────────────────────────┘
              │                         │
              ▼                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Dual Notification                                                    │
│  • Client-side: onTransferFinished callback (immediate UX)           │
│  • Server-side: Webhook POST (source of truth, HMAC-SHA256 signed)   │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Architecture Decisions

1. **linkToken as Self-Contained Session Config**: The token is a base64-encoded URL carrying the full session configuration. Mesh's backend can verify it without database lookups (the token IS the state). This enables stateless horizontal scaling.

2. **Token Broker Pattern**: Mesh maintains adapter implementations for 300+ integrations (Binance, Coinbase, Robinhood, MetaMask, Phantom, etc.). Each adapter translates Mesh's unified API into exchange-specific protocols (OAuth, username/password, wallet deep-links). The `brokerType` enum is the dispatch key.

3. **Two Distinct Transfer Paths**:
   - **CEX (Centralized Exchange)**: Mesh proxies the transfer server-to-server using the user's auth token. User never leaves the modal.
   - **DeFi (Self-Custody Wallets)**: Mesh constructs the transaction and deep-links to the wallet app for user signature. This path REQUIRES the SDK — it cannot be done via API alone.

4. **Mesh Managed Tokens (MMT)**: Encrypted storage of user exchange auth tokens. Returns a `tokenId` to the merchant as an opaque handle. Tokens are scoped per client + per user + per permission level (read vs. write). Mesh handles refresh cycles transparently.

5. **Intelligent Provider Filtering**: At session creation, Mesh runs a server-side pipeline that filters available integrations based on: token/network compatibility, IP geolocation, Travel Rule jurisdiction, VASP ID presence, platform type, and broker geography restrictions. Compliance rules update without merchant code changes.

6. **Manual Deposit Fallback**: Every session offers a QR code fallback. If user's exchange isn't supported, they see a scannable address. Mesh monitors the blockchain for 15 minutes to attribute incoming deposits.

### API Surface

| Endpoint | Purpose |
|----------|---------|
| `integration-api.meshconnect.com` | Core payment/transfer API |
| `sandbox-integration-api.meshconnect.com` | Sandbox environment |
| `admin-api.meshconnect.com` | Account management, sub-clients |

**Auth**: `X-Client-Id` + `X-Client-Secret` headers (static API keys, no OAuth).

**Response Envelope**:
```json
{
  "content": {},
  "status": "ok | serverFailure | permissionDenied | badRequest | ...",
  "message": "...",
  "errorHash": "8d443794",  // Bugsnag grouping
  "teamCode": "P4"          // Internal on-call routing
}
```

### Data Models

- **linkToken**: Session config token (single-use for Paylinks, reusable otherwise)
- **authToken / tokenId**: User's exchange credentials (MMT-managed)
- **Transfer**: The core payment entity with states: `pending` → `succeeded` | `failed`
- **Sub-Client**: Multi-tenant entity for PSPs white-labeling Mesh

### Multi-Tenancy: Three-Level Hierarchy
```
Mesh (platform)
  └── Client (merchant, identified by clientId)
       └── Sub-Client (merchant's downstream customer, identified by subClientId)
```
Each sub-client has its own legal name, branding, and callback URLs. Token isolation ensures cross-merchant token leakage is impossible.

---

## NodeRails

### What It Is
A "Stripe for Crypto" payment processing platform using **smart contract escrow** as the trust layer. Funds flow: customer wallet → escrow contract → merchant wallet. NodeRails never holds funds.

### Architectural Model: Hosted Checkout + Smart Contract Escrow

```
┌─────────────────────────────────────────────────────────────────────┐
│ Merchant Server                                                      │
│  @noderails/sdk  →  POST api.noderails.com/checkout-sessions        │
│  Auth: x-api-key: nr_live_sk_...                                     │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ session.id
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Hosted Checkout (pay.noderails.com/checkout/{session.id})            │
│  • Customer selects chain + token                                    │
│  • Customer connects wallet (MetaMask, etc.)                         │
│  • Customer signs authorization (ERC-20 permit or native approve)    │
└──────────────────────────┬──────────────────────────────────────────┘
                           │ signed authorization
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Smart Contract Escrow (on-chain)                                     │
│  • Funds pulled from customer wallet                                 │
│  • Locked in escrow for dispute window (default: 7 days)             │
│  • Released to merchant wallet after timelock                        │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
┌────────────────────┐    ┌──────────────────────────────┐
│ Dispute Path        │    │ Settlement Path               │
│ Customer disputes   │    │ No dispute raised              │
│ → DISPUTE_RESOLVED  │    │ → Timelock expires             │
│ → DISPUTE_LOST      │    │ → Funds → merchant wallet      │
│   (funds returned)  │    │ → Status: SETTLED              │
└────────────────────┘    └──────────────────────────────┘
```

### Key Architecture Decisions

1. **Non-Custodial Escrow**: The critical design — NodeRails never holds funds. Smart contracts act as trustless intermediaries. This eliminates custodial risk and regulatory burden.

2. **PaymentIntent as Universal Tracking Object**: Every payment, regardless of entry point (checkout session, invoice, subscription, payment link), creates a PaymentIntent. This is the single source of truth. Same pattern as Stripe.

3. **App-Scoped Multi-Tenancy**: Each merchant can create multiple Apps. Each App gets isolated API keys, webhook endpoints, and chain/token configuration. This is the tenancy unit.

4. **Three-Domain Architecture**:
   - `api.noderails.com` — Business logic, resource management
   - `pay.noderails.com` — Customer-facing hosted checkout
   - `merchant.noderails.com` — Merchant dashboard

5. **EVM-Only by Design**: All 6 production chains are EVM-compatible. Authorization mechanisms (ERC-20 permit, EIP-2612, EIP-7702) are EVM-specific. This is a hard architectural constraint of the escrow model.

6. **Timelock + Dispute Window**: Configurable per payment intent. Default: 7-day timelock, 1-day dispute window. Funds are secured in escrow at `CAPTURED` — this is the fulfill signal for merchants.

### Payment Intent State Machine

```
CREATED → AUTHORIZED → CAPTURED → SETTLED (happy path)
                    ↘ CANCELLED
                              ↘ REFUNDED
                              ↘ DISPUTED → DISPUTE_RESOLVED | DISPUTE_LOST
```

- **AUTHORIZED**: Customer signed approval (funds still in wallet)
- **CAPTURED**: Funds pulled into escrow — **this is the merchant's action signal**
- **SETTLED**: Funds released to merchant wallet after timelock (final state)

### API Design

**Key Format**: `nr_<env>_<type>_<random>` (e.g., `nr_live_sk_abc123`)
- `sk` = secret (server-side only)
- `pk` = public (client-side safe)

**REST Pattern**: Standard CRUD + state transition actions (`POST /resource/:id/expire`)

**Pagination**: `page` + `pageSize` (1-100), response includes `{ total, page, pageSize, totalPages }`

**Token Identification**: `SYMBOL-chainId` format (e.g., `USDC-8453` for USDC on Base)

### Subscription Model (Recurring Crypto Payments)

```
ProductPlan → ProductPlanPrice → Subscription
  (what)       (how much/often)    (who + which price)
```

- Initial checkout captures wallet authorization (ERC-20 allowance or permit)
- Authorization stored and reused for automatic renewals
- Each billing cycle auto-generates an invoice and auto-captures
- Retry logic: `captureRetryCount` / `maxCaptureRetries` for failed renewals
- Deferred cancellation: `cancelAtPeriodEnd: true` preserves access until period end

### SDK Architecture

```typescript
const noderails = new NodeRails({
  appId: 'your-app-id',
  apiKey: 'nr_live_sk_...',
  timeout: 30000,
  apiVersion: '2026-03-07',  // pin to specific version
});
```

- Zero runtime dependencies (native `fetch`)
- Cross-runtime: Node.js 18+, Deno, Bun
- Auto-unwraps `{ success: true, data: ... }` envelope
- Rich `retrieve()` vs. lightweight `list()` (deliberate performance optimization)
- Static webhook verification: `NodeRails.webhooks.constructEvent(...)`

---

## Payram

### What It Is
A **fully self-hosted** crypto payment processor. The merchant runs everything on their own infrastructure — no third-party custody, no mandatory KYC, no middlemen.

### Architectural Model: Monolith-in-a-Container + Smart Contract Sweeps

```
┌─────────────────────────────────────────────────────────────────────┐
│ Docker Container (payramapp/payram:latest)                           │
│  ┌─────────────┐ ┌──────────────┐ ┌────────────────────────────┐   │
│  │ Frontend     │ │ Backend API  │ │ Blockchain Orchestration    │   │
│  │ React SPA    │ │ REST Server  │ │ Engine                      │   │
│  │ Ports 80/443 │ │ Ports 8080/  │ │ • RPC node monitoring       │   │
│  │              │ │ 8443         │ │ • Deposit detection          │   │
│  └─────────────┘ └──────────────┘ │ • Confirmation tracking      │   │
│                                    │ • SmartSweep triggers         │   │
│                                    └────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │ PostgreSQL (embedded for dev, external for production)        │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────┐
│ EVM Chains    │ │ Tron         │ │ Bitcoin      │
│ ETH/Base/     │ │ TRX/USDT    │ │ BTC          │
│ Polygon       │ │              │ │              │
│               │ │              │ │              │
│ Smart Contract│ │ Smart Contract│ │ Mobile App   │
│ Sweep         │ │ Sweep        │ │ Sweep        │
└──────┬───────┘ └──────┬───────┘ └──────┬───────┘
       │                │                │
       ▼                ▼                ▼
┌─────────────────────────────────────────────────────────────────────┐
│ Cold Wallet (merchant's secure settlement address)                   │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Architecture Decisions

1. **Self-Hosted Monolith**: Single Docker image ships frontend, backend, blockchain engine, and optional embedded Postgres. Operational simplicity over microservices complexity. Tradeoff: limits horizontal scaling of individual components.

2. **Keyless Sweep Design (SmartSweep)**: The flagship innovation. Smart contracts are deployed from the master account but hard-coded to only send funds to the cold wallet. After deployment, the master account private key doesn't need to remain on the server. Fund movements happen via contract calls, not private key operations.

3. **Wallet Architecture (4 Wallet Types)**:
   - **Master Account**: HD wallet root — all customer deposit addresses are derived from it. Deploys sweep contracts.
   - **Deposit Wallets**: Customer-facing addresses derived via HD derivation. Permanent per customer per blockchain family.
   - **Hot Wallet (Gas Station)**: EOA holding native tokens (ETH/TRX) to pay gas fees for sweep transactions.
   - **Cold Wallet**: Final settlement address. Never exposed to customers.

4. **Blockchain Family Abstraction**: Related chains are grouped: `ETH_Family` = Ethereum + Base + Polygon (same address format). One master account covers all networks in a family. Customers get one address per family, not per network.

5. **AES-256 Encryption**: Single `AES_KEY` encrypts all sensitive data in the database. Losing this key means losing access to decrypted data. Must be preserved across container updates.

### SmartSweep Fund Consolidation

The core differentiator. Three configurable triggers (any can fire):

| Trigger | Description |
|---------|-------------|
| Amount | Individual wallet balance OR batch total reaches USD threshold |
| Address Count | N deposit addresses have received funds |
| Time | Configured time period has elapsed |

**EVM/Tron Flow**: Hot wallet provides gas → sweep contract pulls funds from matched deposit wallets → sends to cold wallet.

**Bitcoin Flow** (different — no smart contracts): Mobile app signs batched sweep transactions. Merchant approves from app's Pending tab.

### Payment Flow

```
POST /api/v1/payment { customerEmail, customerID, amountInUSD }
  → Returns { reference_id, url (hosted payment page) }
  → Customer selects coin/network
  → GET /api/v1/blockchain-currency/reference/{ref} (available options)
  → POST /api/v1/deposit-address/reference/{ref} { blockchain_code }
     (assigns permanent address if first time)
  → Customer sends crypto to address
  → Blockchain engine detects deposit
  → Webhook: "Payment Detected on Network"
  → After N confirmations: paymentState → FILLED
  → Webhook: "Payment Confirmed"
```

**Payment States**: `OPEN` → `FILLED` | `PARTIALLY_FILLED` | `OVER_FILLED` | `CANCELLED`

### Multi-Brand Model

Project-based multi-tenancy within a single instance:
- Organization → multiple Projects (brands/storefronts)
- Each project: own API keys, webhook endpoints, branding, URLs
- Wallet balances unified at organization level
- RBAC roles: Owner > Admin > Project Lead > Project Manager > Project Ops

---

## TrySpeed

### What It Is
A Bitcoin and stablecoin payment processor specializing in **Lightning Network** payments. Speed operates the Lightning node on behalf of merchants — "Lightning-as-a-Service."

### Architectural Model: Custodial Lightning Node + Layered Payment Abstractions

```
┌─────────────────────────────────────────────────────────────────────┐
│ Payment Instrument Hierarchy (each layer adds lifecycle management)  │
│                                                                      │
│  Payment Link (reusable, spawns new checkout sessions per visit)     │
│       │                                                              │
│       ▼                                                              │
│  Checkout Link (one-time use, wraps a single checkout session)       │
│       │                                                              │
│       ▼                                                              │
│  Checkout Session (auto-renews invoices on TTL expiry,               │
│       │            tracks partial payments, owns full lifecycle)      │
│       ▼                                                              │
│  Payment (raw: single-use, one TTL, no auto-renewal)                 │
│       │                                                              │
│       ▼                                                              │
│  Payment Payload (LN invoice / on-chain address / ETH address)       │
└─────────────────────────────────────────────────────────────────────┘
```

```
┌─────────────────────────────────────────────────────────────────────┐
│ Speed Platform                                                       │
│                                                                      │
│  ┌──────────────────┐   ┌──────────────────────────────────────┐    │
│  │ REST API          │   │ Lightning Node                        │    │
│  │ (Stripe-like)     │   │ • Always online (both parties must be)│    │
│  │                   │   │ • Channel liquidity management        │    │
│  │ POST /checkout-   │   │ • Route finding                       │    │
│  │   sessions        │   │ • BOLT11 invoice generation           │    │
│  │ POST /payments    │   │ • LNURL for withdrawals/cashback      │    │
│  └──────────────────┘   └──────────────────────────────────────┘    │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │ Multi-Network Payment Processing                              │    │
│  │  • Bitcoin Lightning (default, instant)                       │    │
│  │  • Bitcoin On-chain (for large transactions)                  │    │
│  │  • Ethereum (USDT, USDC)                                      │    │
│  │  • Tron (USDT)                                                │    │
│  │  • Solana (USDT, USDC)                                        │    │
│  └──────────────────────────────────────────────────────────────┘    │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐    │
│  │ Branding + White-Label                                        │    │
│  │  • Custom checkout domain (pay.merchant.com)                  │    │
│  │  • Custom email domain                                        │    │
│  │  • Custom payment address domain                              │    │
│  │  • Logo, colors, fonts per merchant                           │    │
│  └──────────────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────┘
```

### Key Architecture Decisions

1. **Custodial Lightning Node Operator**: Speed runs the Lightning node. This is a deliberate centralization trade-off that solves: node uptime requirements, channel liquidity management, route discovery, and invoice generation. Merchants never touch Lightning infrastructure.

2. **Layered Payment Abstraction**: Raw Payment → Checkout Session → Checkout Link → Payment Link. Each layer adds lifecycle management above the one below. Raw payments are for full-control integrations; payment links are no-code.

3. **TTL + Exchange Rate Lock**: For fiat-denominated sessions, the exchange rate is locked for 600 seconds (10 min). After TTL expiry, the checkout session auto-regenerates the invoice with a fresh rate. Raw payments don't auto-regenerate — merchant handles expiry.

4. **LNURL as Withdrawal Primitive**: Cashback and withdrawals use LNURL (pull-payment protocol). Speed pre-approves the withdrawal, then the customer's wallet initiates the pull. Elegant because it lets Speed gate withdrawals before funds move.

5. **Serial Account-Level Debits**: Simultaneous debit operations (cashback, transfers) on the same account fail immediately — they don't queue. This prevents double-spend but is a scalability constraint for high-volume merchants.

6. **Marketplace Split Payments**: Checkout sessions support `transfers` array with up to 25 destination Speed accounts and percentage-based splits. This enables marketplace platforms to auto-distribute at payment time.

### Payment States

**Payment**: `unpaid` → `paid` (any funds received) | `expired` | `cancelled`
**Checkout Session**: `active` → `paid` (full amount) | `deactivated`
**Checkout Link**: `active` → `paid` (one-time) | `deactivated`
**Payment Link**: `active` → `deactivated` (never "paid" — reusable)

### Cashback System

- Campaign-level object (one cashback → many links/sessions)
- Types: fixed SATS amount or percentage of payment
- Delivered via LNURL withdrawal (Lightning only, even if original payment was on-chain)
- Debited from merchant balance at claim time, not at creation
- Atomic reversal on failure (balance + fees restored)

### Plugin Ecosystem

Four e-commerce platforms with identical integration pattern:
- **WooCommerce**: OAuth-style "Connect Speed" flow + restricted keys
- **Magento 2**: Manual API key configuration
- **OpenCart**: Manual API key configuration
- **PrestaShop**: Manual API key configuration

All plugins handle partial payments by preserving cart state until full payment received.
