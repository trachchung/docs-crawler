---
url: "https://www.noderails.com/docs/getting-started"
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

# Quick Start

Accept your first crypto payment in under 5 minutes. This guide walks you through setting up your account, configuring your payment preferences, and processing a payment.

💡

Check supported assets first

Before creating payment flows, review the full [supported chains and tokens list](https://www.noderails.com/docs/supported-assets) to confirm what is currently enabled.

## What you'll need

Before you start integrating, you need to set up a few things in the NodeRails Dashboard:

1. **A NodeRails account** with a verified email address.
2. **A connected wallet** where you want to receive payments. This is the wallet funds will settle to after the timelock period.
3. **An App** created in the dashboard. Each app gets its own API keys, webhook endpoints, and payment configuration.
4. **Chains and tokens selected.** You need to choose which blockchains and tokens you want to accept payments in. This is configured per app in the dashboard.

💡

Override chains and tokens per request

The chains and tokens you configure in the dashboard are your defaults. You can override them on a per-request basis when creating checkout sessions or payment intents via the API or SDK by passing specific chain and token parameters. This is useful if you want to offer different payment options for different products or customers.

## 1\. Create your account and app

Sign up at the [NodeRails Dashboard](http://localhost:3001/login) and verify your email. Then:

1. Connect your merchant wallet (this is where your settled funds go).
2. Create a new **App** from the dashboard.
3. Select which chains and tokens you want to accept for this app.

## 2\. Get your API keys

Navigate to **Apps → Your App → API Keys** in the dashboard. You'll need two pieces of information:

- **App ID**: Your app's unique identifier (UUID)
- **Secret Key**: Starts with `nr_live_sk_` or `nr_test_sk_`

⚠️

Keep your secret key safe

Never expose your secret key in client-side code. Only use it on your server. Public keys (`nr_*_pk_`) are for client-side use, but the SDK requires a secret key.

### API Key format

API keys follow the format `nr_<env>_<type>_<random>`:

| Key | Environment | Type |
| --- | --- | --- |
| `nr_live_sk_...` | Production | Secret |
| `nr_test_sk_...` | Test | Secret |
| `nr_live_pk_...` | Production | Public |
| `nr_test_pk_...` | Test | Public |

## Chains and tokens naming

When working with the NodeRails API or SDK, chains and tokens follow a specific naming convention you should be aware of.

### Chains

Chains are identified by their **chain ID**, the same numeric ID you use everywhere else in the blockchain ecosystem. For example:

| Chain | Chain ID |
| --- | --- |
| Ethereum Mainnet | `1` |
| Polygon | `137` |
| Arbitrum One | `42161` |
| Base | `8453` |
| Optimism | `10` |
| Sepolia (testnet) | `11155111` |

When you pass `allowedChains` in the API, you pass an array of these numeric IDs.

### Tokens

Tokens are identified using a **token key** in the format`SYMBOL-chainId`. This combines the token symbol with the chain it lives on. For example:

| Token | Token Key |
| --- | --- |
| USDC on Ethereum | `USDC-1` |
| USDC on Base | `USDC-8453` |
| USDT on Arbitrum | `USDT-42161` |
| ETH on Ethereum | `ETH-1` |
| USDC on Sepolia | `USDC-11155111` |

This format ensures there's no ambiguity. USDC on Ethereum and USDC on Base are different tokens at different contract addresses, so they have different token keys.

💡

Where to find available tokens

The chains and tokens available to your app are configured in the dashboard. You can also see all supported chains and their tokens via the API. When passing `allowedTokens`, you can pass either token keys (`USDC-8453`) for a specific chain, or just the symbol (`USDC`) to allow that token on all enabled chains.

## 3\. Install the SDK

Installbash

Copy

```
npm install @noderails/sdk
```

Or with your preferred package manager:

Copy

```
pnpm add @noderails/sdk
# or
yarn add @noderails/sdk
```

## 4\. Initialize the client

server.tstypescript

Copy

```
import { NodeRails } from '@noderails/sdk';

const noderails = new NodeRails({
  appId: process.env.NODERAILS_APP_ID!,
  apiKey: process.env.NODERAILS_SECRET_KEY!, // nr_live_sk_...
});
```

## 5\. Create a checkout session

A checkout session creates a hosted payment page where your customer can select their blockchain and token, connect their wallet, and complete the payment.

Create Checkout Sessiontypescript

Copy

```
// POST /api/create-checkout (your server endpoint)
const session = await noderails.checkoutSessions.create({
  successUrl: 'https://yoursite.com/success?session={CHECKOUT_SESSION_ID}',
  cancelUrl: 'https://yoursite.com/cancel',
  items: [\
    {\
      name: 'Pro Plan',\
      amount: '29.99',\
      quantity: 1,\
    },\
  ],
});

// Redirect customer to the hosted checkout page
return { checkoutUrl: `https://pay.noderails.com/session/${session.id}` };
```

By default, the checkout page shows the chains and tokens you configured for your app. You can override them for a specific session:

Override chains and tokenstypescript

Copy

```
const session = await noderails.checkoutSessions.create({
  successUrl: 'https://yoursite.com/success',
  cancelUrl: 'https://yoursite.com/cancel',
  // Override: only accept payments on Base and Arbitrum
  allowedChains: [8453, 42161],
  // Accept USDC on any of those chains
  allowedTokens: ['USDC'],
  // Or be specific with token keys:
  // allowedTokens: ['USDC-8453', 'USDC-42161'],
  items: [\
    { name: 'Enterprise License', amount: '499.00', quantity: 1 },\
  ],
});
```

## 6\. Handle the webhook

After the customer completes payment, NodeRails sends a `payment.captured` event to your webhook endpoint once funds are taken from the customer's wallet and locked in escrow on-chain. This is your signal to fulfill the order:

Webhook Handler (Express)typescript

Copy

```
import { NodeRails } from '@noderails/sdk';
import express from 'express';

const app = express();

app.post('/webhooks/noderails', express.raw({ type: 'application/json' }), (req, res) => {
  try {
    const event = NodeRails.webhooks.constructEvent(
      req.body,
      req.headers['x-noderails-signature'] as string,
      req.headers['x-noderails-timestamp'] as string,
      process.env.WEBHOOK_SECRET!,
    );

    switch (event.event) {
      case 'payment.captured':
        // Payment captured, fulfill the order
        console.log('Payment captured:', event.data.id);
        break;
      case 'payment.settled':
        // Funds settled to your wallet
        console.log('Payment settled:', event.data.id);
        break;
    }

    res.sendStatus(200);
  } catch (err) {
    console.error('Webhook error:', err);
    res.sendStatus(400);
  }
});
```

💡

Register your webhook

Create a webhook endpoint in the dashboard under **Apps → Your App → Webhooks**, or programmatically via the SDK:

`noderails.webhookEndpoints.create({ url: '...', events: ['payment.captured'] })`

* * *

## Next steps

[Supported Chains & Tokens →\\
\\
Live list of enabled chains, token symbols, and network coverage.](https://www.noderails.com/docs/supported-assets) [SDK Reference →\\
\\
Full SDK configuration and all available resources.](https://www.noderails.com/docs/sdk) [Webhooks Guide →\\
\\
All webhook events and signature verification.](https://www.noderails.com/docs/webhooks)