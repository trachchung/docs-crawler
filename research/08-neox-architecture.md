# NeoX Architecture Deep Dive

Source: https://docs.neox.vn/docs — scraped into `projects/neox/`.

NeoX is a Vietnamese payment intermediary (licensed by the State Bank of Vietnam, operated by NeoPay JSC, est. 2021). Unlike the four crypto systems in `01-architecture-deep-dive.md`, NeoX is a **fiat, bank-rail fintech platform** covering wallet, gateway, collections, disbursement, and virtual cards. This doc maps its surface so we can compare apples-to-apples and interview the dev who built it.

---

## 1. Platform Map

| Subsystem | Purpose | Actors |
|-----------|---------|--------|
| **NeoX App** | Consumer e-wallet + merchant mobile | End-users, merchants |
| **Payment Gateway** | Hosted checkout for online merchants | Merchant web/app → NeoX |
| **Collections** | Virtual-account receivables + settlement | Billers (Grab-like), utility/COD |
| **Disbursement** | Bulk bank payouts with FX | Marketplaces, payroll |
| **Virtual Card** | Issuance + policy-driven controls | Enterprises, BaaS-style merchants |
| **Merchant Portal** | Web dashboard / ops console | Merchant admins |

Bank rails: top-10 Vietnam banks + NAPAS domestically; Cybersource + Mastercard Payment Gateway internationally (Visa, MC, JCB, Amex). Licensed for payment gateway, e-wallet, collections, and disbursement.

---

## 2. Payment Gateway

### Integration Models
1. **Hosted Checkout** (default): HTTPS redirect to `https://neox-domain/paygate/neopay` with signed params.
2. **Direct API** + **Tokenization**: card capture on merchant side for repeat billing.
3. **SDKs**: Web, iOS, Android, React Native, plugin extensions.

### Core Request (create payment)
```
GET/POST /paygate/neopay
  neo_MerchantCode, neo_Amount (VND int), neo_MerchantTxnID (unique, ≤36 chars),
  neo_OrderID, neo_OrderInfo (≤256), neo_PaymentMethod ∈ {WALLET,ATM,CC,QR,BANK_TRANSFER},
  neo_ReturnURL, neo_ExpiresIn (default 86400s),
  neo_ExtData = { orderData.payItems: [{orderId, desc, price, extraInfo}] },
  neo_SecureHash
```

### Signature Scheme
```
secureHash = SHA256( sort_alpha(params) joined "|"  +  "|"  +  SecretKey )
             → hex, 64 chars, UPPER
```
Same scheme for REFUND (except `neo_RequestID` excluded from hash) and IPN verification.

### Operations
| Command | Endpoint | Notes |
|---------|----------|-------|
| `QUERY_PT` | POST `/api/v1/paygate/neopay` | returns SUCCESS/FAILED/PROCESSING + `refundedAmount` |
| `REFUND`   | POST `/api/v1/paygate/neopay` | `neo_Receiver` = Base64(JSON{accountName,accountNumber,swiftCode}) for QR refunds |
| `CANCEL`   | POST `/api/v1/paygate/neopay` | valid only within 5 min of payment |
| `QUERY_DR` | GET | merchant-side existence check, returns `neo_DRExists = Y|N` |

### IPN (Instant Payment Notification)
- Server-to-server POST to merchant's registered URL with full `neo_*` payload + `neo_SecureHash`.
- Merchant ACK required: `{"respcode":0,"respmsg":"received"}`. Non-zero → NeoX retries.
- `neo_TransAmount` and `neo_ExtData` are carried but **not included in hash** — a real gotcha.

### Error Taxonomy (Gateway)
`0` success · `18` customer cancelled · `19` duplicate txn ID · `30` integration not approved · `31–37,40–43` field/ExtData validation · `51` credit-bill-holding not registered · `99` processing · `-1` expired.

