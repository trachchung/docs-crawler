<!-- Source: https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters -->

[Skip to main content](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Managed Account Authentication
Get Link token with parameters
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


POST
https://integration-api.meshconnect.com https://sandbox-integration-api.meshconnect.com
/
api
/
v1
/
linktoken
Try it
Get Link token with parameters
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/linktoken \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "userId": "UserId",
  "configurationId": "18a20b11-e47f-43b9-8546-94284e9ee547",
  "restrictMultipleAccounts": true,
  "transferOptions": {
    "toAddresses": [

        "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
        "symbol": "ETH",
        "address": "0x00000000000000000000000"
      },

        "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
        "symbol": "USDC",
        "address": "0x00000000000000000000000"
      },

        "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
        "symbol": "MATIC",
        "address": "0x00000000000000000000000"
      },

        "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
        "symbol": "USDC",
        "address": "0x00000000000000000000000"

    ],
    "amountInFiat": 10,
    "isInclusiveFeeEnabled": false,
    "generatePayLink": false
  },
  "disableApiKeyGeneration": false


```

200
400
404

```

  "content": {
    "linkToken": "aHR0cHM6Ly93ZWIubWVzaGNvbm5lY3QuY29tL2IyYi1pZnJhbWUve2NsaWVudElkfS9icm9rZXItY29ubmVjdD9hdXRoX2NvZGU9e2F1dGhDb2RlfQ=="
  },
  "status": "ok",
  "message": "",
  "errorHash": "8d443794",
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
#### Body
application/json text/json application/*+jsonapplication/jsontext/jsonapplication/*+json
Create Link token request.
userId
string
required
A unique Id representing the end user. Typically this will be a user Id from the client application. Personally identifiable information, such as an email address or phone number, should not be used. 300 characters length maximum.
Required string length: `1 - 300`
brokerType
enum<string>
deprecated
Type of integration to redirect to. Will redirect to catalog if not provided. Not supported types: DeFiWallet, CryptocurrencyAddress, CryptocurrencyWallet.
Available options: 
`robinhood`, 
`eTrade`, 
`alpaca`, 
`tdAmeritrade`, 
`weBull`, 
`stash`, 
`interactiveBrokers`, 
`public`, 
`coinbase`, 
`kraken`, 
`coinbasePro`, 
`cryptoCom`, 
`openSea`, 
`binanceUs`, 
`gemini`, 
`cryptocurrencyAddress`, 
`cryptocurrencyWallet`, 
`okCoin`, 
`bittrex`, 
`kuCoin`, 
`etoro`, 
`cexIo`, 
`binanceInternational`, 
`bitstamp`, 
`gateIo`, 
`acorns`, 
`okx`, 
`bitFlyer`, 
`coinlist`, 
`huobi`, 
`bitfinex`, 
`deFiWallet`, 
`krakenDirect`, 
`vanguard`, 
`binanceInternationalDirect`, 
`bitfinexDirect`, 
`bybit`, 
`paxos`, 
`coinbasePrime`, 
`btcTurkDirect`, 
`kuCoinDirect`, 
`okxOAuth`, 
`paribuDirect`, 
`robinhoodConnect`, 
`blockchainCom`, 
`bitsoDirect`, 
`binanceConnect`, 
`binanceOAuth`, 
`revolutConnect`, 
`binancePay`, 
`bybitDirect`, 
`paribuOAuth`, 
`payPalConnect`, 
`binanceTrDirect`, 
`coinbaseRamp`, 
`bybitDirectMobile`, 
`sandbox`, 
`cryptoComPay`, 
`bybitEuDirect`, 
`uphold`, 
`binancePayOnchain`, 
`sandboxCoinbase`, 
`bybitPay`
restrictMultipleAccounts
boolean
The final screen of Link allows users to “continue” back to your app or “Link another account.” If this param is present then this button will be hidden.
transferOptions
object
Encapsulates transaction-related parameters, including destination addresses and the amount to transfer in fiat currency.
Show child attributes
integrationId
string<uuid> | null
A unique identifier representing a specific integration obtained from the list of available integrations.
disableApiKeyGeneration
boolean
For direct integrations that also support API keys, Link presents the user with the option to generate an API key for seamless access. If this param is true, this feature will be disabled.
verifyWalletOptions
object
Encapsulates verify DeFi wallet parameters.
Show child attributes
subClientId
string<uuid> | null
Sub Client ID, for B2B2B clients to tailor Link experience for their clients.
#### Response
200
application/json
Link token created.
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
Show child attributes
Was this page helpful?
YesNo
[ Refresh auth token Next ](https://docs.meshconnect.com/api-reference/managed-account-authentication/refresh-auth-token)
Ctrl+I
Get Link token with parameters
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/linktoken \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "userId": "UserId",
  "configurationId": "18a20b11-e47f-43b9-8546-94284e9ee547",
  "restrictMultipleAccounts": true,
  "transferOptions": {
    "toAddresses": [

        "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
        "symbol": "ETH",
        "address": "0x00000000000000000000000"
      },

        "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
        "symbol": "USDC",
        "address": "0x00000000000000000000000"
      },

        "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
        "symbol": "MATIC",
        "address": "0x00000000000000000000000"
      },

        "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
        "symbol": "USDC",
        "address": "0x00000000000000000000000"

    ],
    "amountInFiat": 10,
    "isInclusiveFeeEnabled": false,
    "generatePayLink": false
  },
  "disableApiKeyGeneration": false


```

200
400
404

```

  "content": {
    "linkToken": "aHR0cHM6Ly93ZWIubWVzaGNvbm5lY3QuY29tL2IyYi1pZnJhbWUve2NsaWVudElkfS9icm9rZXItY29ubmVjdD9hdXRoX2NvZGU9e2F1dGhDb2RlfQ=="
  },
  "status": "ok",
  "message": "",
  "errorHash": "8d443794",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
