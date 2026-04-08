<!-- Source: https://docs.payram.com/api-integration/payouts-apis/payouts-status -->

## 
URL Details
Before making the request, you’ll need the following parameters that define your PayRam environment and platform.
Parameter
Description
Example
BASE_URL
Your PayRam server URL.
[https://yourdomain.com:8443arrow-up-right](https://yourdomain.com:8443%0A)
id
The unique payout ID you want to fetch.
120
API Endpoint
Endpoint to get details of a specific payout.
/api/v1/withdrawal/{id}/merchant
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
curl --location --request GET '${BASE_URL}/api/v1/withdrawal/114/merchant' \
--header 'API-Key: <API_KEY>' \
--header 'Content-Type: application/json' \
--data ''
```

## 
curl Response
You’ll receive essential payout details such as the amount, currency, recipient address, and current status for the specified withdrawal ID.
Copy
```
  "id": 114,
  "currencyCode": "USDC",
  "blockchainCode": "BASE",
  "amount": "1111",
  "toAddress": "0x4e51edd49b62eaca9e06b4afff9a7aab729a6c49",
  "recipientEmail": "kiran@xyz.com",
  "status": "pending-approval",
  "type": "payout_merchant",
  ...

```

circle-info
**Hint: Check the status field in the response to know the current payout state.**
The status field represents the payout’s current progress :
STATUS
DESCRIPTION
pending-otp-verification
Waiting for OTP verification before processing.
pending-approval
Awaiting admin or system approval.
pending
Approved and ready for blockchain processing.
initiated
Payout has been broadcast to the blockchain network and is awaiting confirmation.
sent
Payout successfully sent to the recipient.
failed
Transaction failed due to a processing error.
rejected
Payout request was declined by the system or admin.
processed
Transaction has been confirmed on the blockchain and recorded in the accounting
cancelled
The transaction was intentionally stopped before being sent or processed.
[PreviousCreate Payoutschevron-left](https://docs.payram.com/api-integration/payouts-apis/create-payouts)[NextGET All Payoutschevron-right](https://docs.payram.com/api-integration/payouts-apis/get-all-payouts)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
