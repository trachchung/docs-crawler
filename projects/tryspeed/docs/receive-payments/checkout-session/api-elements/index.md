<!-- Source: https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## API Elements
You have the flexibility to tailor the checkout session API to meet your specific requirements. Below are some important elements that you have the option to customize within the checkout session API.
#### [Checkout session and metadataCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-metadata)
Think of metadata like sticky notes for objects. It's handy for storing extra information. For example, you can tag your order number or customer ID with a checkout session using metadata.
With this feature, you can add any extra notes to key-value pair data. Once you've added notes to something, you'll see them in all the related events and webhooks.
To use this feature, just make sure your request is set up the way it is mentioned below:
json

```
"amount":23,
"currency": "SATS",
"metadata": {
"order_id" : 1234,
"first_name": "John",
"last_name": "Doe",
"Payment_for": "washing_machine"}
```

#### [Checkout session and TTLCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-ttl)
The Time to Live, or TTL, indicates how long the exchange rate will be valid for a checkout session. You have the option to set the expiration time manually, measured in seconds. 
The minimum time limit is 5 minutes, and the maximum is 1 year. By default, it is configured as 600 seconds for fiat currencies and 1 year for cryptocurrency (SATS / BTC, USDT & USDC).
For example, if you create a checkout session for 1 USD, which is equivalent to 2500 SATS, it will remain valid for 10 minutes if TTL is set to 600. After that, the system will again fetch the latest exchange rate and convert 1 USD to an equivalent SATS at that time.
In the API, you can tailor the TTL in the request as outlined below:
json

```
"currency": "USD",
"amount": 1,
"ttl": 600}
```

#### [Checkout session and payment methodsCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-payment-methods)
Payment for the checkout session can be made through either the lightning or on-chain methods for BTC; lightning, Ethereum, Solana or Tron methods for USDT and lightning, Ethereum and Solana methods for USDC.
If you prefer not to collect payments from customers using the on-chain, ethereum, solana or tron method, you can disable it through the 'Web App.' To deactivate any method for your account, navigate to [Business Settings > Payment Method](https://app.tryspeed.dev/settings/payment-method).
Within the API, you have the option to define the accepted payment method for a specific checkout session by including it in the `payment_methods` array.
For example, if you wish to provide lightning and onchain both options to your customers then the request should include payment methods field as below:
json

```
"payment_methods":["onchain", "lightning"]
}
```

#### [Checkout session and Statement descriptorCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-statement-descriptor)
Statement descriptors are designed to provide a concise explanation of the payment's purpose, facilitating quick comprehension later at your customers’ end.
Through the API, you can set this descriptor, ensuring customers see it while making the payment. The `statement_descriptor` is specifically for customers using the lightning method for payment. If the customer chooses the on-chain, ethereum or tron method, this won't apply or appear.
The request should be something like this if you want to set it from the API,
json

```
"statement_descriptor": "Test statement_descriptor Speed"}
```

# Table of contents
[Checkout session and metadata](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-metadata)[Checkout session and TTL](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-ttl)[Checkout session and payment methods](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-payment-methods)[Checkout session and Statement descriptor](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-statement-descriptor)
/docs/receive-payments/checkout-session/api-elements
