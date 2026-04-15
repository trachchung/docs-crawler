<!-- Source: https://docs.neox.vn/docs/collections/refund-request-management/webhook -->

**Event data**
Parameter
Data Type
Description
merchantCode
String
Merchant Code
requestId
String
The requestId when creating refund request.
type
String
Webhook type: Default value "REFUND"
collectionTransId
String
Collection's TransactionId of current refund request
approvalStatus
String
Refund request status, Include: PENDING: Refund request is waiting for approval. APPROVED: Refund request was approved. REJECTED: Refund request was rejected.
status
String
Refund transaction status, Include: SUCCESS: Refund transaction was successful FAILED: Refund transaction was failed
bankSwiftCode
String
Refund/Remitout bank swift code.
bankAccountNumber
String
Refund to bank acount number
bankAccountName
String
Refund to bank acount name.
amount
Number
Amount of refund request in VND
note
String
Note for refund request
failedReason
String
Return failed reason from banking system if refund transaction was failed
createdAt
Datetime String (ISO 8601)
Record created time
secureHash
String
(Base64)
Use SHA256 to hash the above parameters (Not include optional params) (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the Collection service menu)
### 
Sample data
Copy
```
"merchantCode":"FVPLLB",
"requestId":"REFUND-629570097321",
"collectionTransId":"FT193341033222",
"amount":123456,
"bankSwiftCode":"MCOBVNVX",
"bankAccountNumber":"9698890000",
"bankAccountName":"SUMTING WONG",
"status":"PROCESSING",
"approvalStatus":"PENDING",
"createdAt":"2025-05-26T02:43:45.689Z",
"note":"Test create refund request",
"secureHash":"vNWPuLtvgzXpB5GKqQPyZEpM+Dbohf2wGjN2/8ho6e4="

```

With the secretKey "SumtingWong@123", the string used to create secureHash will be:
Copy
```
123456PENDINGSUMTING WONG9698890000MCOBVNVXFT193341033222FVPLLBTest create refund requestREFUND-629570097321PROCESSINGREFUNDSumtingWong@123
```

[PreviousRefund Request Managementchevron-left](https://docs.neox.vn/docs/collections/refund-request-management)[NextWithdraw Request Managementchevron-right](https://docs.neox.vn/docs/collections/withdraw-request-management)
Last updated 10 months ago
Was this helpful?
