<!-- Source: https://docs.payram.com/api-integration/payouts-apis/get-all-payouts -->

## 
URL Details
Before making the request, you’ll need the following parameters that define your PayRam environment and platform.
Parameter
Description
BASE_URL
Your PayRam server URL 
[https://yourdomain.com:8443 arrow-up-right](https://yourdomain.com:8443%0A)
API Endpoint
Full endpoint path for retrieving all payouts.
/api/v1/withdrawal/merchant
## 
Query Parameters
Before making the request, you’ll need the following parameters that define your PayRam environment and platform.
Parameter
Description
Example
limit
Defines how many payout records to fetch per request. Optional but recommended for pagination.
10
offset
Specifies where to start fetching results (used for pagination). Optional.
order
Sorting order. Use ASC for ascending or DESC for descending.
DESC
sortBy
Field name to sort results by (e.g., createdAt, amount).
createdAt
circle-info
**Note** : **If you don’t include limit or offset, all payouts will be retrieved by default.**
## 
Headers
Headers are required for authenticating and defining the content type of your request.
Header
Description
Example
API-Key
Your unique PayRam API key generated from your dashboard.
be703fa47ebe07121102ee260fb3d5c0
Content-Type
Format of the data being sent.
application/json
circle-info
**Note****: You can generate a unique API key for each project directly from the PayRam dashboard. This helps you manage and track payouts separately for every project.**
## 
curl Request
Before running the command, replace the placeholders with your actual details:
  * ${BASE_URL} → Your PayRam server URL
  * <API_KEY> → Your PayRam API key


Copy
```
curl --location --request GET '${BASE_URL}/api/v1/withdrawal' \
--header 'API-Key: <API_KEY>' \
--header 'Content-Type: application/json'
```

## 
curl Response
This API returns an array of payout records. Each object in the array represents a single payout entry from your PayRam database.
Copy
```
    "id": 101,
    "blockchainCode": "ETH",
    "currencyCode": "USDC",
    "amount": "50000",
    "priceInUSD": "1",
    "amountInUSD": "50000",
    "toAddress": "0x1234567890abcdef1234567890abcdef12345678",
    "recipientEmail": "test@test.com",
    "status": "sent",
    ...
    "id": 102,
    "blockchainCode": "TRX",
    "currencyCode": "USDT",
    "amount": "25000",
    "priceInUSD": "1",
    "amountInUSD": "25000",
    "toAddress": "TXYZ1234567890abcdefT1234567890abcd",
    "recipientEmail": "merchant@demo.com",
    "status": "pending-approval",
    ...

```

[PreviousPayouts Statuschevron-left](https://docs.payram.com/api-integration/payouts-apis/payouts-status)[NextTypescript/Javascript SDKchevron-right](https://docs.payram.com/payram-sdk/typescript-javascript-sdk)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
