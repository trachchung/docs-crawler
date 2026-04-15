<!-- Source: https://docs.neox.vn/docs/disbursement/integration/error-codes -->

### 
1. System's error codes
Error code 
Status
Error description 
SUCCESS 
Success. 
FAILED 
System error (default) 
400 
FAILED 
Bad request. 
401 
FAILED 
System error exception 
403 
FAILED 
Forbidden 
404 
FAILED 
Service is not found. 
413 
FAILED 
The request entity too large 
422 
FAILED 
Invalid token. 
429 
FAILED 
System error. (Internal Error) 
500 
FAILED 
System error. (Internal Service error) 
501 
FAILED 
System error. (Exception on gateway) 
502 
FAILED 
Bad gateway 
503 
FAILED 
System error (Internal Request rejected) 
504 
FAILED 
System error (Request timeout) 
505 
FAILED 
System error (Processing failed on gateway) 
514 
FAILED 
System error (Request is skipped) 
### 
2. Logic's error codes
Error code 
Status
Error description 
SUCCESS 
Request/Transaction is successful. 
99 
PROCESSING 
Transaction is processing. 
2009 
FAILED 
Insufficient household account balance 
2014 
FAILED 
Transaction amount exceeded 
2015 
FAILED 
Invalid amount 
2051 
FAILED 
Exceed the number of transactions in 1 request (200 trans/request) 
2052 
FAILED 
Violation of NEOX policy. 
2053 
FAILED 
Invalid request. 
2054 
FAILED 
Disbursement service has not been activated. 
2055 
FAILED 
RequestId already exists. 
2056 
FAILED 
Duplicated transaction 
2057 
FAILED 
The minimum value condition is not met. 
2063 
FAILED 
Invalid currency. 
3000 
FAILED 
An error occurred during the processing. 
3400 
FAILED 
Account/Card number is invalid 
3401 
FAILED 
Incorrect account/card information. 
3402 
FAILED 
Account/Card does not support the transaction 
3403 
FAILED 
Account/Card number is invalid. 
3700 
FAILED 
Banking system error. 
3709 
FAILED 
Transaction is rejected by the issuing bank. 
3710 
FAILED 
Reject due to fraud suspicion. 
3711 
FAILED 
Card/Account is transacted in unauthorized area. 
3715 
FAILED 
Publisher not found. 
[PreviousResponse Data Structurechevron-left](https://docs.neox.vn/docs/disbursement/integration/response-data-structure)[NextDisbursement Accountchevron-right](https://docs.neox.vn/docs/disbursement/disbursement-account)
Last updated 3 years ago
Was this helpful?
