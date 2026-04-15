<!-- Source: https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/apis -->

Structure of Payment Request: _https://neox- domain?[key1=value] &[key2=value]&..._ (Table below is the description of key and value, no ordering required)
Key
Require
Type
Description
neo_MerchantCode
check
String
The merchant representative code that provided by NeoX
neo_Currency
check
String
Transaction currency, default is “VND”
neo_Locale
check
String
The language used on payment page, support: “vi”, “en”
neo_Version
check
String
Payment gateway version, default is “1”
neo_Command
check
String
Default is “PAY”
neo_Amount
check
Number
Order amount
neo_MerchantTxnID
check
String
Transaction id of merchant, unique on merchant’s system and on each request, accept only characters, numerics and list of symbols: “- ”, “_”. Max 36 characters
neo_OrderID
check
String
Order id of transaction, accept only characters, numerics and list of symbols: “-”, “_”. This field can be duplicate on requests. Max 36 characters
neo_OrderInfo
check
String
Order infomation, max length 256.
neo_ReturnURL
check
String
NeoX will redirect to this URL after transaction completed
neo_ExpiresIn
Number
Expiration time (in seconds) of Payment Request. Default is 86400 seconds.
neo_PaymentMethod
Array/ String
A list of below values: **WALLET** : pay with NeoX e-wallet **ATM** : pay with domestic card **CC** : pay with international card **QR** : pay with QR Code This param allows merchants to display one or more payment methods on the payment page. If not set, all methods will be shown.
_Incase GET(http method), this field separeted by the commas_
neo_CustomerPhone
String
Customer phone
neo_CustomerEmail
String
Customer email
neo_CustomerID
String
Merchant’s customer id
neo_CustomerIpAddress
String
Customer IP address
neo_TokenCreate
Boolean
Returning payment token after international card payment.[Tokenization](https://docs.neox.vn/docs/payment-gateway/integrations/direct-api/tokenization)
neo_IframeCreate
Boolean
Returning redirect payment link as a simple payment for HTML <iFrame/> src
neo_CapturedPayment
Boolean
Create captured payment bill (Only support for Credit Card Payment)
neo_SecureHash
check
String
A = all above parameters sorted in alphabetical order
B = merchant’s Secret Key(provided by NeoX)
This value = hashed string(using SHA256) of A + B
neo_ExtData
Object
Bill extra data, eg: sub order info, platform, webUrl..., with schema (view example for more details):
Copy
```
    "orderData": {
        "payItems": [
                "orderId": String,
                "desc": String,
                "price": Number,
                "extraInfo": Object

```

Incase of POST(http method), system will response below data:
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
“redirect”: <Payment link>,
"qrData": A string that used to generate QR code,
"bankName": Beneficial bank name "bankAccount": Beneficial bank account,
"bankAccountName": Account name,
"amount": Order amount,
"remark: Payment description with format:
(50 characters of neo_OrderInfo removed vietnamese accent and special characters) + NEOxxx
_*Return QR info if only_ _**QR**_ _method is chosen_
}
## 
Example
URL for test: <https://sandbox-api.neopay.vn/pg/api/v1/paygate/neopay>[arrow-up-right](https://sandbox-api.neopay.vn/pg/api/v1/paygate/neopay)
  1. **Create payment link by GET method:**


**Request** :
Copy
```
https://sandbox-api.neopay.vn/pg/api/v1/paygate/neopay?neo_MerchantCode=XASUKU&neo_PaymentMethod=WALLET,ATM,CC,BANK_TRANSFER&neo_Currency=VND&neo_Locale=vi&neo_Version=1&neo_Command=PAY&neo_Amount=100000&neo_MerchantTxnID=T15959145&neo_OrderID=DH15959145&neo_OrderInfo=DH15959145&neo_Title=Thanh%20to%C3%A1n&neo_ReturnURL=https://sandbox-api.neopay.vn/pg/paygate/tryitnow&neo_AgainURL=https://google.com&neo_TokenCreate=false&neo_SecureHash=1E0D5C957C7CE67750ED82DD1336AC12AA2434A94FE4B707BA23027FEFA1A248
```

**Response** :
NeoX automatically redirects to payment page.
  1. **Create payment link by POST method**


**Request** :
Copy
```
    "neo_MerchantCode": "XASUKU",
    "neo_Currency": "VND",
    "neo_Locale": "vi",
    "neo_Version": "1",
    "neo_Command": "PAY",
    "neo_Amount": 100000,
    "neo_MerchantTxnID": "123123123030",
    "neo_OrderID": "ORDER00001",
    "neo_OrderInfo": "IFtestpost",
    "neo_ReturnURL": "https://google.com",
    "neo_PaymentMethod": ["QR"],
    "neo_ExtData": {
        "orderData": {
            "payItems": [
                    "orderId": "SUB_20231225_001",
                    "desc": "Description for sub order id 001",
                    "price": 37000,
                    "extraInfo": {"foo": "bar"}
                   "orderId": "SUB_20231225_002",
                    "desc": "Description for sub order id 002",
                    "price": 63000,
                    "extraInfo": {"foo": "bar"}
    "neo_SecureHash": "08D507127FEF12C7719CB33221C708650F21EE3C4CA68B7E5E762B9FE648F916"

```

With the Secret Key "7EDB9708213543968555AD010C42C16C". _neo_SecureHash_ is created by hashing the string below:
100000PAYVNDviXASUKU123123123030ORDER00001IFtestpostQRhttps://google.com17EDB9708213543968555AD010C42C16C *Note: If merchant use "neo_ExtData.orderData.payItems" for additional sub order info, the total price of each payItems must equal to neo_Amount.
**Response** :
Copy
```
    "neo_ResponseCode": 0,
    "neo_ResponseData": {
        "redirect": "https://sandbox-api.neopay.vn/pg/paygate/XASUKU?billId=231018075010VNBRZF",
        "qrData": "00020101021238560010A0000007270126000697045701129020008685300208QRIBFTTA530370454061000005802VN5915NEOX DIEN MAY H62110807NEO20706304051F",
        "bankName": "Wooribank",
        "bankAccount": "902000868530",
        "bankAccountName": "NEOX DIEN MAY H",
        "amount": 100000,
        "remark": "NEO2070"

```

[PreviousWeb SDKchevron-left](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/web-sdk)[NextDirect APIchevron-right](https://docs.neox.vn/docs/payment-gateway/integrations/direct-api)
Last updated 11 months ago
Was this helpful?
