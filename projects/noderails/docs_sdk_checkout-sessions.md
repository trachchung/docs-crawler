---
url: "https://www.noderails.com/docs/sdk/checkout-sessions"
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

# Checkout Sessions

Checkout sessions are the easiest way to accept a payment. Create a session on your server, redirect the customer to the hosted payment page, and wait for the webhook.

## Step 1: Create a checkout session

Create sessiontypescript

Copy

```
const session = await noderails.checkoutSessions.create({
  successUrl: 'https://yoursite.com/success?session={CHECKOUT_SESSION_ID}',
  cancelUrl: 'https://yoursite.com/cancel',
  items: [\
    {\
      name: 'Pro Plan',\
      amount: '49.99',\
      currency: 'USD',\
      quantity: 1,\
    },\
  ],
  metadata: { orderId: 'order_123' },
});

// Redirect customer to the hosted checkout page
const checkoutUrl = `https://pay.noderails.com/checkout/${session.id}`;
```

💡

Session URL

The checkout URL follows the pattern `https://pay.noderails.com/checkout/SESSION_ID`. Redirect your customer here after creating the session.

## Step 2: Customer completes payment

On the hosted checkout page, the customer selects their preferred chain and token, connects their wallet, and approves the transaction. You don't need to build any of this. NodeRails handles the entire payment UI.

Once the customer pays, they're redirected to your `successUrl`. But don't rely on the redirect to confirm the payment. Always use webhooks.

## Step 3: Listen for the webhook

NodeRails sends a `payment.captured` event to your webhook endpoint when funds have been taken from the customer's wallet, locked in escrow, and confirmed on-chain. This is your signal to fulfill the order.

Handle webhooktypescript

Copy

```
app.post('/webhooks/noderails', express.raw({ type: 'application/json' }), (req, res) => {
  const event = NodeRails.webhooks.constructEvent(
    req.body,
    req.headers['x-noderails-signature'] as string,
    req.headers['x-noderails-timestamp'] as string,
    process.env.WEBHOOK_SECRET!,
  );

  switch (event.event) {
    case 'payment.captured':
      // Payment confirmed! Fulfill the order
      const paymentIntentId = event.data.id;
      const amount = event.data.amount;
      const orderId = event.data.metadata?.orderId;
      console.log(`Payment ${paymentIntentId} captured for order ${orderId}`);
      break;

    case 'payment.settled':
      // Funds released to your merchant wallet
      console.log('Funds settled:', event.data.id);
      break;
  }

  res.sendStatus(200);
});
```

## Step 4: Check payment status

After creating a checkout session, you can check its status at any time. When the customer completes payment, the full payment intent is included in the response, no extra API call needed.

Check session and payment statustypescript

Copy

```
const session = await noderails.checkoutSessions.retrieve('session-id');
console.log(session.status);          // "OPEN" | "COMPLETE" | "EXPIRED"
console.log(session.paymentIntentId); // null until customer pays

// Once payment is made, the full payment intent is included
if (session.paymentIntent) {
  console.log(session.paymentIntent.status);              // "CAPTURED"
  console.log(session.paymentIntent.amount);              // "49.99"
  console.log(session.paymentIntent.cryptoAmount);        // "50000000" (in token's smallest unit)
  console.log(session.paymentIntent.captureTxHash);       // "0x..." (on-chain tx hash)
  console.log(session.paymentIntent.authorizationChainId); // 8453 (chain used)
  console.log(session.paymentIntent.authorizationTokenKey); // "USDC-8453" (token used)
  console.log(session.paymentIntent.exchangeRate);        // "1.0001"
}
```

💡

No extra calls needed

When you retrieve a checkout session, the full `paymentIntent` object is automatically included once the customer has paid. You don't need to make a separate call to `paymentIntents.retrieve()`.

## List checkout sessions

List and filtertypescript

Copy

```
const result = await noderails.checkoutSessions.list({
  status: 'OPEN',
  page: 1,
  pageSize: 25,
});

console.log(result.data);              // CheckoutSession[]
console.log(result.pagination.total);  // Total matching sessions
```

## Expire a session

Manually expire an open checkout session. This prevents the customer from completing the payment after the session is expired.

Expire sessiontypescript

Copy

```
const expired = await noderails.checkoutSessions.expire('session-id');
console.log(expired.status); // "EXPIRED"
```

## Methods reference

| Method | Description |
| --- | --- |
| `create(params)` | Create a new checkout session |
| `retrieve(id)` | Retrieve a session by ID |
| `list(params?)` | List sessions with optional filters |
| `expire(id)` | Expire an open session |

## TypeScript types

Type importstypescript

Copy

```
import type {
  CheckoutSession,
  CheckoutSessionCreateParams,
  CheckoutSessionListParams,
} from '@noderails/sdk';
```

## Response body reference

All responses are wrapped in `{ success: true, data: ... }`. The fields below describe what's inside `data`.

### `create()` response

#### CheckoutSession (create)

`id`stringUnique session ID (UUID)

`appId`stringYour app ID

`customerAccountId`string \| nullLinked customer, if provided

`paymentIntentId`nullAlways null at creation

`mode`string"PAYMENT" or "SUBSCRIPTION"

`status`string"OPEN" at creation

`sourceType`string"API" when created via SDK

`sourceId`nullNot set at creation

`amount`string \| nullTotal amount (null until computed)

`currency`stringCurrency code, default "USD"

`subtotal`string \| nullPre-tax total

`taxAmount`string \| nullTax portion

`taxDescription`string \| nullTax label, e.g. "VAT 20%"

`allowedChains`string \| number\[\]"ALL" or array of chain IDs

`allowedTokens`string \| string\[\]"ALL" or array of token keys

`successUrl`stringRedirect URL after payment

`cancelUrl`stringRedirect URL if cancelled

`requireBillingDetails`booleanWhether billing details are required

`metadata`objectYour metadata key-value pairs

`expiresAt`stringISO 8601 expiration timestamp

`completedAt`nullSet when session completes

`createdAt`stringISO 8601 creation timestamp

`updatedAt`stringISO 8601 last update timestamp

`items`CheckoutSessionItem\[\]Line items (see below)

#### CheckoutSessionItem (nested in items\[\])

`id`stringItem ID (UUID)

`checkoutSessionId`stringParent session ID

`productPlanId`string \| nullLinked product plan, if any

`productPlanPriceId`string \| nullLinked price, if any

`name`stringItem name

`description`string \| nullItem description

`amount`string \| nullItem amount (Decimal as string)

`currency`stringItem currency

`quantity`numberItem quantity

`isPriceOption`booleanWhether this is a price selection

`createdAt`stringISO 8601 timestamp

### `retrieve()` response

Returns all fields from `create()` above, plus these additional nested objects:

#### Additional fields on retrieve

`app`AppFull app object (id, name, environment, etc.)

`paymentIntent`PaymentIntent \| nullFull payment intent once customer pays (all PI fields)

`items[].productPlan`ProductPlan \| nullFull product plan on each item, if linked

`items[].productPlanPrice`ProductPlanPrice \| nullFull price on each item, if linked

### `list()` response

Returns an array of sessions. Each session has the same shape as `create()`(with `items` but without `app`, `paymentIntent`, or nested plan/price on items). The response includes pagination:

Paginated response shapejson

Copy

```
{
  "success": true,
  "data": [ /* CheckoutSession[] */ ],
  "pagination": {
    "total": 42,
    "page": 1,
    "pageSize": 20,
    "totalPages": 3
  }
}
```

### `expire()` response

Same shape as `create()` (session + items). The `status` field will be `"EXPIRED"`.