<!-- Source: https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Create a checkout session
You can create a checkout session through the checkout session API. After creating a checkout session, this API will return a payment page URL and many other associated details, using which you can receive funds from your customer.
Before you create a checkout session, you need to first decide whether:
  1. You want to allow your customers to choose what amount they can pay.
  2. You want to decide the amount that your customer is expected to pay yourself.


#### [Case : 1 You choose the amount for your customer to payCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#case-:-1-you-choose-the-amount-for-your-customer-to-pay)
In this case, you have the flexibility to specify the exact amount that your customers are expected to pay.You can make a `POST` /checkout session request specifying the following mandatory parameters:
  * `amount` ,
  * `currency`


You can create a checkout session for your customer on a purchase of 200 USD.
json

```
"amount": 200,
"currency": "USD"}
```

#### [Case : 2 Your customer chooses what amount to payCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#case-:-2-your-customer-chooses-what-amount-to-pay)
Alternatively, Speed supports a dynamic approach, allowing your customers to choose the amount they wish to pay. Let's look at how to utilize the checkout session API when you want your consumers to choose how much they wish to spend.
There are **three unique types** you may pick from under the "customers choose what to pay" option:
###### Any amount
###### Options
###### Preset
#### [Request parametersCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#request-parameters)
To create a checkout session, you need to provide specific details associated with that parameter to get the response.Provide the details associated with the mandatory parameters outlined in the table below:  
| Parameter  | Required  | Type  | Description  |  
| --- | --- | --- | --- |  
| Amount  | BigDecimal  | The total amount you intend to collect from the customer via the checkout session.1. If you specify the amount, your customer is expected to pay, the amount value should be greater than zero.2. If you allow your customer to choose what they would like to pay, then you need to set the type to either preset or options.  |  
| Currency  | String  | The [currency](https://apidocs.tryspeed.com/reference/enum-base-currency) your prefer (fiat or cryptocurrency) to create a checkout session.  |  
#### [Additional request parametersCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#additional-request-parameters)
You can also provide additional information to enhance the checkout experience or provide more information about the transaction.  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| Statement descriptor  | String  | It describes the purpose of payment. Keep this text brief and to the point.  |  
| Payment_methods  | Enum  | Version 2022-10-15 supports BTC payments via on-chain and Lightning; USDT payments via lightning, Ethereum, Solana and Tron; and USDC payments via lightning, Ethereum and Tron. Use this field to select your preferred payment method: lightning, on-chain, Ethereum, Solana or Tron as per the target currency. Additionally, you can create a checkout session for multiple payment methods.  |  
| TTL  | Integer  | Represents the time duration to which the checkout session’s payment has not expired. (Specified in seconds). You can manually add the expiration time in seconds. The minimum time limit is 5 minutes, and the maximum is 1 year. The default is 600 seconds for fiat currencies and 1 year for cryptocurrency. (SATS / BTC, USDT & USDC).  |  
| type  | String  | This parameter allows the user to specify the preferred payment method for customers. 1. If you want your customer to make payment of a fixed amount, no need to specify the type explicitly, you just need to specify the “amount”. 2. If you want your customer to choose what to pay then you need to set the type to either "options" or "preset".  |  
| options  | Array of integers  | If you’ve set the "type=options" you must provide this field wherein you can offer your customers a selection of up to three payment amount options.  |  
| preset  | decimal  | If you’ve set the "type=preset" you can specify a minimum and maximum payment amount for your customers in this field and then they'll pay only within this range.min_amount: The customer must pay an amount equal to or greater than the value specified in this parameter.max_amount: This parameter prevents payments greater than the specified value.  |  
| Transfers  | List  |  To associate a transfer with checkout session, you need to pass below parameters:**Destination account** - This can be any existing Speed account ID that would receive the transferred amount upon payment.**Percentage** - This represents the proportion of the payment that the destination account will receive.**Description** - This is the additional information about the transfer. It is an optional field.  |  
If optional parameters are not specified, then the checkout session object will be generated without them.
More information can be found in our [API reference.](https://apidocs.tryspeed.com/reference/checkout-session-create)
Speed allows you to collect certain additional details about your customers on the payment page, like their email, phone number, billing, and shipping address. Enhance your checkout experience and unlock extra functionality through the Checkout Session API and the Speed Dashboard. Explore a comprehensive list of both built-in and [customizable features](https://docs.tryspeed.com/docs/receive-payments/payment-page).
# Table of contents
[Case : 1 You choose the amount for your customer to pay](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#case-:-1-you-choose-the-amount-for-your-customer-to-pay)[Case : 2 Your customer chooses what amount to pay](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#case-:-2-your-customer-chooses-what-amount-to-pay)[Request parameters](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#request-parameters)[Additional request parameters](https://docs.tryspeed.com/docs/receive-payments/checkout-session/create-a-checkout-session#additional-request-parameters)
/docs/receive-payments/checkout-session/create-a-checkout-session
