<!-- Source: https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/web-sdk -->

## 
Javascript SDK for NeoX Payment Gateway
**Tutorial & Code sample**: [NeoX SDK(javascript)arrow-up-right](https://github.com/neopayvn/neopay-pg-js-sdk)
**Use**
Copy
```
<!-- example-payment.html -->
<!DOCTYPE html>
<html lang="vi-VN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>NEOPAY SDK Example</title>
  </head>
  <body>
    <button onclick="onPayWithPopup()">Thanh toán (Popup)</button>
    <br />
    <br />
    <button onclick="onPayWithRedirect()">Thanh toán (Redirect)</button>
  </body>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script
    neopay-sdk
    type="text/javascript"
    src="https://cdn.jsdelivr.net/gh/neopayvn/neopay-pg-js-sdk/sdk/neopay-sdk.min.js"
  ></script>
  <script>
    const MERCHANT_CODE = "RZRGNY";
    const HASH_KEY = "4F99C21FE8A14FD198FA00D18662A63B";
    $(document).ready(function () {
      const neo_PaymmentBaseUrl = "https://sandbox-api.neopay.vn/pg";
      const configUI = {
        neo_HiddenHeader: false,
        neo_HiddenFooter: true,
        neo_HiddenPaymentMethod: false,
        neo_HiddenOrderInfo: false,
      const callbacks = {
        onSuccess: (data) => {
          console.log("success", data);
        onFailure: (data) => {
          console.log("failure:", data);
        onClose: (data) => {
          console.log(data);
      neopaySDK.init(neo_PaymmentBaseUrl, configUI, callbacks);
    });
    function onPayWithPopup() {
      const config = {
        neo_MerchantCode: MERCHANT_CODE,
        neo_PaymentMethod: ["WALLET", "ATM", "CC", "QR"],
        neo_Currency: "VND",
        neo_Locale: "vi",
        neo_Version: "1",
        neo_Command: "PAY",
        neo_Amount: Math.floor(Math.random() * 600000) + 100000,
        neo_MerchantTxnID: `T${`${Date.now()}`.slice(-8)}`,
        neo_OrderID: `DH${`${Date.now()}`.slice(-8)}`,
        neo_OrderInfo: `Thanh toán ĐH Test`,
        neo_Title: "Thanh toán",
        neo_ReturnURL: "https://sandbox-api.neopay.vn/pg/paygate/tryitnow",
        neo_ViewType: "POPUP", //POPUP | REDIRECT
      neopaySDK.pay(config, HASH_KEY);
    function onPayWithRedirect() {
      const config = {
        neo_MerchantCode: MERCHANT_CODE,
        neo_PaymentMethod: ["WALLET", "ATM", "CC", "QR"],
        neo_Currency: "VND",
        neo_Locale: "vi",
        neo_Version: "1",
        neo_Command: "PAY",
        neo_Amount: Math.floor(Math.random() * 600000) + 100000,
        neo_MerchantTxnID: `T${`${Date.now()}`.slice(-8)}`,
        neo_OrderID: `DH${`${Date.now()}`.slice(-8)}`,
        neo_OrderInfo: `Thanh toán ĐH Test`,
        neo_Title: "Thanh toán",
        neo_ReturnURL: "https://sandbox-api.neopay.vn/pg/paygate/tryitnow",
        neo_ViewType: "REDIRECT", //POPUP | REDIRECT
      neopaySDK.pay(config, HASH_KEY);
  </script>
</html>
```

Copy
```
<!DOCTYPE html>
<html lang="vi-VN">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>NEOPAY SDK Example Checkout</title>
  </head>
  <body>
    <span id="neopay-checkout">Checkout</span>
  </body>
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script
    neopay-sdk
    type="text/javascript"
    src="https://cdn.jsdelivr.net/gh/neopayvn/neopay-pg-js-sdk/sdk/neopay-sdk.min.js"
  ></script>
  <script>
    $(document).ready(function () {
      const neo_PaymmentBaseUrl = "https://sandbox-api.neopay.vn/pg";
      const configUI = {
        neo_HiddenHeader: false,
        neo_HiddenFooter: true,
      const callbacks = {
        onSuccess: (data) => {
          console.log("success", data);
        onFailure: (data) => {
          console.log("failure:", data);
        onClose: (data) => {
          console.log(data);
      neopaySDK.init(neo_PaymmentBaseUrl, configUI, callbacks);
    });
  </script>
</html>
```

#### 
Methods
Method
Description
init
Initialize the necessary configurations for the SDK and UI
pay
Payment
close
Close payment popup
**neopaySDK.init (neo_PaymmentBaseUrl, configUI, callbacks)**
**neo_PaymmentBaseUrl**
Sandbox environment testing URL:_https://sandbox-api.neopay.vn/pg_
#### 
configUI
Parammetter
Data Type
Default Value
Description
neo_HiddenHeader
boolean
false
Hide header
neo_HiddenFooter
boolean
false
Hide footer
neo_HiddenPaymentMethod
boolean
false
Hide payment method
neo_HiddenOrderInfo
boolean
false
Hide order information
#### 
neopaySDK.pay (config, hashKey)
Parameter
Data Type
Default Value
Required
Description
neo_MerchantCode
string
Merchant code is provided by NeoX
neo_Currency
string
VND
Transaction currency, VND as default
neo_Locale
string
vi
Language will display on the checkout page. Support: “vi”, “en”.
#### 
neopaySDK.pay (config, hashKey)
Parameter
Data Type
Default Value
Required
Descript
neo_MerchantCode
string
Merchant code is provided by NeoX
neo_Currency
string
VND
Transaction currency, VND as default
neo_Locale
string
vi
Language will display on the checkout page. Support: “vi”, “en”.
neo_Version
string
Payment gateway version, “1” as default
neo_Command
string
PAY
“PAY” as default
neo_Amount
number
Payment amount
neo_MerchantTxnID
string
Unique - Transaction ID is provided by merchant
neo_OrderID
string
Oder ID
neo_OrderInfo
string
Oder information
neo_Title
string
Thông tin tiêu đề sẽ hiển thị trên trang thanh toán
neo_ReturnURL
string
The website URL of the merchant
neo_ViewType
string
"POPUP" / "REDIRECT"
Choose to open payment gateway as popup or redirect
neo_PaymentMethod
string
["WALLET", "ATM", "CC", "QR"]
Allows to choose to display direct or list payment channels. If this field is not transmitted, all channels will be displayed.
#### 
Request sample
Copy
```
  neo_MerchantCode: "RZRGNY",
  neo_PaymentMethod: ["WALLET", "ATM", "CC", "QR"],
  neo_Currency: "VND",
  neo_Locale: "vi",
  neo_Version: "1",
  neo_Command: "PAY",
  neo_Amount: Math.floor(Math.random() * 600000) + 100000,
  neo_MerchantTxnID: `T${`${Date.now()}`.slice(-8)}`,
  neo_OrderID: `DH${`${Date.now()}`.slice(-8)}`,
  neo_OrderInfo: `Payment for Test Order`,
  neo_Title: "Payment",
  neo_ReturnURL: "https://sandbox-api.neopay.vn/pg/paygate/tryitnow",
  neo_ViewType: "POPUP",

```

#### 
callback
Event
Description
onSuccess
The event occurs when payment is successful.
onFailure
The event occurs when payment fails.
onClose
The event occurs when the popup is closed.
**Callback data from onSuccess and onFailure**
Parameter
Data Type
Description
neo_MerchantCode
string
Merchant code is provided by NeoX
neo_Currency
string
Transaction currency, VND as default
neo_Locale
string
Language will display on the checkout page. Support: “vi”, “en”.
neo_Version
string
Payment gateway version, “1” as default
neo_Command
string
“PAY” as default
neo_Amount
string
Payment amount
neo_MerchantTxnID
string
Unique - Transaction ID is provided by merchant
neo_OrderID
string
Oder ID
neo_OrderInfo
string
Oder Information
neo_TransactionID
string
Unique - Transaction ID is generated by the NeoX system, for reconciling.
neo_ResponseCode
number
The error code is returned by NeoX, indicates the transaction result.
neo_ResponseMsg
string
Error description.
neo_CustomerID
string
The customer ID on the merchant system.
neo_ResponseData
string
The data response of customer's payment.
neo_SecureHash
string
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (will be provided by NeoX after actual integration)
#### 
Response sample
Copy
```
  "neo_Amount": "112214",
  "neo_Command": "PAY",
  "neo_Currency": "VND",
  "neo_Locale": "vi",
  "neo_MerchantCode": "RZRGNY",
  "neo_MerchantTxnID": "T23343243",
  "neo_OrderID": "DH28900084",
  "neo_OrderInfo": "Thanh toán ĐH Test",
  "neo_ResponseCode": "0",
  "neo_ResponseData": "",
  "neo_ResponseMsg": "Success",
  "neo_SecureHash": "80A669689BEE56D02211F8C762D828194C5B3AD121420433D280696B952F3A19",
  "neo_TransactionID": "5226",
  "neo_Version": "1"

```

[PreviousReact Native SDKchevron-left](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/react-native-sdk)[NextAPIschevron-right](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/apis)
Last updated 1 year ago
Was this helpful?
