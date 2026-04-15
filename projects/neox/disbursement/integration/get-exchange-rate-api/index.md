<!-- Source: https://docs.neox.vn/docs/disbursement/integration/get-exchange-rate-api -->

  * This is the API to get the list of fx rates between currency vs VND. 
  * Sequence Diagram 


  * API:
    * Path: _/v2/dib/fxRates_
    * Method: GET 
    * Request: Content-Type: application/json 
  * Request Parameter


Parameter
Data Type 
Required
Description
codes 
String 
Currency codes are separated by commas. ex: USD,EUR 
  * Response Data


Parameter
Data Type 
Description
code 
Number 
System’s error code 
message 
String 
Error description 
data 
Array
[] 
Data response, refer to 
[PreviousGet disbursement transaction APIchevron-left](https://docs.neox.vn/docs/disbursement/integration/get-disbursement-transaction-api)[NextInquiry bank account APIchevron-right](https://docs.neox.vn/docs/disbursement/integration/inquiry-bank-account-api)
Last updated 2 years ago
Was this helpful?
