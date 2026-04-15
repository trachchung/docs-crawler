<!-- Source: https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/create-withdraw-request -->

  * This is the API used to create withdraw request.
  * API:
    * Path: _v2/col/withdraw-requests_
    * Method: _POST_
    * Request: Content-Type: _application/json_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
requestId
String
Withdraw config request id from merchant
bankConfigId
String
The ID of withdraw bank config get from API Get List Withdraw Bank Configs
amount
String
Total Withdraw amount.
Used for DOMESTIC withdraw request
requestToCurrency
String (ISO 4217)
Request withdraw to currency. Default value: "VND"
Used for INTERNATIONAL withdraw/remitout request
virtualAccountIds
String Array
List of Virtual Account Number. To create remitout request for all collection transactions of list virtual accounts
Used for INTERNATIONAL withdraw/remitout request
reconcileCodes
String Array
List of reconciliations code. To create remitout request for all collection transactions for settled reconciliations
Used for INTERNATIONAL withdraw/remitout request
collectionTransIds
String Array
List of collection transaction. To create a remitout request for list of Collection Transaction
Used for INTERNATIONAL withdraw/remitout request
_Note: For Remitout/International withdraw request, merchant only need to use 1 in these optional params: virtualAccountIds, reconcileCodes, collectionTransIds. If those params were not used, NeoX System will automatically select all collection transactions that has payoutStatus of "READY" to create withdraw request._
### 
**Response Data**
Parameter
Data Type
Description
code
Number
Error code, refer to .
message
String
Error description.
data
Object
Refer to [CreateWithdrawRequestResponse](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/create-withdraw-request#createwithdrawrequestresponse).
neoResponseId
String
The ID of NeoX response.
#### 
CreateWithdrawRequestResponse
Parameter
Data Type
Description
merchantCode
String
Merchant Code
requestId
String
The requestId when creating withdraw request.
transId
String
ID of withdraw transaction from NeoX.
amount
Number
Amount of withdraw request in VND.
requestToCurrency
String
(Optional) Remitout request currency.
bankSwiftCode
String
Withdraw request to bank swiftcode.
bankAccountNumber
String
Withdraw request to bank account number.
bankAccountName
String
Withdraw request to bank account name.
bankBranch
String
Withdraw request to bank branch.
approvalStatus
String
Withdraw/Remitout request status, Include: PENDING: Withdraw request is waiting for approval. APPROVED: Withdraw request was approved. REJECTED: Withdraw request was rejected.
status
String
Withdraw/Remitout transaction status, Include: PROCESSING: Withdraw transaction is being processed. SUCCESS: Withdraw transaction was successful. FAILED: Withdraw request was failed.
collectionTransactions
Array Object
(Optional) List of Collection transactions envolved to withdraw request. Object data:
Copy
```
  "virtualAccountId": String,
  "reconcileCode": String,
  "transId": String,
  "amount": Number,
  "transDate": String

```

[PreviousAPI get list withdraw bankschevron-left](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-support-withdraw-bank)[NextAPI get list withdraw requestschevron-right](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-withdraw-requests)
Last updated 8 months ago
Was this helpful?
