<!-- Source: https://docs.neox.vn/docs/virtual-card/api-authenplatform -->

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
“client_credentials” as default.
client_id
String
API integration information in the profile section on the Merchant Portal.
client_secret
String
API integration information in the profile section on the Merchant Portal.
scope
String
“virtual_card” as default.
**Response Data**
Parameter
Data Type
Description
code
Number
Error code. Refer to table of error codes
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
[PreviousVirtual Cardchevron-left](https://docs.neox.vn/docs/virtual-card)[NextError Codeschevron-right](https://docs.neox.vn/docs/virtual-card/error-codes)
Last updated 10 months ago
Was this helpful?
