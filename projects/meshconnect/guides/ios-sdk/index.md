<!-- Source: https://docs.meshconnect.com/guides/ios-sdk -->

[Skip to main content](https://docs.meshconnect.com/guides/ios-sdk#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
iOS SDK
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
Add package [LinkSDK](https://github.com/FrontFin/mesh-ios-sdk) in your project’s Package Dependencies or download [LinkSDK.xcframework](https://github.com/FrontFin/mesh-ios-sdk/tree/main/LinkSDK.xcframework).
##  Get Link token
Link token should be obtained from the POST `/api/v1/linktoken endpoint`. API reference for this request is available [here](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters). The request must be performed from the server side because it requires the client’s secret. You will get the response in the following format: Set up `GetFrontLinkSDK` with the `linkToken`

```

  "content": {
    "linkToken": "{linkToken}"
  },
  "status": "ok",
  "message": ""


```

##  Launch Link
Create a `LinkConfiguration` instance with the `linkToken` and the callbacks:

```
let configuration = LinkConfiguration(
    linkToken: linkToken,
    settings: LinkSettings?,
    onIntegrationConnected: onIntegrationConnected,
    onTransferFinished: onTransferFinished,
    onEvent: onEvent,
    onExit: onExit)

```

The callback `onIntegrationConnected` is called with `LinkPayload` once an integration has been connected.

```
let onIntegrationConnected: (LinkPayload)->() = { linkPayload in
    switch linkPayload {
    case .accessToken(let accessTokenPayload):
        print(accessTokenPayload)
    case .delayedAuth(let delayedAuthPayload):
        print(delayedAuthPayload)



```

The callback `onTransferFinished` callback is called once a crypto transfer has been executed or failed. The parameter is either `success(TransferFinishedSuccessPayload)` or `error(TransferFinishedErrorPayload)`. The callback `onEvent` is called to provide more details on the user’s progress while interacting with the Link. This is a list of possible event types, some of them may have additional parameters:
  * `loaded`
  * `integrationConnectionError`
  * `integrationSelected`
  * `credentialsEntered`
  * `transferStarted`
  * `transferPreviewed`
  * `transferPreviewError`
  * `transferExecutionError`

The callback `onExit` is called once a user exits the Link flow. It might be used to dismiss the Link view controller in case the app manages its life cycle (see `LinkHandler.create()`) Callback closures are optional, but either `onIntegrationConnected` or `onTransferFinished` must be provided. Create a `LinkHandler` instance by calling `createHandler()` function, or handle an error. The following errors can be returned:
  * Invalid `linkToken`
  * Either `onIntegrationConnected` or `onTransferFinished` callback must be provided



```
let result = configuration.createHandler()
switch result {
case .failure(let error):
    print(error)
case .success(let handler):
    handler.present(in: self)


```

In case of success, you can call `LinkHandler.present` (in `viewController`) function to let `LinkSDK` modally present the Link view controller and dismiss it on exit, or get the reference to a view controller by calling `LinkHandler.create()` if you prefer your app to manage its life cycle.
###  Adding URL Schemes to Info.plist
To enable our SDK to interact with specific apps, please add the following URL schemes to your info plist file
  * Open your info.plist located in the ‘ios’ directory of your React Native project
  * Add the following XML snippet within the `<dict></dict>` tag.



```
<key>LSApplicationQueriesSchemes</key>
<array>
string>trust</string>
string>robinhood</string>
string>metamask</string>
string>rainbow</string>
string>uniswap</string>
string>exodus</string>
string>robinhood-wallet</string>
string>blockchain-wallet</string>
string>1inch</string>
string>cryptowallet<string>
string>okx</string>
string>bitkeep</string>
</array>

```

Was this page helpful?
YesNo
Ctrl+I
On this page
  * [Get Link token](https://docs.meshconnect.com/guides/ios-sdk#get-link-token)
  * [Adding URL Schemes to Info.plist](https://docs.meshconnect.com/guides/ios-sdk#adding-url-schemes-to-info-plist)


Assistant
Responses are generated using AI and may contain mistakes.
