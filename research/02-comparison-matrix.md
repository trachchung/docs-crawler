# Comparison Matrix: 4 Crypto Payment Systems

## Quick Identity Card

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **One-liner** | Crypto payments aggregation network (300+ integrations) | "Stripe for Crypto" with smart contract escrow | Self-hosted crypto payment processor | Bitcoin Lightning payment processor |
| **Core Innovation** | Universal broker adapter across exchanges & wallets | Non-custodial escrow with dispute resolution | Keyless SmartSweep fund consolidation | Lightning-as-a-Service with layered abstractions |
| **Custody Model** | Non-custodial (broker/relay) | Non-custodial (smart contract escrow) | Self-custodial (merchant hosts everything) | Custodial (Speed operates LN node) |
| **Target Customer** | Platforms embedding crypto payments, PSPs | Web3 developers, SaaS with crypto billing | Privacy-focused merchants, self-sovereignty advocates | Merchants wanting Bitcoin/Lightning payments |
| **Stripe Analogy** | Plaid for Crypto | Stripe Direct | Self-hosted Stripe | Stripe for Bitcoin |

---

## Architecture Comparison

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Deployment** | Fully hosted SaaS | Fully hosted SaaS | Self-hosted Docker | Fully hosted SaaS |
| **Core Pattern** | BFF + iframe SDK | Hosted checkout + escrow | Monolith-in-container | Custodial LN node + REST API |
| **Server Components** | Integration API, Admin API, Link UI | API server, Hosted Checkout, Smart Contracts | Frontend, Backend, Blockchain Engine, DB | REST API, Lightning Node, Payment Pages |
| **Database** | Managed by Mesh | Managed by NodeRails | PostgreSQL (merchant-managed) | Managed by Speed |
| **Horizontal Scaling** | Stateless linkToken enables easy scaling | SaaS-managed | Limited (monolith) — requires vertical scaling | SaaS-managed |
| **Multi-tenancy Unit** | Sub-Client (for PSPs) | App (per merchant) | Project (per brand) | Account (per merchant) |

---

## Blockchain & Network Support

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Supported Chains** | 24+ networks via 300+ broker integrations | 6 EVM chains (Ethereum, Base, Polygon, Arbitrum, Optimism, Monad) | 5 chains (Ethereum, Base, Polygon, Tron, Bitcoin) | 5 networks (BTC Lightning, BTC On-chain, Ethereum, Tron, Solana) |
| **Chain Type** | Multi-chain via broker abstraction | EVM-only (hard constraint) | EVM + Tron + Bitcoin | Bitcoin-native + EVM + Tron + Solana |
| **Token Support** | 200+ tokens across all integrated exchanges | ERC-20 tokens on supported EVM chains | ETH, USDT, USDC, BTC, TRX, POL, cbBTC | BTC, USDT, USDC |
| **Chain Addition Speed** | Depends on broker support | Claims 24-hour EVM chain addition | Requires platform update | Platform-managed |
| **Lightning Network** | No | No | No | Yes (core feature) |
| **Cross-chain** | Yes (17 source networks, bridging to Base/ETH) | No (single-chain per transaction) | No (single-chain per transaction) | No |

---

## Payment Flow Comparison

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Entry Points** | linkToken → SDK modal, Paylinks | Checkout Session, Payment Intent, Invoice, Payment Link | Payment API → hosted page | Checkout Session, Payment Link, Checkout Link, Raw Payment |
| **Customer UX** | iframe modal overlaying merchant app | Redirect to pay.noderails.com | Redirect to PayRam payment page | Redirect to Speed payment page or embedded Speed.js |
| **Payment Initiation** | User authenticates with their exchange/wallet inside modal | User connects wallet, signs authorization | User sends crypto to assigned deposit address | User scans LN invoice QR or sends to on-chain address |
| **Fund Movement** | Mesh calls exchange API or deep-links wallet | Smart contract pulls funds from wallet to escrow | Customer pushes to deposit address | Customer pushes to Speed's LN node or address |
| **Settlement** | Instant (exchange-to-merchant) | After timelock (default 7 days) | After SmartSweep to cold wallet | Instant (Lightning) or after confirmations (on-chain) |
| **Partial Payments** | Not supported | Not explicitly documented | Supported (PARTIALLY_FILLED state) | Supported (on-chain only, not Lightning) |
| **Returning Users** | Token reuse via MMT (skip login) | Wallet authorization stored for subscriptions | Permanent deposit addresses (no re-auth needed) | N/A (no stored auth) |

