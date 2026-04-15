<!-- Source: https://docs.neox.vn/docs/disbursement/integration/get-merchant-profile-api -->

  * The main purpose of this API is to return QR code information so that the Merchant can make a deposit by transfer to increase the disbursement account. 
  * Sequence Diagram


  * API: 
    * Path: _/v2/dib/myProfile_
    * Method: GET 
    * Request: Content-Type: application/json
  * Response Data


Parameter
Data Type 
Description 
code 
Number 
System’s error code. 
message 
String 
Error description. 
data 
Object 
Profile data, refer to . 
[PreviousGenerate token APIchevron-left](https://docs.neox.vn/docs/disbursement/integration/generate-token-api)[NextRequest disbursement APIchevron-right](https://docs.neox.vn/docs/disbursement/integration/request-disbursement-api)
Last updated 2 years ago
Was this helpful?
