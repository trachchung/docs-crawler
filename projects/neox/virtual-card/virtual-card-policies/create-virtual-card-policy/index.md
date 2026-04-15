<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-card-policies/create-virtual-card-policy -->

### 
Endpoint: `POST {{url_openapi}}/v2/vc/virtual-card-policies/`
### 
Description:
Create a new Virtual Card Policy for a merchant, specifying card limits, expiry, supported MCC groups, and other policy settings.
## 
Request
### 
Request Body Field Descriptions (JSON)
Field
Type
Required
Description
requestId
string
Yes
Unique request ID (_UUID recommended_)
name
string
Yes
Name of the virtual card policy
cardBrand
string
Yes
Card brand (Support: `"visa"`, `"mastercard"`)
cardCurrency
integer
Yes
Card currency (Support: `"USD"`, `"EUR"`, `"GBP"`, `"SGD"`, `"HKD"`, `"VND"`). Default: **USD**
cardLimit
integer
Yes
Maximum card limit (_in currency_)
cardUse
string
Yes
Setting for card multiple-use or single-use (Support: `"SINGLE"`, `"MULTIPLE"`). Default: **MULTIPLE**
expiryDate
string
Yes
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
  "name": "MERCHANT TEST VIRTUAL CARD POLICY",
  "requestId": "de1d2870-b3cf-4c92-ab0c-6b758ae4c7c4",
  "cardBrand": "visa",
  "cardCurrency": "USD",
  "cardLimit": 30000,
  "cardUse": "MULTIPLE",
  "expiryDate": "2028-12",
  "minTransAmount": 10,
  "maxTransAmount": 20000,
  "activeOnCreate": true,
  "autoCloseCard": false,
  "supportedMccGroup": ["9405", "8011"]

```

## 
Response
### 
Response Field Descriptions
Field
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
Details of the created policy
message
string
Status message
neoResponseId
string
Internal response tracking ID
#### 
`data` object fields:
Field
Type
Description
requestId
string
Merchant request ID
merchantCode
string
Merchant code
name
string
Policy name
cardBrand
string
Card brand
cardCurrency
string
Card currency
expiryDate
string
Expiry date
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
Active on create
autoCloseCard
boolean
Auto close card
supportedMccGroup
string[]
Supported MCC groups
isActive
boolean
Is policy active
extraData
object
Reserved for future use
revision
number
Revision number
createdAt
string
Creation timestamp (ISO 8601)
createdBy
string
Creator's email
### 
Response sample
Copy
```
  "code": 1,
  "state": 2,
  "data": {
    "requestId": "de1d2870-b3cf-4c92-ab0c-6b758ae4c7c4",
    "merchantCode": "COLRLC",
    "name": "MERCHANT TEST VIRTUAL CARD POLICY",
    "cardBrand": "visa",
    "cardCurrency": "USD",
    "cardLimit": 3000,
    "cardUse": "MULTIPLE",
    "expiryDate": "2028-12",
    "minTransAmount": 10,
    "maxTransAmount": 2000,
    "activeOnCreate": true,
    "autoCloseCard": false,
    "supportedMccGroup": [
      "9405",
      "8011"
    "isActive": true,
    "extraData": {},
    "revision": 1,
    "createdAt": "2025-06-04T02:08:31.887Z",
    "createdBy": "sony@gmail.com"
  "message": "Successful",
  "neoResponseId": "8bab83be-1048-4dd0-b846-b35241c8eca3"

```

## 
Example cURL
Copy
```
curl -X POST "https://{base_url_openapi}/v2/vc/virtual-card-policies" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en" \
  -d '{
    "name": "MERCHANT TEST VIRTUAL CARD POLICY",
    "requestId": "de1d2870-b3cf-4c92-ab0c-6b758ae4c7c4",
    "cardBrand": "visa",
    "cardCurrency": "USD",
    "cardLimit": 30000,
    "cardUser": "MULTIPLE",
    "expiryDate": "2028-12",
    "minTransAmount": 10,
    "maxTransAmount": 20000,
    "activeOnCreate": true,
    "autoCloseCard": false,
    "supportedMccGroup": ["9405", "8011"]

```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * Use a unique `requestId` for each request to avoid duplicate creations.
  * Ensure the MCC codes are valid and supported by your system.


[PreviousVirtual Card Policy Managementchevron-left](https://docs.neox.vn/docs/virtual-card/virtual-card-policies)[NextAPI Get Detail Card Policychevron-right](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/get-detail-virtual-card-policy)
Last updated 8 months ago
Was this helpful?
