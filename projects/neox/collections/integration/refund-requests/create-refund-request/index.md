<!-- Source: https://docs.neox.vn/docs/collections/integration/refund-requests/create-refund-request -->

  * This is the API used to create refund request.
  * API:
    * Path: _v2/col/refund-requests_
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
Refund request id from merchant
collectionTransId
String
ID of collection transaction being refunded.
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
Refer to [CreateRefundRequestResponse](https://docs.neox.vn/docs/collections/integration/refund-requests/create-refund-request#createrefundrequestresponse).
neoResponseId
String
The ID of NeoX response.
#### 
CreateRefundRequestResponse
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
[PreviousAPIs for refund requests managementchevron-left](https://docs.neox.vn/docs/collections/integration/refund-requests)[NextAPI get list refund requestschevron-right](https://docs.neox.vn/docs/collections/integration/refund-requests/get-list-refund-requests)
Last updated 10 months ago
Was this helpful?
