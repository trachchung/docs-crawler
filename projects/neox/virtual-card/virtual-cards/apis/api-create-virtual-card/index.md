<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/api-create-virtual-card -->

### 
Endpoint: POST /v2/vc/virtual-cards/
### 
Description:
Create a new virtual card based on a specified card policy and cardholder information.
## 
Request
### 
Request Body Field Descriptions (JSON)
Field Name
Type
Required
Description
requestId
string
Yes
Unique request ID (_UUID recommended_)
cardPolicy
string
Yes
Card policy request ID to apply
cardHolderName
string
Yes
Name of the cardholder
cardUserEmail
string
No
Email to receive OTP when user making transactions (Default using merchant's email)
cardUserPhone
string
No
Phone number to receive OTP SMS when user making transactions
cardUserPhoneZoneCode
string
No
Phone number zone code (Insert `"+"` before zone number)
extraInfo
object
No
Additional information (optional)
### 
Request sample
Copy
```
"requestId":"e1b2c3d4-5678-1234-9abc-1234567890ab",
"cardPolicy":"e424ae34-5c56-45c8-882e-98c4325981d3",
"cardBrand":"mastercard",
"cardHolderName":"John Doe",
"cardUserPhoneZoneCode":"+84",
"cardUserPhone":"987654321",
"cardUserEmail":"john.doe@gmail.com",
"extraInfo":{}

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
Details of the created virtual card
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
virtualCardRequestId
string
Unique virtual card request identifier
cardData.cardHolderName
string
Name of the cardholder
cardData.cardNumber
string
Masked card number
cardData.cardBrand
string
Card brand
cardPolicy.policyRequestId
string
Policy request ID
cardPolicy.policyRevision
number
Policy revision number
cardPolicy.cardCurrency
string
Card currency
cardPolicy.cardLimit
number
Card limit
cardPolicy.minTransAmount
number
Minimum transaction amount
cardPolicy.maxTransAmount
number
Maximum transaction amount
cardPolicy.autoCloseCard
boolean
Whether card auto closes
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
extraInfo
object
Additional information
status
string
Status of the virtual card
createdAt
string
Creation timestamp (ISO 8601)
### 
Response sample
Copy
```
  "code": 1,
  "state": 2,
  "data": {
    "virtualCardRequestId": "dcf35140-f306-4a2d-9435-3c2e2d606c19",
    "cardData": {
      "cardHolderName": "John Doe",
      "cardNumber": "530723******1138",
      "cardBrand": "mastercard"
    "cardPolicy": {
      "policyRequestId": "e424ae34-5c56-45c8-882e-98c4325981d3",
      "policyRevision": 3,
      "cardCurrency": "USD",
      "cardLimit": 30000,
      "minTransAmount": 10,
      "maxTransAmount": 2000,
      "autoCloseCard": false,
      "supportedMccGroup": [
        "9405",
        "8011"
    "cardUser": {
      "email": "john.doe@gmail.com",
      "phone": "+84",
      "phoneZoneCode": "987654321"
    "extraInfo": {},
    "status": "INACTIVED",
    "createdAt": "2025-06-05T02:03:39.179Z"
  "message": "Successful",
  "neoResponseId": "ac23ea1c-98db-4ed6-b927-7e7692ef2f69"

```

## 
Example cURL
Copy
```
curl -X POST "https://{base_url_openapi}/v2/vc/virtual-cards/" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en" \
  -d '{
  "requestId": "e1b2c3d4-5678-1234-9abc-1234567890ab",
  "cardPolicy": "e424ae34-5c56-45c8-882e-98c4325981d3",
  "cardBrand": "mastercard",
  "cardHolderName": "John Doe",
  "cardUserPhoneZoneCode": "+84",
  "cardUserPhone": "987654321",
  "cardUserEmail": "john.doe@gmail.com",
  "extraInfo": {}

```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * The card will be created based on the specified policy and cardholder details.
  * Use a unique `requestId` for each request to avoid duplicate creations.


[PreviousVirtual Card APIschevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis)[NextAPI Create List Virtual Cardschevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/api-create-virtual-cards)
Last updated 8 months ago
Was this helpful?
