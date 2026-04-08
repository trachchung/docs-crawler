<!-- Source: https://docs.meshconnect.com/api-reference/managed-transfers/configure-transfer -->

[Skip to main content](https://docs.meshconnect.com/api-reference/managed-transfers/configure-transfer#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Configure transfer
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
transfers
/
managed
/
configure
Try it
cURL
Configure with provided list of addresses

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/transfers/managed/configure \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "isInclusiveFeeEnabled": false,
  "fromAuthToken": "Secret authentication token",
  "fromType": "robinhood",
  "toAddresses": [

      "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
      "symbol": "USDT",
      "address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"
    },

      "networkId": "0291810a-5947-424d-9a59-e88bb33e999d",
      "symbol": "USDT",
      "address": "HN7cABqLq46Es1jh92dQQisAq662SmxELLLsHHe4YWrH"
    },

      "networkId": "0880db06-7c7c-4738-898f-cf74efc03c47",
      "symbol": "BTC",
      "address": "3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5"




```

200
Successful transfer configuration

```

  "content": {
    "status": "succeeded",
    "holdings": [

        "symbol": "USDC",
        "availableBalance": 130,
        "availableBalanceInFiat": 0,
        "price": 0,
        "eligibleForTransfer": true,
        "networks": [

            "name": "Ethereum",
            "id": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
            "minimumAmount": 1,
            "totalEstimatedTransferFeeInFiat": 1.8,
            "estimatedNetworkGasFee": {
              "fee": 0.000850608941007,
              "feeCurrency": "ETH",
              "feeInFiat": 1.8,
              "feeInTransferCurrency": 0

            "institutionTransferFee": {
              "fee": 0,
              "feeCurrency": "ETH",
              "feeInFiat": 0,
              "feeInTransferCurrency": 0

            "eligibleForTransfer": true,
            "eligibleForTransferWithFunding": false,
            "isBridgingAsset": false
          },

            "name": "Solana",
            "id": "0291810a-5947-424d-9a59-e88bb33e999d",
            "minimumAmount": 1,
            "totalEstimatedTransferFeeInFiat": 0.1,
            "estimatedNetworkGasFee": {
              "fee": 0.00025,
              "feeCurrency": "SOL",
              "feeInFiat": 0.1,
              "feeInTransferCurrency": 0

            "institutionTransferFee": {
              "fee": 0,
              "feeCurrency": "SOL",
              "feeInFiat": 0,
              "feeInTransferCurrency": 0

            "eligibleForTransfer": true,
            "eligibleForTransferWithFunding": false,
            "isBridgingAsset": false

        ],
        "eligibleForTransferWithFunding": false


  },
  "status": "ok",
  "message": "",
  "errorHash": "e2c2ef28",
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
fromAuthToken
string
required
The authentication token to send assets from.
Minimum string length: `1`
fromType
enum<string>
required
The type of the integration to send assets from.
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
toAddresses
object[] | null
A list of available addresses provided by the API client. The list can contain all supported addresses by the client. Front API validates the addresses and returns the list of supported tokens and networks as the result of the operation.
Show child attributes
symbol
string | null
If provided, Front API returns only networks that support transferring of this symbol.
amount
number<double> | null
If provided, Front API configures the response to only return holdings with enough amount of this crypto for the transfer
amountInFiat
number<double> | null
If provided, Front API configures the response to only contain holdings with enough value (converted to fiat) for the transfer.
fiatCurrency
string | null
Fiat currency that is to get corresponding converted fiat values of transfer and fee amounts. If not provided, defaults to `USD`.
caipNetworkId
string | null
If provided, from API configures the response to include the requested network only.
networkId
string<uuid> | null
If provided, from API configures the response to include the requested network only.
isAtomicBatchTxAvailable
boolean | null
If provided, if connected wallet supports batched transactions.(DeFi only)
isInclusiveFeeEnabled
boolean
Specifies if all the fees are included in the amount to transfer.
#### Response
200
application/json
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
Show child attributes
Was this page helpful?
YesNo
Ctrl+I
cURL
Configure with provided list of addresses

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/transfers/managed/configure \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "isInclusiveFeeEnabled": false,
  "fromAuthToken": "Secret authentication token",
  "fromType": "robinhood",
  "toAddresses": [

      "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
      "symbol": "USDT",
      "address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"
    },

      "networkId": "0291810a-5947-424d-9a59-e88bb33e999d",
      "symbol": "USDT",
      "address": "HN7cABqLq46Es1jh92dQQisAq662SmxELLLsHHe4YWrH"
    },

      "networkId": "0880db06-7c7c-4738-898f-cf74efc03c47",
      "symbol": "BTC",
      "address": "3FZbgi29cpjq2GjdwV8eyHuJJnkLtktZc5"




```

200
Successful transfer configuration

```

  "content": {
    "status": "succeeded",
    "holdings": [

        "symbol": "USDC",
        "availableBalance": 130,
        "availableBalanceInFiat": 0,
        "price": 0,
        "eligibleForTransfer": true,
        "networks": [

            "name": "Ethereum",
            "id": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
            "minimumAmount": 1,
            "totalEstimatedTransferFeeInFiat": 1.8,
            "estimatedNetworkGasFee": {
              "fee": 0.000850608941007,
              "feeCurrency": "ETH",
              "feeInFiat": 1.8,
              "feeInTransferCurrency": 0

            "institutionTransferFee": {
              "fee": 0,
              "feeCurrency": "ETH",
              "feeInFiat": 0,
              "feeInTransferCurrency": 0

            "eligibleForTransfer": true,
            "eligibleForTransferWithFunding": false,
            "isBridgingAsset": false
          },

            "name": "Solana",
            "id": "0291810a-5947-424d-9a59-e88bb33e999d",
            "minimumAmount": 1,
            "totalEstimatedTransferFeeInFiat": 0.1,
            "estimatedNetworkGasFee": {
              "fee": 0.00025,
              "feeCurrency": "SOL",
              "feeInFiat": 0.1,
              "feeInTransferCurrency": 0

            "institutionTransferFee": {
              "fee": 0,
              "feeCurrency": "SOL",
              "feeInFiat": 0,
              "feeInTransferCurrency": 0

            "eligibleForTransfer": true,
            "eligibleForTransferWithFunding": false,
            "isBridgingAsset": false

        ],
        "eligibleForTransferWithFunding": false


  },
  "status": "ok",
  "message": "",
  "errorHash": "e2c2ef28",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
