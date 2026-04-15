<!-- Source: https://docs.neox.vn/docs/collections/integration/transactions/update-transaction-documents -->

  * This is the API used to update KYC virtual account information.
  * API:
    * Path: _v2/col/transactions/:transId/documents_
    * Method: _PUT_
    * Request: Content-Type: _application/json_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
colTransactionDataFile
String
Collection transaction data file (excel)
colLogisticAttachments
String Array
List of logistic tracking files (images and pdf)
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
[PreviousAPIs for transactions managementchevron-left](https://docs.neox.vn/docs/collections/integration/transactions)[NextAPI get list transactionschevron-right](https://docs.neox.vn/docs/collections/integration/transactions/get-list-transactions)
Last updated 11 months ago
Was this helpful?
