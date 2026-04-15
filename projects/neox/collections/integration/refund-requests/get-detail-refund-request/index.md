<!-- Source: https://docs.neox.vn/docs/collections/integration/refund-requests/get-detail-refund-request -->

  * **Purpose** : This is the API used to get detail of refund request by with requestId provided by merchant.
  * **API** :
    * Path: _**v2/col/refund-requests/:requestId**_
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
The requestId when merchant create refund request.
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
Refer to [GetDetailRefundRequestResponse](https://docs.neox.vn/docs/collections/integration/refund-requests/get-detail-refund-request#getdetailrefundrequestresponse).
neoResponseId
String
The ID of NeoX response.
#### 
GetDetailRefundRequestResponse
Parameter
Data Type
Description
merchantCode
String
Merchant Code
requestId
String
The requestId when creating refund request.
collectionTransId
String
ID of collection transaction being refunded.
refundTransId
String
ID of refund transaction from NeoX.
(Will be returned when refund request was approved)
amount
Number
Refund amount.
bankSwiftCode
String
Refund request to bank swiftcode
bankAccountNumber
String
Refund request to bank account number
bankAccountName
String
Refund request to bank account name
bankBranch
String
Refund request to bank branch
approvalStatus
String
Refund request status, Include: PENDING: Refund request is waiting for approval. APPROVED: Refund request was approved. REJECTED: Refund request was rejected.
status
String
Refund transaction status, Include: PROCESSING: Refund transaction is being processed SUCCESS: Refund transaction was successful FAILED: Refund transaction was failed
note
String
Note for current refund request.
failedReason
String
Return failed reason from banking system if refund transaction was failed
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI get list refund requestschevron-left](https://docs.neox.vn/docs/collections/integration/refund-requests/get-list-refund-requests)[NextAPIs for withdraw requests managementchevron-right](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management)
Last updated 9 months ago
Was this helpful?
