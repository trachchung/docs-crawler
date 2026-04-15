<!-- Source: https://docs.neox.vn/docs/disbursement/transaction-management/query-request-transaction -->

#### 
API getDisbursementTransaction
  * This is the API to get the list of disbursement transactions 
  * Sequence Diagram 


  * API:
    * Path: _/v2/dib/disbursementTransactions_
    * Method: GET 
    * Request: Content-Type: application/json 
  * Request Parameter


Parameter
Data Type 
Required
Description
requestId 
String 
The ID of disbursement request. 
requestTransId 
String 
The ID of disbursement transaction is provided by the merchant (when submitting the request). 
  * Response Data


Parameter
Data Type 
Description
code 
Number 
System’s error code. Refer to 
message 
String 
Error description 
data 
Object 
Data response, refer to [DisbursementTransactionsRespData](https://docs.neox.vn/docs/disbursement/integration/response-data-structure). 
[PreviousTransaction Managementchevron-left](https://docs.neox.vn/docs/disbursement/transaction-management)[NextWebhookchevron-right](https://docs.neox.vn/docs/disbursement/transaction-management/webhook)
Last updated 2 years ago
Was this helpful?
