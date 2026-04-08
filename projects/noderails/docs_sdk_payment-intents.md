---
url: "https://www.noderails.com/docs/sdk/payment-intents"
title: "Documentation NodeRails"
---

[NodeRailsCRYPTO PAYMENT INFRASTRUCTURE](https://www.noderails.com/)

[Documentation](https://www.noderails.com/docs) [API Reference](https://www.noderails.com/docs/api-reference/checkout-sessions)

[Dashboard](https://merchant.noderails.com/login)

[Documentation](https://www.noderails.com/docs)

Getting Started

[Introduction](https://www.noderails.com/docs) [Quick Start](https://www.noderails.com/docs/getting-started) [Supported Chains & Tokens](https://www.noderails.com/docs/supported-assets)

SDK

[Installation & Config](https://www.noderails.com/docs/sdk) [Checkout Sessions](https://www.noderails.com/docs/sdk/checkout-sessions) [Payment Intents](https://www.noderails.com/docs/sdk/payment-intents) [Invoices](https://www.noderails.com/docs/sdk/invoices) [Subscriptions](https://www.noderails.com/docs/sdk/subscriptions) [Customers](https://www.noderails.com/docs/sdk/customers) [Payment Links](https://www.noderails.com/docs/sdk/payment-links) [Product Plans](https://www.noderails.com/docs/sdk/product-plans) [Webhook Endpoints](https://www.noderails.com/docs/sdk/webhook-endpoints) [Tax Rates](https://www.noderails.com/docs/sdk/tax-rates) [Prices](https://www.noderails.com/docs/sdk/prices) [Error Handling](https://www.noderails.com/docs/errors) [Webhooks](https://www.noderails.com/docs/webhooks)

API Reference

[Checkout Sessions](https://www.noderails.com/docs/api-reference/checkout-sessions) [Payment Intents](https://www.noderails.com/docs/api-reference/payment-intents) [Customers](https://www.noderails.com/docs/api-reference/customers) [Invoices](https://www.noderails.com/docs/api-reference/invoices) [Payment Links](https://www.noderails.com/docs/api-reference/payment-links) [Subscriptions](https://www.noderails.com/docs/api-reference/subscriptions) [Product Plans](https://www.noderails.com/docs/api-reference/product-plans) [Tax Rates](https://www.noderails.com/docs/api-reference/tax-rates) [Webhook Endpoints](https://www.noderails.com/docs/api-reference/webhooks) [Prices](https://www.noderails.com/docs/api-reference/prices)

# Payment Intents

Payment intents are the core payment object. Every checkout session creates a payment intent under the hood when the customer pays. You can also create payment intents directly for more control over the payment flow.

💡

Payment intent lifecycle

A payment intent moves through these states: `CREATED` → `AUTHORIZED` → `CAPTURED` → `SETTLED`. It can also be `CANCELLED` (before capture) or `REFUNDED` (after capture). If a dispute is raised, it moves to `DISPUTED` and then `DISPUTE_RESOLVED` or `DISPUTE_LOST`.

## Create a payment intent

Create payment intenttypescript

Copy

```
const intent = await noderails.paymentIntents.create({
  amount: '100.00',
  currency: 'USD',
  captureMode: 'AUTOMATIC',
  allowedChains: [1, 137, 42161],          // Ethereum, Polygon, Arbitrum
  allowedTokens: ['USDC', 'USDT'],         // Accept USDC and USDT
  externalId: 'order_456',                 // Your internal order ID
  metadata: { plan: 'enterprise' },
});

console.log(intent.id);     // Payment intent ID
console.log(intent.status); // "CREATED"
```

## Retrieve a payment intent

Check a payment intent's status at any time. Useful for polling or verifying the state after receiving a webhook.

Check payment statustypescript

Copy

```
const intent = await noderails.paymentIntents.retrieve('payment-intent-id');

console.log(intent.status);           // Current status
console.log(intent.amount);           // Fiat amount
console.log(intent.cryptoAmount);     // Crypto amount paid
console.log(intent.captureTxHash);    // On-chain capture transaction hash
console.log(intent.authorizationChainId);  // Chain the payment was made on
console.log(intent.authorizationTokenKey); // Token used (e.g., "USDC-8453")
console.log(intent.externalId);       // Your order reference
```

## List payment intents

List and filtertypescript

Copy

```
// List all captured payments
const captured = await noderails.paymentIntents.list({
  status: 'CAPTURED',
  page: 1,
  pageSize: 50,
});

for (const intent of captured.data) {
  console.log(intent.id, intent.amount, intent.cryptoAmount);
}
```

## Cancel a payment intent

Cancel a payment that hasn't been captured yet. This releases the authorized funds back to the customer.

Canceltypescript

Copy

```
const cancelled = await noderails.paymentIntents.cancel('payment-intent-id');
console.log(cancelled.status); // "CANCELLED"
```

## Refund a payment

Refund a captured payment. The funds are sent back to the customer's wallet on-chain.

Refundtypescript

Copy

```
const refunded = await noderails.paymentIntents.refund('payment-intent-id', {
  reason: 'Customer requested refund',
});
      console.log(refunded.status); // Updated payment status
```

⚠️

Refund timing

Refunds are processed on-chain and may take a few minutes to complete depending on the network. Track `refundTxHash` and webhook events to confirm completion.

## Webhooks

Listen for these events to track payment intent state changes:

| Event | Description |
| --- | --- |
| `payment.authorized` | Customer gave approval to pull money from their wallet |
| `payment.captured` | Funds taken from wallet, locked in escrow, and confirmed on-chain |
| `payment.settled` | Funds released to your merchant wallet |
| `payment.refunded` | Refund completed on-chain |
| `payment.disputed` | Customer raised a dispute |

## Methods reference

| Method | Description |
| --- | --- |
| `create(params)` | Create a new payment intent |
| `retrieve(id)` | Retrieve a payment intent by ID |
| `list(params?)` | List payment intents with optional filters |
| `cancel(id)` | Cancel an authorized payment |
| `refund(id, params?)` | Refund a captured payment |

## TypeScript types

Type importstypescript

Copy

```
import type {
  PaymentIntent,
  PaymentIntentCreateParams,
  PaymentIntentListParams,
} from '@noderails/sdk';
```

## Response body reference

All responses are wrapped in `{ success: true, data: ... }`. The fields below describe what's inside `data`.

### `create()` response

Returns all scalar fields only (no relations):

#### PaymentIntent (create)

`id`stringUnique payment intent ID (UUID)

`appId`stringYour app ID

`customerAccountId`string \| nullLinked customer

`externalId`string \| nullYour external reference ID

`amount`stringFiat amount (Decimal as string, e.g. "100.00")

`currency`stringCurrency code, e.g. "USD"

`allowedChains`string \| number\[\]"ALL" or array of chain IDs

`allowedTokens`string \| string\[\]"ALL" or array of token symbols

`captureMode`string"AUTOMATIC" or "MANUAL"

`timelockDuration`numberEscrow timelock in seconds (default 604800 = 7 days)

`disputeStartDuration`numberDispute window in seconds (default 86400 = 1 day)

`status`string"CREATED" at creation

`authorizationMethod`nullSet when customer authorizes

`authorizationChainId`nullChain used for payment

`authorizationTokenKey`nullToken key used (e.g. "USDC-8453")

`authorizationWalletAddress`nullCustomer wallet address

`authorizationTxHash`nullAuthorization transaction hash

`authorizedAt`nullTimestamp when authorized

`cryptoAmount`nullCrypto amount in smallest unit

`cryptoTokenKey`nullToken key of crypto used

`cryptoTokenDecimals`nullToken decimals

`exchangeRate`nullUSD-to-crypto exchange rate used

`captureTxHash`nullCapture transaction hash

`capturedAt`nullTimestamp when captured

`captureAttempts`numberNumber of capture attempts (0)

`timelockEndsAt`nullWhen escrow timelock expires

`settledAt`nullTimestamp when settled

`refundedAt`nullTimestamp when refunded

`refundTxHash`nullRefund transaction hash

`refundReason`nullReason for refund

`platformFeeBps`nullPlatform fee in basis points

`expiresAt`string \| nullISO 8601 expiration timestamp

`sourceType`string \| nullWhat created this intent (CHECKOUT\_SESSION, INVOICE, etc.)

`sourceId`string \| nullID of the source entity

`successUrl`string \| nullRedirect URL after payment

`cancelUrl`string \| nullRedirect URL if cancelled

`metadata`objectYour metadata key-value pairs

`idempotencyKey`string \| nullIdempotency key if provided

`createdAt`stringISO 8601 creation timestamp

`updatedAt`stringISO 8601 last update timestamp

### `retrieve()` response

Returns all scalar fields from `create()` above, plus three nested relations:

#### Additional fields on retrieve

`transactions`Transaction\[\]On-chain transactions for this intent

`dispute`Dispute \| nullDispute details if one exists

`customerAccount`CustomerAccount \| nullCustomer who paid

#### Transaction (nested in transactions\[\])

`id`stringTransaction record ID (UUID)

`paymentIntentId`string \| nullLinked payment intent

`mtxmTxId`string \| nullMTXM service transaction ID

`txHash`string \| nullOn-chain transaction hash

`chain`stringChain identifier

`type`stringAUTHORIZE, CAPTURE, SETTLE, DISPUTE, REFUND, or PAYOUT

`status`stringPENDING, CONFIRMED, or FAILED

`blockNumber`number \| nullBlock number when confirmed

`gasUsed`string \| nullGas used for the transaction

`error`string \| nullError message if failed

`createdAt`stringISO 8601 timestamp

`confirmedAt`string \| nullWhen the transaction was confirmed

#### Dispute (nested in dispute)

`id`stringDispute ID (UUID)

`paymentIntentId`stringLinked payment intent

`reason`stringReason for the dispute

`evidence`string \| nullEvidence submitted

`status`stringOPEN, RESOLVED\_MERCHANT, or RESOLVED\_PAYER

`resolvedBy`string \| nullWho resolved the dispute

`deadline`stringDispute resolution deadline

`createdAt`stringISO 8601 timestamp

`resolvedAt`string \| nullWhen it was resolved

### `list()` response

Returns an array of payment intents. Each has all scalar fields plus `transactions[]`. No `dispute` or `customerAccount` in list.

Paginated response shapejson

Copy

```
{
  "success": true,
  "data": [ /* PaymentIntent[] with transactions */ ],
  "pagination": {
    "total": 100,
    "page": 1,
    "pageSize": 20,
    "totalPages": 5
  }
}
```

### `cancel()` response

Returns all scalar fields only (no relations). The `status` field will be `"CANCELLED"`.

### `refund()` response

Returns the updated `PaymentIntent` object (same scalar shape as `create()`):

#### Key refund fields

`id`stringPayment intent ID

`status`stringUpdated payment status (typically "REFUNDED" once finalized)

`refundReason`string \| nullRefund reason you provided

`refundTxHash`string \| nullOn-chain refund tx hash (when available)

`refundedAt`string \| nullTimestamp when refund is finalized