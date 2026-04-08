<!-- Source: https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2 -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Magento 2
Accepting bitcoin and stablecoin payments online has never been easier. You can accept bitcoin and stablecoin payments directly from your store using the **Bitcoin Payments by Speed** plugin.
#### [Benefits of using SpeedCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#benefits-of-using-speed)
  * It enables low-cost, secure, and lightning-fast bitcoin payment processing.
  * There are no setup costs, monthly fees, or hidden costs.
  * It provides robust and adaptable payment processing capabilities.
  * Create your account and start accepting bitcoin / stablecoin payments in no time.
  * Transaction fees are significantly lower (1%) than credit cards (2.9% -3.4%).
  * There is no risk of chargebacks or fraudulent payments.
  * Accept cross-border payments without the involvement of a bank. It's simple to go global with Speed.
  * Speed uses real-time bitcoin prices to save you from losing your revenue.
  * Withdraw your balance instantly in bitcoin, USDT or USDC.


#### [Benefits of using Speed with MagentoCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#benefits-of-using-speed-with-magento)
  * Your customers will have a smooth checkout process.
  * Easy setup. No much coding knowledge required. Connect Speed with your store by simply copying and pasting your secret keys.
  * Integrate quickly by filling in the required details, and your store will be ready to accept payments via Speed.
  * The plugin interface allows you to easily switch your transactions from live mode to test mode or vice versa. It’s a great feature to configure the plugin according to your expectations and validate your transactions before going live.
  * You can also keep track of the order payments regularly on the Speed Web application and get confirmations quickly.


