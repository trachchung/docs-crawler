<!-- Source: https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## WooCommerce
Accepting bitcoin and stablecoin payments online has never been easier. You can accept bitcoin payments directly from your store using the **WooCommerce Bitcoin Payment - Speed** plugin.
#### [Benefits of using SpeedCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#benefits-of-using-speed)
  * It enables low-cost, secure, and lightning-fast bitcoin payment processing.
  * There are no setup costs, monthly fees, or hidden costs.
  * It provides robust and adaptable payment processing capabilities.
  * Create your account and start accepting bitcoin or stablecoin payments in no time.
  * Transaction fees are significantly lower (1%) than credit cards (2.9% -3.4%).
  * There is no risk of chargebacks or fraudulent payments.
  * Accept cross-border payments without the involvement of a bank. It's simple to go global with Speed.
  * Speed uses real-time bitcoin prices to save you from losing your revenue.
  * Withdraw your balance instantly in bitcoin, USDT or USDC.


#### [Benefits of using the Speed Woocommerce pluginCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#benefits-of-using-the-speed-woocommerce-plugin)
  * Your customers will have a smooth checkout process.
  * Easy setup. No need for coding. Connect Speed with your store by simply copying and pasting your secret keys.
  * Integrate quickly by filling in the required details, and your store will be ready to accept payments via Speed.
  * The plugin interface allows you to easily switch your transactions from live mode to test mode or vice versa. It’s a great feature to configure the plugin according to your expectations and validate your transactions before going live.
  * You can also keep track of the order payments regularly on the Speed Web application and get confirmations quickly.


Download it now at: [WordPress.org](https://wordpress.org/plugins/speed-accept-bitcoin-payments/) or via the **`Add New`**option under**Plugins** on your site. For full details of updates, please see the [Changelog](https://wordpress.org/plugins/speed-accept-bitcoin-payments/#developers).
#### [RequirementsCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#requirements)
To install **WooCommerce Bitcoin Payment - Speed** Plugin, you need:
  * WordPress Version 4.0 or newer (installed). Tested up to: 5.9.3
  * WooCommerce Version 3.9 or newer (installed and activated)
  * PHP Version 7.4.29 or newer
  * Speed account. If you don't already have a Speed account, sign up for one here.


#### [InstallationCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#installation)
  1. Log in to WordPress Admin.
  2. Go to **Plugins >** **`Add New`**.
  3. Search for the **WooCommerce Bitcoin Payment - Speed** plugin. The author is Speed.
  4. Click on `Install Now` and wait until the plugin is installed successfully.
  5. You can activate the plugin immediately by clicking on `Activate now`on the success page. If you want to activate it later, you can do so via **Plugins > Installed Plugins**.


To learn more, see **[Installing and Managing Plugins](https://codex.wordpress.org/Managing_Plugins#Installing_Plugins).**
#### [Setup and ConfigurationCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#setup-and-configuration)
After installing the **WooCommerce Bitcoin Payment - Speed** plugin, it must be enabled and configured.
To configure your Speed Bitcoin plugin, go to **WooCommerce > Settings > Payments > Speed**.Click `Finish setup`.
##### Step 1- Users connects Speed
  * Users to click on the “**Connect Speed** ” button. 
  * Users are redirected to Speed for the login. 
  * Users select the account to connect, either an existing one or creating a new one. 
  * Upon account selection, the Speed system will showcase the list of permissions requested by you while registering it with Speed. 
  * Once permissions are granted, Speed provides a restricted key for both Test mode and Live mode. 
  * If permissions are denied, users are redirected back to the WooCommerce store.


##### Step 2- Plugin Settings
After the restricted keys are generated, you will be redirected to the store, where the keys will be processed to connect your Speed account. 
The Plugin status here will read `enabled` if you activate the plugin after installation.
  1. **Transaction mode:** If you want to test payments before accepting real bitcoins / stablecoins, select the transaction mode as **Test**. You can simulate various payments in test mode. However, if you want to start accepting payments with Speed, select the **Live** mode and save your changes.
  2. **Payment Method Name:** You have the flexibility to customize the payment method name, which will be displayed in the payment method section of the checkout page.
  3. **Statement descriptor:** You can customize the statement descriptor, which will appear on the customer's wallet when initiating the payment.
  4. **Description:** You can customize the description which will appear in the payment method section during checkout.
  5. **Logo:** You can choose whether to display the Speed logo on your payment page. Simply enable or disable the logo button according to your preference.
  6. **Order status settings:** When an order is initially created, its status is set to **Payment Pending**. Once your customer completes the payment, the order status automatically changes to **Processing**. This default behavior can be customized based on your preferences. 
You can select the order status of your choice from the following three options to indicate that the customer has made the payment:
    1. **Processing**
    2. **On-hold**
    3. **Completed**
Simply choose the order status that best fits your workflow and update the settings accordingly.


Check all the details are filled in, and click `Connect and Save Changes`.
Once you click `Save Changes` webhooks will be generated and your Speed account will be connected.
#### [Accept Speed Bitcoin at CheckoutCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#accept-speed-bitcoin-at-checkout)
Your customers can easily complete their payment by selecting the Speed - Bitcoin payment option on your store, as shown below. At checkout when the customer selects Speed Bitcoin payment, they will be redirected to the Speed payment page to complete the crypto transaction.
On the Speed payment page, customers can make payments on-chain, ethereum, solana, tron or via the Lightning Network depending on the payment method’s setting in the Speed merchant account. Learn more about each payment method [here](https://docs.tryspeed.com/docs/receive-payments/overview). Customers who choose to pay on-chain, ethereum, solana or tron can make partial payments for their orders.
When a customer makes a partial payment, the order status will be `payment pending`. The customer can make the remaining payment on the same on-chain / ethereum / solana / tron address or the Lightning Network using the QR code on the Speed payment page. The same Speed payment page can be generated by going back to the cart (without updating it) and then selecting the Speed payment option at checkout. This will take the customer back to the same payment page where they can make the remaining partial payment.
If a customer clicks back on the Speed payment page, they will be redirected to the cart page of your WooCommerce store.
#### [ChangelogCopied!](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#changelog)
  * [Click here to see the latest upgrades.](https://wordpress.org/plugins/speed-accept-bitcoin-payments/#developers)


# Table of contents
[Benefits of using Speed](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#benefits-of-using-speed)[Benefits of using the Speed Woocommerce plugin](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#benefits-of-using-the-speed-woocommerce-plugin)[Requirements](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#requirements)[Installation](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#installation)[Setup and Configuration](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#setup-and-configuration)[Accept Speed Bitcoin at Checkout](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#accept-speed-bitcoin-at-checkout)[Changelog](https://docs.tryspeed.com/docs/receive-payments/plugins/woocommerce#changelog)
/docs/receive-payments/plugins/woocommerce
