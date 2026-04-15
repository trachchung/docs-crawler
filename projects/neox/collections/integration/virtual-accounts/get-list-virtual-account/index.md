<!-- Source: https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-list-virtual-account -->

  * **Purpose** : This is the API used to get list virtual accounts.
  * **API** :
    * Path: _**v2/col/virtual-accounts**_
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
To filter virtual account list by status
authorizeStatus
String
To filter virtual account list by authorize status
requestId
String
To filter virtual account list by requestId when create VA
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
  "docs": Array of GetListVirtualAccountsResponse

```

Ref to [GetListVirtualAccountsResponse](https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-list-virtual-account#getlistvirtualaccountsresponse) object.
message
String
Error description
neoResponseId
String
The ID of NeoX response
#### 
GetListVirtualAccountsResponse
Parameter
Data Type
Description
merchantCode
String
Merchant Code
requestId
String
The requestId when creating virtual account.
virtualAccountRequestId
String
The ID of seller/business is provided by merchant.
bankAccountNumber
String
Virtual Account number.
accountName
String
Virtual Account name.
bankId
String
The bank swiftcode of virtual account.
status
String
Virtual account active status, include: ACTIVE: Virtual account has been actived and can be used. INACTIVE: Virtual account has been inactived and can not be used.
authorizeStatus
String
Virtual account authorize status, Include: PENDING_KYC: KYC/KYB documents for VA were not uploaded. VERIFYING: KYC/KYB documents for VA were uploaded, waiting to verify. APPROVED: KYC/KYB documents for VA have been approved. REJECTED: KYC/KYB documents for VA have been rejected
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI set active/inactive Virtual Accountchevron-left](https://docs.neox.vn/docs/collections/integration/virtual-accounts/set-active-virtual-account)[NextAPI get detail virtual accountchevron-right](https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-detail-virtual-account)
Last updated 9 months ago
Was this helpful?
