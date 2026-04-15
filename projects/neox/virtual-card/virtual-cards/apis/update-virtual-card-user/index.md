<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/update-virtual-card-user -->

### 
Endpoint: PUT /v2/vc/virtual-cards/{virtualCardRequestId}/card-user
### 
Description: Update the user contact information associated with a virtual card for receiving transaction notifications and OTP verification. This API allows merchants to modify the email address and phone number that will be used for sending OTP codes and transaction alerts when the virtual card is used for payments.
## 
Request
### 
Request Body Field Descriptions (JSON)
Field Name
Type
Required
Description
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
### 
Request sample
Copy
```
"cardUserPhoneZoneCode":"+84",
"cardUserPhone":"987654321",
"cardUserEmail":"john.doe@gmail.com"

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
data.merchantCode
string
Merchant code
data.virtualCardRequestId
string
Virtual card request identifier
data.cardUser.email
string
Email to receive OTP when user making transactions
data.cardUser.phoneZoneCode
string
Phone number zone code
data.cardUser.phone
string
Phone number to receive OTP SMS when user making transactions
message
string
Response message
neoResponseId
string
Unique Neo response identifier
### 
Response sample
Copy
```
  "code": 1,
  "state": 2,
  "data": {
    "merchantCode": "COLRLC",
    "virtualCardRequestId": "dcf35140-f306-4a2d-9435-3c2e2d606c19",
    "cardUser": {
      "email": "john.doe@gmail.com",
      "phone": "+84",
      "phoneZoneCode": "987654321"
    "status": "ACTIVED"
  "message": "Successful",
  "neoResponseId": "8a724725-dc09-4ef2-8011-b4575ee5090a"

```

## 
Example cURL
Copy
```
curl -X PUT "https://{base_url_openapi}/v2/vc/virtual-cards/{virtualCardRequestId}/set-active" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en" \
  -d '{
    "cardUserPhoneZoneCode": "+84",
    "cardUserPhone": "987654321",
    "cardUserEmail": "john.doe@gmail.com"

```

## 
Notes
  * All fields are optional, allowing partial updates of user information but phone and phoneZoneCode must go in pair
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * The path parameter `{virtualCardRequestId}` should be replaced with the actual virtual card request ID.


[PreviousAPI Set Active Virtual Cardchevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/set-active-virtual-card)[NextWebhookchevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/webhook)
Last updated 8 months ago
Was this helpful?
