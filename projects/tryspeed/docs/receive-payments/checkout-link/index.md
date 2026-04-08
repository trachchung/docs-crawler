<!-- Source: https://docs.tryspeed.com/docs/receive-payments/checkout-link -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Checkout links
Speed’s Checkout Link offers merchants a convenient, secure, and cost-effective solution for accepting Bitcoin and stablecoin payments.
Checkout links are one-of-a-kind URLs that direct your customer to a payment page. On the payment page, customers input their payment information to finish the transaction. After the successful payment, your application will be notified via a webhook, and your application can then fulfill the order by listening to the **checkout.link.paid** event.
Checkout links are the most convenient way to collect on-chain/lightning/ethereum/solana/tron payments from customers for any goods or services without directing them to an app or website. This flexibility allows customers to choose the method that best suits their needs and preferences.
Checkout links have a no-code option, where you can generate a payment page with the web application, and begin collecting payments in seconds. You can perform all the actions of checkout links from the web application - create, activate and deactivate.
Alternatively, you can extend the functionality and generate checkout links programmatically at scale using the Speed platform API, in addition to the benefits of this no-code option. Additionally, subscribe to [webhook events](https://apidocs.tryspeed.com/reference/webhooks-and-events) to receive instant notifications.
#### [Checkout link statusesCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-link#checkout-link-statuses)
Checkout link API creates a checkout link URL, which is used to accept one-time on-chain/lightning/ethereum/solana/tron payments until they are paid or deactivated. When you receive the payment, the checkout link status changes to paid.
After you create a checkout link, it can be in either of the following states described below.
`active`
The status of the checkout link will be active after you create it. It will be in an active state till the customer makes the full payment.
`paid`
The status of the checkout link will be paid after the customer has made a complete payment. No further payments will be accepted using the same link.
`deactivated`
The status of the checkout link changes when you deactivate the link. This link is no longer accessible to the customers.
The following state diagram depicts the various checkout link states:
#### [Get startedCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-link#get-started)
###### [Create a checkout link](https://dev.speed.dev/docs/receive-payments/checkout-link/create-a-checkout-link)
Discover how to create a checkout link using both the web application and the checkout links API.
###### [Manage a checkout link](https://dev.speed.dev/docs/receive-payments/checkout-link/manage-checkout-links)
Let's look at some of the features available for managing a checkout link.
###### [Quickstart](https://apidocs.tryspeed.com/reference/checkout-link-create)
Explore a code sample of an integration with a Speed checkout link.
# Table of contents
[Checkout link statuses](https://docs.tryspeed.com/docs/receive-payments/checkout-link#checkout-link-statuses)[Get started](https://docs.tryspeed.com/docs/receive-payments/checkout-link#get-started)
/docs/receive-payments/checkout-link
