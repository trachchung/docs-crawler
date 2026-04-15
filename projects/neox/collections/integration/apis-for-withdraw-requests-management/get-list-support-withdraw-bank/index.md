<!-- Source: https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-support-withdraw-bank -->

  * **Purpose** : This is the API used to get list approved withdraw bank configs.
  * **API** :
    * Path: _**v2/col/withdraw-bank-configs**_
    * Method: _**GET**_
    * Request: Content-Type: _**application/json**_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
withdrawType
String
Get list approved withdraw bank configs, inclue INTERNATIONAL: Supported international remitout banks. DOMESTIC: local banks in Vietnam.
### 
**Response Data**
Parameter
Data Type
Description
code
Number
Error code, refer to .
data
Array
Return Array object of GetListWithdrawBanksResponse. Ref to [GetListWithdrawBanksResponse](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-list-support-withdraw-bank#getlistwithdrawbanksresponse) object.
message
String
Error description
neoResponseId
String
The ID of NeoX response
#### 
GetListWithdrawBanksResponse
Parameter
Data Type
Description
id
String
Bank config id
bankSwiftCode
String
Bank swiftcode.
bankName
String
Bank name
bankBranch
String
Bank branch
bankAccountNumber
String
Bank account number
bankAccountName
String
Bank account name
[PreviousAPIs for withdraw requests managementchevron-left](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management)[NextAPI create withdraw requestchevron-right](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/create-withdraw-request)
Last updated 1 year ago
Was this helpful?
