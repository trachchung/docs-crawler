<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/api-create-virtual-cards -->

### 
Endpoint: POST /v2/vc/virtual-cards/batch
### 
Description:
Create a batch of virtual cards under a specified card policy.
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
Unique batch request ID (_UUID recommended_)
cardPolicy
string
Yes
Card policy request ID to apply to all cards
virtualCards
array
Yes
List of virtual card creation objects
virtualCards[].virtualCardRequestId
string
Yes
Unique request ID for each virtual card
virtualCards[].cardHolderName
string
Yes
Name of the card holder
virtualCards[].cardUserEmail
string
No
Email to receive OTP when user making transactions (Default using merchant's email)
virtualCards[].cardUserPhone
string
No
Phone to receive OTP SMS when user making transactions
virtualCards[].cardUserPhoneZoneCode
string
No
Phone number zone code (Insert `"+"` before zone number)
virtualCards[].extraInfo
object
No
Additional information (optional)
### 
Request sample
Copy
```
  "requestId": "b1e2c3d4-5678-1234-9abc-1234567890ab",
  "cardPolicy": "e424ae34-5c56-45c8-882e-98c4325981d3",
  "virtualCards": [
      "virtualCardRequestId": "a1b2c3d4-5678-1234-9abc-1234567890ab",
      "cardHolderName": "John Doe"
      "virtualCardRequestId": "b2c3d4e5-6789-2345-9bcd-2345678901bc",
      "cardHolderName": "Jane Smith"

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
data.requestId
object
Detail data of batch VirtualCard create request
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
Unique request identifier
merchantCode
string
Merchant code
createdAt
string
Creation timestamp (ISO 8601)
status
string
Status of the batch creation (default: "PASSED")
message
string
Processing message
### 
Response sample
Copy
```
  "code": 1,
  "state": 2,
  "data": {
    "requestId": "14453285-93d2-4fef-8a3e-fa6b8a99cf6f",
    "merchantCode": "COLRLC",
    "createdAt": "2025-06-04T01:15:39.529Z",
    "status": "PASSED",
    "message": "Please wait while we are processing your request"
  "message": "Successful",
  "neoResponseId": "c3f228b8-fc58-45c2-a01c-e954d1225635"

```

## 
Example cURL
Copy
```
curl -X POST "https://{base_url_openapi}/v2/vc/virtual-cards/batch" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en" \
  -d '{
    "requestId": "b1e2c3d4-5678-1234-9abc-1234567890ab",
    "cardPolicy": "e424ae34-5c56-45c8-882e-98c4325981d3",
    "virtualCards": [
        "virtualCardRequestId": "a1b2c3d4-5678-1234-9abc-1234567890ab",
        "cardHolderName": "John Doe"
        "virtualCardRequestId": "b2c3d4e5-6789-2345-9bcd-2345678901bc",
        "cardHolderName": "Jane Smith"

```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * The request body must be in JSON format.
  * Use a unique `requestId` for each request to avoid duplicate creations.
  * Use a unique `virtualCardRequestId` for each virtual card to avoid duplicate creations.


[PreviousAPI Create Virtual Cardchevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/api-create-virtual-card)[NextAPI Get List Virtual Cardschevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-list-virtual-cards)
Last updated 8 months ago
Was this helpful?
