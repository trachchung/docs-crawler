<!-- Source: https://docs.meshconnect.com/advanced/mesh-managed-tokens -->

[Skip to main content](https://docs.meshconnect.com/advanced/mesh-managed-tokens#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Mesh Managed Tokens (MMT)
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


#  Overview
Mesh’s Managed Tokens system (MMT) is a service designed to simplify how clients manage user authentication tokens. Rather than requiring clients to handle the lifecycle of access and refresh tokens for each integration, MMT securely stores and manages tokens on behalf of the client. Clients receive a persistent `tokenId` that can be used to create a clean return user experience for exchanges, and to interact with certain Mesh APIs without needing to refresh or re-authenticate.
##  Benefits
  * **Simplified Token Lifecycle** : Clients do not need to handle the storage or refresh logic for tokens directly.
  * **Streamlined UX** : End-users can skip repetitive authentication steps, enhancing the embedded experience.
  * **Persistent Access** (where supported): For exchange integrations that provide long-lived or refreshable tokens (e.g., Coinbase), the same `tokenId` remains valid indefinitely. For integrations with expiring tokens (e.g., Binance), users may still need to re-authenticate, but the `tokenId` remains unchanged, allowing clients to reuse it without needing to update backend storage.
  * **Seamless Re-authentication** : When a token expires (e.g., Binance), Mesh Link will prompt the user to re-authenticate. Once complete, the same `tokenId` is revalidated and continues to work as before—reducing backend complexity for clients.
  * **Integration-Agnostic** : Works across different auth methods (OAuth, credentials-based) with no added client-side complexity.


#  How to Implement MMT
##  1. Obtain a `tokenId`
When a user authenticates with their exchange or wallet account, you will receive the SDK event `integrationConnected`, which contains an object like this:

```

    "accessToken": {
        "accountTokens": [

                "account": {
                    "meshAccountId": "<meshAccountId>",
                    "frontAccountId": "<frontAccountId>",
                    "accountId": "<accountId>",
                    "accountName": "<accountName>",
                    "fund": 0,
                    "cash": 0

                "accessToken": "<accessToken>",
                "tokenId": "<tokenId>"

        ],
        "brokerType": "<brokerType>",
        "brokerName": "<brokerName>",
        "brokerBrandInfo": {}



```

Pull out the `tokenId` and `brokerType` values and construct the following object. Because Mesh will be managing the token refresh logic for you, you’ll be providing the `tokenId` value from the SDK event in the `accessToken` field in this object. This will be used when initializing future sessions of the Mesh SDK for this user. Note: The `brokerName`, `accountId`, and `accountName` fields are obsolete but must still be passed (can be empty) when initializing the SDK.

```
const accessTokens: IntegrationAccessToken[] = [

    accessToken: '<accessToken>',
    brokerType: '<brokerType>',
    brokerName: '',
    accountId: '',
    accountName: ''



```

_**Important: Be sure to maintain a strict mapping to the appropriate user.**_
##  2. Pass the `accessTokens` object to the Mesh SDK
You can pass this object (including one `tokenId`, or multiple if the user has authenticated into multiple different exchange accounts) into the Mesh Link SDK so that user can skip re-authentication and proceed directly into the transfer or portfolio flow. **SDK Setup Example:**

```
const connection = createLink({
  clientId: 'abc123', // Replace Mesh Client ID
  theme: 'system', // Possible values: 'system', 'dark', 'light'
  language: 'system', // Refer to the Enabling Multi-Language Support Document
  displayFiatCurrency: 'USD' // Refer to the Foreign Currency Support Document
  accessTokens: accessTokens, // This references the IntegrationAccessToken[] constant
  onIntegrationConnected: payload => {
    console.debug('[MESH LINK integration connected]', payload) // Payload contains integration tokens that can be used for a return user experience or calling certain Mesh APIs
  },
  onTransferFinished: payload => {
    console.debug('[MESH LINK transfer finished]', payload) // Payload contains pending transfer data
  },
  onExit: () => {
    console.debug('[MESH LINK exited]') // Payload contains error and session summary
  },
  onEvent: ev => {
    console.debug('[MESH LINK event]', ev) // Allows you to handle other specific events

})

connection.openLink(linkToken) // open in popup iframe

```

Link: [Enabling Multi-Language Support](https://docs.meshconnect.com/advanced/language) Link: [Foreign Currency Support](https://docs.meshconnect.com/advanced/foreign-currency-support) If the account `accessToken` associated with the `tokenId` is no longer valid, Link will prompt the user to re-authenticate and automatically update the `accessToken` associated with that `tokenId`, meaning no update is required on your end.
###  4. Token Lifecycle and Behavior  
| Scenario  | Result  |  
| --- | --- |  
| **Same user reconnects with same integration**  | Returns same `TokenId`  |  
| **Different user connects to same integration**  | Returns a new `TokenId`  |  
| **Same user connects with different scopes (e.g., read vs write)**  | Returns distinct `TokenId`s per scope  |  
| **`Write endpoint called using read-only TokenId`** |  API returns a scope mismatch error  |  
| **Token revoked by client (use[Remove connection](https://docs.meshconnect.com/api-reference/managed-account-authentication/remove-connection) endpoint)**  | Associated access is permanently disabled and Mesh also deletes the token physically, without any way to restore it  |  
##  Supported Integrations (as of today)
  * **Coinbase** (OAuth)
  * **Binance** (Username/Password)
  * **Uphold** (OAuth)
  * _Note: connections with self-custody wallets are maintained on subsequent sessions (unless the user actively kills the connection in their wallet app) without the need for handling tokens. This means the same smooth return user journey is achieved for wallet transactions._

For testing with sandbox accounts, see [our sandbox guide](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide).
##  Security Considerations
While MMT streamlines token handling and unlocks powerful functionality, it also requires thoughtful security practices given its expanded role in managing user access. Mesh has designed the system with robust safeguards to ensure token integrity and data protection, including:
  * **Encrypted Storage** : All tokens are encrypted at rest using modern encryption standards.
  * **Scoped Access** : Each `TokenId` is tied to the permission scope (read or write) associated with the API key. Unauthorized operations (e.g., calling a write endpoint with a read-scoped token) will be rejected.
  * **Client-Level Isolation** : Each `TokenId` is also scoped to a specific `clientId`. Even if the same end user connects the same integration account across multiple client apps, the tokens are isolated and not shared across clients.
  * **User-Level Isolation** : Each `TokenId` is unique to a specific `EndUserId` and integration.
  * **Token Revocation** : Clients can revoke a `TokenId`, permanently disabling access and triggering a secure deletion process. There is no path to restore a revoked token.


Was this page helpful?
YesNo
[ Configuring Transfer Options Previous ](https://docs.meshconnect.com/advanced/configuring-transfer-options)[ Intelligent Provider Filtering in Mesh Link Next ](https://docs.meshconnect.com/advanced/intelligent-provider-filtering)
Ctrl+I
On this page
  * [How to Implement MMT](https://docs.meshconnect.com/advanced/mesh-managed-tokens#how-to-implement-mmt)
  * [1. Obtain a tokenId](https://docs.meshconnect.com/advanced/mesh-managed-tokens#1-obtain-a-tokenid)
  * [2. Pass the accessTokens object to the Mesh SDK](https://docs.meshconnect.com/advanced/mesh-managed-tokens#2-pass-the-accesstokens-object-to-the-mesh-sdk)
  * [4. Token Lifecycle and Behavior](https://docs.meshconnect.com/advanced/mesh-managed-tokens#4-token-lifecycle-and-behavior)
  * [Supported Integrations (as of today)](https://docs.meshconnect.com/advanced/mesh-managed-tokens#supported-integrations-as-of-today)
  * [Security Considerations](https://docs.meshconnect.com/advanced/mesh-managed-tokens#security-considerations)


Assistant
Responses are generated using AI and may contain mistakes.
