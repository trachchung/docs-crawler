<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-card-policies/get-list-virtual-card-policies -->

### 
Endpoint: GET /v2/vc/virtual-card-policies
### 
Description:
Get list created virtual card policies.
## 
Request
### 
Request Params Field Descriptions
Field Name
Type
Required
Description
pageIndex
number
No
Index of the page to retrieve (pagination).
pageSize
number
No
Number of items per page (pagination).
dateFr
date string
No
Filter policies created from this date (YYYY-MM-DD).
dateTo
date string
No
Filter policies created up to this date (YYYY-MM-DD).
cardBrand
string
No
Filter by card brand (e.g., visa, mastercard).
isActive
boolean
No
Filter by active status.
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
data.docs
array object
List of virtual card policy documents
data.totalDocs
number
Total number of documents
data.totalPages
number
Total number of pages
message
string
Response message
neoResponseId
string
Unique Neo response identifier
#### 
`docs` object item fields:
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
    "docs": [
        "requestId": "5684fde0-2f5f-4ca3-892f-91619d9c93ca",
        "merchantCode": "COLRLC",
        "name": "Reactive national utilisation - quia architecto provident",
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
        "extraData": {},
        "revision": 1,
        "createdAt": "2025-06-04T09:48:36.387Z",
        "createdBy": "sony@gmail.com",
        "updatedAt": "2025-06-04T09:48:36.387Z"
    "totalDocs": 1,
    "totalPages": 1
  "message": "Successful",
  "neoResponseId": "4a0ba9cc-e11e-4e1b-9ec1-e3a2a1b6e3a9"

```

## 
Example cURL
Copy
```
curl -X GET "https://{base_url_openapi}/v2/vc/virtual-card-policies?isActive=true&cardBrand=visa&pageIndex=1&pageSize=10&dateFr=2025-06-01&dateTo=2025-06-30" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en"
```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * No request body required.
  * Common query parameters: isActive, cardBrand, pageIndex, pageSize, dateFr, dateTo,


[PreviousAPI Get Detail Card Policychevron-left](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/get-detail-virtual-card-policy)[NextAPI Set Active Card Policychevron-right](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/set-active-virtual-card-policy)
Last updated 9 months ago
Was this helpful?
