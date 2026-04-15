<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-detail-virtual-card -->

### 
Endpoint: GET /v2/vc/virtual-cards/{virtualCardRequestId}
### 
Description:
Retrieve detailed information about a specific virtual card, including card data (masked), associated policy, and status.
## 
Request
### 
Request Body Field Descriptions (JSON)
Field Name
Type
Required
Description
N/A
N/A
N/A
GET request does not require a JSON body.
### 
Request sample
Copy
```
// No request body required for this GET endpoint.
```

## 
Response
### 
Response Field Descriptions
Field Name
Type
Description
code
number
Response code
state
number
State of the response
data
object
Details of the virtual card
message
string
Response message
neoResponseId
string
Unique Neo response identifier
#### 
`data` object fields:
Field Name
Type
Description
requestId
string
Bath Request identifier
virtualCardRequestId
string
Virtual card request identifier
merchantCode
string
Merchant code
cardData.cardHolderName
string
Card holder's name
cardData.cardNumber
string
**Masked** card number
cardData.cardExpiryDate
string
Card expiry date (YYYY-MM)
cardData.cardBrand
string
Card brand (e.g., mastercard)
cardData.cardCVV
string
**Masked** card CVV
cardPolicy.policyRequestId
string
Policy request identifier
cardPolicy.policyRevision
number
Policy revision number
cardPolicy.cardCurrency
string
Card currency
cardPolicy.cardLimit
number
Card limit
cardPolicy.cardUse
string
Card usage setting
cardPolicy.minTransAmount
number
Minimum transaction amount
cardPolicy.maxTransAmount
number
Maximum transaction amount
cardPolicy.autoCloseCard
boolean
Whether card auto closes
cardPolicy.activeOnCreate
boolean
Whether active on creation
cardPolicy.supportedMccGroup
array
Supported MCC groups
cardUser.email
string
Email to receive OTP when user making transactions
cardUser.phoneZoneCode
string
Phone number zone code
cardUser.phone
string
Phone number to receive OTP SMS when user making transactions
status
string
Card status
extraInfo
object
Additional information
createdAt
string
Creation timestamp (ISO 8601)
updatedAt
string
Last update timestamp (ISO 8601)
### 
Response sample
Copy
```
  "code": 1,
  "state": 2,
  "data": {
    "requestId": "dcf35140-f306-4a2d-9435-3c2e2d606c19",
    "virtualCardRequestId": "dcf35140-f306-4a2d-9435-3c2e2d606c19",
    "merchantCode": "COLRLC",
    "cardData": {
      "cardHolderName": "Money Market Account",
      "cardNumber": "530723******1138",
      "cardExpiryDate": "2028-12",
      "cardBrand": "mastercard",
      "cardCVV": "***"
    "cardPolicy": {
      "policyRequestId": "e424ae34-5c56-45c8-882e-98c4325981d3",
      "policyRevision": 3,
      "cardCurrency": "USD",
      "cardLimit": 30000,
      "minTransAmount": 10,
      "maxTransAmount": 2000,
      "autoCloseCard": false,
      "activeOnCreate": true,
      "supportedMccGroup": [
        "9405",
        "8011"
    "cardUser": {
      "email": "john.doe@gmail.com",
      "phone": "+84",
      "phoneZoneCode": "987654321"
    "status": "INACTIVED",
    "extraInfo": {},
    "createdAt": "2025-06-05T02:03:39.179Z",
    "updatedAt": "2025-06-05T02:03:39.238Z"
  "message": "Successful",
  "neoResponseId": "942f1a34-c640-4371-a6af-a4b6f6622ebc"

```

## 
Example cURL
Copy
```
curl -X GET "https://{base_url_openapi}/v2/vc/virtual-cards/{virtualCardRequestId}" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en"
```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * No request body required.
  * Replace `{virtualCardRequestId}` with the actual virtual card request ID.
  * Common response status: 200 OK.


[PreviousAPI Get List Virtual Cardschevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-list-virtual-cards)[NextAPI Get Virtual Card Sensitive Datachevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-detail-virtual-card-info)
Last updated 8 months ago
Was this helpful?
