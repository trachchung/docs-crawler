<!-- Source: https://docs.neox.vn/docs/collections/integration/virtual-accounts/set-active-virtual-account -->

  * This is the API used to update KYC virtual account information.
  * API:
    * Path: _v2/col/virtual-accounts/:virtualAccountRequestId/setActive_
    * Method: _PUT_
    * Request: Content-Type: _application/json_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
isActive
boolean
true: to set active virtual account
false: to set inactive virtual account
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
neoResponseId
String
The ID of NeoX response.
[PreviousAPI update Virtual Account transaction data from merchantchevron-left](https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-virtual-account-transaction-data-from-merchant)[NextAPI get list virtual accountschevron-right](https://docs.neox.vn/docs/collections/integration/virtual-accounts/get-list-virtual-account)
Last updated 11 months ago
Was this helpful?
