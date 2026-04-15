<!-- Source: https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-detail-withdraw-request -->

  * **Purpose** : This is the API used to get detail of withdraw request with requestId provided by merchant.
  * **API** :
    * Path: _**v2/col/withdraw-requests/:requestId**_
    * Method: _**GET**_
    * Request: Content-Type: _**application/json**_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
requestId
String
The requestId when merchant create withdraw request.
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
Refer to [GetDetailWithdrawRequestResponse](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-detail-withdraw-request#getdetailwithdrawrequestresponse).
neoResponseId
String
The ID of NeoX response.
#### 
GetDetailWithdrawRequestResponse
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
remitedAmount
Number
(Optional) Amount of remitout request in currency.
fxRate
Number
(Optional) Foreign exchange rate for remitout request.
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
(Optional) Withdraw request to bank branch.
approvalStatus
String
Withdraw/Remitout request status, Include: PENDING: Withdraw request is waiting for approval. APPROVED: Withdraw request was approved. REJECTED: Withdraw request was rejected.
status
String
Withdraw/Remitout transaction status, Include: PROCESSING: Withdraw transaction is being processed. SUCCESS: Withdraw transaction was successful. FAILED: Withdraw request was failed.
approvalDate
Datetime String (ISO 8601)
(Optional) Date of approval from NeoX.
(Will be returned when withdraw request was approved)
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

note
String
Note for current withdraw request.
failedReason
String
Return failed reason from banking system if withdraw transaction was failed
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI get list withdraw requestschevron-left](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-withdraw-requests)[NextEvent Notificationchevron-right](https://docs.neox.vn/docs/collections/integration/event-notification)
Last updated 8 months ago
Was this helpful?
