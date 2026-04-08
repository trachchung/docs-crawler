<!-- Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/retrieve-the-list-of-all-available-integrations -->

[Skip to main content](https://docs.meshconnect.com/api-reference/managed-account-authentication/retrieve-the-list-of-all-available-integrations#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Managed Account Authentication
Retrieve the list of all available integrations.
##### Managed Account Authentication
  * [POST Get Link token with parameters](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters)
  * [POST Refresh auth token](https://docs.meshconnect.com/api-reference/managed-account-authentication/refresh-auth-token)
  * [DEL Remove connection](https://docs.meshconnect.com/api-reference/managed-account-authentication/remove-connection)
  * [GET Get health status](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-health-status)
  * [GET Retrieve the list of all available integrations.](https://docs.meshconnect.com/api-reference/managed-account-authentication/retrieve-the-list-of-all-available-integrations)


##### Managed Transfers
  * [GET Get networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks)
  * [GET Get integrations](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations)
  * [GET Get supported tokens list](https://docs.meshconnect.com/api-reference/managed-transfers/get-supported-tokens-list)
  * [POST Get deposit address](https://docs.meshconnect.com/api-reference/managed-transfers/get-deposit-address)
  * [POST Get deposit addresses](https://docs.meshconnect.com/api-reference/managed-transfers/get-list-of-deposit-addresses)
  * [GET Get transfers initiated by Mesh](https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh)


##### Portfolio
  * [POST Get holdings.](https://docs.meshconnect.com/api-reference/portfolio/get-holdings)
  * [POST Get holdings values.](https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values)
  * [GET Get aggregated portfolio](https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio)


##### Balance
  * [POST Get account balance](https://docs.meshconnect.com/api-reference/balance/get-account-balance)
  * [GET Get aggregated portfolio fiat balances](https://docs.meshconnect.com/api-reference/balance/get-aggregated-portfolio-fiat-balances)


##### Verify
  * [POST Verify account identity.](https://docs.meshconnect.com/api-reference/verify/verify)
  * [GET Get wallet verifications for user and address.](https://docs.meshconnect.com/api-reference/verify/wallet)


##### Transfers to/from User's Linked Account
  * [POST Get deposit address](https://docs.meshconnect.com/api-reference/transfers/get-deposit-address)


GET
https://integration-api.meshconnect.com https://sandbox-integration-api.meshconnect.com
/
api
/
v1
/
integrations
Try it
Retrieve the list of all available integrations.
cURL

```
curl --request GET \
  --url https://integration-api.meshconnect.com/api/v1/integrations \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>'
```

200

```

  "content": {
    "items": [

        "id": "47624467-e52e-4938-a41a-7926b6c27acf",
        "name": "Coinbase",
        "type": "coinbase",
        "style": {
          "fieldActiveLight": "0052FF",
          "buttonPrimaryLight": "0052FF",
          "buttonHoverLight": "014CEC",
          "buttonTextLight": "FFFFFF",
          "buttonTextHoverLight": "FFFFFF",
          "fieldActiveDark": "578BFA",
          "buttonPrimaryDark": "578BFA",
          "buttonHoverDark": "507FE5",
          "buttonTextDark": "0A0B0D",
          "buttonTextHoverDark": "0A0B0D"
        },
        "logo": {
          "logoLightUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Light.svg",
          "logoDarkUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Dark.svg",
          "logoWhiteUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_White.svg",
          "logoBlackUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Black.svg",
          "logoColorUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Color.svg",
          "iconLightUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Light.svg",
          "iconDarkUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Dark.svg",
          "iconWhiteUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_White.svg",
          "iconBlackUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Black.svg",
          "iconColorUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Color.svg",
          "base64Logo": "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAA1VBMVEUAAAAAgP8AVf8AM/8AVdUAROgAQ+kAROkAROkAQ+oAQuoAROoAQ+gAROkAQ+kAQ+kAROkAQ+kAQ+kAROkAQugAQ+kAQ+kAROkAQ+kAQ+kAQ+kAQ+kAQ+kXVesOTuoAQ+kBROkERukFR+kNTeoOTeoUUusZVeshW+wpYe0qYu0uZe0yaO00ae05be5fifFgivGMqvWSr/amvfeqwPi7zfnE0/rO2/vU3/vY4vzc5fze5/zh6fzi6vzl7P3m7f3p7/3u8v7x9f73+f75+/76+//+/v////94Z10/AAAAH3RSTlMAAgMFBk9QUlNUVVZXiImKi4ykptfY2dvc3fHz9Pr8ZrpFhQAAAAFiS0dERhe6+e0AAADPSURBVBgZncHXVsJAFAXQExM6UhJCwEGPYsfesKCiAvf/P8m5swIhPLI3thbUo3gwiKNagJxyn6leCZmdNte0PCy1mdNAqswNRThBn+r0/n3+/XRAKwmg6lTnnyI/s2c6VaiI6kVerzg8phNCdWmNZHHBlRjK0LqVCTMGytC6kwkze1BdWteyGHElhopoHY7l7YZHJ3RCqBrV5VTk9288pKpABT2qs4eP2dfjPq3Eh1PihgJSLebsYslrck3DQ6aYMJUUkONXw44xnbDiY1v/vNIqVzlyMewAAAAASUVORK5CYII="
        },
        "cryptoTransfersSupported": true
      },

        "id": "3d8f5c31-9fc0-4b61-bdfb-00fb18cbb9ad",
        "name": "CoinCircle",
        "type": "deFiWallet",
        "deFiWalletProviderId": "36d8d9c0c7fe2957149ce8e878f3a01...",
        "categories": [
          "deFiWallet"
        ],
        "style": {
          "fieldActiveLight": "0052FF",
          "buttonPrimaryLight": "0052FF",
          "buttonHoverLight": "014CEC",
          "buttonTextLight": "FFFFFF",
          "buttonTextHoverLight": "FFFFFF",
          "fieldActiveDark": "578BFA",
          "buttonPrimaryDark": "578BFA",
          "buttonHoverDark": "507FE5",
          "buttonTextDark": "0A0B0D",
          "buttonTextHoverDark": "0A0B0D"
        },
        "logo": {
          "logoColorUrl": "https://file-cdn.meshconnect.com/public/logos/CoinCircle_Logo_Color.svg",
          "iconColorUrl": "https://file-cdn.meshconnect.com/public/logos/CoinCircle_Icon_Color.svg"
        },
        "cryptoTransfersSupported": true


  },
  "status": "ok",
  "message": "",
  "errorHash": "d48f676e",
  "teamCode": "P4",
  "errorType": ""

```

#### Authorizations
X-Client-Secret
string
header
required
Contact Mesh to get client Secret
X-Client-Id
string
header
required
Contact Mesh to get client Id
#### Response
200 - application/json
OK
status
enum<string>
Available options: 
`ok`, 
`serverFailure`, 
`permissionDenied`, 
`badRequest`, 
`notFound`, 
`conflict`, 
`tooManyRequest`, 
`locked`, 
`unavailableForLegalReasons`
message
string | null
A message generated by the API
displayMessage
string | null
User-friendly display message that can be presented to the end user
errorHash
string | null
An error grouping hash from string components and caller information. Used by bugsnag on FE for correct error grouping
teamCode
string | null
Opaque team code for error routing. Resolved from exception origin or caller file path via CODEOWNERS. Format: 2-character code (e.g., "7K", "M2"). Use for alerting/routing, not display.
errorType
string | null
Strictly-typed error type that is explaining the reason of an unsuccessful status of the operation. All possible error types are available in the documentation.
errorData
unknown
content
object
Integration response.
Show child attributes
Was this page helpful?
YesNo
[ Get health status Previous ](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-health-status)[ Get networks Next ](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks)
Ctrl+I
Retrieve the list of all available integrations.
cURL

```
curl --request GET \
  --url https://integration-api.meshconnect.com/api/v1/integrations \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>'
```

200

```

  "content": {
    "items": [

        "id": "47624467-e52e-4938-a41a-7926b6c27acf",
        "name": "Coinbase",
        "type": "coinbase",
        "style": {
          "fieldActiveLight": "0052FF",
          "buttonPrimaryLight": "0052FF",
          "buttonHoverLight": "014CEC",
          "buttonTextLight": "FFFFFF",
          "buttonTextHoverLight": "FFFFFF",
          "fieldActiveDark": "578BFA",
          "buttonPrimaryDark": "578BFA",
          "buttonHoverDark": "507FE5",
          "buttonTextDark": "0A0B0D",
          "buttonTextHoverDark": "0A0B0D"
        },
        "logo": {
          "logoLightUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Light.svg",
          "logoDarkUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Dark.svg",
          "logoWhiteUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_White.svg",
          "logoBlackUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Black.svg",
          "logoColorUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Logo_Color.svg",
          "iconLightUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Light.svg",
          "iconDarkUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Dark.svg",
          "iconWhiteUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_White.svg",
          "iconBlackUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Black.svg",
          "iconColorUrl": "https://file-cdn.meshconnect.com/public/logos/Coinbase_Icon_Color.svg",
          "base64Logo": "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAA1VBMVEUAAAAAgP8AVf8AM/8AVdUAROgAQ+kAROkAROkAQ+oAQuoAROoAQ+gAROkAQ+kAQ+kAROkAQ+kAQ+kAROkAQugAQ+kAQ+kAROkAQ+kAQ+kAQ+kAQ+kAQ+kXVesOTuoAQ+kBROkERukFR+kNTeoOTeoUUusZVeshW+wpYe0qYu0uZe0yaO00ae05be5fifFgivGMqvWSr/amvfeqwPi7zfnE0/rO2/vU3/vY4vzc5fze5/zh6fzi6vzl7P3m7f3p7/3u8v7x9f73+f75+/76+//+/v////94Z10/AAAAH3RSTlMAAgMFBk9QUlNUVVZXiImKi4ykptfY2dvc3fHz9Pr8ZrpFhQAAAAFiS0dERhe6+e0AAADPSURBVBgZncHXVsJAFAXQExM6UhJCwEGPYsfesKCiAvf/P8m5swIhPLI3thbUo3gwiKNagJxyn6leCZmdNte0PCy1mdNAqswNRThBn+r0/n3+/XRAKwmg6lTnnyI/s2c6VaiI6kVerzg8phNCdWmNZHHBlRjK0LqVCTMGytC6kwkze1BdWteyGHElhopoHY7l7YZHJ3RCqBrV5VTk9288pKpABT2qs4eP2dfjPq3Eh1PihgJSLebsYslrck3DQ6aYMJUUkONXw44xnbDiY1v/vNIqVzlyMewAAAAASUVORK5CYII="
        },
        "cryptoTransfersSupported": true
      },

        "id": "3d8f5c31-9fc0-4b61-bdfb-00fb18cbb9ad",
        "name": "CoinCircle",
        "type": "deFiWallet",
        "deFiWalletProviderId": "36d8d9c0c7fe2957149ce8e878f3a01...",
        "categories": [
          "deFiWallet"
        ],
        "style": {
          "fieldActiveLight": "0052FF",
          "buttonPrimaryLight": "0052FF",
          "buttonHoverLight": "014CEC",
          "buttonTextLight": "FFFFFF",
          "buttonTextHoverLight": "FFFFFF",
          "fieldActiveDark": "578BFA",
          "buttonPrimaryDark": "578BFA",
          "buttonHoverDark": "507FE5",
          "buttonTextDark": "0A0B0D",
          "buttonTextHoverDark": "0A0B0D"
        },
        "logo": {
          "logoColorUrl": "https://file-cdn.meshconnect.com/public/logos/CoinCircle_Logo_Color.svg",
          "iconColorUrl": "https://file-cdn.meshconnect.com/public/logos/CoinCircle_Icon_Color.svg"
        },
        "cryptoTransfersSupported": true


  },
  "status": "ok",
  "message": "",
  "errorHash": "d48f676e",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
