<!-- Source: https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh -->

[Skip to main content](https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Managed Transfers
Get transfers initiated by Mesh
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
transfers
/
managed
/
mesh
Try it
Get transfers initiated by Mesh
cURL

```
curl --request GET \
  --url https://integration-api.meshconnect.com/api/v1/transfers/managed/mesh \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>'
```

200
400

```

  "content": {
    "items": [

        "amountToReceive": 0,
        "networkId": "00000000-0000-0000-0000-000000000000",
        "networkLogoUrl": "https://file-cdn.meshconnect.com/public/logos/networks/Polygon.svg",
        "from": {
          "logoUrl": "https://logo.com/logo.jpg",
          "id": "8e25acb5-a9e2-4d00-8772-a255f010a2a9",
          "type": "robinhood",
          "name": "Robinhood"
        },
        "totalFeesAmountInFiat": 0.5,
        "totalTransactionAmountInFiat": 1000.5,
        "fundingMethods": [

            "type": "cryptocurrencyConversion",
            "amount": 2,
            "amountInFiat": 20,
            "toSymbol": "WETH",
            "fromAmount": 1,
            "fromSymbol": "BTC",
            "fee": {
              "fee": 0.0001,
              "feeCurrency": "ETH",
              "feeInFiat": 0.1,
              "feeInTransferCurrency": 0

          },

            "type": "paymentMethodDepositUsage",
            "amount": 3,
            "amountInFiat": 30,
            "toSymbol": "WETH",
            "fromAmount": 1,
            "fromSymbol": "USD",
            "paymentMethodType": "bankAccount",
            "fee": {
              "fee": 0.0001,
              "feeCurrency": "USD",
              "feeInFiat": 0.1,
              "feeInTransferCurrency": 0

          },

            "type": "existingCryptocurrencyBalance",
            "amount": 5,
            "amountInFiat": 50,
            "toSymbol": "WETH",
            "fromAmount": 5,
            "fromSymbol": "ETH"

        ],
        "webhookLogs": [],
        "id": "8e25acb5-a9e2-4d00-8772-a255f010a2a9",
        "clientTransactionId": "123456",
        "institutionTransactionId": "456789",
        "status": "succeeded",
        "amountInFiat": 1000.3,
        "amountToReceiveInFiat": 0,
        "amountInFiatCurrencyCode": "USD",
        "amount": 10.123,
        "symbol": "WETH",
        "tokenAddress": "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
        "networkName": "Polygon",
        "createdTimestamp": 1653211113,
        "hash": "0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...",
        "gasFee": {
          "fee": 0.0001,
          "feeCurrency": "MATIC",
          "feeInFiat": 0.1,
          "feeInTransferCurrency": 0
        },
        "withdrawalFee": {
          "fee": 0.0001,
          "feeCurrency": "WETH",
          "feeInFiat": 0.1,
          "feeInTransferCurrency": 0
        },
        "processingFee": {
          "fee": 0.0001,
          "feeCurrency": "WETH",
          "feeInFiat": 0.1,
          "feeInTransferCurrency": 0
        },
        "executedTimestamp": 1707462614,
        "transferType": "payment",
        "isFeeIncluded": false,
        "infoUrl": "https://polygonscan.com/tx/0x5b0ac59e43b63f2985d78994b6270d747f1019777201ca18ebb36ad1e1a8693e",
        "isSmartFundingTransfer": false,
        "unitPrice": 0,
        "requestedTransferAmount": 0,
        "isBridgingTransfer": false,
        "userId": "123456798",
        "sourceAmount": 10.122,
        "destinationAmount": 10
      },

        "amountToReceive": 0,
        "networkId": "00000000-0000-0000-0000-000000000000",
        "from": {
          "logoUrl": "https://logo.com/logo.jpg",
          "id": "8e25acb5-a9e2-4d00-8772-a255f010a2a9",
          "type": "deFiWallet",
          "name": "MetaMask"
        },
        "totalFeesAmountInFiat": 0,
        "totalTransactionAmountInFiat": 10.3,
        "fundingMethods": [],
        "webhookLogs": [],
        "id": "12345678-a9e2-4d00-8772-a255f010a2a9",
        "clientTransactionId": "123456",
        "institutionTransactionId": "456789",
        "status": "failed",
        "amountInFiat": 10.3,
        "amountToReceiveInFiat": 0,
        "amountInFiatCurrencyCode": "USD",
        "amount": 0.123,
        "symbol": "WETH",
        "tokenAddress": "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
        "networkName": "Polygon",
        "createdTimestamp": 1653211113,
        "hash": "0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...",
        "isFeeIncluded": false,
        "isSmartFundingTransfer": false,
        "unitPrice": 0,
        "requestedTransferAmount": 0,
        "isBridgingTransfer": false,
        "userId": "123456798"

    ],
    "total": 10,
    "range": {
      "start": 0,
      "end": -1,
      "isValid": false,
      "count": 0
    },
    "hasMorePages": true
  },
  "status": "ok",
  "message": "",
  "errorHash": "bf6d53f3",
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
#### Query Parameters
Count
integer<int32>
Number of items to return. Default 10, maximum - 1000.
Offset
integer<int32>
Number of items to skip.
Id
string<uuid>
Mesh transfer identifier.
ClientTransactionId
string
Client transaction identifier.
Maximum string length: `128`
UserId
string
Client's user identifier.
Maximum string length: `50`
IntegrationIds
string<uuid>[]
Transfered integration.
Maximum array length: `100`
Statuses
enum<string>[]
Transfer statuses.
Maximum array length: `5`
Available options: 
`pending`, 
`succeeded`, 
`failed`
FromTimestamp
integer<int64>
Transfer created minimum timestamp.
ToTimestamp
integer<int64>
Transfer created maximum timestamp.
MinAmountInFiat
number<double>
Minimum amount in fiat.
MaxAmountInFiat
number<double>
Maximum amount in fiat.
OrderBy
enum<string>
Order by column.
Available options: 
`id`, 
`clientTransferId`, 
`userId`, 
`fromType`, 
`amountInFiat`, 
`status`, 
`createdTimestamp`, 
`symbol`, 
`networkName`
Hash
string
Transfer hash.
SubClientId
string<uuid>
Sub-client identifier.
DescendingOrder
boolean
Value indicating if ordering is descending.
IncludeRefundInformation
boolean
When true, includes refund information (summary and details) in the response. This includes partial refund data with transaction hashes, statuses, and amounts. Default is false for backward compatibility.
IncludeWebhooksLogs
boolean
When true, includes Transfer Status update webhooks data sent to client.
#### Response
200
application/json
Transfers obtained.
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
[ Get deposit addresses Previous ](https://docs.meshconnect.com/api-reference/managed-transfers/get-list-of-deposit-addresses)[ Get holdings. Next ](https://docs.meshconnect.com/api-reference/portfolio/get-holdings)
Ctrl+I
Get transfers initiated by Mesh
cURL

```
curl --request GET \
  --url https://integration-api.meshconnect.com/api/v1/transfers/managed/mesh \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>'
```

200
400

```

  "content": {
    "items": [

        "amountToReceive": 0,
        "networkId": "00000000-0000-0000-0000-000000000000",
        "networkLogoUrl": "https://file-cdn.meshconnect.com/public/logos/networks/Polygon.svg",
        "from": {
          "logoUrl": "https://logo.com/logo.jpg",
          "id": "8e25acb5-a9e2-4d00-8772-a255f010a2a9",
          "type": "robinhood",
          "name": "Robinhood"
        },
        "totalFeesAmountInFiat": 0.5,
        "totalTransactionAmountInFiat": 1000.5,
        "fundingMethods": [

            "type": "cryptocurrencyConversion",
            "amount": 2,
            "amountInFiat": 20,
            "toSymbol": "WETH",
            "fromAmount": 1,
            "fromSymbol": "BTC",
            "fee": {
              "fee": 0.0001,
              "feeCurrency": "ETH",
              "feeInFiat": 0.1,
              "feeInTransferCurrency": 0

          },

            "type": "paymentMethodDepositUsage",
            "amount": 3,
            "amountInFiat": 30,
            "toSymbol": "WETH",
            "fromAmount": 1,
            "fromSymbol": "USD",
            "paymentMethodType": "bankAccount",
            "fee": {
              "fee": 0.0001,
              "feeCurrency": "USD",
              "feeInFiat": 0.1,
              "feeInTransferCurrency": 0

          },

            "type": "existingCryptocurrencyBalance",
            "amount": 5,
            "amountInFiat": 50,
            "toSymbol": "WETH",
            "fromAmount": 5,
            "fromSymbol": "ETH"

        ],
        "webhookLogs": [],
        "id": "8e25acb5-a9e2-4d00-8772-a255f010a2a9",
        "clientTransactionId": "123456",
        "institutionTransactionId": "456789",
        "status": "succeeded",
        "amountInFiat": 1000.3,
        "amountToReceiveInFiat": 0,
        "amountInFiatCurrencyCode": "USD",
        "amount": 10.123,
        "symbol": "WETH",
        "tokenAddress": "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
        "networkName": "Polygon",
        "createdTimestamp": 1653211113,
        "hash": "0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...",
        "gasFee": {
          "fee": 0.0001,
          "feeCurrency": "MATIC",
          "feeInFiat": 0.1,
          "feeInTransferCurrency": 0
        },
        "withdrawalFee": {
          "fee": 0.0001,
          "feeCurrency": "WETH",
          "feeInFiat": 0.1,
          "feeInTransferCurrency": 0
        },
        "processingFee": {
          "fee": 0.0001,
          "feeCurrency": "WETH",
          "feeInFiat": 0.1,
          "feeInTransferCurrency": 0
        },
        "executedTimestamp": 1707462614,
        "transferType": "payment",
        "isFeeIncluded": false,
        "infoUrl": "https://polygonscan.com/tx/0x5b0ac59e43b63f2985d78994b6270d747f1019777201ca18ebb36ad1e1a8693e",
        "isSmartFundingTransfer": false,
        "unitPrice": 0,
        "requestedTransferAmount": 0,
        "isBridgingTransfer": false,
        "userId": "123456798",
        "sourceAmount": 10.122,
        "destinationAmount": 10
      },

        "amountToReceive": 0,
        "networkId": "00000000-0000-0000-0000-000000000000",
        "from": {
          "logoUrl": "https://logo.com/logo.jpg",
          "id": "8e25acb5-a9e2-4d00-8772-a255f010a2a9",
          "type": "deFiWallet",
          "name": "MetaMask"
        },
        "totalFeesAmountInFiat": 0,
        "totalTransactionAmountInFiat": 10.3,
        "fundingMethods": [],
        "webhookLogs": [],
        "id": "12345678-a9e2-4d00-8772-a255f010a2a9",
        "clientTransactionId": "123456",
        "institutionTransactionId": "456789",
        "status": "failed",
        "amountInFiat": 10.3,
        "amountToReceiveInFiat": 0,
        "amountInFiatCurrencyCode": "USD",
        "amount": 0.123,
        "symbol": "WETH",
        "tokenAddress": "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
        "networkName": "Polygon",
        "createdTimestamp": 1653211113,
        "hash": "0x77f3a280aa5cfe956a5759c24cf774325504070b32b4159...",
        "isFeeIncluded": false,
        "isSmartFundingTransfer": false,
        "unitPrice": 0,
        "requestedTransferAmount": 0,
        "isBridgingTransfer": false,
        "userId": "123456798"

    ],
    "total": 10,
    "range": {
      "start": 0,
      "end": -1,
      "isValid": false,
      "count": 0
    },
    "hasMorePages": true
  },
  "status": "ok",
  "message": "",
  "errorHash": "bf6d53f3",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
