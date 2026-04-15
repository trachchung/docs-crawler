<!-- Source: https://docs.neox.vn/docs/payment-gateway/integrations/refund/apis -->

## 
1. Get payment list API
**Path:** /api/v1/paygate/neopay
**Method** : POST
### 
Request
Parameter
Data type
Required
Description
neo_Command
String
"QUERY_PT"
neo_MerchantCode
String
The merchant code is provided by NeoX
neo_TransactionID
String
neo_TransactionID returned in IPN payload. Ref to 
neo_Version
String
Version of API, "1" as default
neo_SecureHash
String
Use **SHA256** to hash the above parameters (sort the key by Alphabet order) + Secret Key (is provided by NeoX after actual integrating)
With the secret key: **311235E7043244EC8306F96720748C56**
Copy
```
neo_Command:"QUERY_PT"
neo_MerchantCode:"UFLIYL"
neo_TransactionID:"240830080146NDTISR"
neo_Version:"1"
neo_SecureHash:"df594d1e467bd327a30fa45ce259987718a68bd54cc67afe74d1e15e255182a4"

```

### 
Response
Key
Type
Description
neo_ResponseCode
Number
0: Successful.
<>0: Failed, refer 
neo_ResponseData
Object
Array of payments: [{
id: NeoX's PaymentID
status: SUCCESS | FAILED | PROCESSING
amount: Refund amount, paymentMethod: QR | ATM | CC
refundedAmount: Total refunded amount
}]
neo_ResponseMsg
String
Error message
Copy
```
  "neo_ResponseCode": 0,
  "neo_ResponseData": [
          "id": "1439209",
          "status": "PROCESSING",
          "amount": 20000000,
          "refundedAmount": 0,
          "paymentMethod": "CC"
          "id": "1439211",
          "status": "SUCCESS",
          "amount": 20000000,
          "refundedAmount": 100000,
          "paymentMethod": "QR"
  "neo_ResponseMsg": "Successful"

```

## 
2. Refund request API
**Path:** /api/v1/paygate/neopay
**Method** : POST
### 
Request
Parameter
Data type
Required
Description
neo_Command
String
“REFUND”
neo_MerchantCode
String
The merchant code is provided by NeoX
neo_RequestID
String
Unique - The merchant transaction ID is provided by merchant
neo_PaymentID
String
Payment ID, Ref
neo_Amount
Number
Refund amount
neo_Receiver
String
Require beneficiary information if the user pays using the QR method.
Encode base64 follow Jsonformat: `{"accountName":"value", "accountNumber": "1234567", "swiftCode": "ASCBVNVX"}` => neo_Receiver: `eyJhY2NvdW50TmFtZSI6InZhbHVlIiwiYWNjb3VudE51bWJlciI6ICIxMjM0NTY3Iiwic3dpZnRDb2RlIjoiQVNDQlZOVlgifQ==`
neo_Version
String
Version of API, "1" as default
neo_SecureHash
String
Use **SHA256** to hash the above parameters (sort the key by Alphabet order) + Secret Key (is provided by NeoX after actual integrating)
*** Except neo_RequestID field**
Copy
```
  neo_MerchantCode: "UFLIYL"
  neo_Command: "REFUND"
  neo_RequestID: "a68de39f-ea76-43fb-848f-b605b4aaf44e"
  neo_PaymentID: "1439211"
  neo_Amount: 10000
  neo_Version: "1"
  neo_Receiver: "eyJhY2NvdW50TmFtZSI6Ik5HVVlFTiBWQU4gQSIsImFjY291bnROdW1iZXIiOiIxMjM0NTY3ODkiLCJzd2lmdENvZGUiOiJBU0NCVk5WWCJ9"
  neo_SecureHash: "88cafbc3bc1312a4dbae11dedf17819ea6462b85a218298417a917f1797597fa"

```

### 
Response
Key
Type
Description
neo_ResponseCode
Number
0: Successful.
<>0: Failed, refer 
neo_ResponseData
Object
{
transId: <Refund ID>
}
neo_ResponseMsg
String
Error message
Copy
```
    "neo_ResponseCode": 0,
    "neo_ResponseData": {
        "transId": "5SYNM1OELUND"
    "neo_ResponseMsg": "Successful"

```

[PreviousRefundchevron-left](https://docs.neox.vn/docs/payment-gateway/integrations/refund)[NextIPNchevron-right](https://docs.neox.vn/docs/payment-gateway/integrations/refund/ipn)
Last updated 1 month ago
Was this helpful?
