<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-card-policies/update-create-virtual-card-policy -->

### 
Endpoint: PUT /v2/vc/virtual-card-policies/{requestId}
### 
Description:
Update an existing virtual card policy with new parameters such as name, card brand, currency, limits, and supported MCC groups.
## 
Request
### 
Request Body Field Descriptions (JSON)
Field Name
Type
Required
Description
name
string
No
Name of the policy
cardBrand
string
No
Card brand (`"visa"`, `"mastercard"`)
cardCurrency
integer
No
Card currency (Support: `"USD"`, `"EUR"`, `"GBP"`, `"SGD"`, `"HKD"`, `"VND"`). Default: **USD**
cardLimit
integer
No
Maximum card limit (_in currency_)
expiryDate
string
No
Card expiry date in format `YYYY-MM`
minTransAmount
integer
No
Minimum transaction amount (_in currency_)
maxTransAmount
integer
No
Maximum transaction amount (_in currency_)
activeOnCreate
boolean
No
Whether the card is active upon creation. Default: `false`
autoCloseCard
boolean
No
Whether the card should auto-close. Default: `false`
supportedMccGroup
string[]
No
List of supported Merchant Category Codes (MCC)
### 
Request sample
Copy
```
  "name": "Synchronised reciprocal open architecture",
  "cardBrand": "visa",
  "cardCurrency": "USD",
  "cardLimit": 30000,
  "minTransAmount": 10,
  "maxTransAmount": 2000,
  "activeOnCreate": true,
  "autoCloseCard": false,
  "expiryDate": "2028-12",
  "supportedMccGroup": [
    "9405",
    "8011"

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
Details of the updated virtual card policy
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
    "name": "Synchronised reciprocal open architecture",
    "cardBrand": "visa",
    "cardCurrency": "USD",
    "cardLimit": 30000000,
    "expiryDate": "2028-12",
    "minTransAmount": 10000,
    "maxTransAmount": 20000000,
    "activeOnCreate": true,
    "autoCloseCard": false,
    "supportedMccGroup": [
      "9405",
      "8011"
    "isActive": true,
    "revision": 2,
    "createdAt": "2025-06-04T09:34:25.959Z",
    "createdBy": "sony@gmail.com",
    "updatedAt": "2025-06-05T01:52:37.480Z"
  "message": "Successful",
  "neoResponseId": "269524e2-5050-4b84-bb7d-f7f85c4c5a52"

```

## 
Example cURL
Copy
```
curl -X PUT "https://{base_url_openapi}/v2/vc/virtual-card-policies/{requestId}" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "accept-language: vi" \
  -d '{
    "name": "Synchronised reciprocal open architecture",
    "cardBrand": "visa",
    "cardCurrency": "USD",
    "cardLimit": 30000,
    "minTransAmount": 10,
    "maxTransAmount": 2000,
    "activeOnCreate": true,
    "autoCloseCard": false,
    "expiryDate": "2028-12",
    "supportedMccGroup": [
      "9405",
      "8011"

```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * Replace `{requestId}` in the endpoint with the actual policy request ID.
  * Ensure the MCC codes are valid and supported by your system.


[PreviousAPI Set Active Card Policychevron-left](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/set-active-virtual-card-policy)[NextVirtual Card Managementchevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards)
Last updated 9 months ago
Was this helpful?
