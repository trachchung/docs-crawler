<!-- Source: https://docs.tryspeed.com/docs/receive-payments/checkout-session -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Checkout session
Speed’s Checkout Session is a prebuilt payment form that allows businesses to securely accept bitcoin payments online from their customers.
Your application starts a new checkout session when a customer is prepared to finish their purchase. A URL is provided during the checkout session, which takes users to a hosted payment page. On the payment page, customers input their payment information to finish the transaction. After the successful payment, your application will be notified via a webhook, and your application can then fulfill the order by listening to the **checkout.session.paid** event.
The checkout session supports Bitcoin payment methods, such as on-chain and Lightning Network payments. This flexibility allows customers to choose the method that best suits their needs and preferences. Checkout sessions can also be customized to meet your specific payment collection needs.
Let's explore the flow of the checkout session.
Speed's [**Sessions**](https://app.tryspeed.com/sessions) offers a comprehensive view of all your checkout sessions. Whether you've created these sessions through a payment link, checkout link, or the checkout session API, this module provides an organized overview of your transactional history.
Log in to your account and follow the steps below to view checkout sessions.
  * On the left sidebar, click **Sessions** under "Developers".
  * Upon entering the "Sessions" module, you'll find a list of all checkout sessions you've created over time.
  * To streamline your view, the module offers filtering options. You can filter sessions based on their status: 
    * Paid
    * Active
    * Deactivated
  * Here you can see all the checkout sessions whether you've created it via payment link, checkout link or checkout session API.


#### [Checkout session statusesCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session#checkout-session-statuses)
The checkout session is initially created with an active status and a payment request (QR code). Your customer can pay by scanning this QR code. Once the customer initiates a money transfer, regardless of the amount, the **checkout session’s payment** status is updated to "paid”. However, the status of the **checkout session** is only updated to "paid" when the entire payment has been successfully received.
The checkout session has an active status that will remain until it is deactivated or paid. As a result, the checkout session can have the following statuses, as shown below:
`active`
The checkout session is active after its generation until it is paid or deactivated.
`paid`
The checkout session is marked paid once the full payment is received. No further lightning payments will be accepted by a checkout session marked as paid.
`deactivated`
One can manually deactivate the checkout session if it they don’t want to get paid. The session will no longer accept payments.
#### [Get startedCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session#get-started)
###### [Create a checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session)
The Checkout Session API allows you to create a checkout session, providing a payment page URL and other details. This enables you to receive funds from your customers.
###### [Manage a checkout session](https://docs.tryspeed.com/docs/payments/checkout-session/manage-checkout-session)
Let's look at some of the features available for managing a checkout session.
###### [Quickstart](https://apidocs.tryspeed.com/reference/checkout-session-create)
Explore a code sample of an integration with a Speed checkout session.
#### [Customize checkoutCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session#customize-checkout)
###### [Extended functionalities](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities)
Customize branding, the success page, custom fields, and customer collection status.
###### [Customize your domain](https://docs.tryspeed.com/docs/business-operations/custom-domain)
Customize your payment experience through a dedicated domain.
###### [Customize amount](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#case-:-1-you-choose-the-amount-for-your-customer-to-pay)
Customize amount whether you choose what to pay or your customer chooses what to pay.
#### [Additional featuresCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session#additional-features)
###### [Cashback](https://docs.tryspeed.com/docs/send-payments/cashback)
Use Speed’s cashback resource to reward your customers.
###### [Transfers](https://docs.tryspeed.com/docs/send-payments/transfers)
Utilize Speed transfers to move your balance from one Speed account to another.
###### [API elements](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements)
Customize the API elements to suit your requirements within the checkout session API.
# Table of contents
[Checkout session statuses](https://docs.tryspeed.com/docs/receive-payments/checkout-session#checkout-session-statuses)[Get started](https://docs.tryspeed.com/docs/receive-payments/checkout-session#get-started)[Customize checkout](https://docs.tryspeed.com/docs/receive-payments/checkout-session#customize-checkout)[Additional features](https://docs.tryspeed.com/docs/receive-payments/checkout-session#additional-features)
/docs/receive-payments/checkout-session
