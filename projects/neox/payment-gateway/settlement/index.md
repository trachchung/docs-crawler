<!-- Source: https://docs.neox.vn/docs/payment-gateway/settlement -->

Merchant has a (T) settlement period and start time of (T). The (T) will be configured by NeoX.
**Conditions:** merchant has at least one successful reconciliation in the settlement period.
Ex: the (T) is 3 days and start time is 10th October. All successful reconciliations are from 10th October - 13th October, they will be settled on 13th October.
**Settlement Process:**
  * The reconciliations' status will be changed to "**Paid".**
  * The Merchant wallet will be plus reconciliations' amount.


To check the reconciliations have **"Paid"** status, **choose Payment gateway** , then choose **Reconciliation report.**
To check the settlement, choose **Merchant Wallet** and then check records with **"Revenue settlement"** type
[PreviousReconciliationchevron-left](https://docs.neox.vn/docs/payment-gateway/reconciliation)[NextDisbursementchevron-right](https://docs.neox.vn/docs/disbursement)
Last updated 3 years ago
Was this helpful?
