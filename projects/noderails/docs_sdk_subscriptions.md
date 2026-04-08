---
url: "https://www.noderails.com/docs/sdk/subscriptions"
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

# Subscriptions

Subscriptions enable recurring crypto payments. Create a product plan with a price, then subscribe customers to it.

## Full flow

### Step 1: Create a product plan and price

A subscription requires a product plan with at least one price. Plans define what you're selling, and prices define how much and how often the customer is billed.

Set up your producttypescript

Copy

```
// Create a product plan
const plan = await noderails.productPlans.create({
  name: 'Pro Plan',
  description: 'Full access to all features',
  planType: 'SUBSCRIPTION',
  prices: [\
    {\
      amount: '29.99',\
      billingInterval: 'MONTH',\
      billingIntervalCount: 1,\
      nickname: 'Monthly',\
      isDefault: true,\
    },\
  ],
});

const monthlyPrice = plan.prices![0];

// Add an annual price (optional)
const annualPrice = await noderails.productPlans.createPrice(plan.id, {
  amount: '299.00',
  currency: 'USD',
  billingInterval: 'YEAR',
  billingIntervalCount: 1,
  nickname: 'Annual',
});
```

💡

Product Plans

See the [Product Plans](https://www.noderails.com/docs/sdk/product-plans) page for full details on creating and managing product plans and their prices.

### Step 2: Create a customer

Create a customertypescript

Copy

```
const customer = await noderails.customers.create({
  email: 'alice@example.com',
  name: 'Alice',
  walletAddress: '0x...',   // Optional: their wallet address
});
```

### Step 3: Create the subscription

Subscribe the customertypescript

Copy

```
const subscription = await noderails.subscriptions.create({
  customerAccountId: customer.id,
  productPlanId: plan.id,
  productPlanPriceId: monthlyPrice.id,
});

console.log(subscription.id);              // Subscription ID
console.log(subscription.status);          // "CREATED"
console.log(subscription.currentPeriodEnd); // Next billing date
```

### Step 4: Create checkout for initial authorization

Create subscription checkouttypescript

Copy

```
const checkout = await noderails.subscriptions.createCheckout(subscription.id);
console.log(checkout.id); // Checkout session ID
// Redirect customer to hosted checkout:
// https://pay.noderails.com/checkout/${checkout.id}
```

## Pause a subscription

Temporarily pause billing. The customer keeps access until the current period ends.

Pausetypescript

Copy

```
await noderails.subscriptions.pause('sub-id');
```

## Resume a subscription

Resumetypescript

Copy

```
await noderails.subscriptions.resume('sub-id');
```

## Cancel a subscription

Canceltypescript

Copy

```
// Cancel at end of current period (customer keeps access until then)
await noderails.subscriptions.cancel('sub-id', {
  cancelAtPeriodEnd: true,
});

// Cancel immediately
await noderails.subscriptions.cancel('sub-id', {
  cancelAtPeriodEnd: false,
});
```

## List subscriptions

List and filtertypescript

Copy

```
// List all active subscriptions
const subs = await noderails.subscriptions.list({ status: 'ACTIVE' });

for (const sub of subs.data) {
  console.log(sub.id, sub.status, sub.currentPeriodEnd);
}
```

## Retrieve a subscription

When you retrieve a subscription, the response includes the last 10 invoices. Each paid invoice includes its full payment intent with on-chain transaction details.

Retrieve with payment detailstypescript

Copy

```
const sub = await noderails.subscriptions.retrieve('sub-id');
console.log(sub.status);           // "ACTIVE" | "PAUSED" | "CANCELLED"
console.log(sub.currentPeriodEnd); // Next billing date

// Each invoice includes its payment intent
for (const invoice of sub.invoices ?? []) {
  console.log(invoice.status);                              // "PAID"
  if (invoice.paymentIntent) {
    console.log(invoice.paymentIntent.status);               // "SETTLED"
    console.log(invoice.paymentIntent.captureTxHash);        // "0x..."
    console.log(invoice.paymentIntent.authorizationTokenKey); // "USDC-8453"
  }
}
```

## Webhooks

| Event | Description |
| --- | --- |
| `subscription.created` | Subscription was created |
| `subscription.activated` | Subscription became active |
| `subscription.renewed` | Recurring payment was collected |
| `subscription.cancelled` | Subscription was cancelled |
| `subscription.paused` | Subscription was paused |
| `subscription.resumed` | Subscription was resumed |

## Methods reference

| Method | Description |
| --- | --- |
| `create(params)` | Create a new subscription |
| `retrieve(id)` | Retrieve a subscription by ID |
| `list(params?)` | List subscriptions with optional filters |
| `pause(id)` | Pause billing |
| `resume(id)` | Resume a paused subscription |
| `cancel(id, params?)` | Cancel a subscription |
| `createCheckout(id)` | Create a hosted checkout session for initial authorization |

## TypeScript types

Type importstypescript

Copy

```
import type {
  Subscription,
  SubscriptionCreateParams,
  SubscriptionListParams,
} from '@noderails/sdk';
```

## Response body reference

All responses are wrapped in `{ success: true, data: ... }`. The fields below describe what's inside `data`.

### `create()` response

#### Subscription (create)

`id`stringUnique subscription ID (UUID)

`appId`stringYour app ID

`customerAccountId`stringCustomer being subscribed

`productPlanId`stringProduct plan ID

`productPlanPriceId`stringPrice ID

`status`string"CREATED" or "TRIALING"

`customerWalletId`nullSet after customer authorizes

`authorizationMethod`nullNATIVE, PERMIT, or EIP7702

`authorizationChainId`nullChain selected for payments

`authorizationTokenKey`nullToken selected for payments

`permitSignature`nullPermit signature if applicable

`permitDeadline`nullPermit deadline if applicable

`permitNonce`nullPermit nonce if applicable

`approvedAllowance`nullERC-20 allowance amount

`currentPeriodStart`stringCurrent billing period start

`currentPeriodEnd`stringCurrent billing period end

`billingCycleAnchor`stringAnchor date for billing

`trialStart`string \| nullTrial start date if applicable

`trialEnd`string \| nullTrial end date if applicable

`cancelAt`nullScheduled cancellation date

`cancelledAt`nullWhen the subscription was cancelled

`cancelAtPeriodEnd`booleanWhether cancel is deferred to period end

`pausedAt`nullWhen the subscription was paused

`pastDueSince`nullWhen subscription entered past-due state

`captureRetryCount`numberCurrent retry count for payments

`maxCaptureRetries`numberMax retries before cancellation

`allowedChains`string \| number\[\]"ALL" or array of chain IDs

`allowedTokens`string \| string\[\]"ALL" or array of token keys

`metadata`objectYour metadata key-value pairs

`createdAt`stringISO 8601 creation timestamp

`updatedAt`stringISO 8601 last update timestamp

`productPlan`ProductPlanFull product plan object

`productPlanPrice`ProductPlanPriceFull price object

### `retrieve()` response

Returns all fields from `create()` above, plus these additional nested objects. This is the most complete response:

#### Additional fields on retrieve

`app`AppFull app object

`productPlan.taxRate`TaxRate \| nullTax rate on the plan

`customerAccount`CustomerAccountFull customer object

`customerWallet`CustomerWallet \| nullWallet used for payments (with chain info)

`invoices`Invoice\[\]Last 10 invoices (descending by date)

💡

Invoices are richly nested

Each invoice in `invoices[]` includes its own `taxRate`, `items[]` (with each item's `taxRate`), and `paymentIntent` (full payment intent object). This gives you complete billing history with on-chain tx details in a single call.

### `list()` response

Returns a lighter response than `retrieve()`. Each subscription includes`productPlan` (with `taxRate`), `productPlanPrice`, and `customerAccount`. Does not include `app`, `customerWallet`, or `invoices`.

Paginated response shapejson

Copy

```
{
  "success": true,
  "data": [ /* Subscription[] */ ],
  "pagination": {
    "total": 15,
    "page": 1,
    "pageSize": 20,
    "totalPages": 1
  }
}
```

### `pause()`, `resume()`, `cancel()` response

All three return the subscription with scalar fields only (no relations). Key fields that change:

#### State changes per action

`pause → status`string"PAUSED", pausedAt is set

`resume → status`string"ACTIVE", pausedAt is cleared, new period dates set

`cancel → status`string"CANCELLED" (immediate) or unchanged (if cancelAtPeriodEnd=true)

`cancel → cancelAtPeriodEnd`booleantrue if deferred, cancelAt is set to period end