<!-- Source: https://docs.payram.com/api-integration/payouts-apis/create-payouts -->

## 
URL Details
Before making the request, you’ll need the following parameters that define your PayRam environment and platform.
Parameter
Description
Example
BASE_URL
Your PayRam server URL. This varies depending on where you’ve hosted PayRam (with or without SSL).
[https://yourdomain.com:8443 arrow-up-right](https://yourdomain.com:8443%0A)
API Endpoint
Full endpoint path to create a payout request.
/api/v1/withdrawal/merchant
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
Specifies that the request body is in JSON format.
application/json
circle-info
**Note****: You can generate a unique API key for each project directly from the PayRam dashboard. This helps you manage and track payouts separately for every project.**
## 
Request Body
The body contains all required details for processing the payout. All fields are mandatory and must be provided.
Field
Description
Example
Required
email
Recipient’s email address.
test@test.com
✅ Yes
blockChainCode
Blockchain network used for the payout (e.g., ETH, TRX, BASE)
ETH
✅ Yes
currencyCode
Token symbol to be used for the payout (e.g., USDC, USDT).
USDC
✅ Yes
amount
Amount to transfer.
100000
✅ Yes
toAddress
Recipient’s wallet address must belong to the selected blockchain.
0x291b68732f14F47Fd21bE81ec5Cf1bcfC0DB14Ea
✅ Yes
mobileNumber
Recipient’s mobile number.
123456789
❌ Optional
residentialAddress
Recipient’s address.
No 22 oc street
❌ Optional
customerID
Unique identifier for the customer.
414817384
✅ Yes
## 
curl Request 
Before running the command, replace the placeholders with your actual details:
  * ${BASE_URL} → Your PayRam server URL
  * <API_KEY> → Your PayRam API key


circle-exclamation
#### 
Default Payout Limits
  * Auto-approve limit: Payouts up to $500 are automatically approved.
  * Hourly limit: You can process up to $5,000 in total payouts per hour.
  * Daily limit: You can process up to $10,000 in total payouts per day.


If any of these limits are exceeded, the payout must be approved by an Admin from the dashboard before processing. These default values can be customized as well, contact PayRam support for more details.
Copy
```
curl --location '${BASE_URL}/api/v1/withdrawal/merchant' \
--header 'API-Key: <API_KEY>' \
--header 'Content-Type: application/json' \
--data-raw '{
  "email": "<your_email>",
  "blockChainCode": "<blockchain_code>",
  "currencyCode": "<currency_code>",
  "amount": "<amount_to_send>",
  "toAddress": "<recipient_wallet_address>",
  "mobileNumber": "<recipient_mobile_number>",
  "residentialAddress": "<recipient_address>",
  "customerID": "<customer_id>"

```

circle-info
**Available blockchain codes: ETH (Ethereum), TRX (Tron), BASE (Base)**
## 
curl response
This API returns detailed information about the payout, including the amount, currency used, recipient wallet address, and current status.
Copy
```
  "id": 120,
  "blockchainCode": "ETH",
  "currencyCode": "USDC",
  "amount": "100000",
  "priceInUSD": "1",
  "amountInUSD": "100000",
  "toAddress": "0x9F8E7D6C5B4A39281706F5E4D3C2B1A098765432",
  "recipientEmail": "test@test.com",
  "status": "pending-approval",
  ...

```

circle-info
**Note: The id field is very important. It uniquely identifies the payout and will be required for checking its status or performing any follow-up actions.**
[PreviousPayouts APIschevron-left](https://docs.payram.com/api-integration/payouts-apis)[NextPayouts Statuschevron-right](https://docs.payram.com/api-integration/payouts-apis/payouts-status)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
