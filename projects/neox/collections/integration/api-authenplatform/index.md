<!-- Source: https://docs.neox.vn/docs/collections/integration/api-authenplatform -->

  * PLATFORM should call this API to get Bearer token to use in all other APIs.
  * Authentication mechanism: OAuth 2.0
  * API:
    * Path: _/v2/auth/oauth2/token_
    * Method: _POST_
    * Request: Content-Type: _application/json_


**Request Parameter**
Parameter
Data Type 
Required
Description
grant_type
String
“ _client_credentials_ ” as default.
client_id
String
API integration information in the profile section on the Merchant Portal.
client_secret
String
API integration information in the profile section on the Merchant Portal.
scope
String
“ _collection_ ” as default.
**Response Data**
Parameter
Data Type 
Description
code 
Number 
Error code. Refer to 
message 
String 
Error description. 
access_token 
String 
To authenticate for all other APIs. 
token_type 
String 
“bearer” as default. 
expires_in 
Number 
“access_token” expiration time, in seconds. 
[PreviousSecurity Methodchevron-left](https://docs.neox.vn/docs/collections/integration/security-method)[NextAPI upload filechevron-right](https://docs.neox.vn/docs/collections/integration/api-upload-kyc-file)
Last updated 2 years ago
Was this helpful?
