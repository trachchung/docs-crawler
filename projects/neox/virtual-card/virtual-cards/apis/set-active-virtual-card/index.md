<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/set-active-virtual-card -->

### 
Endpoint: PUT /v2/vc/virtual-cards/{virtualCardRequestId}/set-active
### 
Description:
Activate or deactivate a specific virtual card by setting its active status.
## 
Request
### 
Request Body Field Descriptions (JSON)
Field Name
Type
Required
Description
isActive
boolean
Yes
Set to true to activate, false to deactivate the card.
### 
Request sample
Copy
```
"isActive":true

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
data.isActive
boolean
Whether the card is active
data.status
string
Status of the card (e.g., ACTIVED)
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
    "isActive": true,
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
  -d '{"isActive": true}'
```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * The path parameter `{virtualCardRequestId}` should be replaced with the actual virtual card request ID.


[PreviousAPI Get Virtual Card Sensitive Datachevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-detail-virtual-card-info)[NextAPI Update Virtual Card Userchevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/update-virtual-card-user)
Last updated 10 months ago
Was this helpful?
