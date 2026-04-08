<!-- Source: https://docs.payram.com/api-integration/payments-api/get-blockchain-currencies -->

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
/api/v1/payment
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
  * reference_id → Use the value returned from the Create Payment API


Copy
```
curl --location '${BASE_URL}/api/v1/blockchain-currency/reference/{reference_id}' \
--data ''
```

## 
curl response
You’ll receive an array of blockchain currencies for that payment:
  * Available networks & coins – e.g., ETH/USDC on Ethereum, BTC on Bitcoin, USDT on Tron, etc.
  * Deposit info per option – including token contract address, precision, and family.
  * Customer address state – customerAddress is empty for first-time users (no deposit address assigned yet).


Copy
```
    "id": 7,
    "blockchainCode": "BASE",
    "network": "Base",
    "currencyCode": "USDC",
    "currency": "USDC",
    "customerAddress": "",
    "tokenAddress": "0x036cbd53842c5426634e7929541ec2318f3dcf7e",
    "standard": "ERC20",
    "walletPrecision": 6,
    "family": "ETH_Family",
    "recommended": false,
    "mostUsed": false,
    "blockchainID": 4,
    "currencyID": 2
  ...

```

#### 
Response breakdown
  * blockchainCode – Blockchain symbol (e.g., ETH, BTC, TRX, BASE).
  * network – Network name (e.g., Ethereum, Base, Polygon, Tron).
  * currencyCode / currency – Token or coin name (e.g., USDC, ETH).
  * customerAddress – Deposit address for the user (empty if not yet assigned).
  * tokenAddress – Token’s contract or native address.
  * standard – Token type (ERC20, TRC20, BTC, etc.).
  * walletPrecision – Decimal precision supported.
  * family – Blockchain family group (e.g., ETH_Family).
  * recommended / mostUsed – Suggested or frequently used options for display.


circle-info
**NOTE** **If customerAddress is empty for a given family, you can call the****Assign Deposit Address API****to assign a static deposit address for that user on that blockchain family.**
[PreviousFetch Tickerschevron-left](https://docs.payram.com/api-integration/payments-api/fetch-tickers)[NextAssign Deposit Addresschevron-right](https://docs.payram.com/api-integration/payments-api/assign-deposit-address)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
