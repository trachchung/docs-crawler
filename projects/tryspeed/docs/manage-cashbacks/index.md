<!-- Source: https://docs.tryspeed.com/docs/manage-cashbacks -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Manage Cashback
Let's look at some of the features available for managing a cashback object.
#### [Create a CashbackCopied!](https://docs.tryspeed.com/docs/manage-cashbacks#create-a-cashback)
You can create cashback in the web app by going to [Send Payments>Cashback](https://docs.tryspeed.com/docs/send-payments/cashback/create-cashback). Cashback will be created, and you can associate this cashback with the checkout link, payment link, or checkout session.
#### [Retrieve a cashbackCopied!](https://docs.tryspeed.com/docs/manage-cashbacks#retrieve-a-cashback)
Through the cashback listed below or the Speed web application, you can view a list of all cashback objects associated with checkouts, payment links, and checkout sessions.
  * `GET` [Retrieve a cashback](https://apidocs.tryspeed.com/reference/cashback-retrieve) `API`
  * `GET` [List all cashbacks](https://apidocs.tryspeed.com/reference/cashback-list) `API`


#### [Claiming a cashbackCopied!](https://docs.tryspeed.com/docs/manage-cashbacks#claiming-a-cashback)
Once the checkout session is marked as paid, i.e., the customer has made a full payment, a cashback pop-up will appear containing a QR code of the amount derived based on that cashback.
Your customer can scan the QR code in their LNURL-supported lightning wallet and receive a defined cashback amount.
#### [How does a failed cashback claim work?Copied!](https://docs.tryspeed.com/docs/manage-cashbacks#how-does-a-failed-cashback-claim-work?)
If a cashback transaction (debit) is currently processing in an account and another transaction is requested simultaneously at the same timestamp, the new transaction will not be processed until the current cashback transaction is completed. This means that such a newer transaction would fail and prompt you with an error.
Also, if the ongoing cashback withdrawal fails due to any reason, the withdrawal will be reversed, and the cashback amount deducted earlier will be restored to the merchant account balance along with the network fees.
#### [Deactivate a cashbackCopied!](https://docs.tryspeed.com/docs/manage-cashbacks#deactivate-a-cashback)
Cashback can be deactivated in multiple ways.
  * If you want to deactivate a cashback, you can explicitly and manually deactivate through the web application.
  * In contrast, a cashback is deactivated automatically when its expiry is over i.e., after the end date.


# Table of contents
[Create a Cashback](https://docs.tryspeed.com/docs/manage-cashbacks#create-a-cashback)[Retrieve a cashback](https://docs.tryspeed.com/docs/manage-cashbacks#retrieve-a-cashback)[Claiming a cashback](https://docs.tryspeed.com/docs/manage-cashbacks#claiming-a-cashback)[How does a failed cashback claim work?](https://docs.tryspeed.com/docs/manage-cashbacks#how-does-a-failed-cashback-claim-work?)[Deactivate a cashback](https://docs.tryspeed.com/docs/manage-cashbacks#deactivate-a-cashback)
/docs/manage-cashbacks
