<!-- Source: https://docs.meshconnect.com/guides/web-sdk -->

[Skip to main content](https://docs.meshconnect.com/guides/web-sdk#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Web SDK
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


##  Installation
To get started with Web Link SDK, clone the [GitHub repository](https://github.com/FrontFin/mesh-web-sdk), and review the example application. Next, you will need to install the **[@meshconnect/web-link-sdk](https://www.npmjs.com/package/@meshconnect/web-link-sdk)** package.

```
npm install --save @meshconnect/web-link-sdk

```

With `yarn`:

```
yarn add @meshconnect/web-link-sdk

```

Then import the necessary components and types:
JSX

```
import {
  Link,
  LinkPayload,
  TransferFinishedPayload,
  createLink,
} from "@meshconnect/web-link-sdk";

```

##  Creating Link Connection
The `createLink` function accepts one argument, a configuration Object typed `LinkOptions` and returns an Object with two functions, `openLink` and `closeLink`. Calling `openLink` will display the Link UI in an iframe, and the overlay around it. Calling the `closeLink` will close the already displayed Link UI. Please note, that the Link UI will close itself once the user finishes their workflow in Link UI.
####  `createLink` arguments  
| Key  | Type  | Description  |  
| --- | --- | --- |  
| clientId  | string  | A Client ID, unique to your company, which can be obtained at <https://dashboard.meshconnect.com/company/keys>  |  
| onIntegrationConnected  | callback  | A callback function that is called when an integration is successfully connected.The function should expect an argument typed LinkPayload.  |  
| onExit (optional)  | callback  | A callback function, that is called, when the Link UI is closed.The function should expect two arguments:1. Nullable error string as an argument.2. Nullable summary object.  |  
| onTransferFinished (optional)  | callback  | A callback function that is called when an asset transfer is finished.The function should expect an argument typed TransferFinishedPayload.  |  
| onEvent (optional)  | callback  | A callback function that is called when various events occur within the Link UI.The function should expect an argument typed LinkEventType.See [Link UI Events](https://docs.meshconnect.com/guides/link-ui-events) for more details on event types.  |  
| accessTokens (optional)  | Array of IntegrationAccessToken  | These access tokens are used to initialize crypto transfers flow at ‘Select asset step’ using previously obtained integration auth_tokens .See [Link Initialization and Use Cases](https://docs.meshconnect.com/guides/link-initialization) for more details.  |  
| transferDestinationTokens (optional)  | Array of IntegrationAccessToken  | These access tokens are used to initialize crypto transfers flow at ‘Select asset step’ using previously obtained integration auth_tokens .See [Link Initialization and Use Cases](https://docs.meshconnect.com/guides/link-initialization) for more details.  |  
####  createLink code example
JSX

```

const meshLink =
		createLink({
				clientId: 'clientId',
        onIntegrationConnected: (payload) => {},
        onExit: (error) => {},
        onTransferFinished: (transferData) => {},
        onEvent: (ev) => {},
				accessTokens: [],
				transferDestinationTokens: []
		})


```

###  onIntegrationConnected
The `onIntegrationConnected` callback is called when an integration is successfully connected. It takes one argument called `payload` with the type of `LinkPayload`
####  `LinkPayload` properties  
| Key  | Type  | Description  |  
| --- | --- | --- |  
| accessToken (nullable)  | Object of type AccessTokenPayload  | The an accessToken payload is returned, when a user successfully connects an integration.It contains all the necessary data to interact with the users connected account via the Mesh API.Make sure, that you handle this data securely and you follow our recommended [best practices](https://docs.meshconnect.com/guides/handling-auth-tokens). See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/963dfe9820ec634c8d68f45e7df9b8c30d8402b7/packages/link/src/utils/types.ts#L48C24-L48C24).  |  
| delayedAuth (nullable)  | Object of type DelayedAuthPayload  | The a delayedAuth payload is returned, when a user successfully connects an Interactive Brokers account for the first time.It contains a refresh_token that can be exchanged into an auth_token in 24 hours, using the Mesh API. See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/963dfe9820ec634c8d68f45e7df9b8c30d8402b7/packages/link/src/utils/types.ts#L57).  |  
###  onExit
The `onExit` callback is called, when the Link UI is closed. This can be due to an error, or the user can close the Link UI by choosing so. It takes two arguments:
  1. `error` with the type of `string`, which is the reason, why the Link UI was closed in an user friendly message.
  2. `summary` object that contains session summary in following format


JSX

```

  /**
   *   Current page of application. Possible values:
   * `startPage`
   * `integrationsCatalogPage`
   * `integrationLoginPage`
   * `integrationMfaPage`
   * `integrationAccountSelectPage`
   * `integrationConnectedPage`
   * `errorPage`
   * `transferKycPage`
   * `transferHoldingSelectionPage`
   * `transferNetworkSelectionPage`
   * `transferAmountSelectionPage`
   * `transferPreviewPage`
   * `transferMfaPage`
   * `transferFundingPage`
   * `transferExecutedPage`
   * `termsAndConditionPage`

   * This list may change in future.
   */
  page: string
  /** Selected integration */
  selectedIntegration?: {
    id?: string
    name?: string

  /** Transfer information */
  transfer?: {
    previewId?: string
    symbol?: string
    amount?: number
    amountInFiat?: number
    transactionId?: string
    networkId?: string

  errorMessage?: string


```

###  onTransferFinished
The `onTransferFinished` callback is called, when an asset transfer is finished successfully or unsuccessfully. It takes one argument called `payload` with the type of `TransferFinishedSuccessPayload` or `TransferFinishedErrorPayload`.
####  `TransferFinishedSuccessPayload` properties
See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/main/packages/link/src/utils/types.ts).  
| Key  | Type  | Description  |  
| --- | --- | --- |  
| status  | string  | The status of the transfer in case of TransferFinishedSuccessPayload it will be always success  |  
| txId  | string  | The identifier of the executed transaction, received from the integration  |  
| fromAddress  | string  | Address where the crypto funds were sent from  |  
| toAddress  | string  | Address where the crypto funds were sent to  |  
| symbol  | string  | The symbol of the crypto asset  |  
| amount  | string  | The amount in the given cryptocurrency that was sent  |  
| networkId  | string  | Id of the network over which the transaction was executed.See more about network IDs in our [API reference](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks)  |  
####  `TransferFinishedErrorPayload` properties
See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/main/packages/link/src/utils/types.ts).  
| Key  | Type  | Description  |  
| --- | --- | --- |  
| status  | string  | The status of the transfer in case of TransferFinishedErrorPayload it will be always error  |  
| errorMessage  | string  | A user friendly message on why the transaction failed.  |  
###  onEvent
The `onEvent` callback is called, when various events occur within the Link UI. It takes one argument, called `event` with the type of `LinkEventType`. See [Link UI Events](https://docs.meshconnect.com/guides/link-ui-events) for more details on events and their type definitions.
###  accessTokens
The `accessTokens` parameter is used to initialize crypto transfers flow at the ‘Select asset step’ using previously obtained integration `auth_token`. It can be used if you have a valid `auth_token` and want to bypass authentication to jump right into a transfer. The type of the `accessTokens` parameter is an array of `IntegrationAccessToken`, however, please note, only the first item in the array will be taken into account. See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/main/packages/link/src/utils/types.ts).
####  `accessTokens` code example
JSX

```
const accessTokens =


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
				accessTokens: accessTokens, // Provide a previously obtained integration auth_token
				transferDestinationTokens: []
		})

```

###  transferDestinationTokens
The `transferDestinationTokens` are used for crypto transfers flow. It is an alternative way of providing target addresses for crypto transfers by using previously obtained integration `auth_tokens`. See [Link initialization and use cases](https://docs.meshconnect.com/guides/link-initialization) for more details. The type of the `transferDestinationTokens` parameter is an array of `IntegrationAccessToken`. See the type definition on our [GitHub](https://github.com/FrontFin/mesh-web-sdk/blob/main/packages/link/src/utils/types.ts).
####  `transferDestinationTokens` code example
JSX

```
const transferDestinationTokens = [

    accountId: "accountId",
    accountName: "accountName",
    accessToken: "accessToken",
    brokerType: "brokerType",
    brokerName: "brokerName",
  },
];

const meshLink = createLink({
  clientId: "clientId",
  onIntegrationConnected: (payload) => {},
  onExit: (error) => {},
  onTransferFinished: (transferData) => {},
  onEvent: (ev) => {},
  accessTokens: [],
  transferDestinationTokens: transferDestinationTokens, // Provide a previously obtained integration auth_tokens to use as destination address
});

```

###  openLink()
Calling `openLink` will display the Link UI in an iframe, and the overlay around it. It takes `linkToken` as an argument, which can be obtained from the POST `/api/v1/linktoken` endpoint. Request must be preformed from the server side because it requires the client secret and ID. See more about obtaining the `linkToken` and [initialization use cases](https://docs.meshconnect.com/guides/link-initialization)
####  `openLink` code example
JSX

```
const meshLink = createLink({
  clientId: "clientId",
  onIntegrationConnected: (payload) => {},
  onExit: (error) => {},
  onTransferFinished: (transferData) => {},
  onEvent: (ev) => {},
  accessTokens: [],
  transferDestinationTokens: [],
});

meshLink.openLink("linktoken"); // Open the Link UI popup

```

###  closeLink()
Calling the `closeLink` will close the already displayed Link UI. Please note, that the Link UI will close itself once the user finishes their workflow in Link UI.
###  Typescript support
TypeScript definitions for `@meshconnect/web-link-sdk` are built into the NPM package.
Was this page helpful?
YesNo
Ctrl+I
On this page
  * [Creating Link Connection](https://docs.meshconnect.com/guides/web-sdk#creating-link-connection)
  * [createLink arguments](https://docs.meshconnect.com/guides/web-sdk#createlink-arguments)
  * [createLink code example](https://docs.meshconnect.com/guides/web-sdk#createlink-code-example)
  * [onIntegrationConnected](https://docs.meshconnect.com/guides/web-sdk#onintegrationconnected)
  * [LinkPayload properties](https://docs.meshconnect.com/guides/web-sdk#linkpayload-properties)
  * [onTransferFinished](https://docs.meshconnect.com/guides/web-sdk#ontransferfinished)
  * [TransferFinishedSuccessPayload properties](https://docs.meshconnect.com/guides/web-sdk#transferfinishedsuccesspayload-properties)
  * [TransferFinishedErrorPayload properties](https://docs.meshconnect.com/guides/web-sdk#transferfinishederrorpayload-properties)
  * [accessTokens code example](https://docs.meshconnect.com/guides/web-sdk#accesstokens-code-example)
  * [transferDestinationTokens](https://docs.meshconnect.com/guides/web-sdk#transferdestinationtokens)
  * [transferDestinationTokens code example](https://docs.meshconnect.com/guides/web-sdk#transferdestinationtokens-code-example)
  * [openLink code example](https://docs.meshconnect.com/guides/web-sdk#openlink-code-example)
  * [Typescript support](https://docs.meshconnect.com/guides/web-sdk#typescript-support)


Assistant
Responses are generated using AI and may contain mistakes.
