<!-- Source: https://docs.meshconnect.com/guides/link-initialization -->

[Skip to main content](https://docs.meshconnect.com/guides/link-initialization#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Link Utilization and Use cases
##### Get Started


##### Advanced
  * [Best UX Practices & Examples](https://docs.meshconnect.com/advanced/best-ux-practices)
  * [Configuring Transfer Options](https://docs.meshconnect.com/advanced/configuring-transfer-options)
  * [Mesh Managed Tokens (MMT)](https://docs.meshconnect.com/advanced/mesh-managed-tokens)
  * [Intelligent Provider Filtering in Mesh Link](https://docs.meshconnect.com/advanced/intelligent-provider-filtering)
  * [Enabling Multi-Language Support for Link](https://docs.meshconnect.com/advanced/language)
  * [Verifying Self-Hosted Wallets](https://docs.meshconnect.com/advanced/verifying-self-hosted-wallets)
  * [Managing Sub-Clients](https://docs.meshconnect.com/advanced/sub-client-branding)
  * [Mesh Link SDK Events](https://docs.meshconnect.com/advanced/link-ui-events)
  * [Foreign Currency Support](https://docs.meshconnect.com/advanced/foreign-currency-support)


##### Testing
  * Sandbox
  * [Troubleshooting link](https://docs.meshconnect.com/testing/troubleshooting-link)
  * [Transfer Webhooks](https://docs.meshconnect.com/testing/webhooks)


##  Overview
Mesh Link SDK allow client applications to connect users to their accounts across brokerages, centralized exchanges, and self-custody wallets. Mesh Link UI handles credential validation, multi-factor authentication, and error handling when connecting to each account. After an end user authenticates with their account credentials, clients will be passed authentication tokens to provide access to the account which allows client applications to read account information such as holdings, transactions, and balances, and initiate trades and transfers on behalf of the end user.
##  Getting Your API Keys
You can generate two different API keys (one for Sandbox and another for Production) on the [Mesh Dashboard](https://dashboard.meshconnect.com/company/keys), you should **store the API keys immediately** after generating them as they will no longer be viewable after leaving the page.
> ❗️ These API keys should never be stored on your client-side application, always store them securely on your applications backend, following security best practices.
##  LinkToken Endpoint
This [endpoint](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters) provides a short-lived, one-time-use token for initializing a Link session, when passed to one of the client side SDKs. Depending on the payload of the API call, the Link UI will load into different workflows, such as user authentication, or asset transfer. The LinkToken endpoint should always be called from your backend, since it requires an API secret.
##  Link UI Use Cases
In the next section we will go trough the different ways Link UI can be initialized:
##  Account Authentication
###  Basic Account Authentication
The most basic way to initialize Link is to simply pass the `UserId` body param. The `UserId` is a unique ID representing the end user. This identifier is a map to reference which customers you are logging in through Mesh Link.

```

    "UserId": "EndUserId",


```

POST /api/v1/linktoken body
###  Direct to Exchange or Brokerage Integration
Many of our customers and UI/UX designers want to launch link directly to a specific integration (eg. Binance or Coinbase) and skip our Full Catalogue. This is easily achieved by including the `IntegrationId` param. The `IntegrationId` of the integration you wish to connect can be obtained by calling the **[Retrieve the list of all available integrations.](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations)** endpoint and referencing the `id` field.

```

    "UserId": "EndUserId",
		"IntegrationId": "9226e5c2-ebc3-4fdd-94f6-ed52cdce1420"


```

POST /api/v1/linktoken body
###  Direct to Self Custody Wallet
Many of our customers and UI/UX designers want to load up Link directly to a specific wallet (eg. Metamask) and skip our Full Catalogue. This is easily achieved by including the `IntegrationId` param. The `IntegrationId` of the integration you wish to connect can be obtained by calling the **[Retrieve the list of all available integrations.](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations)** endpoint and referencing the `id` field.

```

    "UserId": "EndUserId",
		"IntegrationId": "34aeb688-decb-485f-9d80-b66466783394"


```

POST /api/v1/linktoken body
###  Restricting User to Connect only One Account
By default, Link UI lets users authenticate with more than one provider in one session. This is great for portfolio management use cases or when a user wants to transfer from one provider to another within your application. To limit the authentication to one provider, set the RestrictMultipleAccounts param to true.

```

    "UserId": "EndUserId",
		"RestrictMultipleAccounts": true


```

POST /api/v1/linktoken body
##  Deposits
###  Sending Assets to a Single Crypto Address
You can include as many `toAddresses` object items, but the most streamlined way for users to transfer assets is to include a single token/network/address combo. Please remember that for each item in the ‘toAddresses’ array, you must provide the Mesh UID for the network to which you are sending the supported token. The comprehensive list of tokens, networks and integrations that can Mesh supports can be found here: [Tokens](https://docs.meshconnect.com/api-reference/managed-transfers/get-supported-tokens-list) | [Networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks) | [Integrations](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations)
> 👍 If only one destination address is provided, the Link UI skips the ‘Select asset’ and ‘Select network’ screens to streamline the user experience.

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": [

                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "ETH",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"





```

POST /api/v1/linktoken body - single network and token
###  Configuring for Multiple Crypto Tokens or Networks
You can include as many `toAddresses` object items as needed to enable your users to perform transfers. Each item, represents the symbol they can transfer and the network it could be sent over. Please remember that for each item in the ‘toAddresses’ array, you must provide the Mesh UID for the network to which you are sending the supported token. The comprehensive list of tokens, networks and integrations that can Mesh supports can be found here: [Tokens](https://docs.meshconnect.com/api-reference/managed-transfers/get-supported-tokens-list) | [Networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks) | [Integrations](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations)

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": [

                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "ETH",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "USDC",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "USDT",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
                "Symbol": "MATIC",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"





```

POST /api/v1/linktoken body - multiple networks/tokens
###  Sending Assets to a Previously Connected User Account
In the case if the end user has an already connected integration, and you want to move some funds between the users accounts, you can pass the `auth_token` when initializing the SDK.
####  `accessTokens` Code Example
`transferDestinationTokens` The `transferDestinationTokens` are used for crypto transfers flow. It is an alternative way of providing target addresses for crypto transfers by using previously obtained integration `auth_tokens`. The type of the `transferDestinationTokens` parameter is an array of `IntegrationAccessToken`. See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/main/packages/link/src/utils/types.ts).

```
const transferDestinationTokens = 


	          accountId: 'accountId',
	          accountName: 'accountName',
	          accessToken: 'accessToken',
	          brokerType: 'brokerType',
	          brokerName: 'brokerName',
	        },


const meshLink = 
		createLink({
				clientId: 'clientId',
        onIntegrationConnected: (payload) => {},
        onExit: (error) => {},
        onTransferFinished: (transferData) => {},
        onEvent: (ev) => {},
				accessTokens: [],  
				transferDestinationTokens: transferDestinationTokens // Provide a previously obtained integration auth_tokens to use as destination address
		})

```

In this case you need to provide an **empty** `toAddresses` array to the LinkToken endpoint, to indicate that you wish to use the transfers workflow.

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": []



```

POST /api/v1/linktoken body
##  Payments
###  Transferring for a Specific Amount
If you’d like to initialize Mesh Link with the transfer amount pre-populated with a supplied destination address, include the assets you want to let the user pay with, plus the destination addresses of those tokens. In the example below, the user can pay with Solana or USDC over Ethereum networks (notice how the network IDs are different). You can achieve this by providing the `AmountInFiat` parameter when calling the LinkToken endpoint By providing a unique `TransactionID`, you’ll be to map a payments to a specific identifier, similar to an order number.

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": [

                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "ETH",
                "Amount": 0.0032,
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "USDC",
                "Amount": 10,
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "USDT",
                "Amount": 10,
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
                "Symbol": "MATIC",
                "Amount": 22.8,
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"

        ],
				"TransactionId": "TransactionId"



```

POST /api/v1/linktoken body - multiple networks/tokens
> 👍 If `AmountInFiat` is included and only a single network/token/address combo is included, Link will skip directly to the preview page, making even more streamlined for a user to complete their transfer.

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": [

                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "ETH",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"

        ],
				"AmountInFiat": 10,
				"TransactionId": "TransactionId"



```

POST /api/v1/linktoken body - single network and token
####  Adding a Fee for a Payment
If you’d like to charge a client fee for processing a transfer, you can append the `ClientFee` field to the above JSON object examples. This fee should only be used for **Payments** (when the transfer destination is an address owned by your company), and not for Deposits (when the transfer destination is an address owned by the end-user). A percentage fee (input as a ratio, eg. 0.02500 = 2.500%) added onto your users’ gross transfer to your company. This will override any default fee entered in your Mesh dashboard for an individual transaction.

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": [

                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "ETH",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "USDC",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "USDT",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"


                "NetworkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
                "Symbol": "MATIC",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"

        ],
				"AmountInFiat": 10,
				"ClientFee": 0.025



```

POST /api/v1/linktoken body - multiple networks/tokens

```

    "UserId": "EndUserId",
		"TransferOptions": {
				"ToAddresses": [

                "NetworkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "Symbol": "ETH",
                "Address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"

        ],
				"AmountInFiat": 10,
				"TransactionId": "TransactionId"
				"ClientFee": 0.025



```

POST /api/v1/linktoken body - single network and token
Was this page helpful?
YesNo
Ctrl+I
On this page
  * [Getting Your API Keys](https://docs.meshconnect.com/guides/link-initialization#getting-your-api-keys)
  * [LinkToken Endpoint](https://docs.meshconnect.com/guides/link-initialization#linktoken-endpoint)
  * [Link UI Use Cases](https://docs.meshconnect.com/guides/link-initialization#link-ui-use-cases)
  * [Account Authentication](https://docs.meshconnect.com/guides/link-initialization#account-authentication)
  * [Basic Account Authentication](https://docs.meshconnect.com/guides/link-initialization#basic-account-authentication)
  * [Direct to Exchange or Brokerage Integration](https://docs.meshconnect.com/guides/link-initialization#direct-to-exchange-or-brokerage-integration)
  * [Direct to Self Custody Wallet](https://docs.meshconnect.com/guides/link-initialization#direct-to-self-custody-wallet)
  * [Restricting User to Connect only One Account](https://docs.meshconnect.com/guides/link-initialization#restricting-user-to-connect-only-one-account)
  * [Sending Assets to a Single Crypto Address](https://docs.meshconnect.com/guides/link-initialization#sending-assets-to-a-single-crypto-address)
  * [Configuring for Multiple Crypto Tokens or Networks](https://docs.meshconnect.com/guides/link-initialization#configuring-for-multiple-crypto-tokens-or-networks)
  * [Sending Assets to a Previously Connected User Account](https://docs.meshconnect.com/guides/link-initialization#sending-assets-to-a-previously-connected-user-account)
  * [accessTokens Code Example](https://docs.meshconnect.com/guides/link-initialization#accesstokens-code-example)
  * [Transferring for a Specific Amount](https://docs.meshconnect.com/guides/link-initialization#transferring-for-a-specific-amount)
  * [Adding a Fee for a Payment](https://docs.meshconnect.com/guides/link-initialization#adding-a-fee-for-a-payment)


Assistant
Responses are generated using AI and may contain mistakes.
