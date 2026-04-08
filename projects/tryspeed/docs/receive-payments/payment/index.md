<!-- Source: https://docs.tryspeed.com/docs/receive-payments/payment -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Payments
The "Payment" module offers a secure and convenient method for receiving payments, enhancing the overall user experience, and facilitating swift transactions. It is the most granular-level entity that can be used to get payments from your customers.
Merchants can receive payments from their customers by generating a payment that provides a payment payload for BTC (via lightning and on-chain address), USDT (via lightning, Ethereum, Solana and Tron address) or USDC (via lightning, Ethereum and Solana address). This request can be exhibited to customers via a QR code, which they can scan and make payment.
Mainly, payments will be automatically created by checkout sessions (for respective checkout links, payment links, etc.). Alternatively, users can create payments directly via API.
The mechanisms through which the payment object can be created are:
  1. Checkout session
  2. Checkout link (via checkout session)
  3. Payment link (via checkout session)
  4. Invoices


Payments possess an important characteristic wherein, once the specified TTL has elapsed, the current payment request expires. It means users won’t be able to take payments via it, and hence, Speed suggests their users rely on creating payments directly only when they would like to create a new payment on their own every time upon its expiry.
Alternatively, other modules like Checkout session, checkout link etc.. creates a new payment automatically upon payments TTL elapse allowing end customers to make payment for a virtually unlimited time.
Payments are recognized by a unique ID with the prefix "pi." An illustration of a payment ID is `pi_l7sygu3xYQukjvzS`.
#### [Payment life cycleCopied!](https://docs.tryspeed.com/docs/receive-payments/payment#payment-life-cycle)
Payment creation can be initiated through the checkout link, payment link, checkout session API, or by Payments API directly.
  * In case of payment link, checkout link, or checkout session API, the checkout session is created first. Upon accessing the checkout session, the payment is subsequently generated. The checkout session is designed to regenerate the payment object repeatedly, respecting the respective TTL, until the corresponding checkout session is officially marked as paid.
  * If the payment is directly created through the API, it indicates that the checkout session won't be generated, and only the raw payment is created. It will expire after the specified TTL and will not undergo automatic regeneration logic.


> In a nutshell, If you initiate payment directly, it is expected that you will handle the essential aspects of payment expiration, creating a new payment after expiry, and addressing partial payment (you can receive lesser payment too) scenarios independently on your own.
> Those who prefer not to deal with the regenerating task of payments by themselves can opt for Speed's checkout session, which internally takes care of these scenarios.
#### [Let's look at the payment status-Copied!](https://docs.tryspeed.com/docs/receive-payments/payment#let's-look-at-the-payment-status-)
Throughout its lifetime, payment transitions through multiple statuses; initially upon creation, the status is unpaid. When any amount of funds is received (i.e., it can also be a partial payment), it changes to paid. The payment object is marked "expired” if the time frame (TTL) expires. You may cancel or deactivate a payment, if you no longer wants to accept payment, at any point before it is either paid or expired.
status string
A payment object can have four statuses, as mentioned below.
Show allHide all
`unpaid`
It has unpaid status after its generation until it is paid or expired.
`paid`
It is marked as paid once the funds are received within the time frame (TTL).
`expired`
If funds are not received within the stipulated time frame (TTL), then the payment is marked as expired.
`cancelled`
If you don’t require any payment, you can cancel or deactivate it before it expires or is paid. Payments created by checkout session, checkout link or payment link get deactivated upon deactivating the respective checkout session, checkout link, or payment link.
#### [Get startedCopied!](https://docs.tryspeed.com/docs/receive-payments/payment#get-started)
###### [Create a payment](https://docs.tryspeed.com/docs/receive-payments/payment/create-payments)
You can generate a payment by providing a set of required and optional parameters in the request.
###### [Manage a payment](https://docs.tryspeed.com/docs/receive-payments/payment/payments-manage)
Post-creation, there are additional APIs available that you can utilize to meet your specific requirements.
###### [Quickstart](https://apidocs.tryspeed.com/reference/payment-create)
Explore a code sample of an integration with a Speed payment.
# Table of contents
[Payment life cycle](https://docs.tryspeed.com/docs/receive-payments/payment#payment-life-cycle)[Let's look at the payment status-](https://docs.tryspeed.com/docs/receive-payments/payment#let's-look-at-the-payment-status-)[Get started](https://docs.tryspeed.com/docs/receive-payments/payment#get-started)
/docs/receive-payments/payment
