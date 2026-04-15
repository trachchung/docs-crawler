<!-- Source: https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-kyc-virtual-account-information -->

  * This is the API used to update KYC virtual account information.


### 
Sequence Diagram
  * API:
    * Path: _v2/col/merchantVirtualAccounts_ OR _v2/col/virtual-accounts_
    * Method: _PUT_
    * Request: Content-Type: _application/json_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
virtualAccountRequestId
String
The ID of seller/business is provided by merchant
accountName
String
The name of seller/business is provided by merchant
accountAddress
String
The address of account.
(Includes the district, province)
frontIdCard
String
The photo of the front of the ID card
backIdCard
String
The photo of the back of the ID card
profileImg
String
The portrait
businessRegistration
String
The file of the business license.
profileData
Object
Virtual account profile data. Refer: 
### 
**Response Data**
Parameter
Data Type
Description
code
Number
Error code, refer to [table of error codesarrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/virtual-accounts/error-codes.md).
message
String
Error description.
data
Object
Refer to [UpdateVirtualAccountsResponse](https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-kyc-virtual-account-information#updatevirtualaccountresponse)
neoResponseId
String
The ID of NeoX response
#### 
UpdateVirtualAccountResponse
Parameter
Data Type
Description
requestId
String
The ID of the request.
virtualAccountRequestId
String
The ID of seller/business is provided by merchant.
[PreviousAPI create list of virtual accountschevron-left](https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-create-list-of-virtual-accounts)[NextAPI update Virtual Account transaction data from merchantchevron-right](https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-virtual-account-transaction-data-from-merchant)
Last updated 9 months ago
Was this helpful?
