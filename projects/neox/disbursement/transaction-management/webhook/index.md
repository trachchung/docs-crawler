<!-- Source: https://docs.neox.vn/docs/disbursement/transaction-management/webhook -->

### 
Configure the webhook to receive the IPN
  * Enable **Use APIs**
  * Fill in the **URL to receive notifications for changes in credit limit**
  * Fill in the **Secret Key**


### 
Sequence Diagram
### 
Response Data 
Parameter
Data Type 
Description
service 
String 
“ _DISBURSEMENT_ ” 
type 
String 
“ _TRANSACTION_ ” 
data 
Object 
Data response, refer to [DisbursementTransactionItem](https://docs.neox.vn/docs/disbursement/integration/response-data-structure)
time 
String 
The time of the event. 
secureHash 
String 
(Base64) 
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the “Disbursement service” menu) 
### 
Sample data
Copy
```
  "service": "DISBURSEMENT",
  "type": "TRANSACTION",
  "data": {
    "requestId": "826ae17b-8c96-42aa-aca2-196b94e21772",
    "amount": 200000,
    "fee": 0,
    "requestTransId": "transid-e360530e-5176-4830-aaf2-e744627ea931",
    "transId": "CH-101020230NLUW19L",
    "status": "SUCCESS",
    "receiver": "NGUYEN VAN A",
    "bankAccountNumber": "4396828945",
    "failedReason": "Successful transaction",
    "srcAmount": 200000,
    "srcCurrency": "VND",
    "fxRate": 1,
    "code": 1
  "time": "2023-10-10T07:15:12.042Z",
  "secureHash": "ELsrE1knfvTD8JxPmyChO8VayUUzry6ptZJ0I+jPsac="

```

With the secretKey "123", the string used to create secureHash will be:
Copy
```
20000043968289451Successful transaction01NGUYEN VAN A826ae17b-8c96-42aa-aca2-196b94e21772transid-e360530e-5176-4830-aaf2-e744627ea931200000VNDSUCCESSCH-101020230NLUW19LDISBURSEMENT2023-10-10T07:15:12.042ZTRANSACTION123
```

[PreviousQuery Request/Transactionchevron-left](https://docs.neox.vn/docs/disbursement/transaction-management/query-request-transaction)[NextError Codeschevron-right](https://docs.neox.vn/docs/disbursement/transaction-management/error-codes)
Last updated 2 years ago
Was this helpful?
