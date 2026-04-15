<!-- Source: https://docs.neox.vn/docs/collections/integration/transactions/get-detail-transaction -->

  * **Purpose** : This is the API used to get detail collection transaction.
  * **API** :
    * Path: _**v2/col/transactions/:transId**_
    * Method: _**GET**_
    * Request: Content-Type: _**application/json**_


### 
**Request Parameter**
Parameter
Data Type
Required
Description
transId
String
ID of Collection transaction returned from transaction management webhook
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
data
Object
Refer to [GetDetailTransactionResponse](https://docs.neox.vn/docs/collections/integration/transactions/get-detail-transaction#getdetailtransactionresponse).
neoResponseId
String
The ID of NeoX response.
#### 
GetDetailTransactionResponse
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
String
The amount of collection transaction.
fee
String
Collection transaction fee caculated by NeoX.
refundedAmount
String
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
serviceInfomation
Object
Refer to [ServiceInformationData.arrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/transactions/api-upload-kyc-file.md#uploadfileresponse)
debitorInformation
Object
Refer to [DebitorInformationData.arrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/transactions/api-upload-kyc-file.md#uploadfileresponse)
Note
String
Note for current collection transaction.
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
[PreviousAPI get list transactionschevron-left](https://docs.neox.vn/docs/collections/integration/transactions/get-list-transactions)[NextAPIs for refund requests managementchevron-right](https://docs.neox.vn/docs/collections/integration/refund-requests)
Last updated 11 months ago
Was this helpful?
