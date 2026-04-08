<!-- Source: https://docs.tryspeed.com/docs/receive-payments/payment/create-payments -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Create a payment
You can create a payment through the payments API. This API will return an object with a payment payload that comprises an LN invoice, an on-chain address, and many other associated details, using which you can receive funds from your customer.
Use the `POST`[/payments](https://apidocs.tryspeed.com/reference/payment-create) `API` endpoint and basic details such as amount, currency, and some optional parameters to create a payment object.
In this example below, we'll show you how you can create a payment for your customer to receive 200 USD. Make a POST /payments request specifying the following mandatory parameters:
json

```
“amount”: 200,
“currency”: "USD"}
```

#### [Request parametersCopied!](https://docs.tryspeed.com/docs/receive-payments/payment/create-payments#request-parameters)
To create a payment, you need to provide specific details associated with that parameter to get a response.
Provide the details associated with the mandatory parameters outlined in the table below:  
| Parameter  | Required  | Type  | Description  |  
| --- | --- | --- | --- |  
| Amount  | BigDecimal  |  The total amount you intend to collect from the customer via the raw payment entity. You have the following options:
  1. Define the required payment amount as greater than zero to accept a specific amount of payment.
  2. Keep it as 0 if you want your customers to make payments of any amount of their choice. 

 |  
| Currency  | String  | The [currency](https://apidocs.tryspeed.com/reference/enum-base-currency) you prefer (fiat or cryptocurrency) to create a checkout session.  |  
#### [Additional request parametersCopied!](https://docs.tryspeed.com/docs/receive-payments/payment/create-payments#additional-request-parameters)
You can also provide additional information to enhance the checkout experience or provide more information about the transaction.
The optional parameters include:  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| Payment_methods  | Enum  |  BTC can be received via on-chain or Lightning, USDT via lightning, Ethereum, Solana or Tron, and USDC via lightning, Ethereum or Solana. Please choose your preferred method as per the target currency. The API response for the payment resource varies depending on the payment method(s) that have been selected within the [Speed web application](https://app.tryspeed.com/settings/payment-method)  |  
| TTL  | Integer  | Represents the time duration to which the checkout payment has not expired. (Specified in seconds). You can manually add the expiration time in seconds. The minimum time limit is 5 minutes, and the maximum is 1 year. The default is 600 seconds for fiat currencies and 1 year for cryptocurrency. (SATS/BTC, USDT & USDC).  |  
| Statement descriptor  | String  | It describes the purpose of payment. Keep this text brief and to the point. To learn more about the statement descriptor, [click here](https://docs.tryspeed.com/docs/receive-payments/checkout-session/api-elements#checkout-session-and-statement-descriptor)  |  
| metadata  | Object  | You can use this object to store additional information in key value pairs about the payment object in a structured format. You can add up to 50 key-value pairs in a raw JSON format.  |  
| Transfers  | List  |  To associate a transfer with payment, make sure to specify the following parameters:
  * **Destination account** - This can be any existing Speed account ID that would receive the transferred amount upon payment.
  * **Percentage** - This represents the proportion of the payment that the destination account will receive after deducting all the applicable fees.
  * **Description** - This is the additional information about the transfer. It is an optional field.

 |  
| Target_currency  | String  | The cryptocurrency in which you want to receive funds to your customer. As of now, Speed supports SATS, USDT and USDC.  |  
If optional parameters are not specified, then the payment object will be generated without them.
More information can be found in our [API reference.](https://apidocs.tryspeed.com/reference/payment-object)
# Table of contents
[Request parameters](https://docs.tryspeed.com/docs/receive-payments/payment/create-payments#request-parameters)[Additional request parameters](https://docs.tryspeed.com/docs/receive-payments/payment/create-payments#additional-request-parameters)
/docs/receive-payments/payment/create-payments
