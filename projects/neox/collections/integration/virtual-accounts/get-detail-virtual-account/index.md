<!-- Source: https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-detail-virtual-account -->

  * **Purpose** : This is the API used to get detail of virtual account by The ID of seller/business is provided by merchant.
  * **API** :
    * Path: _**v2/col/virtual-accounts/:virtualAccountRequestId**_
    * Method: _**GET**_
    * Request: Content-Type: _**application/json**_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
virtualAccountRequestId
String
The ID of seller/business is provided by merchant.
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
Refer to [GetDetailVirtualAccountResponse](https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-detail-virtual-account#getdetailvirtualaccountresponse).
neoResponseId
String
The ID of NeoX response.
#### 
GetDetailVirtualAccountResponse
Parameter
Data Type
Description
merchantCode
String
Merchant Code
merchantId
String
Merchant Id
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
accountAddress
String
Virtual Account address.
bankId
String
The bank swiftcode of virtual account.
bankName
String
The bank name of virtual account.
qrText
String
Napas QR Code plain data for virtual account.
status
String
Virtual account active status, include: ACTIVE: Virtual account has been actived and can be used. INACTIVE: Virtual account has been inactived and can not be used.
authorizeStatus
String
Virtual account authorize status, Include: UNAUTHORIZED: KYC/KYB documents for VA were not uploaded. PENDING: KYC/KYB documents for VA were uploaded, waiting to verify. AUTHORIZED: KYC/KYB documents for VA have been approved. REJECTED: KYC/KYB documents for VA have been rejected.
serviceInfomation
Object
Refer to 
profileData
Object
Refer to 
note
String
Note for current virtual account.
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI get list virtual accountschevron-left](https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-list-virtual-account)[NextAPIs for transactions managementchevron-right](https://docs.neox.vn/docs/collections/integration/transactions)
Last updated 9 months ago
Was this helpful?
