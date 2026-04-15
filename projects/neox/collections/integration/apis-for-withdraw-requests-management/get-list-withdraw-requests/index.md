<!-- Source: https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-withdraw-requests -->

  * **Purpose** : This is the API used to get list withdraw requests.
  * **API** :
    * Path: _**v2/col/withdraw-requests**_
    * Method: _**GET**_
    * Request: Content-Type: _**application/json**_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
pageIndex
Number
Pagination index (start from 1, default value is 1)
pageSize
Number
Current Page size (Default value is 20, maximum value is 500)
dateFr
Datetime String (ISO 8601)
Get records created from date
dateTo
Datetime String (ISO 8601)
Get records created to date
status
String
To filter withdraw list by status
### 
**Response Data**
Parameter
Data Type
Description
code
Number
Error code, refer to .
data
Object
Return Object as follow:
Copy
```
  "totalDocs": Number, // Total records base on request params
  "totalPages": Number, // Total pages base on request pageSize
  "docs": Array of GetListWithdrawRequestsResponse

```

Ref to [GetListWithdrawRequestsResponse](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-withdraw-requests#getlistwithdrawrequestsresponse) object.
message
String
Error description
neoResponseId
String
The ID of NeoX response
#### 
GetListWithdrawRequestsResponse
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
Amount of payout/remitout request in VND.
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
approvalStatus
String
Withdraw/Remitout request status, Include: PENDING: Withdraw request is waiting for approval. APPROVED: Withdraw request was approved. REJECTED: Withdraw request was rejected.
status
String
Withdraw/Remitout transaction status, Include: PROCESSING: Withdraw transaction is being processed. SUCCESS: Withdraw transaction was successful. FAILED: Withdraw request was failed.
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI create withdraw requestchevron-left](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/create-withdraw-request)[NextAPI get detail withdraw requestchevron-right](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-detail-withdraw-request)
Last updated 8 months ago
Was this helpful?
