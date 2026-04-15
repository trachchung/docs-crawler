<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-card-policies/get-detail-virtual-card-policy -->

### 
Endpoint: GET /v2/vc/virtual-card-policies/{requestId}
### 
Description:
Get created Virtual Card Policy.
## 
Request
### 
Request Body Field Descriptions
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
Details of the virtual card policy
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
name
string
Name of the policy
cardBrand
string
Card brand (e.g., visa)
expiryDate
string
Expiry date (YYYY-MM)
cardCurrency
string
Card currency
cardLimit
number
Card limit (_in currency_)
cardUse
string
Card usage setting
minTransAmount
number
Minimum transaction amount (_in currency_)
maxTransAmount
number
Maximum transaction amount (_in currency_)
activeOnCreate
boolean
Whether active on creation
autoCloseCard
boolean
Whether card auto closes
supportedMccGroup
array
Supported MCC groups
isActive
boolean
Whether the policy is active
revision
number
Revision number
createdAt
string
Creation timestamp (ISO 8601)
createdBy
string
Creator's email
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
    "requestId": "e424ae34-5c56-45c8-882e-98c4325981d3",
    "merchantCode": "COLRLC",
    "name": "DMD TEST CHINH SACH THE AO CHO MASTERCARD",
    "cardBrand": "visa",
    "expiryDate": "2028-12",
    "cardCurrency": "USD",
    "cardLimit": 30000000,
    "minTransAmount": 10000,
    "maxTransAmount": 20000000,
    "activeOnCreate": true,
    "autoCloseCard": false,
    "supportedMccGroup": [
      "9405",
      "8011"
    "isActive": true,
    "revision": 1,
    "createdAt": "2025-06-04T09:34:25.959Z",
    "createdBy": "sony@gmail.com",
    "updatedAt": "2025-06-04T09:34:25.959Z"
  "message": "Successful",
  "neoResponseId": "ed849a63-1ffb-4032-b200-0548e53e2c08"

```

## 
Example cURL
Copy
```
curl -X GET "https://{base_url_openapi}/v2/vc/virtual-card-policies/e424ae34-5c56-45c8-882e-98c4325981d3" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "accept-language: en"
```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * No request body required.


[PreviousAPI Create Card Policychevron-left](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/create-virtual-card-policy)[NextAPI Get List Card Policieschevron-right](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/get-list-virtual-card-policies)
Last updated 9 months ago
Was this helpful?
