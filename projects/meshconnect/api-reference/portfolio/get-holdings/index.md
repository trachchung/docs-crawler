<!-- Source: https://docs.meshconnect.com/api-reference/portfolio/get-holdings -->

[Skip to main content](https://docs.meshconnect.com/api-reference/portfolio/get-holdings#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Portfolio
Get holdings.
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
holdings
/
get
Try it
Get holdings.
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/holdings/get \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "authToken": "<string>",
  "type": "robinhood",
  "includeMarketValue": true


```

200
Trading platform example

```

  "content": {
    "equityPositions": [

        "symbol": "AAPL",
        "amount": 3,
        "costBasis": 109
      },

        "symbol": "F",
        "amount": 27,
        "costBasis": 7.05791

    ],
    "cryptocurrencyPositions": [

        "marketValue": 75.15,
        "lastPrice": 0.05,
        "symbol": "DOGE",
        "amount": 1503,
        "costBasis": 0.033
      },

        "symbol": "BTC",
        "amount": 3.0001672,
        "costBasis": 18000

    ],
    "status": "succeeded",
    "errorMessage": "",
    "displayMessage": "",
    "notSupportedEquityPositions": [

        "symbol": "CUSIP38259P508",
        "amount": 1

    ],
    "notSupportedCryptocurrencyPositions": [],
    "nftPositions": [],
    "optionPositions": [],
    "type": "robinhood",
    "accountId": "5FUVPB0",
    "institutionName": "Robinhood",
    "accountName": "Margin account"
  },
  "status": "ok",
  "message": "",
  "errorHash": "a394c021",
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
application/json
Request containing authentication token
authToken
string
required
Auth token that allows connecting to the target institution
Minimum string length: `1`
type
enum<string>
required
Type of the institution to connect
### Supported integrations:
`Robinhood` `Coinbase` `Kraken` `CryptoCom` `OpenSea` `Binance` `Gemini` `OkCoin` `KuCoin` `CexIo` `BinanceInternational` `Bitstamp` `GateIo` `Okx` `BitFlyer` `Coinlist` `Huobi` `Bitfinex` `KrakenDirect` `BinanceInternationalDirect` `BitfinexDirect` `Bybit` `Paxos` `CoinbasePrime` `BtcTurkDirect` `KuCoinDirect` `OkxOAuth` `ParibuDirect` `RobinhoodConnect` `BlockchainCom` `BitsoDirect` `BinanceOAuth` `BybitDirect` `ParibuOAuth` `BinanceTrDirect` `BybitDirectMobile` `Sandbox` `Uphold` `SandboxCoinbase` `DeFiWallet`
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
includeMarketValue
boolean
#### Response
200
application/json
Holdings obtained
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
[ Get transfers initiated by Mesh Previous ](https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh)[ Get holdings values. Next ](https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values)
Ctrl+I
Get holdings.
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/holdings/get \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "authToken": "<string>",
  "type": "robinhood",
  "includeMarketValue": true


```

200
Trading platform example

```

  "content": {
    "equityPositions": [

        "symbol": "AAPL",
        "amount": 3,
        "costBasis": 109
      },

        "symbol": "F",
        "amount": 27,
        "costBasis": 7.05791

    ],
    "cryptocurrencyPositions": [

        "marketValue": 75.15,
        "lastPrice": 0.05,
        "symbol": "DOGE",
        "amount": 1503,
        "costBasis": 0.033
      },

        "symbol": "BTC",
        "amount": 3.0001672,
        "costBasis": 18000

    ],
    "status": "succeeded",
    "errorMessage": "",
    "displayMessage": "",
    "notSupportedEquityPositions": [

        "symbol": "CUSIP38259P508",
        "amount": 1

    ],
    "notSupportedCryptocurrencyPositions": [],
    "nftPositions": [],
    "optionPositions": [],
    "type": "robinhood",
    "accountId": "5FUVPB0",
    "institutionName": "Robinhood",
    "accountName": "Margin account"
  },
  "status": "ok",
  "message": "",
  "errorHash": "a394c021",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