---

## Security Model Comparison

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Authentication** | X-Client-Id + X-Client-Secret headers | x-api-key header (nr_live_sk_...) | API-Key header | Publishable + Secret API keys |
| **Key Format** | Opaque strings | `nr_<env>_<type>_<random>` (typed prefix) | Opaque strings | `wsec_` prefix for webhook secrets |
| **Webhook Signing** | HMAC-SHA256, `X-Mesh-Signature-256` header | HMAC, `x-noderails-signature` + timestamp | API-Key header validation | HMAC with `wsec_` signing secret |
| **Webhook IP Allowlist** | Yes (static IP: 20.22.113.37) | Not documented | Recommended | Not documented |
| **Key Rotation** | Not documented | Via dashboard per App | Per project, independent rotation | Per environment |
| **Credential Storage** | MMT (encrypted, client+user scoped) | On-chain authorization (permit/allowance) | AES-256 encrypted in Postgres | N/A (no stored credentials) |
| **MFA** | Handled inside iframe for all integrations | N/A (wallet-based) | OTP for payout approval | N/A |
| **Dispute Resolution** | N/A (instant settlement) | On-chain escrow + timelock + dispute window | N/A (crypto is irreversible) | N/A (crypto is irreversible) |

---

## API Design Comparison

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Style** | REST (POST-heavy, sensitive data in body) | REST (standard CRUD + state transitions) | REST (standard CRUD) | REST (Stripe-like) |
| **Versioning** | `/api/v1/` path prefix | SDK `apiVersion` option (date-based) | Not documented | Not documented |
| **Pagination** | Not documented (returns full datasets) | `page` + `pageSize` (1-100) | Not documented | Not documented |
| **Idempotency** | `transactionId` in transferOptions | SDK idempotency key on any mutation | Not documented | Not documented |
| **Response Envelope** | `{ content, status, message, errorHash, teamCode }` | `{ success: true, data: ..., pagination: ... }` | Standard response | Standard response |
| **Resource ID Format** | GUIDs (TransferId) | UUIDs | UUIDs (reference_id) | Typed prefixes (`pi_`, `acct_`, `wsec_`) |
| **SDK** | Web, iOS, Android, React Native, Flutter | TypeScript (zero deps, cross-runtime) | TypeScript (with retry policies) | Speed.js (embedded checkout) |
| **Public Endpoints** | N/A | 2 factory endpoints (from-link, from-invoice) | N/A | N/A |

---

## Feature Matrix

| Feature | Mesh Connect | NodeRails | Payram | TrySpeed |
|---------|-------------|-----------|--------|----------|
| **One-time Payments** | Yes | Yes | Yes | Yes |
| **Recurring/Subscriptions** | No (no subscription primitive) | Yes (full subscription model) | No (must build at app layer) | No |
| **Invoicing** | No | Yes (DRAFT→OPEN→PAID lifecycle) | No | Yes (mentioned in nav, not detailed) |
| **Payment Links** | Yes (Paylinks, single-use, ~30min expiry) | Yes (via dashboard) | Yes (via dashboard) | Yes (reusable, never expires until deactivated) |
| **Checkout Sessions** | No (uses linkToken sessions) | Yes (Stripe-like) | No | Yes (Stripe-like) |
| **Customer Management** | No (uses userId) | Yes (multi-wallet, billing address) | Yes (customerID + email) | No explicit customer object |
| **Payouts** | No | No (merchant manages) | Yes (with approval workflow) | Yes (transfers between Speed accounts) |
| **Cashback/Rewards** | No | No | No | Yes (LNURL-based) |
| **Fiat Onramp** | No | No | Yes (third-party delegation) | No |
| **SmartFunding/Conversion** | Yes (auto-convert user holdings) | No | No | No |
| **Wallet Verification** | Yes (signed message, Travel Rule) | N/A | N/A | N/A |
| **Portfolio/Balance View** | Yes (aggregated across exchanges) | No | No | No |
| **White-Label** | Sub-client branding | No | Project-based branding | Custom domain (checkout, email, payment address) |
| **E-commerce Plugins** | No | No | No | Yes (WooCommerce, Magento, OpenCart, PrestaShop) |
| **MCP / AI Integration** | No | No | Yes (hosted MCP server + Telegram bot) | No |
| **Mobile SDK** | Yes (iOS, Android, React Native, Flutter) | No (web only) | Mobile app (BTC sweep only) | No |

