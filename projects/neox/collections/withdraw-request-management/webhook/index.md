<!-- Source: https://docs.neox.vn/docs/collections/withdraw-request-management/webhook -->

**Event data**
Parameter
Data Type
Description
requestId
String
Withdraw/Remitout request id
type
String
Webhook type: Default value "WITHDRAW"
approvalStatus
String
Withdraw/Remitout request status, Include: PENDING: Withdraw request is waiting for approval. APPROVED: Withdraw request was approved. REJECTED: Withdraw request was rejected.
status
String
Withdraw/Remitout transaction status, Include: PROCESSING: Withdraw transaction is being processed. SUCCESS: Withdraw transaction was successful. FAILED: Withdraw request was failed.
bankSwiftCode
String
Withdraw/Remitout bank swift code.
bankAccountNumber
String
Withdraw/Remitout bank acount number.
bankAccountName
String
Withdraw/Remitout bank acount name.
amount
Number
Amount of withdraw/remitout request in VND
requestToCurrency
String
(Optional) Remitout request currency.
remitedAmount
Number
(Optional) Amount of remitout request in currency
collectionTransactions
Array Object
(Optional) List of Collection transactions envolved to withdraw/remitout request. Object data:
Copy
```
  "virtualAccountId": String,
  "reconcileCode": String,
  "transId": String,
  "amount": Number,
  "transDate": String

```

note
String
Note for withdraw/remitout request
failedReason
String
Return failed reason from banking system if withdraw transaction was failed
secureHash
String
(Base64)
Use SHA256 to hash the above parameters (Not include optional params) (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the Collection service menu)
### 
Sample data
Copy
```
"requestId":"09c7e5b6-bba7-47da-8fda-bf95e6ecac66",
"merchantCode":"COLRLC",
"amount":3000000,
"requestToCurrency":"USD",
"remitedAmount":12341,
"transId":"51CNMDFMJ9MD",
"bankSwiftCode":"HSBCXVXX",
"bankAccountNumber":"ABC123456",
"bankAccountName":"MINH DUC",
"bankBranch":"HSBC Singapore",
"status":"SUCCESS",
"approvalStatus":"APPROVED",
"approvalDate":"2025-07-23T07:10:53.013Z",
"collectionTransactions":[
"virtualAccountId":"902000871135",
"reconcileCode":"TH-18042024-COLRLC",
"transId":"240418ANKRBO",
"amount":5000000,
"transDate":"2024-04-18T09:37:11.688Z"
"createdAt":"2025-07-23T07:10:25.836Z",
"updatedAt":"2025-07-23T07:10:53.065Z",
"note":"One withdraw request please",
"secureHash":"I/M2Y6rsb1x+hImL1fEBr4WHQpk6OJ8jUN4X2F3OM4Q="

```

With the secretKey "SUMTING", the string used to create secureHash will be:
Copy
```
150000STANDARD CHARTERED BANK TEST ACCOUNT0107201111SCBLSG22XXX100000TH-13122024-SUMTIN2024-12-12T02:47:05.409ZFT24323L4AAA9698890002161550000TH-13122024-SUMTIN2024-12-09T02:47:05.409ZFT24323L4ZZZ96988900021615USD5.9125380.71CASHOUT-443826686072PENDINGWITHDRAWSUMTING
```

[PreviousWithdraw Request Managementchevron-left](https://docs.neox.vn/docs/collections/withdraw-request-management)[NextReconciliationchevron-right](https://docs.neox.vn/docs/collections/reconciliation)
Last updated 8 months ago
Was this helpful?
