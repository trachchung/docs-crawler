<!-- Source: https://docs.payram.com/api-integration/payments-api/assign-deposit-address -->

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
Request Body
Field
Description
Example
blockchain_code
Blockchain code to assign address for (BTC, ETH, TRX, BASE, POLYGON)
ETH
## 
curl request
Before running the command, replace the placeholders with your actual details:
  * ${BASE_URL} → Your PayRam server URL
  * <your_api_key> → Your PayRam API key
  * reference_id → Use the value returned from the Create Payment API


Copy
```
curl --location '${BASE_URL}/api/v1/deposit-address/reference/{reference_id}' \
--header 'Content-Type: application/json' \
--data '{
  "blockchain_code": "ETH"

```

## 
curl response
  * Address – The user’s assigned deposit address for this blockchain family. This address will be reused for all future payments in the same family.
  * Family – The blockchain family (e.g., ETH_Family, BTC_Family, TRX_Family). Each family can include multiple chains — for example, Base, Polygon, and Ethereum share the same ETH_Family.
  * Status – Indicates the current state of the assigned address (e.g., active, inactive).


Copy
```
  "id": 324,
  "createdAt": "2025-11-05T06:53:42.419556Z",
  "Address": "0xCb12499d865271D1FfFf16308E523e0BB624a779",
  "Family": "ETH_Family",
  "Status": "active",
  "MemberID": 271,
  "xpub_id": 18,
  "BlockchainFamilyID": 1,
  "Member": { ... },
  "BlockchainFamily": { ... },
  "wallet": { ... }

```

circle-info
**Note****: Once a deposit address is assigned, it becomes permanent for that user within the same blockchain family. PayRam automatically reuses this address for subsequent transactions.**
[PreviousGet Blockchain Currencieschevron-left](https://docs.payram.com/api-integration/payments-api/get-blockchain-currencies)[NextPayment Statuschevron-right](https://docs.payram.com/api-integration/payments-api/payment-status)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
