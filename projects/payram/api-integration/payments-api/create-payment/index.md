<!-- Source: https://docs.payram.com/api-integration/payments-api/create-payment -->

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
Request Body
Field
Description
Example
customerEmail
Customer’s email address where the payment link will be associated.
test@payram.com
customerID
Unique identifier for the customer.
amountInUSD
The payment amount in USD.
10
## 
curl request
Before running the command, replace the placeholders with your actual details:
  * ${BASE_URL} → Your PayRam server URL
  * <your_api_key> → Your PayRam API key
  * Replace the request body fields with real customer data


Copy
```
curl --location '${BASE_URL}/api/v1/payment' \
--header 'API-Key: <your_api_key>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "customerEmail": "<customer_email>",
  "customerID": "<customer_id>",
  "amountInUSD": <amount_in_usd>

```

## 
curl response
Copy
```
  "host": "https://yourdomain.com:8443",
  "reference_id": "c80f5363-0397-4761-aa1a-3155c3a21470",
  "url": "https://yourdomain.com/payments?reference_id=c80f5363-0397-4761-aa1a-3155c3a21470&host=https://yourdomain.com:8443"

```

circle-info
**Note****: The url field provides a ready-to-use PayRam payment page. You can share this link directly with your customers, or build a custom UI using other API endpoints.**
[PreviousPayments APIchevron-left](https://docs.payram.com/api-integration/payments-api)[NextFetch Tickerschevron-right](https://docs.payram.com/api-integration/payments-api/fetch-tickers)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
