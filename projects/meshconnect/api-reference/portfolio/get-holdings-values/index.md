<!-- Source: https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values -->

[Skip to main content](https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Portfolio
Get holdings values.
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
value
Try it
Get holdings values.
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/holdings/value \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "authToken": "Secret authentication token",
  "type": "binanceInternationalDirect"


```

200
400

```

  "content": {
    "totalValue": 186.03,
    "totalPerformance": 6.23,
    "equitiesValue": 100.12,
    "equitiesPerformance": 5.3457,
    "cryptocurrenciesValue": 50.37,
    "cryptocurrenciesPerformance": 7.23,
    "nftsValue": 15.34,
    "fiatValue": 20.2
  },
  "status": "ok",
  "message": "",
  "errorHash": "f2b4f62e",
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
Request with authentication token.
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
#### Response
200
application/json
Market values of assets
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
[ Get holdings. Previous ](https://docs.meshconnect.com/api-reference/portfolio/get-holdings)[ Get aggregated portfolio Next ](https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio)
Ctrl+I
Get holdings values.
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/holdings/value \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "authToken": "Secret authentication token",
  "type": "binanceInternationalDirect"


```

200
400

```

  "content": {
    "totalValue": 186.03,
    "totalPerformance": 6.23,
    "equitiesValue": 100.12,
    "equitiesPerformance": 5.3457,
    "cryptocurrenciesValue": 50.37,
    "cryptocurrenciesPerformance": 7.23,
    "nftsValue": 15.34,
    "fiatValue": 20.2
  },
  "status": "ok",
  "message": "",
  "errorHash": "f2b4f62e",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
