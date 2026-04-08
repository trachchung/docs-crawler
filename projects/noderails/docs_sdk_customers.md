---
url: "https://www.noderails.com/docs/sdk/customers"
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

# Customers

Customers represent the people paying you. Link payments, subscriptions, and invoices to a customer for tracking and management.

## Create a customer

Createtypescript

Copy

```
const customer = await noderails.customers.create({
  email: 'bob@example.com',
  name: 'Bob',
  metadata: { plan: 'enterprise' },
});

console.log(customer.id);    // Customer ID
console.log(customer.email); // "bob@example.com"
```

## Retrieve a customer

Retrievetypescript

Copy

```
const customer = await noderails.customers.retrieve('customer-id');
console.log(customer.name, customer.email);
```

## Update a customer

Updatetypescript

Copy

```
const updated = await noderails.customers.update('customer-id', {
  name: 'Robert',
  metadata: { plan: 'pro' },
});
```

## List customers

Listtypescript

Copy

```
const customers = await noderails.customers.list({
  page: 1,
  pageSize: 50,
});

for (const c of customers.data) {
  console.log(c.id, c.name, c.email);
}
```

## Manage wallets

Customers can have multiple wallets across different chains. Add and remove wallets to track which addresses belong to a customer.

Add and remove walletstypescript

Copy

```
// Add a wallet to a customer
const wallet = await noderails.customers.addWallet('customer-id', {
  walletAddress: '0xdef...',
  chainId: 1,
});

console.log(wallet.id);             // Wallet ID
console.log(wallet.walletAddress);   // "0xdef..."

// Remove a wallet
await noderails.customers.removeWallet('customer-id', wallet.id);
```

## Methods reference

| Method | Description |
| --- | --- |
| `create(params)` | Create a new customer |
| `retrieve(id)` | Retrieve a customer with wallets and history |
| `list(params?)` | List customers with pagination |
| `update(id, params)` | Update customer details |
| `addWallet(customerId, params)` | Add a wallet to a customer |
| `removeWallet(customerId, walletId)` | Remove a wallet |

## TypeScript types

Type importstypescript

Copy

```
import type {
  Customer,
  CustomerCreateParams,
  CustomerUpdateParams,
  CustomerListParams,
  CustomerWallet,
  CustomerAddWalletParams,
} from '@noderails/sdk';
```

## Response body reference

All responses are wrapped in `{ success: true, data: ... }`. The fields below describe what's inside `data`.

### `create()` and `update()` response

#### Customer

`id`stringUnique customer ID (UUID)

`appId`stringYour app ID

`externalId`string \| nullYour external customer ID

`email`string \| nullCustomer email

`name`string \| nullCustomer name

`address`string \| nullStreet address

`city`string \| nullCity

`state`string \| nullState or province

`country`string \| nullCountry

`postalCode`string \| nullPostal/ZIP code

`metadata`objectYour metadata key-value pairs

`createdAt`stringISO 8601 creation timestamp

`updatedAt`stringISO 8601 last update timestamp

`wallets`CustomerWallet\[\]All wallets linked to this customer

#### CustomerWallet (nested in wallets\[\])

`id`stringWallet record ID (UUID)

`customerAccountId`stringParent customer ID

`chainId`numberChain ID (e.g. 1, 137, 8453)

`walletAddress`stringWallet address (lowercased)

`hasActiveAuthorization`booleanWhether the wallet has an active authorization

`authorizationType`string \| nullType of authorization (PERMIT, NATIVE, etc.)

`authorizationTxHash`string \| nullAuthorization transaction hash

`authorizedAt`string \| nullWhen authorization was granted

`createdAt`stringISO 8601 timestamp

`updatedAt`stringISO 8601 timestamp

### `retrieve()` response

Returns all customer fields above, plus rich nested data:

#### Additional fields on retrieve

`app`AppFull app object

`wallets[].chain`{ chainId, name }Chain info on each wallet

`paymentIntents`PaymentIntent\[\]Last 50 payment intents (selected fields: id, status, amount, currency, cryptoAmount, cryptoTokenKey, authorizationChainId, createdAt, capturedAt)

`invoices`Invoice\[\]Last 50 invoices (selected fields: id, invoiceNumber, status, total, currency, dueDate, paidAt, createdAt)

### `list()` response

Returns paginated customers. Each includes `wallets[]` plus counts:

#### Additional fields on list

`_count.paymentIntents`numberTotal number of payment intents

`_count.subscriptions`numberTotal number of subscriptions

`_count.invoices`numberTotal number of invoices

### `addWallet()` response

Returns the new wallet with chain info:

#### Wallet response

`id`stringWallet ID (UUID)

`customerAccountId`stringParent customer ID

`chainId`numberChain ID

`walletAddress`stringWallet address (lowercased)

`chain`{ chainId, name }Chain metadata

### `removeWallet()` response

Returns `204 No Content` (no response body).