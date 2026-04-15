<!-- Source: https://docs.neox.vn/docs/payment-gateway/integrations/direct-api/tokenization -->

## 
Generate token
  1. Contact NeoX to register the service.


Check registration status at Account information page
  1. Create bill with enabled `neo_TokenCreate` field.


The bill created with field `neo_TokenCreate = true` will return the token (`neo_PayToken`) after payment success via . The token can be used for the next payment.
## 
Next payment
  1. Authentication 


Reference to .
Using `scope = payment`
  1. Pay by token API


  * URL: https://api.neopay.vn/oapi/v2/payment/payByToken
  * Method: POST 
  * Request: Content-Type: application/json


**Request Parameter**
Parameter
Data type
Required
Description
orderId
String
Order ID 
orderInfo
String
Order description
merchantTxnId
String
Merchant's transaction ID (unique)
currency
String
Currency (default VND)
amount
Number
Bill amount
payToken
String
`neo_PayToken` NeoX returned 
Example:
Copy
```
    "orderId": "DH123232234",
    "orderInfo": "Thanh toan DH123232234",
    "merchantTxnId": "323123221434",
    "currency": "VND",
    "amount": 100000,
    "payToken": "c9291339613c4e4a80818c87cbedb483"

```

**Response Data**
Field name
Data type
Description
code
Number
message
String
Response message
data
Object
  * orderId: String
  * merchantTxnId: String


Example:
Copy
```
    "code": 99,
    "message": "Order is processing",
    "data": {
        "orderId": "DH12323234234",
        "merchantTxnId": "323123221434"

```

#### 
Payment result
Last result of the request will be sent via .
[PreviousDirect APIchevron-left](https://docs.neox.vn/docs/payment-gateway/integrations/direct-api)[NextRefundchevron-right](https://docs.neox.vn/docs/payment-gateway/integrations/refund)
Last updated 1 year ago
Was this helpful?
