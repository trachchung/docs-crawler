---
url: "https://www.noderails.com/docs"
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

# NodeRails Documentation

Accept crypto payments as easily as you accept fiat. A comprehensive, developer-friendly crypto payments infrastructure.

💡

Need support or want to join the community?

Join our [Telegram channel](https://t.me/+fzUTcAYr-zhhZjg1) or [Discord channel](https://discord.gg/8uwSfv9Tvk).

✅

Quick Start

Already know about NodeRails? Jump straight to the [Quick Start guide](https://www.noderails.com/docs/getting-started) to accept your first payment in under 5 minutes.

## What is NodeRails?

If you've ever wanted to accept crypto payments in your app but couldn't find anything as simple and reliable as what Stripe, Razorpay, or Dodo Payments offer for fiat, NodeRails is built exactly for you.

NodeRails is a comprehensive crypto payments infrastructure that gives you everything you need to accept, manage, and settle cryptocurrency payments. We've worked hard to make it feel as familiar and effortless as accepting fiat, with all the power that comes from building on blockchain: instant cross-border settlement, low fees, and full transparency.

No complicated wallet integrations. No manually tracking transactions on block explorers. You create a payment, your customer pays, you get notified. That's it.

## Key features

- **Multi-chain, multi-token:** Accept payments across multiple blockchains and tokens. Your customers pick the chain and token they prefer, you receive the funds.
- **Hosted checkout:** A ready-to-use payment page. Create a session, redirect your customer, done. No frontend work needed.
- **Recurring payments & subscriptions:** Set up subscription plans with automatic renewal. Perfect for SaaS, memberships, or any recurring billing.
- **Invoicing:** Create professional invoices with line items and tax, send them via email, and let customers pay with one click.
- **Payment links:** Generate shareable payment links for quick, no-code payment collection.
- **Developer-first SDK:** A clean TypeScript SDK with type safety, zero dependencies, and a familiar API design. If you've used Stripe's SDK, you'll feel right at home.
- **Webhooks:** Get real-time notifications for every payment event with signed payloads and automatic retries.

## How it works

1. **Create a checkout session** from your server using the SDK or REST API.
2. **Redirect your customer** to the hosted payment page. They pick their preferred chain and token, connect their wallet, and approve the transaction.
3. **Payment is captured**: funds are taken from the customer's wallet and locked in escrow on-chain. You receive a `payment.captured` webhook confirming the funds are secured.
4. **Funds are settled** to your merchant wallet automatically. You get a `payment.settled` webhook when it's done.

## Why NodeRails?

### Your money is always safe

One of the biggest reasons people hesitate to pay with crypto is the fear that if something goes wrong, if the product isn't delivered or the service doesn't work, they can't get their money back. With traditional crypto payments, that's a real concern.

NodeRails solves this with an on-chain escrow system. When a customer pays, the funds are held in a secure smart contract, not in anyone's personal wallet. The money can only go to one of two places: the merchant or the customer. No middlemen, no third-party custody. It's all enforced by code on the blockchain.

### Built-in dispute resolution

If a customer has a problem with their purchase, they can raise a dispute during the dispute window. The merchant or an admin reviews it and decides the outcome. If the customer wins, their funds are returned automatically. If the merchant wins, the funds are released to them. The entire process is transparent and settled on-chain.

This means customers can pay with crypto with the same confidence they have with credit card chargebacks, and merchants know their money is protected from fraudulent claims once the dispute window closes.

### No middlemen

There is no intermediary holding your funds. Payments flow directly from the customer's wallet to the on-chain escrow, and then to your merchant wallet. NodeRails never has custody of your money at any point.

## Understanding payment states

Every payment in NodeRails goes through a lifecycle of states. Understanding these states is key to building a solid integration.

### Authorized

When a customer approves the payment, the payment moves to `AUTHORIZED`. Think of it like a credit card authorization: the customer has given permission for you to charge a specific amount from their wallet, but the money hasn't moved yet.

On the blockchain, this typically means the customer has signed an approval or permit allowing the specified amount to be pulled from their wallet. The funds are still in the customer's wallet at this point. Authorization can still fail (insufficient balance, revoked approval, etc.), so don't fulfill orders at this stage.

### Captured

Once the authorized funds are actually pulled from the customer's wallet and locked in the escrow contract, the payment becomes `CAPTURED`. **This is the confirmation you're waiting for.** Captured means the money has left the customer's wallet and is now secured. You can safely fulfill the order, deliver the product, or activate the service.

The only scenario where captured funds don't end up in your wallet is if the customer raises a dispute and wins. Outside of that, captured funds will automatically settle to your wallet.

### Settled

After the timelock period passes without any disputes, the funds are released from the escrow and transferred to your merchant wallet. The payment moves to `SETTLED`. This is the final, irreversible state, the funds are now in your wallet.

### Disputed

If a customer raises a dispute during the dispute window (after capture but before settlement), the payment moves to `DISPUTED`. Funds remain in escrow until the dispute is resolved. The outcome is either:

- **Resolved in merchant's favor:** Funds are released to your wallet as normal.
- **Resolved in customer's favor:** Funds are returned to the customer's wallet.

💡

When to fulfill orders

Listen for the `payment.captured` webhook event. That's your signal to deliver the product or activate the service. Don't wait for settlement, capture is your green light.

## Tracking payments

No matter how you accept payments (checkout sessions, invoices, payment links, or subscriptions), there is one object that ties everything together: the **payment intent**.

When you create a checkout session, invoice, or payment link, a payment intent doesn't exist yet. It is created the moment your customer actually authorizes the payment, picks their chain and token, and signs the transaction. Once it exists, the payment intent becomes the single source of truth for that payment.

### What to store

Store the ID of whatever you created (checkout session, invoice, etc.) in your database against your order. Once the customer pays, that object will contain a `paymentIntentId` linking to the payment intent.

### What the payment intent gives you

- `status` — current state: `AUTHORIZED`, `CAPTURED`, `SETTLED`, `DISPUTED`, etc.
- `sourceType` — what created it: `CHECKOUT_SESSION`, `INVOICE`, `SUBSCRIPTION`, `PAYMENT_LINK`
- `sourceId` — the ID of the checkout session, invoice, or subscription that created it
- `authorizationChainId`, `authorizationTokenKey` — which chain and token the customer used
- `cryptoAmount`, `exchangeRate` — exact crypto amount and conversion rate
- `captureTxHash` — the on-chain transaction hash
- `metadata`, `externalId` — your custom data and order reference

### Two ways to track

**1\. Webhooks (recommended):** Listen for `payment.captured` and other events. The webhook payload includes the full payment intent with all the fields above, plus any metadata you set.

**2\. Polling:** If you don't use webhooks, retrieve the object you created to check its status. For example, retrieve a checkout session to see if it moved to `COMPLETE` and read its `paymentIntentId`, then retrieve the payment intent for transaction details.

💡

One ID to rule them all

Once a payment intent exists, you can track everything from it: the payment status, on-chain transaction details, which invoice or subscription it belongs to, and your custom metadata. It's the single object that connects your order to the blockchain transaction.

## Three ways to accept payments

NodeRails gives you flexibility in how you integrate. Pick the approach that fits your use case.

### 1\. Merchant Dashboard

No code required. Log into your NodeRails dashboard, create payment links or invoices, and share them with your customers. Great for freelancers, small businesses, or one-off payments.

### 2\. REST API

Use the REST API directly from any language or framework. Create checkout sessions, manage subscriptions, send invoices, all through standard HTTP requests with your API key.

### 3\. TypeScript SDK

The fastest way to integrate if you're building with Node.js, Deno, or Bun. The SDK wraps the REST API with full type safety, automatic error handling, and a clean, intuitive interface. Install it with `npm install @noderails/sdk` and you're ready to go.

## Services we offer

NodeRails provides several payment services. Here's a quick overview of what's available and when to use each one.

### Checkout Sessions

The simplest way to accept a one-time payment. You create a checkout session on your server, redirect the customer to our hosted payment page, and we handle everything: chain selection, wallet connection, transaction approval, and confirmation. Use this when you want to charge a customer for a specific amount right now.

### Payment Intents

The core payment object. Every checkout session creates a payment intent under the hood. If you need more control over the payment flow (custom UIs, server-to-server payments), you can work with payment intents directly.

### Invoices

Send a professional invoice with line items, tax rates, and a payment link. The customer receives an email with a one-click pay button. Use invoices when you need to bill a specific customer for specific items, especially for B2B or freelance work.

### Subscriptions

Recurring payments on a schedule. You create a product plan with a price (monthly, yearly, etc.), and customers subscribe to it. NodeRails handles the billing cycle, renewals, and notifications. Use subscriptions for SaaS products, memberships, or any service with regular billing.

To set up subscriptions, you'll need:

- **A product plan:** What you're selling (e.g., "Pro Plan", "Enterprise Tier").
- **A price:** How much and how often (e.g., $29/month, $299/year). A product can have multiple prices.
- **A customer:** Who is subscribing. Customers are tracked by email and wallet address.

### Payment Links

Shareable URLs that open a payment page. No integration needed at all. Create a link in the dashboard or via API, share it anywhere (email, social media, QR code), and anyone with the link can pay. Great for tips, donations, or quick payments.

## Get started

[Quick Start →\\
\\
Install the SDK and accept your first payment in minutes.](https://www.noderails.com/docs/getting-started) [SDK Reference →\\
\\
Full configuration options, all resources, and usage patterns.](https://www.noderails.com/docs/sdk) [Supported Chains & Tokens →\\
\\
See all currently enabled chains and payment tokens.](https://www.noderails.com/docs/supported-assets) [API Reference →\\
\\
Complete REST API documentation with request and response examples.](https://www.noderails.com/docs/api-reference/checkout-sessions) [Webhooks →\\
\\
Receive real-time events and verify webhook signatures.](https://www.noderails.com/docs/webhooks)