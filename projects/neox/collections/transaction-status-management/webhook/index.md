<!-- Source: https://docs.neox.vn/docs/collections/transaction-status-management/webhook -->

, 
### 
**Sequence Diagram**
**Event data**
Parameter
Data Type
Description
transId
String
The ID of transaction.
type
String
TRANSACTION_STATUS
transDate
String
The time of transaction.
virtualAccountId
String
The ID of virtual account.
accountName
String
The account name.
amount
Number
The amount of collection transaction.
note
String
Note.
status
String
Transaction status
reconcileStatus
String
Transaction reconcile status, Include: UPLOADED: Documents for transaction were uploaded, waiting for verifying APPROVED: Transaction documents were verified REJECTED: Transaction documents were verified has been rejected. RECONCILED: Transaction was reconconciled SETTLED: Transaction was settled
payoutStatus
String
Transaction payout status, Include: READY: Transaction was settled and ready for Remitout (Appear when reconcileStatus change to "SETTLED"). PROCESSING: Remitout/Payout request is processing. REJECTED: Remitout/Payout request has been rejected. SUCCESS: Remitout/Payout request has success.
serviceInformation
Object
Extra data includes "code", "groupId", "desc"
secureHash
String
(Base64)
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the Collection service menu)
### 
Sample data
Copy
```
"transId":"FT246560944209",
"type":"TRANSACTION_STATUS",
"merchantCode":"UFLIYL",
"transDate":"2023-10-10T07:06:37.436Z",
"virtualAccountId":"NEO0001675",
"accountName":"HIEP HOANG H",
"amount":20000,
"note":"",
"status":"SUCCESS",
"reconcileStatus":"SETTLED",
"payoutStatus":"READY",
"serviceInformation":{
"code":"GRAB",
"desc":"TEST",
"groupId":"DRIVER"

```

With the secretKey "SUMTING", the string used to create secureHash will be:
Copy
```
HIEP HOANG H20000UFLIYLREADYSETTLEDGRABTESTDRIVERSUCCESS2023-10-10T07:06:37.436ZFT246560944209TRANSACTION_STATUSNEO0001675SUMTING
```

[PreviousTransaction Status Managementchevron-left](https://docs.neox.vn/docs/collections/transaction-status-management)[NextRefund Request Managementchevron-right](https://docs.neox.vn/docs/collections/refund-request-management)
Last updated 1 year ago
Was this helpful?
