<!-- Source: https://docs.neox.vn/docs/collections/integration/transactions/get-list-transactions -->

  * **Purpose** : This is the API used to get list collection transactions.
  * **API** :
    * Path: _**v2/col/transactions**_
    * Method: _**GET**_
    * Request: Content-Type: _**application/json**_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
pageIndex
Number
Pagination index (start from 1, default value is 1)
pageSize
Number
Current Page size (Default value is 20, maximum value is 500)
dateFr
Datetime String (ISO 8601)
Get records created from date
dateTo
Datetime String (ISO 8601)
Get records created to date
status
String
To filter transaction list by transaction status
reconcileStatus
String
To filter transaction list by reconcile status
payoutStatus
String
To filter transaction list by payout status
virtualAccountId
String
To filter transaction list by virtual account number
virtualAccountRequestId
String
To filter transaction list by ID of seller/business is provided by merchant
### 
**Response Data**
Parameter
Data Type
Description
code
Number
Error code, refer to .
data
Object
Return Object as follow:
Copy
```
  "totalDocs": Number, // Total records
  "totalPages": Number, // Total pages base on request pageSize
  "docs": Array of GetListTransactionsResponse

```

Ref to [GetListTransactionsResponse](https://docs.neox.vn/docs/collections/integration/transactions/get-list-transactions#getlisttransactionsresponse) object.
message
String
Error description
neoResponseId
String
The ID of NeoX response
#### 
GetListTransactionsResponse
Parameter
Data Type
Description
merchantCode
String
Merchant Code
transId
String
The ID of transaction.
transDate
Datetime String (ISO 8601)
The date and time of transaction.
virtualAccountRequestId
String
The ID of seller/business is provided by merchant.
virtualAccountId
String
Virtual Account number.
accountName
String
Virtual Account name.
amount
Number
The amount of collection transaction.
fee
Number
Collection transaction fee caculated by NeoX.
refundedAmount
Number
Total refunded amount of collection transaction.
status
String
Transaction status.
reconcileStatus
String
Transaction reconcile status, Include: WAITING_UPLOAD: Documents for transaction were not uploaded, waiting for upload UPLOADED: Documents for transaction were uploaded, waiting for verifying APPROVED: Transaction documents were verified REJECTED: Transaction documents were verified has been rejected. RECONCILED: Transaction was reconconciled SETTLED: Transaction was settled
payoutStatus
String
Transaction payout status, Include: READY: Transaction was settled and ready for Remitout (Appear when reconcileStatus change to "SETTLED"). PROCESSING: Remitout/Payout request is processing. REJECTED: Remitout/Payout request has been rejected. SUCCESS: Remitout/Payout request has success.
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record lastest updated time
[PreviousAPI update transaction documentschevron-left](https://docs.neox.vn/docs/collections/integration/transactions/update-transaction-documents)[NextAPI get detail transactionchevron-right](https://docs.neox.vn/docs/collections/integration/transactions/get-detail-transaction)
Last updated 1 year ago
Was this helpful?
