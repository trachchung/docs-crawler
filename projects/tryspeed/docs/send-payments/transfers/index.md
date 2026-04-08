<!-- Source: https://docs.tryspeed.com/docs/send-payments/transfers -->

All use cases
Receive Payments Overview Payments Create a payment Manage a payment Customize-Payments; Checkout session Create a checkout session Manage Checkout Session Customize checkout session API Elements; Checkout links Create a checkout link Manage checkout links Customize checkout link; Payment links Create a payment link Manage payment links Customize payment link; Payment page Payment page settings; Payrequests Create a payrequest Manage a payrequest Customize Payrequests; Payment Addresses Create a payment address Manage payment addresses; One QRs Create One QR Manage One QRs; Plugins WooCommerce OpenCart Magento 2 Prestashop; Invoicing Create an invoice; Customers Create a customer Manage a customer; Products Create a product Manage Products; Price Create a price Manage price; Connect How connect works Manage Connect; Terminals Create a store Create a terminal Manage terminals; Send Payments Instant payout Create an instant payout; Transfers Cashback Create a cashback Manage cashbacks; Withdrawal links Create a withdrawal link Manage withdrawal links; Withdraw requests Create a withdraw request Manage withdraw requests; Withdraw session Create a withdraw session Manage withdraw sessions; Instant send Create an instant send Manage instant send; After the Payments Transactions Business Operations Build a team Account Ownership Transfer; Custom domain Email Checkout Payment address; Affiliate partners Accepting affiliate invite Managing affiliate settings; Payout Scheduling Create a Payout Schedule Manage a Payout Schedule; Search Tips Notification preferences
## Transfers
Utilize Speed Transfers to move your balance from one Speed account to another. It makes it easier to manage your finances. You can consolidate your funds into one same account. This will make your finances simpler and easier to track. If you require funds in a specific account for various activities such as bill payments, purchases, or expenses, you can utilize transfers to ensure the availability of necessary funds in that particular account.
#### [How transfer works?Copied!](https://docs.tryspeed.com/docs/send-payments/transfers#how-transfer-works?)
If a transfer is currently processing in an account and another transaction (credit or debit) is requested simultaneously, the new transaction will not be processed until the current transfer is completed. This means that such a newer transaction would fail and prompt you with an error.
Also, If the ongoing transfer fails for any reason, the withdrawal will be reversed, and the transfer amount will be restored to the account balance.
#### [What is the process for transferring funds between two Speed accounts?Copied!](https://docs.tryspeed.com/docs/send-payments/transfers#what-is-the-process-for-transferring-funds-between-two-speed-accounts?)
  * Login to your [Speed](https://app.tryspeed.com/) account.
  * Go to [Transfers](https://app.tryspeed.com/transfers).
  * Click on `Create New`.
  * Enter the Transfer details as below:
    * **From Account:** This is your account's ID from which you intend to transfer the balance. It is already filled in and cannot be modified.
    * **Destination Account:** This is the account ID of the account to which you intend to transfer the balance. For your convenience, if you wish to transfer funds to your own Speed accounts, you can select the account id from the provided list. If you prefer to transfer to any other Speed merchant account, simply input their associated account ID, and the transfer will be initiated. You can find the account id from**Settings > Profile Settings > Associated Accounts.**
      * The transfer of funds can only occur between any Speed merchant accounts.
      * You cannot transfer from and to the same account. 
    * Description: You may enter an optional description regarding the transfer in the provided field.
    * Transfer Amount: Please input the desired amount in SATS for the transfer to the other account.
      * To initiate a transfer from your Speed business account, a minimum of 1 SATS is required.
      * You can transfer funds from your Speed business account until the available balance reaches zero. This means that the maximum amount that can be transferred is equal to the available balance in your Speed account.


> The transfer takes place in real time. Therefore, during the transfer process, the system verifies whether the account being used has sufficient funds by comparing the entered amount to be transferred with the actual account balance.
#### [View your Transfer detailsCopied!](https://docs.tryspeed.com/docs/send-payments/transfers#view-your-transfer-details)
You can access the details of the transfers sent or received by your Speed account for future reference in the [Transfers](https://app.tryspeed.com/transfers) section. The details available in this section include the following:
  * Transfer ID: The unique ID of the transfer.
  * From Account: The account ID of the sender’s account.
  * Destination Account: The account ID of the receiver’s account.
  * Type: Transfer has 2 types: 
    * Transfer Out: Transfer has this type when the amount is sent from your account. This is of debit type.
    * Transfer In: Transfer has this type when the amount is received by your account. This is of credit type.
  * Transfer Amount: The amount (in SATS) that has been transferred or received.
  * Created on: The date and time when the transfer was initiated.


# Table of contents
[How transfer works?](https://docs.tryspeed.com/docs/send-payments/transfers#how-transfer-works?)[What is the process for transferring funds between two Speed accounts?](https://docs.tryspeed.com/docs/send-payments/transfers#what-is-the-process-for-transferring-funds-between-two-speed-accounts?)[View your Transfer details](https://docs.tryspeed.com/docs/send-payments/transfers#view-your-transfer-details)
/docs/send-payments/transfers
