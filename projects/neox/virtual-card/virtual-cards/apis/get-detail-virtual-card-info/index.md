<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-detail-virtual-card-info -->

### 
Endpoint: GET /v2/vc/virtual-cards/{virtualCardRequestId}/card-data
### 
Description:
Retrieve detailed encrypted information for a specific virtual card by its request ID.
## 
Request
### 
Request Body Field Descriptions (JSON)
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
data.merchantCode
string
Merchant code
data.virtualCardRequestId
string
Virtual card request identifier
data.cardEncryptedData.encryptedData
string
Encrypted card data
data.cardEncryptedData.encryptedKey
string
Encrypted key for decrypting card data
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
    "cardEncryptedData": {
      "encryptedData": "bjbtE2ZXiyJiNU3wQ0NASbRygKTUClngYDZKR3RnP7vvr1Rw2d9zNdmpR41fPT9+Gyhf1sVz7RWEbzxeobHAuCIBZbYY/v8kDnYblPPL+03dG/xoEVRQHnkYUj2qfL8A8r57oVlWSex9soe27s3vqIa5PTcqGggZh0LzAahfLgs0Ip43mP11ozvqp2p3",
      "encryptedKey": "DylKG9fhcOnWUmx+lk3izP8y2LHmQpiFwZMmvL/2lr7ZhPBqVETTtYVNgS7k0oS0r3vVtsn0rJiPN5gF7v4vM68Ba5/dxyUgbGeoqwHGHiuKUjPY/AiwWkLv+pYodHaXCClYPvNwyzWt4hLUwIWVjo58wm81JFigAbYHoIEFyFw="
  "message": "Successful",
  "neoResponseId": "de7750c5-772e-4136-ac78-62c57a106cce"

```

## 
Example cURL
Copy
```
curl -X GET "https://{base_url_openapi}/v2/vc/virtual-cards/{virtualCardRequestId}/card-data" \
  -H "Authorization: Bearer <YOUR_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Accept-Language: en"
```

## 
Notes
  * Requires Bearer token in the Authorization header.
  * The Accept-Language header can be used to specify the response language (Support: "vi", "en").
  * No request body required.
  * The card data is returned in encrypted form for security.


[PreviousAPI Get Detail Virtual Cardchevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/get-detail-virtual-card)[NextAPI Set Active Virtual Cardchevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/set-active-virtual-card)
Last updated 10 months ago
Was this helpful?
