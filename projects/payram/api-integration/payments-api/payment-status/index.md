<!-- Source: https://docs.payram.com/api-integration/payments-api/payment-status -->

## 
URL Details
Parameter
Description
Example
BASE_URL
Your PayRam server URL 
[https://yourdomain.com:8443 arrow-up-right](https://yourdomain.com:8443%0A)
API Endpoint
Endpoint to create a new payment link.
/api/v1/ticker
## 
Headers
Header
Description
Example
API-Key
Your unique PayRam API key generated from your dashboard.
811b12035f0dfa8ffd62296df3c98b27
Content-Type
Format of the request data.
application/json
circle-info
**Note****: You can generate a unique API key for each project directly from the PayRam dashboard. This helps you manage and track payouts separately for every project.**
## 
curl request
Before running the command, replace the placeholders with your actual details:
  * ${BASE_URL} → Your PayRam server URL
  * <your_api_key> → Your PayRam API key


Copy
```
curl --location '<BASE_URL>/api/v1/payment/reference/<reference_id>' \
--header 'API-Key: <API_KEY>' \
--data ''
```

## 
curl response
You’ll receive a list of supported blockchain assets, each containing:
  * Blockchain info – e.g., ETH, BTC, TRX, BASE
  * Token details – contract address, precision, and standard
  * Live pricing – current USD value for each token


Copy
```
  "invoiceID": "0dec6a8c-9cbc-4086-8680-10d45319a8d1",
  "customerID": "0",
  "amountInUSD": "1",
  "paymentState": "OPEN",
  "merchantName": "Payout",
  "referenceID": "0dec6a8c-9cbc-4086-8680-10d45319a8d1",
  "createdAt": "2025-11-07T11:37:59.012304Z",
  ...

```

circle-info
**Note :****Check the paymentState field in the response to track the payment status.**
STATUS
DESCRIPTION
OPEN
The payment has not been processed yet.
CANCELLED
The payment link has expired. 
FILLED
The user has paid the full requested amount.
PARTIALLY_FILLED
The user has paid less than the requested amount.
OVER_FILLED
The user has paid more than the requested amount.
[PreviousAssign Deposit Addresschevron-left](https://docs.payram.com/api-integration/payments-api/assign-deposit-address)[NextWebhookchevron-right](https://docs.payram.com/api-integration/payments-api/webhook)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
