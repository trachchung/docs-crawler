<!-- Source: https://docs.tryspeed.com/docs/receive-payments/payment-link -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Payment links
Merchants can collect bitcoin payments from their customers multiple times using the same payment link with Speed's Payment Link, making it an efficient solution. With the ability to be shared across various platforms, including social media, emails, and other communication channels, payment links streamline transactions.
When your customers open any payment link, it leads them directly to a Speed hosted payment page and creates a new [checkout session](https://www.docs.tryspeed.com/docs/receive-payments/checkout-session). Based on the options selected by you while creating a payment link, your customer has to first submit the required details, and then the system will show the payment QR code. The customer can scan the QR and make a full or partial payment. Upon full payment, the system will notify the merchant via webhook (if subscribed to **payment_link.paymentreceived** events).
#### [Payment link statusesCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-link#payment-link-statuses)
Payment link creates a URL, which is used to accept multiple on-chain/lightning/ethereum/solana/tron BTC, USDT and USDC payments until they are manually deactivated.
When the payment link is open, it creates a new checkout session every time, as it is intended to accept multiple payments. Hence, a payment link can’t be marked as paid ever, but once the full payment is received for every checkout session created, the status of that specific checkout session changes to **paid.**
Thus, the payment link can have only two statuses as shown below,
`active`
The status of the payment link will be active after you create it until it is manually deactivated. 
`deactivated`
You can manually deactivate a payment link when you don't intend to get paid via it.
The following state diagram depicts the various payment link statuses:
#### [Get startedCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-link#get-started)
###### [Create a payment link](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link)
Discover how to create a payment link using both the web application and the payment links API.
###### [Manage a payment link](https://docs.tryspeed.com/docs/receive-payments/payment-link/manage-a-payment-link)
Let's look at some of the features available for managing a payment link.
###### [Quickstart](https://apidocs.tryspeed.com/reference/payment-link-create)
Explore a code sample of an integration with a Speed payment link.
# Table of contents
[Payment link statuses](https://docs.tryspeed.com/docs/receive-payments/payment-link#payment-link-statuses)[Get started](https://docs.tryspeed.com/docs/receive-payments/payment-link#get-started)
/docs/receive-payments/payment-link
