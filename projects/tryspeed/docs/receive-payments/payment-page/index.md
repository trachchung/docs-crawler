<!-- Source: https://docs.tryspeed.com/docs/receive-payments/payment-page -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Payment Page
The payment page is displayed when the customer initiates the payment via a checkout session, opens the checkout link, payment link, invoice, or is looking for a withdrawal.
It means this is the page where customers scan the QR code to either make the payment or receive the payment.
Within this page
  * To make the BTC payment, the LN invoice for lightning transactions and the on-chain address for on-chain payment are shown in the form of a QR code. Similarly, lightning invoice, Ethereum address, Solana address and the Tron address for USDT and lightning invoice, Ethereum address and Solana address are shown as QR code to make USDC payment.
  * To receive the payment via a withdrawal link, a LNURL withdrawal is shown in the form of a QR code.


Each payment page encompasses the following elements:
  1. The checkout session
  2. The payment payload (either to make or receive the payment)
  3. The branding configuration (set for each Speed account separately)


#### [Checkout sessionCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-page#checkout-session)
The checkout session is responsible for consistently renewing the payment upon its expiry due to TTL exceeds. When payment is received for any amount, it will be marked as 'paid’. Additional information about the attributes of the checkout session is available [here](https://docs.tryspeed.com/docs/receive-payments/checkout-session).
#### [Payment payloadCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-page#payment-payload)
The BTC payment payload includes the LN invoice for lightning payments and the on-chain address for on-chain transactions. Similarly for USDT and USDC payments, the payload includes the lightning invoice, Ethereum address, Solana address or Tron address based on the payment method.
You can read more about payments [here](https://docs.tryspeed.com/docs/receive-payments/payment).
#### [Branding configurationCopied!](https://docs.tryspeed.com/docs/receive-payments/payment-page#branding-configuration)
You have the flexibility to personalize the appearance of the payment page your customer will see by accessing Business Settings > Branding:
  1. Upload a logo or icon of your choice.
  2. Select your preference between using the logo or the icon.
  3. Tailor the background color of the payment page by inputting the hex code for the desired color.
  4. Choose the font family that you would like to use.


You'll observe that any adjustments you make will be reflected in real time, providing you with the ability to preview the appearance of the payment page on both web and mobile platforms.
Utilize the branding feature to customize the visual representation of the checkout link, payment link, QR code, withdrawal link, invoice PDF, and invoice payment page. Once the branding is configured, you can preview the appearance to gain a clear understanding of how it will be presented to your customers.
# Table of contents
[Checkout session](https://docs.tryspeed.com/docs/receive-payments/payment-page#checkout-session)[Payment payload](https://docs.tryspeed.com/docs/receive-payments/payment-page#payment-payload)[Branding configuration](https://docs.tryspeed.com/docs/receive-payments/payment-page#branding-configuration)
/docs/receive-payments/payment-page
