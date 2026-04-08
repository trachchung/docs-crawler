---
url: "https://www.noderails.com/docs/api-reference/checkout-sessions"
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

A checkout session represents a hosted payment page. Create a session, redirect your customer to the session URL, and NodeRails handles the rest: chain selection, wallet connection, and payment capture.

💡

Hosted payment page

Checkout sessions power the NodeRails hosted payment UI. Your customer never leaves a NodeRails-hosted page, reducing PCI-equivalent complexity for crypto payments.

* * *

## Create a checkout session

POST`/checkout-sessions`

Creates a new checkout session. Returns a session object with line items.

### Request body

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `appId` | `string` | Yes | Your app UUID |
| `successUrl` | `string` | Yes | URL to redirect on successful payment |
| `cancelUrl` | `string` | Yes | URL to redirect on cancellation |
| `items` | `CheckoutItem[]` | Yes | Line items (min 1) |
| `customerAccountId` | `string` | No | Existing customer UUID |
| `mode` | `"PAYMENT" | "SUBSCRIPTION"` | No | Checkout mode (default: PAYMENT) |
| `expiresInMinutes` | `number` | No | Auto-expire in 1–1440 minutes |
| `metadata` | `object` | No | Arbitrary key-value metadata |

#### CheckoutItem

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `name` | `string` | Yes | Item name (1–255 chars) |
| `amount` | `string` | No | Price in fiat (decimal string) |
| `currency` | `string` | No | Currency code (max 10 chars) |
| `quantity` | `number` | No | Item quantity (positive integer) |
| `description` | `string` | No | Item description (max 500) |
| `productPlanId` | `string` | No | Link to a product plan |
| `productPlanPriceId` | `string` | No | Specific price option |
| `isPriceOption` | `boolean` | No | Whether to use price option |

SDK exampletypescript

Copy

```
const session = await noderails.checkoutSessions.create({
  successUrl: 'https://example.com/success',
  cancelUrl: 'https://example.com/cancel',
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

// Redirect your customer to the hosted payment page:
// https://pay.noderails.com/checkout/{session.id}
console.log(session.id);     // UUID
console.log(session.status); // "OPEN"
```

cURLbash

Copy

```
curl -X POST https://api.noderails.com/checkout-sessions \
  -H "x-api-key: nr_live_sk_..." \
  -H "Content-Type: application/json" \
  -d '{
    "appId": "your-app-id",
    "successUrl": "https://example.com/success",
    "cancelUrl": "https://example.com/cancel",
    "items": [{\
      "name": "Pro Plan",\
      "amount": "49.99",\
      "currency": "USD",\
      "quantity": 1\
    }]
  }'
```

* * *

## List checkout sessions

GET`/checkout-sessions`

### Query parameters

| Parameter | Type | Description |
| --- | --- | --- |
| `appId` | `string` | Filter by app UUID |
| `status` | `"OPEN" | "COMPLETE" | "EXPIRED"` | Filter by status |
| `page` | `number` | Page number (default: 1) |
| `pageSize` | `number` | Items per page (1–100) |

SDK exampletypescript

Copy

```
const result = await noderails.checkoutSessions.list({
  status: 'OPEN',
  page: 1,
  pageSize: 25,
});

console.log(result.data);       // CheckoutSession[]
console.log(result.pagination); // { total, page, pageSize, totalPages }
```

* * *

## Retrieve a checkout session

GET`/checkout-sessions/:id`

SDK exampletypescript

Copy

```
const session = await noderails.checkoutSessions.retrieve('cs_abc123');
console.log(session.status); // "OPEN" | "COMPLETE" | "EXPIRED"
```

* * *

## Expire a checkout session

POST`/checkout-sessions/:id/expire`

Manually expires an open checkout session, preventing any further payments.

SDK exampletypescript

Copy

```
const expired = await noderails.checkoutSessions.expire('cs_abc123');
console.log(expired.status); // "EXPIRED"
```

* * *

## Create from payment link

POST`/checkout-sessions/from-link`

Creates a checkout session from a payment link slug. This is a **public** endpoint, no authentication required.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `slug` | `string` | Yes | Payment link slug (1–100 chars) |

* * *

## Create from invoice

