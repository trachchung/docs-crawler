<!-- Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-deposit-address -->

[Skip to main content](https://docs.meshconnect.com/api-reference/managed-transfers/get-deposit-address#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Managed Transfers
Get deposit address
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
address
/
get
Try it
Get deposit address
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/transfers/managed/address/get \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "symbol": "DOGE",
  "networkId": "34b66a94-f9f9-49ef-81e8-6ebd5a866f9d",
  "authToken": "Secret authentication token",
  "type": "binanceInternational"


```

200
400
404

```

  "content": {
    "symbol": "DOGE",
    "address": "D641Fmzx...",
    "chain": "DOGE"
  },
  "status": "ok",
  "message": "",
  "errorHash": "010074a1",
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
authToken
string
required
Auth token that allows connecting to the target institution
Minimum string length: `1`
type
enum<string>
required
Type of the institution to connect
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
symbol
string | null
Symbol of the required cryptocurrency, e.g. ETH or BTC. Can be used instead of the `AddressType` field.
addressType
enum<string>
Type of the address of symbol to be transferred. Providing `EthAddress` will assume a transfer of ETH over Ethereum blockchain. Can be used instead of `Symbol` field.
Available options: 
`ethAddress`, 
`btcAddress`, 
`ltcAddress`, 
`solAddress`, 
`algoAddress`, 
`celoAddress`, 
`cardanoAddress`, 
`polygonAddress`, 
`bnbAddress`, 
`elrondAddress`, 
`neoAddress`, 
`xrpAddress`, 
`flowAddress`, 
`harmonyOneAddress`, 
`tronAddress`, 
`dogeAddress`, 
`opAddress`
networkId
string<uuid>
Specifies which the network to use to obtain the deposit address of the `Symbol` asset.
mfaCode
string | null
Some of integrations require MFA code to create a deposit address, e.g. KrakenDirect
#### Response
200
application/json
Address successfully obtained or generation initiated.
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
[ Get supported tokens list Previous ](https://docs.meshconnect.com/api-reference/managed-transfers/get-supported-tokens-list)[ Get deposit addresses Next ](https://docs.meshconnect.com/api-reference/managed-transfers/get-list-of-deposit-addresses)
Ctrl+I
Get deposit address
cURL

```
curl --request POST \
  --url https://integration-api.meshconnect.com/api/v1/transfers/managed/address/get \
  --header 'Content-Type: application/json' \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>' \
  --data '

  "symbol": "DOGE",
  "networkId": "34b66a94-f9f9-49ef-81e8-6ebd5a866f9d",
  "authToken": "Secret authentication token",
  "type": "binanceInternational"


```

200
400
404

```

  "content": {
    "symbol": "DOGE",
    "address": "D641Fmzx...",
    "chain": "DOGE"
  },
  "status": "ok",
  "message": "",
  "errorHash": "010074a1",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
