<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/webhook -->

### 
Event data
Field Name
Type
Description
requestId
string
Unique batch request ID generated from merchant system
type
string
Webhook type, default value `"VIRTUAL_CARD"`
merchantCode
string
Merchant code.
merchantCode
string
Merchant code.
virtualCards
array
List of virtual card objects.
createdAt
string
Creation timestamp of the webhook event (ISO 8601).
#### 
`virtualCards` object item fields:
Field Name
Type
Description
virtualCardRequestId
string
Virtual card request identifier.
cardEncryptedData
object
Encrypted card data object.
cardEncryptedData.encryptedData
string
Encrypted card data.
cardEncryptedData.encryptedKey
string
Encrypted key for decrypting card data.
cardData
object
Card data object.
cardData.cardHolderName
string
Card holder's name.
cardData.cardNumber
string
Card number (masked or encrypted).
cardData.cardBrand
string
Card brand (e.g., visa, mastercard).
cardPolicy
object
Card policy object.
cardPolicy.policyRequestId
string
Policy request identifier.
cardPolicy.policyRevision
integer
Policy revision number.
cardPolicy.cardLimit
integer
Card limit.
cardPolicy.cardUse
string
Card usage setting
cardPolicy.cardCurrency
string
Card currency.
cardPolicy.minTransAmount
integer
Minimum transaction amount.
cardPolicy.maxTransAmount
integer
Maximum transaction amount.
cardPolicy.autoCloseCard
boolean
Whether card auto closes.
cardPolicy.supportedMccGroup
array
Supported MCC groups.
extraInfo
object
Additional information.
status
string
Card status.
createdAt
string
Creation timestamp (ISO 8601).
#### 
Card Status Values
Status
Description
INACTIVE
The card has been issued but is not yet active/usable.
ACTIVE
The card is currently active and can be used for payment.
EXPIRED
The card has passed its expiry date and cannot be used.
LOCKED
The card is temporarily locked and cannot be used.
FAILED
Card creation or activation failed; card is unusable.
### 
Sample data
Copy
```
  "requestId": "3af8dd44-d869-4fa1-8ec6-44bd12a26daa",
  "type": "VIRTUAL_CARD",
  "merchantCode": "COLRLC",
  "virtualCards": [
      "virtualCardRequestId": "cb549460-89da-4e06-b41b-e285c0d695a0",
      "cardEncryptedData": {
        "encryptedData": "vqBS9d7dehPOtEKJDwahAefMJ44l6HJAsUz4vvSnPb6ueNkfSLhoruXIVXzJSuT/caadc/7psCgJLYx3R3ZYIiLnLp5GYuKEKJKf6qKdlwHOrJZsXaRp9/tw158Lm2zq0CJrgVDQr+jSOicnGACi1ENUl5MNTM/VH0qx0MkphzYG9OAZ3MSXS7wqzw==",
        "encryptedKey": "jnI1VkbDs23JcBG7A6G6VSKJYd4mQzjEg6U+RiKE1hlsEjYNlJ442e2+3vc4MA45gyGADRWIv2Ad2xjcJA60Wp5W/ya4dJ1MRylemoqRNnuzkwSHdQOFjKX5x4OKuUDw6khphjUKMqb24rAbwzCWnc/aGvRdLIXC4+wZ54kQ1lk="
      "cardData": {
        "cardHolderName": "NEMO EST EXCEPTURI",
        "cardNumber": "513385******7331",
        "cardBrand": "mastercard"
      "cardPolicy": {
        "policyRequestId": "e424ae34-5c56-45c8-882e-98c4325981d3",
        "policyRevision": 3,
        "cardLimit": 30000,
        "cardCurrency": "USD",
        "minTransAmount": 10,
        "maxTransAmount": 2000,
        "autoCloseCard": false,
        "supportedMccGroup": ["9405", "8011"]
      "extraInfo": {},
      "status": "ACTIVED",
      "createdAt": "2025-06-05T03:31:47.045Z"
  "createdAt": "2025-06-05T03:31:47.025Z"

```

[PreviousAPI Update Virtual Card Userchevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/apis/update-virtual-card-user)[NextDecrypting Card Data Algorithmchevron-right](https://docs.neox.vn/docs/virtual-card/virtual-cards/decrypt-card-sensitive-data)
Last updated 9 months ago
Was this helpful?
