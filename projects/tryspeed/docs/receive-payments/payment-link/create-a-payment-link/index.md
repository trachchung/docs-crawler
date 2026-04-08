<!-- Source: https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Create a payment link
Discover how to create a payment link without coding (via the web application) or programmatically (via the payment links API).
A complete end-to-end flow for creating payment links is provided below.
#### [Create payment linkCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link#create-payment-link)
  * Web App
  * API


Before you create a payment link, you need to first decide whether:
  1. You want to allow your customers to choose what amount they can pay.
  2. You want to decide the amount that your customer is expected to pay yourself.


###### You choose what to pay
###### Customer choose what to pay
While creating a payment link, there are several functionalities you can include to enhance the checkout experience:
  * Decide whether to include **cashback** with the payment link. If there is no existing cashback and you wish to establish a new one, you can follow the steps outlined [here](https://www.speed.dev/docs/send-payments/cashback/create-cashback#let's-check-how-to-add-cashback) to create it and subsequently link it.
  * If you wish to collect certain predefined details from your customers, like their email address, phone number, or billing and shipping address, you need to enable these options while creating a payment link.
  * You can also use **custom_fields** for specific data collection requirements. The custom fields can be categorized into three types: text, numbers only, or dropdown. You can designate the custom fields as optional, allowing you to decide whether the input is required from the customer or not.
  * You also have the option to personalize your **Success message** or **Success URL,** crafting a unique expression of gratitude. 


#### [Request parametersCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link#request-parameters)
Provide the basic information outlined in the table below:  
| Parameter  | Required  | Type  | Description  |  
| --- | --- | --- | --- |  
| Amount  | BigDecimal  | This is the total amount you intend to collect from the customer via the payment link. Please add a positive value. Values up to 32 digits can be handled by the amount param, which can have a decimal precision of up to 16 digits.  |  
| Currency  | String  | In this parameter, you must specify your preferred base currency (fiat or cryptocurrency) to create a payment link. A three-lettered ISO-compliant currency name must be used. You can choose one of the 167 available currencies.  |  
#### [Additional request parametersCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link#additional-request-parameters)
You can also provide additional information to enhance the checkout experience or provide more information about the transaction.  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| Statement descriptor  | String  | Customers need this information because it describes the purpose of payment. Keep this text brief and to the point. On the payment page, this description will be visible.  |  
| Success_url  | String  | When the payment is successfully done, you can use this parameter to redirect the customer to your hosted page.  |  
| Success_message  | String  | When the payment is successfully done, you can use this parameter to thank them with a customized message. `Success_url` and `success-message` are mutually exclusive request parameters only one of them can be used.  |  
| Title  | String  | You can use this parameter to add the header or title to your payment page.  |  
| Title_description  | String  | You can use this parameter to provide a brief description of your payment page.  |  
| Title_image  | String  | You can include a related image illustrating the purpose of a payment page along with the title and description. Image size must not be more than 2 MB.  |  
| type  | String  | This parameter allows the user to specify the preferred payment method for customers.1. If you want your customer to make payment of a fixed amount, no need to specify the type explicitly, you just need to specify the “amount”.2. If you want your customer to choose what to pay then you need to set the type to either "options" or "preset".  |  
| options  | array of integers  | If you’ve set the "type=options" you must provide this field wherein you can offer your customers a selection of up to three payment amount options.  |  
| preset  | decimal  | If you’ve set the "type=preset" you can specify a minimum and maximum payment amount for your customers in this field and then they'll pay only within this range.min_amount: The customer must pay an amount equal to or greater than the value specified in this parameter.max_amount: This parameter prevents payments greater than the specified value.  |  
| custom_fields  | Object  | You can use this object to collect specific information from users during at payment page. Whether you need textual input, numerical data, or selections from a dropdown menu, this object empowers you to tailor the payment experience as per your unique requirement. The options goes as:1. “**label** ”: The label is the text displayed to the user, indicating the type of information you are requesting.2. “**type** ”: This defines the input type accepted for the custom field. It can be:a. "text" for general text input,b. "number" for numeric input, orc. "dropdown" for a pre-defined list of options.3.”**options** ”: The "Options" parameter under "type: dropdown" would typically refer to a list of predefined choices that a user can select from in a dropdown menu, limited to a maximum of 10 choices.4.“**is_optional** ”: This parameter determines whether the your customer is required to provide information for the custom field. If set to `true `, the field is optional; if set to `false `, the user must provide the information.  |  
| customer_collections_status  | Object  | You can use this object to decide if either email, phone number , shipping or billing address is required before processing the payment. You have to pass these options as true if you wish to collect them from the customer. The options goes as-1. is_phone_enabled - If you wish to collect customer’s phone number.2. is_email_enabled - If you wish to collect customer’s email.3. is_billing_address_enabled - If you wish to collect customer’s billing address.4. is_shipping_address_enabled - If you wish to collect customer’s shipping address.  |  
| Metadata  | Object  | You can use this object to store additional information in key-value pairs about the payment link object in a structured format. You can add up to 50 key-value pairs in a raw JSON format.  |  
| Cashback  | Object  | You can use this parameter to associate an active [cashback ](https://docs.tryspeed.com/docs/send-payments/cashback)with a payment link.  |  
More information can be found in our [API reference](https://apidocs.tryspeed.com/reference/payment-link-object).
Speed allows you to collect certain additional details about your customers on the payment page, like their email, phone number, billing, and shipping address. Enhance your checkout experience and unlock extra functionality through the payment link API and the Speed Dashboard. Explore a comprehensive list of both built-in and [customizable features](https://docs.tryspeed.com/docs/receive-payments/payment-page).
# Table of contents
[Create payment link](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link#create-payment-link)[Request parameters](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link#request-parameters)[Additional request parameters](https://docs.tryspeed.com/docs/receive-payments/payment-link/create-a-payment-link#additional-request-parameters)
/docs/receive-payments/payment-link/create-a-payment-link
