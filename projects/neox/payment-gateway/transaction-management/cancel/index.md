<!-- Source: https://docs.neox.vn/docs/payment-gateway/transaction-management/cancel -->

### 
Structure of Cancel Request
https://neopay-domain?[key1=value]&[key2=value]&... (below table is the description of key and value, no ordering required)
**Method** : POST
### 
Table of Parameter
Parameter
Data type
Required
Description
neo_Command
String
“CANCEL” as default
neo_MerchantCode
String
The merchant code is provided by NeoX
neo_MerchantTxnID
String
Unique - The merchant transaction ID is provided by merchant
neo_Version
String
Version of API, "1" as default
neo_SecureHash
String
Use **SHA256** to hash the above parameters (sort the key by Alphabet order) + Secret Key (is provided by NeoX after actual integrating)
### 
Table of Data Response
Parameter
Data type
Description
neo_ResponseCode
Number
Result of transaction: 0: transaction success != 0: transaction failed, refer to 
neo_ResponseMsg
String
Refer to 
_Note: Should call this API 5 mins after payment made._
[PreviousQuery DRchevron-left](https://docs.neox.vn/docs/payment-gateway/transaction-management/query-dr)[NextIPNchevron-right](https://docs.neox.vn/docs/payment-gateway/transaction-management/ipn)
Last updated 1 year ago
Was this helpful?
