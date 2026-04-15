<!-- Source: https://docs.neox.vn/docs/collections/integration/refund-requests/get-list-refund-requests -->

  * **Purpose** : This is the API used to get list refund requests.
  * **API** :
    * Path: _**v2/col/refund-requests**_
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
To filter refund request list by status
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
  "docs": Array of GetListRefundRequestsResponse

```

Ref to [GetListRefundRequestsResponse](https://docs.neox.vn/docs/collections/integration/refund-requests/get-list-refund-requests#getlistrefundrequestsresponse) object.
message
String
Error description
neoResponseId
String
The ID of NeoX response
#### 
GetListRefundRequestsResponse
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
status
String
Refund request status, include: PENDING: Refund request has been created and waiting for approval. APPROVED: Refund request has been approved. REJECTED: Refund request has been rejected, view note for reject reasons.
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI create refund requestchevron-left](https://docs.neox.vn/docs/collections/integration/refund-requests/create-refund-request)[NextAPI get detail refund requestchevron-right](https://docs.neox.vn/docs/collections/integration/refund-requests/get-detail-refund-request)
Last updated 1 year ago
Was this helpful?