POST`/checkout-sessions/from-invoice`

Creates a checkout session from an invoice ID. This is a **public** endpoint, no authentication required.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `invoiceId` | `string` | Yes | Invoice UUID |

* * *

## Response object

All responses are wrapped in `{ "success": true, "data": ... }`. List endpoints add `pagination` with `total`, `page`,`pageSize`, and `totalPages`.

CheckoutSession object (create / expire)json

Copy

```
{
  "success": true,
  "data": {
    "id": "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",
    "appId": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "customerAccountId": null,
    "paymentIntentId": null,
    "mode": "PAYMENT",
    "status": "OPEN",
    "sourceType": "CHECKOUT",
    "sourceId": null,
    "amount": "49.99",
    "currency": "USD",
    "subtotal": "49.99",
    "taxAmount": "0",
    "taxDescription": null,
    "allowedChains": "ALL",
    "allowedTokens": "ALL",
    "successUrl": "https://example.com/success",
    "cancelUrl": "https://example.com/cancel",
    "selectedPriceId": null,
    "requireBillingDetails": false,
    "metadata": { "orderId": "order_123" },
    "expiresAt": "2025-01-16T10:30:00.000Z",
    "completedAt": null,
    "createdAt": "2025-01-15T10:30:00.000Z",
    "updatedAt": "2025-01-15T10:30:00.000Z",
    "items": [\
      {\
        "id": "b2c3d4e5-f6a7-8901-bcde-f12345678901",\
        "checkoutSessionId": "d4e5f6a7-b8c9-0d1e-2f3a-4b5c6d7e8f9a",\
        "productPlanId": null,\
        "productPlanPriceId": null,\
        "name": "Pro Plan",\
        "description": null,\
        "amount": "49.99",\
        "currency": "USD",\
        "quantity": 1,\
        "isPriceOption": false,\
        "createdAt": "2025-01-15T10:30:00.000Z"\
      }\
    ]
  }
}
```

#### CheckoutSession fields

`id`stringUnique checkout session UUID

`appId`stringApp this session belongs to

`customerAccountId`string \| nullLinked customer UUID, if any

`paymentIntentId`string \| nullAssociated payment intent UUID once payment begins

`mode`stringPAYMENT or SUBSCRIPTION

`status`stringOPEN, COMPLETE, or EXPIRED

`sourceType`stringOrigin type: CHECKOUT, PAYMENT\_LINK, INVOICE, or SUBSCRIPTION

`sourceId`string \| nullID of the originating resource (payment link, invoice, etc.)

`amount`stringTotal payment amount as a decimal string

`currency`stringFiat currency code (e.g. USD)

`subtotal`stringAmount before tax

`taxAmount`stringCalculated tax amount

`taxDescription`string \| nullTax label shown to customer (e.g. 'VAT 20%')

`allowedChains`'ALL' \| number\[\]Permitted blockchain chain IDs

`allowedTokens`'ALL' \| string\[\]Permitted token identifiers

`successUrl`stringRedirect URL after successful payment

`cancelUrl`stringRedirect URL on cancellation

`selectedPriceId`string \| nullSelected product plan price UUID

`requireBillingDetails`booleanWhether billing details are required at checkout

`metadata`objectArbitrary key-value pairs

`expiresAt`stringISO 8601 expiration timestamp

`completedAt`string \| nullISO 8601 timestamp when session completed

`createdAt`stringISO 8601 creation timestamp

`updatedAt`stringISO 8601 last-update timestamp

`items`CheckoutSessionItem\[\]Line items in this session

#### CheckoutSessionItem fields

`id`stringItem UUID

`checkoutSessionId`stringParent checkout session UUID

`productPlanId`string \| nullLinked product plan UUID

`productPlanPriceId`string \| nullLinked price UUID

`name`stringItem display name

`description`string \| nullItem description

`amount`stringPrice per unit as decimal string

`currency`stringCurrency code

`quantity`numberItem quantity

`isPriceOption`booleanWhether this item uses a price option

`createdAt`stringISO 8601 creation timestamp

💡

Retrieve response

The **retrieve** endpoint returns additional nested objects:`app` (full app record), `paymentIntent` (full payment intent), and each item includes `productPlan` and `productPlanPrice` when linked.