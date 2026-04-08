<!-- Source: https://docs.meshconnect.com/advanced/link-ui-events -->

[Skip to main content](https://docs.meshconnect.com/advanced/link-ui-events#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Mesh Link SDK Events
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
Mesh Link UI offers an event tracking system, allowing you to gain insights into user interactions within the Link UI. These events can be used for analytics and understanding user behavior. The event data can be obtained directly from the SDKs and includes various user actions, such as initiating a connection, completing authentication, completing an asset transfer, or encountering errors. The way in which these events are captured and transmitted varies slightly across different platforms (Web, iOS, Android, and React Native). For detailed instructions, see the page for your specific platform.
#  SDK Callback Functions  
| **SDK callback function**  | **Description of callback function**  | **Payload details**  |  
| --- | --- | --- |  
| **`onIntegrationConnected()`** |  A callback function that allows you (Mesh client) to run specific business logic when the user has successfully completed connecting an account.  | • **`accessToken`**: the access and refresh tokens to the connected account with some basic metadata about the account and tokens.•**`brokerBrandInfo`**: links to icons and logos for the connected integration  |  
| **`onTransferFinished()`** |  A callback function that allows you (Mesh client) to run specific business logic when the user has successfully completed a transfer.  | • **`status`**: pending / succeeded / failed•**`txId`**: A unique client identifier•**`transferId`**: A unique Mesh identifier•**`txHash?`**: A unique blockchain identifier•**`fromAddress`**: Address transfer is sent from•**`toAddress`**: Address transfer is sent to•**`symbol`**: Symbol of asset being transferred•**`amount`**: Amount being transferred•**`amountInFiat`**: Fiat equivalent of transfer amount•**`totalAmountInFiat`**: Total amount transferred, including transfer-related fees•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`refundAddress`**: The address that the user can receive back to  |  
| **`onExit()`** |  A callback function that allows you (Mesh client) to run specific business logic when the user has exited Link at some point.  | • **`errorMessage`**: Descriptive error message, if applicable•**`summary`**: // optional•**`page`**: the page the user was on when they exited•**`selectedIntegration`**: Name and Id of integration•**`transfer`**: previewId and other details about the transfer preview  |  
| **`onEvent()`** |  A general callback function that allows you (Mesh client) to run specific business logic in more granular scenarios, like when the user exits Link from specific parts in the user journey.The events that can be used in this callback function are listed below.  | Different payload structure for different events  |  
#  SDK Events  
| **SDK Event Type**  | **Description of Occurrence**  | **Payload Details**  |  
| --- | --- | --- |  
| **`pageLoaded`** |  Triggered when the first page is fully loaded. The first page the user sees may differ based on use case.  | No additional payload.  |  
| **`methodSelected`** |  Triggered on HomePage when the user selects a particular method for their flow.  | • **`method`**: The selected method type (‘embedded’ / ‘manual’ / ‘buy’)  |  
| **`close`** |  Triggered when the user exits the Mesh Link modal.  | • **`page`**: the page the user was on when they exited.• Note: In the context of a transfer flow,`page: 'transferExecutedPage'` would indicate the full flow was successful because the user exited from the Success page. And if the page is anything else, then the flow was not successfully completed.  |  
| **`integrationSelected`** |  Triggered when a user selects an integration from the catalog list.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`userSearched?`**: true/false if the user searched selected this integration from search results or not.  |  
| **`legalTermsViewed`** |  Triggered if a user views the terms of use page in Link.  | No additional payload.  |  
| **`credentialsEntered`** |  Triggered when a user submits exchange login credentials.  | No additional payload.  |  
| **`integrationMfaRequired`** |  Triggered when the user is prompted to enter MFA in an exchange authentication flow.  | No additional payload.  |  
| **`integrationMfaEntered`** |  Triggered when the user enters their MFA code in an exchange authentication flow.  | No additional payload.  |  
| **`integrationOAuthStarted`** |  Triggered when an exchange’s OAuth window is launched in authentication flow.  | No additional payload.  |  
| **`integrationAccountSelectionRequired`** |  Triggered if user is prompted to select a specific account within linked exchange.  | No additional payload.  |  
| **`integrationConnected`** |  Triggered when a user successfully connects to an integration.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.• **`accessToken` **payload: The access token to the user account and relevant metadata about the integration  |  
| **`integrationConnectionError`** |  Triggered when there is an error in connecting to an integration.  | • **`errorMessage`**: Descriptive error message.  |  
| **`transferStarted`** |  Triggered when the user begins the transfer flow. This means they have successfully connected an account and have moved on to either configuring or previewing their transfer. It does NOT mean they have initiated a transfer of assets.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.  |  
| **`transferAssetSelected`** |  Triggered when the user selects an asset to transfer. This does not relate to assets used for funding operations. This is about the asset being transferred.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`symbol`**: Currency symbol  |  
| **`transferNetworkSelected`** |  Triggered when the user selects a network to transfer on.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`symbol`**: Currency symbol•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name  |  
| **`transferAmountEntered`** |  Triggered when the user enters an amount to transfer.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`symbol`**: Currency symbol•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`amount`**: Amount the user enters for transfer  |  
| **`transferNoEligibleAssets`** |  Triggered when there are no assets in the user’s account eligible for the transfer, or Mesh cannot use the assets in the account to fund the transfer.  | • **`arrayOfTokensHeld`**: A list of tokens held in the user’s account •**`symbol`**: Currency symbol •**`amount`**: Amount of holding •**`amountInFiat`**: Amount of holding in fiat •**`ineligibilityReason`**: Why the token is ineligible.•**`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`noAssetsType`**:  |  
| **`transferConfigureError`** |  This may happen if the session linkToken expires during the configuration flow of a transfer. Very rare.  | • **`errorMessage`**: Descriptive error message.•**`requestId`**:  |  
| **`transferPreviewed`** |  Triggered when a user previews the details of a pending transfer.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`symbol`**: Currency symbol•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`amount`**: Crypto amount of the transfer•**`amountInFiat`**(optional): Amount in fiat currency•**`fiatCurrency`**: fiat currency symbol for the**`amountInFiat`**value.•**`toAddress`**: Destination address•**`fees`**: •`institutionTransferFee` • `estimatedNetworkGasFee` • `customClientFee`• **`fiatPurchaseStrategy`**: an enumeration of a fiat funding option used to fund this transaction plus any applicable`tradingFee`.• **`cryptocurrencyFundingOptionType`**: an enumeration of any funding options used to fund this transactionplus any applicable`cryptocurrencyConversionFee` or `depositFee`.• **`previewId`**: Unique ID for the preview  |  
| **`transferPreviewError`** |  Triggered when there is an error in building a transfer preview.  | • **`errorMessage`**: Descriptive error message.  |  
| **`linkTransferQRGenerated`** |  Triggered when the user lands on the Manual QR screen.  | • **`token`**(optional): Token symbol for the transfer•**`network`**(optional): Network being used•**`toAddress`**(optional): Destination address•**`qrUrl`**(optional): Generated QR code URL  |  
| **`fundingOptionsViewed`** |  Triggered when the user views the funding options page.  | No additional payload.  |  
| **`fundingOptionsUpdated`** |  Triggered when the user makes updates to the selected funding options and clicks save (ie. saves a new funding strategy).  | No additional payload. When a user saves a new funding strategy, it would build a new Preview, which would fire a new **`transferPreviewed`**event with new funding options enumerated.  |  
| **`transferInitiated`** |  Triggered when the user clicks to Proceed from the Preview screen. This will send a request to transfer to the exchange or wallet, which the user then needs to approve (via 2FA for exchange, or signing for wallet).  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`symbol`**: Currency symbol•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`amount`**: Crypto amount of the transfer•**`amountInFiat`**(optional): Amount in fiat currency•**`fiatCurrency`**: fiat currency symbol for the**`amountInFiat`**value.•**`toAddress`**: Destination address•**`fees`**: •`institutionTransferFee` • `estimatedNetworkGasFee` • `customClientFee`• **`fiatPurchaseStrategy`**: an enumeration of a fiat funding option used to fund this transaction plus any applicable`tradingFee`.• **`cryptocurrencyFundingOptionType`**: an enumeration of any funding options used to fund this transactionplus any applicable`cryptocurrencyConversionFee` or `depositFee`.  |  
| **`executeFundingStep`** |  Triggered when there is a success or error on a funding operation before a transfer.  | • **`fundingOptionType`**: The operation that has completed or failed.•**`status`**: Outcome of the funding operation.•**`errorMessage`**: Descriptive error message.  |  
| **`gasIncreaseWarning`** |  Triggered after funding operations and before initiation of transfer if the cost of gas has gone higher than the buffered estimate shown to the user on the Preview page.  | No additional payload.  |  
| **`transferMfaRequired`** |  Triggered when the user is prompted to enter an MFA code to perform an exchange transfer.  | No additional payload.  |  
| **`transferMfaEntered`** |  Triggered when the user submits their MFA code to perform an exchange transfer.  | No additional payload.  |  
| **`transferKycRequired`** |  Triggered when the user has not completed KYC in the linked account, is prompted to do so before being able to transfer assets.  | No additional payload.  |  
| **`transferExecuted`** |  Do not use. Obsolete.  | Do not use. Obsolete.  |  
| **`transferCompleted`** |  Triggered when the user views the Success page at the conclusion of the transfer flow.It is recommended to use the **`onTransferFinished()`**callback function to properly handle the user experience returning to your app after a successful transfer.  |  **`transferFinished`**payload:•**`status`**: pending / succeeded / failed•**`txId`**: A unique client identifier•**`transferId`**: A unique Mesh identifier•**`txHash?`**: A unique blockchain identifier•**`fromAddress`**: Address transfer is sent from•**`toAddress`**: Address transfer is sent to•**`symbol`**: Symbol of asset being transferred•**`amount`**: Amount being transferred•**`amountInFiat`**: Fiat equivalent of transfer amount•**`totalAmountInFiat`**: Total amount transferred, including transfer-related fees•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`refundAddress`**: The address that the user can receive back to  |  
| **`transferExecutionError`** |  Triggered when there is an error in executing a transfer.  | • **`errorMessage`**: Descriptive error message.  |  
| **`seeWhatHappenedClicked`** |  Triggered when the user clicks the See what happened link on the Transfer Success screen  | No additional payload.  |  
| **`connectionUnavailable`** |  Triggered when a timeout occurs when attempting to open a wallet on mobile, most likely because the DeFi wallet app is not installed on the device.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`reason`**: string  |  
| **`connectionDeclined`** |  Triggered when the user rejects a connection request in their wallet, or some error causes an auto-rejection.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`reason`**: string.•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`toAddress`**: Address transfer is sent to.•**`errorMessage`**: Descriptive error message.  |  
| **`transferDeclined`** |  Triggered when the user rejects the transfer request in their wallet, or some error causes an auto-rejection.  | • **`integrationType`**: For exchanges, this is the same as the name. For wallets, this is ‘deFiWallet’.•**`integrationName`**: Name of the selected integration.•**`reason`**: string•**`networkId`**: Selected network identifier•**`networkName`**: Selected network name•**`toAddress`**: Address transfer is sent to•**`symbol`**: Symbol of asset being transferred•**`amount`**: Amount being transferred•**`status`**: pending / succeeded / failed  |  
| **`walletMessageSigned`** |  Triggered when a user signs a message in their wallet to verify ownership.  | • **`address`**: wallet address that signed the message•**`isVerified`**: true / false indicator of whether the user has signed the exact message sent for signature from this address•**`message`**: Message that was signed•**`signedMessageHash`**: The hash of the message signed by the wallet•**`timeStamp`**: Time stamp of when the signature happened  |  
| **`verifyDonePage`** |  Triggered when the user views the Success page after successfully completing the wallet verification flow.  | No additional payload.  |  
| **`verifyWalletRejected`** |  Triggered when the user rejects the message signature request in their wallet, or some error causes an auto-rejection.  | No additional payload.  |  
| **`done`** |  Triggered when the user exits Link after successfully completing a read-only account connection flow (ie. for Mesh Verify) or after successfully completing the wallet verification flow (ie. for Mesh Verify).  | • **`page`**: the page the user was on when they exited.• Note: In wallet verification (ie. Mesh Verify) flow,`page: verifyDonePage` would indicate successful completion of the flow. And in a read-only (ie Mesh Portfolio) flow, `page: integrationConnectedPage` would indicate successful completion of the flow.  |  
| **`registerTransferError`** |  Shown when we are unable to receive the transfer hash from a self-custody wallet at the conclusion of a transfer flow.  | • **`errorMessage`**: Descriptive error message.  |  
Was this page helpful?
YesNo
[ Managing Sub-Clients Previous ](https://docs.meshconnect.com/advanced/sub-client-branding)[ Foreign Currency Support Next ](https://docs.meshconnect.com/advanced/foreign-currency-support)
Ctrl+I
On this page
  * [SDK Callback Functions](https://docs.meshconnect.com/advanced/link-ui-events#sdk-callback-functions)


Assistant
Responses are generated using AI and may contain mistakes.
