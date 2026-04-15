<!-- Source: https://docs.neox.vn/docs/disbursement/integration/response-data-structure -->

### 
MerchantProfileData
Parameter
Data Type 
Description
merchantCode 
String 
Merchant code 
merchantName 
String 
Merchant name 
currentCredit 
Number 
The current amount in disbursement account of merchant (for VND currency) 
currencies 
Array
[] 
The array contains the currency information. 
topupData 
Array
[] 
The array contains the method information to cash in the disbursement account. 
### 
TopupDataItem
Parameter
Data Type 
Description
type 
String 
“BANK_TRANSFER” 
qrText 
String 
This string to generate the QR code, and then use the app of banks which can support scanning & transferring. Only for the BANK_TRANSFER type. 
bankAccountNumber 
String 
The bank account number of the receiver. 
bankAccountName 
String 
The bank account name of the receiver. 
bankName 
String 
The name of receiving bank. 
transferRemark 
String 
Transfer remark. 
### 
DisbursementRequestRespData
Parameter
Data Type 
Description
requestId 
String 
The ID of request. 
code 
Number 
Logic’s error code. 
status 
String 
_PASSED_ : Request is submitted successfully. _FAILED_ : Request is submitted fail. 
### 
DisbursementTransactionsRespData
Parameter
Data Type 
Description
requestId 
String 
The ID of disbursement request. 
refCode 
String 
The Ref code from NeoPay. 
status 
String 
The status of request: 
_PASSED_
_FAILED_
_APPROVED_
_REJECTED_
transactions 
Array
[[DisbursementTransactionItem](https://docs.neox.vn/docs/disbursement/integration/response-data-structure#disbursementtransactionitem)] 
The array contains the disbursement transaction information. 
### 
DisbursementTransactionItem
Parameter
Data Type 
Description
requestId 
String 
The ID of disbursement request. 
transId 
String 
The ID of disbursement transaction. 
requestTransId 
String 
The ID of disbursement transaction is provided by the merchant (when submitting the request). 
amount 
Number 
The amount of disbursement transaction (VND as default). 
srcAmount 
Number 
The amount - foreign currency (different from VND). Which will be deducted from pre-fund account 
srcCurrency 
String 
The pre-fund account currency. 
fxRate 
Number 
The exchange rate between the srcCurrency against the VND 
fee 
Number 
The fee of disbursement transaction. 
receiver 
String 
The name of receiving person/organization. 
bankAccountNumber 
String 
The bank account number of the receiver. 
status 
String 
The status of transaction: _SUCCESS_
_FAILED_
_PROCESSING_
_WAITING_PROCESS_
failedReason 
String 
The reason of failure (If the status is not “FAILED”, the failedReason will be null). 
code 
Number 
Logic’s error code. Refer to 
### 
ExchangeRateRespItem
Parameter
Data Type 
Description
currency 
String 
The currency 
fxRate 
Number 
The value of forex rate 
### 
CurrencyDataItem
Parameter
Data Type 
Description
code 
String 
Currency code 
balance 
Number 
The balance of corresponding currency type. 
### 
ExchangeTransactionItem
Parameter
Data Type 
Description
requestId 
String 
The ID of exchange request. 
srcAmount 
Number 
The amount of srcCurrency
dstAmount
Number
The amount of dstAmount
srcCurrency 
String 
The source currency. 
dstCurrency
String
The destination currency. 
fxRate 
Number 
The exchange rate between the srcCurrency against the VND
status 
String 
SUCCESS: Exchange success
FAILED: Exchange failed
failedReason 
String 
The reason of failure
code 
Number 
Logic’s error code. Refer to 
[PreviousEvent Notificationchevron-left](https://docs.neox.vn/docs/disbursement/integration/event-notification)[NextError codeschevron-right](https://docs.neox.vn/docs/disbursement/integration/error-codes)
Last updated 2 years ago
Was this helpful?
