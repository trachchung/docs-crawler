<!-- Source: https://docs.meshconnect.com/guides/react-native-sdk -->

[Skip to main content](https://docs.meshconnect.com/guides/react-native-sdk#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
React Native SDK
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
With `npm`: `npm install --save @meshconnect/react-native-link-sdk` With `yarn`: `yarn add @meshconnect/react-native-link-sdk` 💡 This package requires `react-native-webview` to be installed in your project. Although it is listed as direct dependency, some times it is not installed automatically (This is a known [npm issue](https://stackoverflow.com/questions/18401606/npm-doesnt-install-module-dependencies)). You should install it manually via following command in this case:

```
npm install --save react-native-webview

# or with yarn
yarn add react-native-webview

```

##  Get Link token
Link token should be obtained from the POST `/api/v1/linktoken` endpoint. API reference for this request is available here. The request must be performed from the server side because it requires the client’s secret. You will get the response in the following format:

```

  "content": {
    "linkToken": "{linkToken}"
  },
  "status": "ok",
  "message": ""


```

##  Launch Link

```
import React from 'react';
import {
  LinkConnect,
  LinkPayload,
  TransferFinishedPayload,
  TransferFinishedSuccessPayload,
  TransferFinishedErrorPayload
} from '@meshconnect/react-native-link-sdk';

export const App = () => {
  return (
LinkConnect
      linkToken={"YOUR_LINKTOKEN"}
      onIntegrationConnected={(payload: LinkPayload) => {
        // use broker account data

      onTransferFinished={(payload: TransferFinishedPayload) => {
        if (payload.status === 'success') {
          const successPayload = payload as TransferFinishedSuccessPayload
          // use transfer finished data
else {
          const errorPayload = payload as TransferFinishedErrorPayload
          // handle transfer error


      onExit={(err?: string) => {
        // use error message

      onEvent={(event: string, payload: LinkPayload) => {
        // use event

    />



export default App;

```

ℹ️ See full source code example at [examples/](https://github.com/FrontFin/mesh-react-native-sdk/tree/main/examples).
###  `LinkConnect` component arguments  
| Key  | Type  | Required/Optional  |  
| --- | --- | --- |  
| linkToken  | string  | required  |  
| onIntegrationConnected  | (payload: LinkPayload) => void  | optional  |  
| onTransferFinished  | (payload: TransferFinishedPayload) => void  | optional  |  
| onExit  | (err: string) => void)  | optional  |  
###  Typescript support
Typescript definitions for `@meshconnect/react-native-link-sdk` are built into the npm package.
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
  * [Get Link token](https://docs.meshconnect.com/guides/react-native-sdk#get-link-token)
  * [LinkConnect component arguments](https://docs.meshconnect.com/guides/react-native-sdk#linkconnect-component-arguments)
  * [Typescript support](https://docs.meshconnect.com/guides/react-native-sdk#typescript-support)
  * [Adding URL Schemes to Info.plist](https://docs.meshconnect.com/guides/react-native-sdk#adding-url-schemes-to-info-plist)


Assistant
Responses are generated using AI and may contain mistakes.
