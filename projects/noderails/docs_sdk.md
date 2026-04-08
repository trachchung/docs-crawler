---
url: "https://www.noderails.com/docs/sdk"
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

# Installation & Configuration

The official Node.js SDK for integrating NodeRails crypto payments. Zero runtime dependencies, full TypeScript support, and cross-runtime compatibility.

## Installation

Installbash

Copy

```
npm install @noderails/sdk
```

### Requirements

- Node.js 18+ (uses native `fetch`)
- Also works in Deno and Bun
- TypeScript 5+ recommended (full type inference)

## Configuration

Initialize the clienttypescript

Copy

```
import { NodeRails } from '@noderails/sdk';

const noderails = new NodeRails({
  appId: 'your-app-id',          // Required: your app UUID
  apiKey: 'nr_live_sk_...',      // Required: secret API key
  baseUrl: 'https://api.noderails.com', // Optional: override API URL
  timeout: 30000,                // Optional: request timeout in ms
  apiVersion: '2026-03-07',      // Optional: pin to a specific API version
});
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `appId` | `string` |  | Your app UUID from the dashboard |
| `apiKey` | `string` |  | Secret API key (`nr_*_sk_*`) |
| `baseUrl` | `string` | `https://api.noderails.com` | Override the API base URL |
| `timeout` | `number` | `30000` | Request timeout in milliseconds |
| `apiVersion` | `string` | Latest | Pin requests to a specific API version |

⚠️

Secret keys only

The SDK requires a secret key (`sk`). Public keys cannot be used as they are for client-side operations only.

## Common patterns

### Pagination

All list endpoints return a `PaginatedResult` with `data` and `pagination`:

Paginated resultstypescript

Copy

```
const result = await noderails.paymentIntents.list({
  page: 1,
  pageSize: 50,
  status: 'CAPTURED',
});

console.log(result.data);              // PaymentIntent[]
console.log(result.pagination.total);  // Total count
console.log(result.pagination.totalPages); // Total number of pages
```

### Idempotency keys

For safe retries, pass an idempotency key on any mutating request. If you send the same key twice, you'll get back the same response without creating a duplicate.

Idempotent requeststypescript

Copy

```
const intent = await noderails.paymentIntents.create(
  {
    amount: '100.00',
    currency: 'USD',
  },
  { idempotencyKey: 'order_456' },
);
```

### Authentication header

The SDK automatically sends your API key using the `x-api-key` header. Manually, the headers look like:

HTTP headerstext

Copy

```
x-api-key: nr_live_sk_abc123...
    Content-Type: application/json
```

### Response format

API responses use a standard envelope. The SDK unwraps this automatically so you always get the `data` directly:

Raw API response (unwrapped by SDK)json

Copy

```
{
  "success": true,
  "data": {
    "id": "abc123...",
    "status": "OPEN",
    ...
  }
}
```

## TypeScript support

All request parameters and response types are fully typed. Import types directly from the SDK:

Type importstypescript

Copy

```
import type {
  CheckoutSession,
  CheckoutSessionCreateParams,
  PaymentIntent,
  PaymentIntentCreateParams,
  Invoice,
  Subscription,
  PaginatedResult,
} from '@noderails/sdk';
```

* * *

## Resources

Each resource has its own page with full usage examples, method references, and TypeScript types:

[Checkout Sessions →\\
\\
Create hosted checkout pages. Full flow: create → redirect → webhook → status.](https://www.noderails.com/docs/sdk/checkout-sessions) [Payment Intents →\\
\\
Core payment object. Create, authorize, capture, settle, cancel, refund.](https://www.noderails.com/docs/sdk/payment-intents) [Invoices →\\
\\
Bill customers with line items. Create → open → send → paid.](https://www.noderails.com/docs/sdk/invoices) [Subscriptions →\\
\\
Recurring payments. Create plans, subscribe customers, pause/resume/cancel.](https://www.noderails.com/docs/sdk/subscriptions) [Customers →\\
\\
Manage customers and their wallets.](https://www.noderails.com/docs/sdk/customers) [Payment Links →\\
\\
Shareable payment URLs. No integration needed.](https://www.noderails.com/docs/sdk/payment-links) [Product Plans →\\
\\
Define products with multiple pricing tiers for subscriptions.](https://www.noderails.com/docs/sdk/product-plans) [Webhook Endpoints →\\
\\
Register endpoints, rotate secrets, verify signatures.](https://www.noderails.com/docs/sdk/webhook-endpoints) [Tax Rates →\\
\\
Create and manage tax rates for invoices.](https://www.noderails.com/docs/sdk/tax-rates) [Prices →\\
\\
Real-time USD ↔ crypto conversion.](https://www.noderails.com/docs/sdk/prices)