---

## Webhook Comparison

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Method** | POST | POST | GET | POST |
| **Registration** | Dashboard (1 URL per environment) | Dashboard or API | Dashboard (multiple endpoints) | Dashboard |
| **Events** | Transfer status (pending/succeeded/failed) | payment.*, invoice.*, subscription.* (12+ events) | 3 events (rendered, detected, confirmed) | checkout_session.*, payment_link.*, checkout.link.* |
| **Dedup Key** | EventId (delivery attempt has separate Id) | Event type + resource ID | reference_id | Not documented |
| **Retry** | Yes (on non-200 or >200ms timeout) | Yes (automatic retries) | Not documented | Not documented |
| **Signature** | HMAC-SHA256, base64 encoded | HMAC with timestamp (replay protection) | API-Key header match | HMAC with wsec_ secret |

---

## Scalability & Operational Characteristics

| Dimension | Mesh Connect | NodeRails | Payram | TrySpeed |
|-----------|-------------|-----------|--------|----------|
| **Ops Burden** | Zero (fully managed) | Zero (fully managed) | High (self-host everything) | Zero (fully managed) |
| **Infrastructure** | Mesh manages | NodeRails manages | Merchant manages Docker, DB, SSL, RPC nodes | Speed manages |
| **Blockchain Monitoring** | Mesh monitors for manual deposits | Smart contracts handle | Merchant's blockchain engine monitors RPC nodes | Speed's Lightning node handles |
| **Fee Model** | Not documented in reviewed docs | Not documented | 1-5% on settlement (zero subscription) | Flat 1% transaction fee |
| **Minimum Hardware** | N/A | N/A | 2 CPU, 4GB RAM, 50GB SSD | N/A |
| **Testnet Support** | Sandbox v2 (2 simulated brokers) | 4 test chains (Sepolia variants) | `BLOCKCHAIN_NETWORK_TYPE=testnet` toggle | Test mode API keys |

---

## Best Fit Scenarios

| Scenario | Best Choice | Why |
|----------|------------|-----|
| Platform aggregating multiple exchanges/wallets | **Mesh Connect** | 300+ broker integrations, universal adapter pattern |
| SaaS with recurring crypto billing | **NodeRails** | Only one with subscription + invoice support |
| Maximum privacy/control, no third-party dependency | **Payram** | Self-hosted, self-custodial, no KYC |
| Microtransactions, instant settlement | **TrySpeed** | Lightning Network = instant, near-zero fees |
| Marketplace with split payments | **TrySpeed** | Built-in transfers array (25 destinations, %-based) |
| PSP white-labeling for multiple merchants | **Mesh Connect** | Sub-client multi-tenancy designed for this |
| Enterprise with dispute resolution needs | **NodeRails** | On-chain escrow with configurable dispute windows |
| Merchant wanting plug-and-play e-commerce | **TrySpeed** | 4 e-commerce plugins ready to go |
| Cross-chain/bridge payments | **Mesh Connect** | 17 source networks, bridging support |
| AI-integrated payment analytics | **Payram** | MCP server + Telegram analytics bot |
