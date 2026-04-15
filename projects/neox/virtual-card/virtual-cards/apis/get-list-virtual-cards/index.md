<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-list-virtual-cards -->

### 
Endpoint: GET /v2/vc/virtual-cards
### 
Description:
Retrieve a paginated list of virtual cards, optionally filtered by requestId, status, cardBrand, or cardHolderName.
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
requestId
string
No
Filter by virtual card batch request ID.
status
string
No
Filter by card status (e.g., ACTIVED).
cardBrand
string
No
Filter by card brand (e.g., visa, mastercard).
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
array
List of virtual card documents
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
Virtual card batch request ID
virtualCardRequestId
string
Virtual card request identifier
merchantId
string
Merchant unique identifier
merchantCode
string
Merchant code
merchantEmail
string
Merchant email
cardData.cardHolderName
string
Card holder name
cardData.cardBrand
string
Card brand
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
Card limit amount
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
status
string
Card status
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
    "docs": [
        "requestId": "dcf35140-f306-4a2d-9435-3c2e2d606c19",
        "virtualCardRequestId": "dcf35140-f306-4a2d-9435-3c2e2d606c19",
        "merchantId": "65e04347da1793874c4f9476",
        "merchantCode": "COLRLC",
        "merchantEmail": "sony@gmail.com",
        "cardData": {
          "cardHolderName": "Money Market Account",
          "cardBrand": "mastercard"
        "cardPolicy": {
          "policyRequestId": "e424ae34-5c56-45c8-882e-98c4325981d3",
          "policyRevision": 3,
          "cardCurrency": "USD",
          "cardLimit": 30000,
          "minTransAmount": 10,
          "maxTransAmount": 2000,
          "autoCloseCard": false,
        "status": "INACTIVED",
        "extraInfo": {},
        "createdAt": "2025-06-05T02:03:39.179Z",
        "updatedAt": "2025-06-05T02:03:39.238Z"
    "totalDocs": 1,
    "totalPages": 1
  "message": "Successful",
  "neoResponseId": "99598a34-5d76-4543-9580-0c7c89f998fa"

```

## 
Example cURL
Copy
```
curl -X GET "https://{base_url_openapi}/v2/vc/virtual-cards/" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en"
```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * Common query parameters: pageIndex, pageSize, dateFr, dateTo, requestId, status, cardBrand.
  * No request body required.


[PreviousAPI Create List Virtual Cardschevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/api-create-virtual-cards)[NextAPI Get Detail Virtual Cardchevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-detail-virtual-card)
Last updated 9 months ago
Was this helpful?
