<!-- Source: https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio -->

[Skip to main content](https://docs.meshconnect.com/api-reference/portfolio/get-aggregated-portfolio#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Portfolio
Get aggregated portfolio
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
holdings
/
portfolio
Try it
Get aggregated portfolio
cURL

```
curl --request GET \
  --url https://integration-api.meshconnect.com/api/v1/holdings/portfolio \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>'
```

200
CEX example

```

  "content": {
    "portfolioCostBasis": 1819.9,
    "actualPortfolioPerformance": 6.1,
    "equitiesValue": 1934.78,
    "cryptocurrenciesValue": 1185.12,
    "nftsValue": 0,
    "equityPositions": [

        "portfolioPercentage": 0.44,
        "totalReturn": -1.3,
        "returnPercentage": -8.67,
        "companyName": "Tesla",
        "totalDailyReturn": 0.45,
        "dailyReturnPercentage": 3.45,
        "marketValue": 13.69,
        "lastPrice": 214.44,
        "symbol": "TSLA",
        "amount": 0.063,
        "costBasis": 234.8
      },

        "portfolioPercentage": 38.98,
        "totalReturn": 144.97,
        "returnPercentage": 13.71,
        "companyName": "Apple",
        "totalDailyReturn": 31.65,
        "dailyReturnPercentage": 2.7,
        "marketValue": 1201.67,
        "lastPrice": 147.27,
        "symbol": "AAPL",
        "amount": 8.15,
        "costBasis": 129.5

    ],
    "cryptocurrencyPositions": [

        "portfolioPercentage": 11.4018,
        "totalReturn": -592.6533,
        "returnPercentage": -62.7737,
        "companyName": "Ethereum",
        "totalDailyReturn": -3.6081,
        "dailyReturnPercentage": -1.0162,
        "marketValue": 351.457,
        "lastPrice": 1350.07,
        "symbol": "ETH",
        "amount": 0.260325,
        "costBasis": 3626.66
      },

        "portfolioPercentage": 7.8,
        "totalReturn": -85.45,
        "returnPercentage": -26.2,
        "companyName": "Dogecoin",
        "totalDailyReturn": -2.45,
        "dailyReturnPercentage": -1.0103,
        "marketValue": 240.5754,
        "lastPrice": 0.05977,
        "symbol": "DOGE",
        "amount": 4025.02,
        "costBasis": 0.081

    ],
    "nftPositions": []
  },
  "status": "ok",
  "message": "",
  "errorHash": "29c0cd7f",
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
UserId
string
required
End user ID to get the aggregated portfolio for.
TimezoneOffset
integer<int64>
Offset in second, used to calculate daily return for cryptocurrencies.
#### Response
200
application/json
Portfolio obtained
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
[ Get holdings values. Previous ](https://docs.meshconnect.com/api-reference/portfolio/get-holdings-values)[ Get account balance Next ](https://docs.meshconnect.com/api-reference/balance/get-account-balance)
Ctrl+I
Get aggregated portfolio
cURL

```
curl --request GET \
  --url https://integration-api.meshconnect.com/api/v1/holdings/portfolio \
  --header 'X-Client-Id: <api-key>' \
  --header 'X-Client-Secret: <api-key>'
```

200
CEX example

```

  "content": {
    "portfolioCostBasis": 1819.9,
    "actualPortfolioPerformance": 6.1,
    "equitiesValue": 1934.78,
    "cryptocurrenciesValue": 1185.12,
    "nftsValue": 0,
    "equityPositions": [

        "portfolioPercentage": 0.44,
        "totalReturn": -1.3,
        "returnPercentage": -8.67,
        "companyName": "Tesla",
        "totalDailyReturn": 0.45,
        "dailyReturnPercentage": 3.45,
        "marketValue": 13.69,
        "lastPrice": 214.44,
        "symbol": "TSLA",
        "amount": 0.063,
        "costBasis": 234.8
      },

        "portfolioPercentage": 38.98,
        "totalReturn": 144.97,
        "returnPercentage": 13.71,
        "companyName": "Apple",
        "totalDailyReturn": 31.65,
        "dailyReturnPercentage": 2.7,
        "marketValue": 1201.67,
        "lastPrice": 147.27,
        "symbol": "AAPL",
        "amount": 8.15,
        "costBasis": 129.5

    ],
    "cryptocurrencyPositions": [

        "portfolioPercentage": 11.4018,
        "totalReturn": -592.6533,
        "returnPercentage": -62.7737,
        "companyName": "Ethereum",
        "totalDailyReturn": -3.6081,
        "dailyReturnPercentage": -1.0162,
        "marketValue": 351.457,
        "lastPrice": 1350.07,
        "symbol": "ETH",
        "amount": 0.260325,
        "costBasis": 3626.66
      },

        "portfolioPercentage": 7.8,
        "totalReturn": -85.45,
        "returnPercentage": -26.2,
        "companyName": "Dogecoin",
        "totalDailyReturn": -2.45,
        "dailyReturnPercentage": -1.0103,
        "marketValue": 240.5754,
        "lastPrice": 0.05977,
        "symbol": "DOGE",
        "amount": 4025.02,
        "costBasis": 0.081

    ],
    "nftPositions": []
  },
  "status": "ok",
  "message": "",
  "errorHash": "29c0cd7f",
  "teamCode": "P4",
  "errorType": ""

```

Assistant
Responses are generated using AI and may contain mistakes.
