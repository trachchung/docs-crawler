<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-card-policies/set-active-virtual-card-policy -->

### 
Endpoint: PUT /v2/vc/virtual-card-policies/{requestId}/set-active
### 
Description:
Set the active status of a specific virtual card policy by its ID.
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
Set to `true` to activate, `false` to deactivate the policy.
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
data.requestId
string
Unique request identifier
data.merchantCode
string
Merchant code
data.name
string
Name of the policy
data.isActive
boolean
Whether the policy is active
data.createdBy
string
Creator's email
data.createdAt
string
Creation timestamp (ISO 8601)
data.updatedAt
string
Last update timestamp (ISO 8601)
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
    "requestId": "e424ae34-5c56-45c8-882e-98c4325981d3",
    "merchantCode": "COLRLC",
    "name": "Synchronised reciprocal open architecture",
    "isActive": true,
    "createdBy": "sony@gmail.com",
    "createdAt": "2025-06-04T09:34:25.959Z",
    "updatedAt": "2025-06-05T01:58:03.365Z"
  "message": "Successful",
  "neoResponseId": "48589ad9-009b-4ac9-af10-d7680ea83ca6"

```

## 
Example cURL
Copy
```
curl -X PUT "https://{base_url_openapi}/v2/vc/virtual-card-policies/{requestId}/set-active" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en" \
  -d '{
    "isActive": true

```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * Replace `{requestId}` with the actual policy request ID.


[PreviousAPI Get List Card Policieschevron-left](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/get-list-virtual-card-policies)[NextAPI Update Card Policychevron-right](https://docs.neox.vn/docs/virtual-card/virtual-card-policies/update-create-virtual-card-policy)
Last updated 10 months ago
Was this helpful?
