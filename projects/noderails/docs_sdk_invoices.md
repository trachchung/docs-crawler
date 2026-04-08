---
url: "https://www.noderails.com/docs/sdk/invoices"
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

# Invoices

Invoices let you bill specific customers with line items, tax, and a one-click payment link. The customer receives an email with a pay button that opens the hosted checkout.

## Full flow

An invoice follows this lifecycle: `DRAFT` → `OPEN` → `PAID`. You can also `VOID` an unpaid invoice at any time.

### Step 1: Create an invoice

Create invoicetypescript

Copy

```
const invoice = await noderails.invoices.create({
  customerAccountId: 'customer-id',
  currency: 'USD',
  dueDate: '2026-04-01T00:00:00Z',
  memo: 'March consulting services',
  items: [\
    { description: 'Strategy consulting (10 hrs)', amount: '1500.00', quantity: 1 },\
    { description: 'Implementation support', amount: '750.00', quantity: 1 },\
  ],
});

console.log(invoice.id);     // Invoice ID
console.log(invoice.status); // "DRAFT"
```

### Step 2: Open the invoice

Transition the invoice from `DRAFT` to `OPEN`. Once open, the invoice is finalized and can be paid.

Open invoicetypescript

Copy

```
await noderails.invoices.open(invoice.id);
```

### Step 3: Send to customer

Send the invoice via email. The customer receives an email with the invoice details and a pay button that opens the hosted checkout.

Send invoicetypescript

Copy

```
const result = await noderails.invoices.send(invoice.id);
console.log(result.sent); // true
```

💡

One step

You can call `open` and `send` separately, or just call `send` which will automatically open a draft invoice before sending.

### Step 4: Check status

Check invoice statustypescript

Copy

```
const invoice = await noderails.invoices.retrieve(invoice.id);
console.log(invoice.status); // "DRAFT" | "OPEN" | "PAID" | "VOID"

// Once paid, the full payment intent is included automatically
if (invoice.paymentIntent) {
  console.log(invoice.paymentIntent.status);              // "CAPTURED"
  console.log(invoice.paymentIntent.captureTxHash);       // "0x..." (on-chain tx hash)
  console.log(invoice.paymentIntent.cryptoAmount);        // "2250000000" (in token's smallest unit)
  console.log(invoice.paymentIntent.authorizationChainId); // 8453 (chain used)
  console.log(invoice.paymentIntent.authorizationTokenKey); // "USDC-8453" (token used)
}
```

💡

No extra calls needed

When you retrieve an invoice, the full `paymentIntent` object is automatically included once the customer has paid. You don't need to make a separate call to `paymentIntents.retrieve()`.

## List invoices

List and filtertypescript

Copy

```
// List all open invoices
const invoices = await noderails.invoices.list({ status: 'OPEN' });

for (const inv of invoices.data) {
  console.log(inv.id, inv.status, inv.amount);
}
```

## Void an invoice

Void an unpaid invoice. This marks it as cancelled and prevents the customer from paying.

Void invoicetypescript

Copy

```
await noderails.invoices.void('invoice-id');
```

## Webhooks

| Event | Description |
| --- | --- |
| `invoice.created` | Invoice was created |
| `invoice.sent` | Invoice was emailed to customer |
| `invoice.paid` | Customer paid the invoice |
| `invoice.voided` | Invoice was voided |

## Methods reference

| Method | Description |
| --- | --- |
| `create(params)` | Create a new invoice |
| `retrieve(id)` | Retrieve an invoice by ID |
| `list(params?)` | List invoices with optional filters |
| `open(id)` | Transition from DRAFT to OPEN |
| `send(id)` | Send the invoice via email |
| `void(id)` | Void an unpaid invoice |

## TypeScript types

Type importstypescript

Copy

```
import type {
  Invoice,
  InvoiceCreateParams,
  InvoiceListParams,
} from '@noderails/sdk';
```

## Response body reference

All responses are wrapped in `{ success: true, data: ... }`. The fields below describe what's inside `data`.

### `create()` response

#### Invoice (create)

`id`stringUnique invoice ID (UUID)

`appId`stringYour app ID

`customerAccountId`stringCustomer being billed

`subscriptionId`string \| nullLinked subscription, if auto-generated

`paymentIntentId`nullAlways null at creation (set when paid)

`invoiceNumber`stringSequential number, e.g. "INV-00001"

`status`string"DRAFT" at creation

`subtotal`stringPre-tax total (Decimal as string)

`taxAmount`stringTax portion (Decimal as string)

`total`stringFinal total including tax

`currency`stringCurrency code, default "USD"

`taxRateId`string \| nullApplied tax rate ID

`dueDate`string \| nullISO 8601 due date

`paidAt`nullSet when invoice is paid

`voidedAt`nullSet when invoice is voided

`periodStart`string \| nullBilling period start (subscriptions)

`periodEnd`string \| nullBilling period end (subscriptions)

`allowedChains`string \| number\[\]"ALL" or array of chain IDs

`allowedTokens`string \| string\[\]"ALL" or array of token keys

`memo`string \| nullNote to customer

`metadata`objectYour metadata key-value pairs

`createdAt`stringISO 8601 creation timestamp

`updatedAt`stringISO 8601 last update timestamp

`items`InvoiceItem\[\]Line items (see below)

`customerAccount`CustomerAccountFull customer object

`taxRate`TaxRate \| nullFull tax rate object, if applied

#### InvoiceItem (nested in items\[\])

`id`stringItem ID (UUID)

`invoiceId`stringParent invoice ID

`productPlanId`string \| nullLinked product plan

`productPlanPriceId`string \| nullLinked price

`taxRateId`string \| nullItem-level tax rate

`description`stringItem description

`amount`stringItem amount (Decimal as string)

`currency`stringItem currency

`quantity`numberItem quantity

`taxAmount`stringTax for this item

`createdAt`stringISO 8601 timestamp

### `retrieve()` response

Returns all fields from `create()` above, plus these additional nested objects:

#### Additional fields on retrieve

`app`AppFull app object (id, name, environment, etc.)

`paymentIntent`PaymentIntent \| nullFull payment intent with nested transactions\[\], once paid

`items[].taxRate`TaxRate \| nullTax rate on each individual item

💡

retrieve() includes transactions

The `paymentIntent` on retrieve also includes its `transactions[]` array, so you can see all on-chain tx hashes, statuses, and block numbers.

### `list()` response

Same as `retrieve()` but without the `app` relation. Includes `items` (with nested `taxRate`),`customerAccount`, `taxRate`, and `paymentIntent` (with `transactions`).

Paginated response shapejson

Copy

```
{
  "success": true,
  "data": [ /* Invoice[] */ ],
  "pagination": {
    "total": 42,
    "page": 1,
    "pageSize": 20,
    "totalPages": 3
  }
}
```

### `open()` and `void()` response

Both return the invoice with `items[]` only (no customer, no tax rate, no payment intent). The `status` will be `"OPEN"` or `"VOID"` respectively.

### `send()` response

Returns a simple confirmation:

Send responsejson

Copy

```
{ "success": true, "data": { "sent": true } }
```