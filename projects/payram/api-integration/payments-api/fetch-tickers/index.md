<!-- Source: https://docs.payram.com/api-integration/payments-api/fetch-tickers -->

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
circle-info
**Note****: You can generate a unique API key for each project directly from the PayRam dashboard. This helps you manage and track payouts separately for every project.**
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
## 
curl request
Before running the command, replace the placeholders with your actual details:
  * ${BASE_URL} → Your PayRam server URL
  * <your_api_key> → Your PayRam API key
  * Replace the request body fields with real customer data


Copy
```
curl --location '${BASE_URL}/api/v1/ticker' \
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
    "blockchainCode": "TRX",
    "currencyCode": "TRX",
    "tokenAddress": "T9yD14Nj9j7xAB4dbGeiX9h8unkKHxuWwb",
    "standard": "TRX",
    "walletPrecision": 6,
    "family": "TRX_Family",
    "price": "0.2796"
  ...

```

circle-info
**Note :** **Each object represents a supported token on PayRam with its blockchain code, token standard, and real-time price.**
[PreviousCreate Paymentchevron-left](https://docs.payram.com/api-integration/payments-api/create-payment)[NextGet Blockchain Currencieschevron-right](https://docs.payram.com/api-integration/payments-api/get-blockchain-currencies)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