### Reconciliation & Settlement
- Nightly batch: all successful payments + refunds from previous day.
- Merchant-configured T-day period + start time (e.g. T=3, start 10-Oct → txns 10–13 Oct settled on 13th).
- Settlement flips reconciliation record to `Paid`; merchant wallet is credited.

---

## 3. Disbursement

### Auth
OAuth 2.0 `client_credentials` at `POST /v2/auth/oauth2/token` with `scope=disbursement`. Bearer token with `expires_in`.

### APIs
| Endpoint | Purpose |
|----------|---------|
| `GET /v2/dib/bank/accountInquiry` | name-check a `(accountNumber, swiftCode, accountType)` |
| `POST /v2/dib/disbursementRequests` | batch payout; `transactions[]` ≤ 200 per request |
| `POST /v2/dib/exchange/{src}-{dst}` | FX (only `dst=VND` supported currently) |
| `GET /v2/dib/disbursementTransactions` | by `requestId` or `requestTransId` |

Each `TransactionItem` carries `amount`, `bankSwiftCode`, `bankAccountNumber`, `bankAccountName`, `description` (restricted charset), `requestTransId`, and optional `srcAmount` / `srcCurrency` / `fxRate` for multi-currency.

### Webhooks
Three types, all Base64(SHA256(sort_alpha(JSON) + SecretKey)):
- **BALANCE**: current float balance with timestamp.
- **TRANSACTION**: per-item result with `status ∈ {SUCCESS, FAILED, PROCESSING}`.
- **EXCHANGE**: async FX result (quote is sync → result is async).

### Error Codes
Logic codes: `2009` insufficient balance · `2014` amount exceeded · `2051` >200 txns/request · `2052` policy violation · `2055/2056` duplicate request/txn · `2063` invalid currency · `3400–3403` account/card invalid · `3700–3715` bank-side failures. HTTP: 400/401/403/404/413/422/429/500/502–505/514.

---

## 4. Collections (Virtual Account)

The heart of NeoX's B2B2C story — Grab-driver-style disbursement of bank transfers through per-entity virtual accounts.

### Lifecycle
1. **Create VA**: `POST /v2/col/requests` with rich KYB profile (`profileData`: `merchantName`, `legalRepresentative`, `nationalIdNumber`, `businessLicenseNumber`, etc.) + document filenames uploaded separately (SFTP or API).
2. **Query transaction**: `GET /v2/col/transactions/:transId` returns two independent state machines:
   - **reconcileStatus**: `WAITING_UPLOAD → UPLOADED → APPROVED|REJECTED → RECONCILED → SETTLED`
   - **payoutStatus**: `READY → PROCESSING → REJECTED|SUCCESS`
3. **Refund**: `POST /v2/col/refundRequests` (bank info required for QR/bank-transfer refunds).
4. **Withdraw**: `POST /v2/col/withdrawRequests`; bank list from `GET /v2/col/withdrawBanks`.

### Webhook Filtering
Events: `ACCOUNT`, `TRANSACTION`, `TRANSACTION_STATUS`, `REFUND`, `PAYOUT`. Merchants can filter by `serviceInformation.code` and/or `groupId` — conjunctive ($and) — enabling multi-tenant fan-out (e.g., one webhook endpoint per service or driver group).

### Concrete webhook payload
```json
{
  "transId":"FT246560944209","type":"TRANSACTION","merchantCode":"UFLIYL",
  "transDate":"2023-10-10T07:06:37.436Z",
  "virtualAccountId":"NEO0001675","accountName":"HIEP HOANG","amount":20000,
  "serviceInformation":{"code":"GRAB","groupId":"DRIVER","desc":"..."},
  "debitorInformation":{"bankName":"Simulator","bankAccountNumber":"...", ...},
  "secureHash":"<Base64(SHA256(alpha_sorted_values + secret))>"
}
```

---

## 5. Virtual Card

