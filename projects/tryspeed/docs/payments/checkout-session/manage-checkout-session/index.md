<!-- Source: https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Manage Checkout Session
Let's look at some of the features available for managing a checkout session.
#### [Creating a checkout sessionCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#creating-a-checkout-session)
A new checkout session is automatically created when a customer clicks on a checkout/payment link. Additionally, you can create a checkout session directly through the checkout sessions APIs.
#### [Updating a checkout sessionCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#updating-a-checkout-session)
You can also update a checkout session at any point. The **metadata** , **description** , **success_url** , **cancel_url** and **success_message** of a checkout session can be updated.
#### [Retrieving a checkout sessionCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#retrieving-a-checkout-session)
Additionally, you may always retrieve a checkout session. The checkout session can be obtained via the API after it has been formed.
#### [Retrieve a checkout session by payment IDCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#retrieve-a-checkout-session-by-payment-id)
You can retrieve checkout session details through this API using its payment ID. These details include the email, phone number, billing address, and shipping address that your customers submitted on the payment page.
#### [Deactivating a checkout sessionCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#deactivating-a-checkout-session)
A checkout session can be marked as “deactivate” in multiple ways, just like you can create a checkout session in various ways. If you want to deactivate a checkout session, you must do so before it is paid.
As of now, you can deactivate a checkout session associated with the checkout link or payment link by deactivating respective link through APIs or the Speed web application. Once you deactivate a checkout session, the associated payment’s status changes to cancel.
The following are the checkout sessions API endpoints for creating and deactivating, updating, retrieving and retrieving the checkout session by payment ID. Additionally, subscribe to [webhook events](https://apidocs.tryspeed.com/reference/webhooks-and-events) to receive instant notifications.
  1. `POST` [Create a checkout session](https://apidocs.tryspeed.com/reference/checkout-session-create) `API`
  2. `POST` [Deactivate a checkout session](https://apidocs.tryspeed.com/reference/checkout-session-deactivate) `API`
  3. `POST` [Update a checkout session](https://apidocs.tryspeed.com/reference/update-a-checkout-session) `API`
  4. `GET` [Retrieve a checkout session](https://apidocs.tryspeed.com/reference/checkout-session-retrieve) `API`
  5. `GET` [Retrieve a checkout session by payment ID](https://apidocs.tryspeed.com/reference/checkout-session-retrieve-payments) `API`


#### [Track paymentsCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#track-payments)
Unlock advanced payment tracking capabilities with our upcoming feature! Soon, you'll be able to utilize URL parameters and Urchin Tracking Module (UTM) codes to gain valuable insights into customer behaviors and assess the effectiveness of your marketing strategy. Effortlessly change your payments using these helpful tools. They enable you to keep a close eye on payments, helping you make smart decisions based on data to improve your business.
Stay tuned for the release of this feature, designed to enhance your payment tracking experience.
#### [After the paymentCopied!](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#after-the-payment)
###### Use webhooks to track the payments
###### Events
# Table of contents
[Creating a checkout session](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#creating-a-checkout-session)[Updating a checkout session](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#updating-a-checkout-session)[Retrieving a checkout session](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#retrieving-a-checkout-session)[Retrieve a checkout session by payment ID](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#retrieve-a-checkout-session-by-payment-id)[Deactivating a checkout session](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#deactivating-a-checkout-session)[Track payments](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#track-payments)[After the payment](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session#after-the-payment)
/docs/payments/checkout-session/manage-checkout-session
