<!-- Source: https://docs.neox.vn/docs/disbursement/integration/generate-token-api -->

  * PLATFORM should call this API to get Bearer token to use in all other APIs. 
  * Authentication Mechanism: OAuth 2.0 
  * API: 
    * Path: _/v2/auth/oauth2/token_
    * Method: POST 
    * Request: Content-Type: application/json 


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
“ _disbursement_ ” as default.
**Response Data**
Parameter
Data Type 
Description
code 
Number 
System’s error code. 
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
[PreviousSecurity Methodchevron-left](https://docs.neox.vn/docs/disbursement/integration/security-method)[NextGet merchant profile APIchevron-right](https://docs.neox.vn/docs/disbursement/integration/get-merchant-profile-api)
Last updated 2 years ago
Was this helpful?