### Hybrid Encryption for Card Data (the only crypto in the system)
Sensitive PAN/CVV/expiry is never plaintext on NeoX:
```
cardEncryptedData = { encryptedKey, encryptedData }  // both Base64

1) RSA-OAEP(SHA256) decrypt `encryptedKey` with merchant private key
   → 60-byte buffer  [AES_KEY(32) | IV(12) | AUTH_TAG(16)]
2) AES-256-GCM decrypt `encryptedData` with (AES_KEY, IV, AUTH_TAG)
   → JSON { pan, cvv, expiry, ... }
```
Merchant must pre-register an RSA public key on the portal (error `2226` if missing).

### Policies
First-class resource: spending limits (per-txn / daily / monthly), MCC restrictions, auto-activation, lifetime. Versioning is marked DEVELOPING. Cards reference a policy; policies are activate/deactivate-able.

### Lifecycle
`Created → Active → Locked | Expired | Deactivated`. APIs for create, get details, get encrypted info, activate/deactivate, reassign user.

---

## 6. NeoX App + eKYC

- Consumer: cash-in / cash-out / P2P transfer / merchant payment.
- **eKYC gates wallet activation**: biometric + AI-driven ID verification, 100% remote.
- Individual onboarding: email, phone, address, ID front/back, portrait.
- Business onboarding: + tax code + business license (≤20 images).

---

## 7. Cross-Cutting

### Authentication Landscape (three very different schemes co-exist)
| Channel | Scheme |
|---------|--------|
| Merchant Portal | Email + password |
| Payment Gateway | Merchant Code + Secret Key, SHA256 signing |
| Disbursement / Collections / Virtual Card | OAuth 2.0 client-credentials → Bearer |

### Idempotency
Merchant-generated unique IDs are the contract: `neo_MerchantTxnID`, `requestId`, `requestTransId`, `virtualAccountRequestId`. NeoX rejects duplicates (codes `19`, `2055`, `2056`, `2203`).

### Error Taxonomy (unified across APIs)
- `0` success · `99` processing/failure
- `20xx` validation / merchant / request
- `21xx`–`22xx` VA / policy / card lifecycle
- `30xx`–`37xx` bank/account integration
- HTTP layer on top.

### Settlement Model (single pattern, re-used everywhere)
Nightly reconciliation batch → configurable T-day window → "Paid" flip → credit merchant wallet / collection account / debit float. For collections, settlement additionally requires document upload → approval before `RECONCILED → SETTLED`.

---

## 8. How NeoX Compares to the 4 Crypto Systems

| Axis | NeoX | Mesh / NodeRails / Payram / TrySpeed |
|------|------|---------------------------------------|
| Rails | Bank + NAPAS + Cybersource | Public blockchains + Lightning |
| Custody | Custodial by license (merchant wallet, VA float) | Ranges: relay → escrow → self-hosted → custodial |
| Consistency boundary | Nightly batch reconciliation + T-day window | On-chain confirmations + webhook |
| Signature | SHA256 hex / Base64 over alpha-sorted params | HMAC-SHA256 over raw body |
| Idempotency | Merchant-generated IDs, dup-reject | Idempotency-Key header / EventId dedup |
| State machines | Separated `reconcileStatus` + `payoutStatus` (Collections) — closest thing to NodeRails' "captured vs settled" split | PaymentIntent / session state machines |
| Multi-tenancy | `serviceInformation.code` + `groupId` webhook filter | Sub-clients / Apps / Projects |
| Encryption | RSA-OAEP + AES-256-GCM hybrid for card data | Smart-contract escrow, HD derivation |
| Edge cases | Partial refund amount carried in IPN but not hashed; 5-min cancel window; 200-txn disbursement cap | Partial/over-filled, reorgs, TTL/rate drift |

**Key insight (mirroring Janesh's feedback):** NeoX independently arrived at the same **"capture vs settle" separation** that NodeRails expresses on-chain — here it's `reconcileStatus` vs `payoutStatus`, and a transaction can be confirmed-received but not yet settled, with document approval as the gating step. That decoupling is the universal pattern in production payments, regardless of rails.
