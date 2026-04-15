<!-- Source: https://docs.neox.vn/docs/disbursement/integration/inquiry-bank-account-api -->

  * This is the API to inquiry bank account number.
  * API:
    * Path: /v2/dib/bank/accountInquiry
    * Method: GET 
    * Request: Content-Type: application/json 
  * Request Parameter


Parameter
Data Type 
Require
Description
accountNumber 
String
check
Bank account number
swiftCode
String 
check
Bank swiftcode
accountType 
String
check
ACCOUNT | CARD. Default ACCOUNT
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
Object
{ fullName: "String" }
[PreviousGet exchange rate APIchevron-left](https://docs.neox.vn/docs/disbursement/integration/get-exchange-rate-api)[NextCurrency conversion APIchevron-right](https://docs.neox.vn/docs/disbursement/integration/currency-conversion-api)
Last updated 2 years ago
Was this helpful?
