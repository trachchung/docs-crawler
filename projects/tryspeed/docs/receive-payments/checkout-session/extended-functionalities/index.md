<!-- Source: https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Extended Functionalities
You have the flexibility to personalize your checkout session according to your preferences, utilizing the various additional features facilitated by Speed. Explore the brief overview below to discover the customizable functionalities that can enhance the checkout experience for your customers.
#### [Customer collection object with the checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#customer-collection-object-with-the-checkout-session)
If you want to collect certain predefined details from your customers, like their email address, phone number, or billing and shipping address, you need to enable the following options while creating a CS:
  1. Collect the customer’s billing and shipping address 
    1. When it comes to the address section, you have the flexibility to customize whether you wish to include just the billing address or both the billing and shipping addresses.
  2. Require the customer to provide email
  3. Require the customer to provide phone number


Whichever options you select will become mandatory, requiring your customers to mandatorily provide them before they are shown the QR code to make the payment.
To create the checkout session with the customer collection object through the API, you have to pass the request in the following manner:
json

```
"customer_collections_status": {
"is_phone_enabled": true,
"is_email_enabled": true,
"is_billing_address_enabled": true,
"is_shipping_address_enabled": true  }
}
```

#### [Custom fields with the checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#custom-fields-with-the-checkout-session)
If you desire additional details beyond email, phone numbers, and addresses from customers, you can tailor the checkout session according to your specific requirements using custom fields.
  1. You can incorporate up to **three custom fields** into your checkout session.
  2. The custom fields can be categorized into three types: text, numbers only, or dropdown. 
    1. In the dropdown, it will permit you to enter a maximum of 10 options.
  3. You can designate the custom fields as optional, allowing you to decide whether the input is required from the customer or not.
  4. You need to provide details, such as the 
    1. field's label
    2. type
    3. Options (if type= dropdown)
    4. is_optional (true if it is optional)


###### Custom field with type "text”
###### Custom field with type "numeric”
###### Custom field with type "dropdown”
#### [Customizing the success message and success URL for the checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#customizing-the-success-message-and-success-url-for-the-checkout-session)
Once the payment has been successfully processed, you have the flexibility to decide whether you'd like to,
  1. display the confirmation page 
    1. The default message will be "Thanks for your payment.” but you can personalize the success message.
  2. redirect to the website; the choice is yours 
    1. You will need to provide the URL of your website if you wish to "redirect to your website.”


However, it's important to note that you can choose either one option and not both.
The request should include a success message along with other parameters as below:
###### Request with success_message
###### Request with success_url
#### [Customizing the ‘title’ and ‘description’ in checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#customizing-the-%E2%80%98title%E2%80%99-and-%E2%80%98description%E2%80%99-in-checkout-session)
Besides branding, you have the option to personalize the payment page by customizing the title, description, and image. 
You can choose to input a custom title to replace the default one; your personalized choice will replace the dummy title currently kept as "Raising Donations for Dogs”. 
Likewise, you can replace the default dog image with your preferred image and the dummy description with your custom description.
To configure the title, description, and image using the API, you need to provide parameters like `title`, `title_description`, and `title_image`.
json

```
"title": "Contribute to crowdfunding",
"title_description": "You can contribute to the crowdfunding by scanning the QR code",
"title_image": "https://images.ctfassets.net/hrltx12pl8hq/5596z2BCR9KmT1KeRBrOQa/4070fd4e2f1a13f71c2c46afeb18e41c/shutterstock_451077043-hero1.jpg"}
```

#### [Transfers with the checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#transfers-with-the-checkout-session)
Associating transfers while creating a checkout session empowers you to assign a portion of the funds (defined in % by you) received from the customer to another Speed account instantly.
To initiate transfers while creating a checkout session, you need to add 'transfers'.
This includes the
  * account_id of the destination account,
  * the percentage to be transferred to this destination account from the total checkout session amount,
  * an optional description if you wish to provide information about this specific checkout session.


You have the option to transfer to multiple accounts (upto 25 accounts at a time), but it is essential to ensure that the combined percentage does not surpass 100.
The request to include transfers will look something like this:
json

```
"transfers": [
"destination_account": "acct_xxxxxxxxx",
"percentage": 10,
"description": "Payment for user 1"    },
  {
"destination_account": "acct_xxxxxxxxx",
"percentage": 60,
"description": "Payment for user 2"  ]

```

###### Consider the following example:
#### [Associating cashback with the checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#associating-cashback-with-the-checkout-session)
When you have an offer or discount campaign running, you can use Speed's cashback resource to reward your customers.
With cashback, you can automatically send funds to your customers as soon as they have made the full payment. Once the transaction is complete, your customer can scan the QR code shown to accept the reward they have earned.
Cashback will walk you through the steps of rewarding your customers. To learn more about cashback, [click here](https://docs.tryspeed.com/docs/send-payments/cashback/create-cashback).
# Table of contents
[Customer collection object with the checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#customer-collection-object-with-the-checkout-session)[Custom fields with the checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#custom-fields-with-the-checkout-session)[Customizing the success message and success URL for the checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#customizing-the-success-message-and-success-url-for-the-checkout-session)[Customizing the ‘title’ and ‘description’ in checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#customizing-the-%E2%80%98title%E2%80%99-and-%E2%80%98description%E2%80%99-in-checkout-session)[Transfers with the checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#transfers-with-the-checkout-session)[Associating cashback with the checkout session](https://docs.tryspeed.com/docs/receive-payments/checkout-session/extended-functionalities#associating-cashback-with-the-checkout-session)
/docs/receive-payments/checkout-session/extended-functionalities