Download it now at: [Magento Marketplace](https://commercemarketplace.adobe.com/tryspeed-magento-payment-plugin.html).
#### [RequirementsCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#requirements)
To install **Bitcoin Payments by Speed** plugin, you need:
  * Magento Open Source Version 2.4 or newer (installed). Tested up to: 2.4.6
  * PHP Version 7.4.29 or newer
  * Speed account. If you don't already have a Speed account, sign up for one here.


#### [InstallationCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#installation)
  1. Log in to Magento Admin.
  2. Go to [Magento Marketplace](https://commercemarketplace.adobe.com/).
  3. Search for **Bitcoin Payments by Speed**. The author is Speed.
  4. Add the plugin to your cart and place an order.
  5. Login to your Adobe account. Make sure it is the same as the Magento admin.
  6. Go to **Marketplace » My Purchases**.
  7. Locate the Speed plugin and note its component-name and version number.
  8. Update the Magento composer.json file by opening the command prompt and running the command “composer require tryspeed/magento-payment-plugin:1.0.0” to add the extension to your site.


#### [Setup and ConfigurationCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#setup-and-configuration)
After installing the **Bitcoin Payments by Speed** plugin, it must be configured.
To configure your **Bitcoin Payments by Speed** plugin, go to **Stores » Configuration » Sales » Payment Methods » Recommended Solutions**. Click `Configure`.
There are 3 types of settings tabs you will find on the Speed Configure page.
  * General
  * Test
  * Live


##### General Settings
The plugin status here will be **enabled** , as the plugin is already activated after installation.
  1. First, you can choose the `transaction mode` here. 
    1. If you want to test payments before accepting real bitcoins / stablecoins, select the transaction mode as Test. You can simulate various payments in test mode.
    2. However, if you want to start accepting payments with Speed, select the live mode and save your changes.Whichever mode you select, you will find the mode displayed on the top-most right corner of the Speed Configure settings page. 
  2. Although Speed by default suggests the `payment method name` and `description`, you can modify them as you see fit.
  3. Next, you will see the `statement descriptor`, which is additional information about a payment made to your account via Speed. You can add a customized one as well.
  4. Enable the logo or no logo button, depending on whether you want your payment page to show the Speed logo or not.


##### Test and Live Settings
Next, let’s fill in the Test and Live settings’ required fields. For Test mode details, make sure you turn on the “Test mode” toggle in [Speed web application.](https://app.tryspeed.com/) For live settings, keep this toggle off.
  1. Enter the Publishable [API keys](https://www.speed.dev/reference/keys) in test mode to configure the **Bitcoin Payments by Speed** with a new or existing Speed account (copy the keys from your [Speed web application](https://app.tryspeed.com/apikeys)) by keeping the toggle on in Speed web application. 
  2. Fill in the **webhook URL** and **Webhook Test Signing Secret Key**. Click [here](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#webhooks) for more instructions.
  3. Click on the `Test Connection` to see if Test / Live keys provided establish a successful connection or not. As this would be required to connect your website to your Speed account.


##### Webhooks
Webhooks will help keep the communication between Speed and your site synchronized. It provides information such as whether the payment is received or not and is used to update the orders based on certain events.Let us see the steps to enable webhooks for your Magento website.
  * Head to **Stores » Configuration » Sales » Payment methods » Bitcoin Payments by Speed**. Click Configure to configure your **Bitcoin Payments by Speed** settings. Under the  _Live/Test settings_ section, you’ll find a webhook endpoint URL ready for you to copy and paste into your Speed web application. 
  * Log into your [Speed](https://app.tryspeed.com/dashboard) web application with your login credentials.
  * Navigate to [Dashboard → Developers → Webhooks.](https://app.tryspeed.com/webhooks) (with “Test mode” enabled or disabled, depending on which mode is being configured).
  * On the left sidebar, click `Add endpoint`.
  * _Paste_ the webhook endpoint URL you copied earlier into the `Endpoint URL` field, and enter a `description`.
  * Select the `version` of your choice.
  * Click next. You will see a list of events. Select your desired events. Make sure to select the following events at a minimum.
  * For example, you must select below given events, 
    * `Checkout_session.paid`
    * `Checkout_session.created`
    * `Checkout_session.payment_paid`
  * After selecting events, you can see the selected ones in the sample endpoint code on the Speed web application.
  * Click Add endpoint. This will take you to the webhook detail page, where you can find the webhook endpoint status, secret, id, and many other details.
  * _Copy_ the Signing secret (wsec_xxxxxxxxxxxxxxxxxxxx) after clicking Reveal.
  * Back in **Stores » Configuration » Sales » Payment Methods » Speed » Test/Live Settings** ,  _paste_ the secret into the **Webhook Signing Secret Key** field. 
  * Test your connection, and if it is successful then you are good to go using Speed at your website.
  * If this was done in test mode, repeat the process after switching to live mode.


#### [Accept Speed Bitcoin at CheckoutCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#accept-speed-bitcoin-at-checkout)
Your customers can easily complete their payment by selecting the **Bitcoin Payments by Speed** option on your store, as shown below. At checkout when the customer selects **Bitcoin Payments by Speed** payment, they will be redirected to the Speed payment page to complete the crypto transaction.
On the Speed payment page, customers can make payments in bitcoin / stablecoin via the Lightning / Ethereum / Tron / Solana Network. Learn more about each payment method [here](https://docs.tryspeed.com/docs/receive-payments/overview/#payment-methods). Customers who choose to pay via bitcoin / ethereum / tron / solana can make partial payments for their orders.
When a customer makes a partial payment, the order status will be pending. The customer can make the remaining payment on the same on-chain / etehreum/ tron / solana address or the Lightning Network using the QR code on the Speed payment page. The same Speed payment page can be generated by going back to the cart (without updating it) and then selecting the **Bitcoin Payments by Speed** payment option at checkout. This will take the customer back to the same payment page where they can make the remaining partial payment.
If a customer clicks back on the Speed payment page, they will be redirected to the cart page of your Magento store with the cart retained.
# Table of contents
[Benefits of using Speed](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#benefits-of-using-speed)[Benefits of using Speed with Magento](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#benefits-of-using-speed-with-magento)[Requirements](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#requirements)[Installation](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#installation)[Setup and Configuration](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#setup-and-configuration)[Accept Speed Bitcoin at Checkout](https://docs.tryspeed.com/docs/receive-payments/plugins/magento-2#accept-speed-bitcoin-at-checkout)
/docs/receive-payments/plugins/magento-2
