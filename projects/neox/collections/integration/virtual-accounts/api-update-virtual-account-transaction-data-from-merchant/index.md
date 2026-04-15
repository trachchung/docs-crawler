<!-- Source: https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-virtual-account-transaction-data-from-merchant -->

  * API:
    * Path: _v2/col/virtual-accounts/:vaNumber/trans-data_
    * Method: _PUT_
    * Request: Content-Type: _application/json_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
transData
Array
The array contains the list of transaction data from the merchant.
Refer to TransactionData
batchId
String
The Id of merchant batch process for this Virtual Account
batchTime
Date
The ISODate of merchant batch process for this Virtual Account
batchAmount
Number
The amount of merchant batch process for this Virtual Account
neoTransInfo
Array
The array contains the list of Neo Collection transactions related to this merchant batch process.
Refer to NeoTransactionInfo.
note
String
The note for this merchant batch process
### 
**TransactionData**
Parameter
Data Type
Required
Description
id
String
The ID of transaction/Order
amount
Number
The transaction/order amount
desc
String
The description of transaction
extraInfo
Object
The extra info for transaction. Refer to 
### 
**TransactionExtraInfo**
Parameter
Data Type
Required
Description
depot
String
Extra info from merchant for transaction.
invoicingCompany
String
Invoicing Company
vendor
String
vendor
dmId
String
Delivery man ID
dmName
String
Delivery man name
invoiceDate
String
Invoice Date
### 
**NeoTransactionInfo**
Parameter
Data Type
Required
Description
transId
String
The Transaction Id of collection transaction from NeoX.
amount
Number
The actual process amount from merchant for this collection transaction.
## 
**Response Data**
Parameter
Data Type
Description
code
Number
Error code, refer to [table of error codesarrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/virtual-accounts/error-codes.md).
message
String
Error description.
data
Object
Refer to [UpdateVirtualAccountTransactionsResponse](https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-virtual-account-transaction-data-from-merchant#updatevirtualaccounttransactionsresponse)
neoResponseId
String
The ID of NeoX response
### 
UpdateVirtualAccountTransactionsResponse
Parameter
Data Type
Description
batchId
String
The Id of merchant batch process for this Virtual Account
virtualAccountBalance
Number
Current Virtual Account balance
transData
Array
The array contains the list of transaction data from the merchant.
Refer to 
### 
TransactionDataResult
Parameter
Data Type
Description
id
String
The ID of transaction/Order
amount
Number
The transaction/order amount
desc
String
The description of transaction
settleStatus
String
Settlement status of transaction. "UNSETTLED": Transaction has not been settled yet "SETTLED": The transaction has been settled
extraInfo
Object
The extra info for transaction. Refer to **TransactionExtraInfo**
[PreviousAPI update KYC virtual account informationchevron-left](https://docs.neox.vn/docs/collections/integration/virtual-accounts/api-update-kyc-virtual-account-information)[NextAPI set active/inactive Virtual Accountchevron-right](https://docs.neox.vn/docs/collections/integration/virtual-accounts/set-active-virtual-account)
Last updated 1 month ago
Was this helpful?
