<!-- Source: https://docs.meshconnect.com/manual -->

[Skip to main content](https://docs.meshconnect.com/manual#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Get Started
Manual
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


This guide provides a step-by-step walkthrough for integrating the Mesh SDK across all supported platforms. The core flow is the same everywhere: your secure backend creates a linkToken, which your client-side application then uses to open the Link UI.
##  Setting up your developer dashboard (team members, API keys, and Link customization)
  * Go to [Account > Team](https://dashboard.meshconnect.com/company/team) to add team members. New team members can be invited with varying permission sets to ensure you control access to only what’s needed on a per-member basis.


  * Go to [Account > API keys](https://dashboard.meshconnect.com/company/keys) to add callback URLs (where the Mesh SDK will be allowed to render) and to generate your production or sandbox API keys (you’ll have to complete a business verification check before being able to generate production keys).


  * Go to [Account > Link configuration](https://dashboard.meshconnect.com/company/link) to customize the Link SDK for your branding and other needs.


##  Create Link Token (Backend)
This first step is a mandatory server-side operation and is the same for all client platforms. The Link UI is always initialized with a linkToken, which must be generated from your backend to protect your apiSecret. **🔒 Security First** Never expose your `X-Client-Secret` in a client-side application. The `/api/v1/linktoken` endpoint must always be called from a secure server environment. Make a `POST` request from your backend to the appropriate Mesh API endpoint: Sandbox: [https://sandbox-integration-api.meshconnect.com](https://sandbox-integration-api.meshconnect.com/api/v1/linktoken) Production: <https://integration-api.meshconnect.com> **Example** `cURL` **request from your backend**

```
curl --request POST \
     --url https://integration-api.meshconnect.com/api/v1/linktoken \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'X-Client-Id: YOUR_CLIENT_ID' \
     --header 'X-Client-Secret: YOUR_CLIENT_SECRET' \
     --data '{
        "userId": "example_user123",
  		"restrictMultipleAccounts": true,
  		"transferOptions": {
    		"transactionId": "example_tx123",
    		"transferType": "payment", // payment or deposit

    	"isInclusiveFeeEnabled": false,
    	"toAddresses": [

        		"symbol": "USDT",
        		"address": "0x314838D6783865908456257c0b07Ea4Bc272cF98", 
        		"networkId": "18fa36b0-88a8-43ca-83db-9a874e0a2288",
        		"amount": 99.99 // pass an amount when enabling SmartFunding


      }'

```

The API will respond with a linkToken that you can then send to your client application.
##  Configuring the Link Token
The `linkToken` is a powerful tool that allows you to tailor the Link UI for your specific use case. By passing different parameters in the body of your `POST /api/v1/linktoken` request, you can control the entire user journey.
####  **Setting up a Transfer**
If you want the user to transfer assets, you must include the `transferOptions` object in your request body. This object contains all the necessary details for the transaction.
####  Finding the `networkId`
The `networkId` is a required field that tells Mesh which blockchain to use for the transfer. You can retrieve a complete list of all supported networks and their corresponding `networkId` values by making a `GET` request to our [transfers/managed/networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks) endpoint.
####  **Configuring Destination Addresses (**`toAddresses`**)**
This array tells Mesh where the user can send their funds.
  * **Single Address (Streamlined UX):** If your user has already selected a token and network in your app, or if you only accept one specific asset, you can pass a single object in the `toAddresses` array. This provides the most direct user experience, as Link will skip the asset and network selection screens.
  * **Multiple Addresses (Recommended for Flexibility):** For greater flexibility and potentially higher conversion, we recommend passing an array of all possible tokens and networks that you accept. This allows the user to choose their preferred asset within the Link UI.


####  **Enabling SmartFunding**
To maximize conversion and increase average transfer size, you should always enable SmartFunding.
  * **How to Enable:** Set `enabled: true` within the `fundingOptions` object inside `transferOptions`.
  * **Why it’s important:** SmartFunding allows users to complete a payment even if they don’t have enough of the target asset by auto-converting their other available tokens. This is a key feature for ensuring a successful transaction.



```
"transferOptions": {
  "toAddresses": [
    // ... your single or multiple addresses here
  ],
  "fundingOptions": {
    "enabled": true



```

####  **Controlling the User Flow**
You can control where the user lands when the Link UI opens.
  * **Go to Catalog:** By default, if you only provide a `userId`, the user will see the full catalog of supported exchanges and wallets.
  * **Go Straight to an Integration:** To bypass the catalog and send the user directly to a specific institution (e.g., Coinbase), include the `integrationId` in your `linkToken` request.


####  **Using Paylinks**
If you want to simplify your integration and avoid using the client-side SDKs, you can use Paylinks. This feature generates a unique, Mesh-hosted URL that you can redirect your customers to.
  * **How to Enable:** Set `"generatePayLink": true` inside your `transferOptions`.
  * **Learn More:** For a detailed guide on this feature, please see our [**Paylinks**](https://docs.meshconnect.com/advanced/paylinks) Documentation.


##  Open Link UI (Client-Side)
Once your client application receives the linkToken, you can use it to initialize and open the Link UI. **Installation**
  * Web
  * iOS
  * Android
  * React Native
  * Flutter



```
npm install --save @meshconnect/web-link-sdk

```

Add the LinkSDK package in your project’s Package Dependencies or download the LinkSDK.xcframework.
In your build.gradle file:

```
dependencies { implementation 'com.meshconnect:link:2.0.0' } 

```


```
npm install --save @meshconnect/react-native-link-sdk

# Also ensure react-native-webview is installed
npm install --save react-native-webview

```

Add to your `pubspec.yaml`:

```
dependencies:
  mesh_sdk_flutter: <latest_version>

```

Then add localization delegates to your `MaterialApp`:

```
import 'package:mesh_sdk_flutter/mesh_sdk_flutter.dart';

MaterialApp(
  localizationsDelegates: [
    ...MeshLocalizations.localizationsDelegates,
  ],
);

```

**Code Implementation**
  * Web
  * iOS
  * Android
  * React Native
  * Flutter



```
import { createLink } from "@meshconnect/web-link-sdk";

// Initialize the Link connection with your callbacks
const meshLink = createLink({
  clientId: "YOUR_CLIENT_ID",
  onIntegrationConnected: (payload) => { /* Handle success */ },
  onExit: (error) => { /* Handle exit */ },
  onTransferFinished: (payload) => { /* Handle transfer result */ }
});

// Use the linkToken from your server to open the UI
meshLink.openLink("YOUR_LINK_TOKEN");

```


```
// Create a configuration with the linkToken and callbacks
let configuration = LinkConfiguration(
linkToken: "YOUR_LINK_TOKEN",
onIntegrationConnected: { linkPayload in /* Handle success */ },
onTransferFinished: { transferPayload in /* Handle transfer result */ },
onExit: { /* Handle exit */ }


// Create a handler and present the UI
let result = configuration.createHandler()
switch result {
case .failure(let error):
    print(error)
case .success(let handler):
    handler.present(in: self)


```


```
// Register a launcher to handle the result from the Link flow
private val linkLauncher = registerForActivityResult(LinkContract()) { result ->
when (result) {
is LinkSuccess -> {
// Handle successful connection or transfer
handlePayloads(result.payloads)

is LinkExit -> {
// Handle user exit or error
// result.errorMessage will contain details




// Launch the Link UI with the linkToken from your server
linkLauncher.launch("YOUR_LINK_TOKEN")

```


```
import React from 'react';
import { LinkConnect } from '@meshconnect/react-native-link-sdk';

export const App = () => {
  return (
LinkConnect
      linkToken={"YOUR_LINK_TOKEN"}
      onIntegrationConnected={(payload) => { /* Handle success */ }}
      onTransferFinished={(payload) => { /* Handle transfer result */ }}
      onExit={(err) => { /* Handle exit */ }}
    />
  );
};

```


```
import 'package:mesh_sdk_flutter/mesh_sdk_flutter.dart';

Future<void> openMeshLink(String linkToken) async {
  final result = await MeshSdk.show(
    context,
    configuration: MeshConfiguration(
      linkToken: linkToken,
      onIntegrationConnected: (integration) { /* Handle success */ },
      onTransferFinished: (transfer) { /* Handle transfer result */ },
      onExit: (error) { /* Handle exit */ },
    ),
  );

  switch (result) {
    case MeshSuccess():
      // Handle success
    case MeshError():
      // Handle error: result.type



```

**iOS Implementation Note** If you are implementing any of our SDKs in an iOS environment please make sure you add the below to your Info.plist config file:

```
<key>LSApplicationQueriesSchemes</key>
<array>
<string>tronlinkoutside</string>
<string>tpoutside</string>
<string>bitcoin</string>
<string>zengo</string>
<string>okx</string>
<string>uniswap</string>
<string>rainbow</string>
<string>bitkeep</string>
<string>ledgerlive</string>
<string>dfw</string>
<string>exodus</string>
<string>cbwallet</string>
<string>bnc</string>
<string>phantom</string>
<string>trust</string>
<string>metamask</string>
</array>

```

###  Handle Events
Your application needs to respond to events to know the outcome of a user’s session. This happens in two places: on the client-side from the SDK, and on the server-side from webhooks. **From Link UI (Client-Side)** The client-side SDK provides immediate feedback about the user’s interaction. Please see the [Mesh Link SDK events](https://docs.meshconnect.com/advanced/link-ui-events) guide for full details on callback functions and events emitted from Mesh’s SDKs.
  * Web
  * iOS
  * Android
  * React Native
  * Flutter


The `createLink` function takes callbacks as arguments:
  * `onIntegrationConnected`: Called on a successful account connection. The payload contains the accessToken.
  * `onTransferFinished`: Called when a transfer is complete (either success or failure).
  * `onExit`: Called when the user closes the UI.


The `LinkConfiguration` object takes callbacks:
  * `onIntegrationConnected`: Called on successful connection.
  * `onTransferFinished`: Called when a transfer is complete.
  * `onExit`: Called when the user closes the UI.


The `registerForActivityResult` callback provides a result object:
  * `LinkSuccess`: Contains a list of payloads, including AccessTokenPayload for connections and TransferFinishedSuccessPayload for successful transfers.
  * `LinkExit`: Indicates the user closed the UI. The errorMessage property will contain details if an error occurred.


The `<LinkConnect>` component accepts props for callbacks:
  * `onIntegrationConnected`: Called on successful connection.
  * `onTransferFinished`: Called when a transfer is complete.
  * `onExit`: Called when the user closes the UI.


The `MeshConfiguration` object accepts callbacks:
  * `onIntegrationConnected`: Called on successful connection.
  * `onTransferFinished`: Called when a transfer is complete.
  * `onExit`: Called when the user closes the UI.
  * `onEvent`: Called for various UI events.

The `MeshSdk.show()` method returns a `MeshResult` that can be `MeshSuccess` or `MeshError`.
**From Webhooks (Server-Side)** Webhooks are the definitive source of truth for the status of a transfer. While the client-side onTransferFinished event provides immediate feedback, a webhook from Mesh ensures your backend is notified of the final state (succeeded or failed), even if the user closes the app. **Retrieving Historical Data** To retrieve a history of past transfers and their final statuses, you can also use the `GET /v1/transfers/managed/mesh` endpoint. This is useful for reconciliation or auditing purposes after a transfer has already completed. You can find the API reference for this endpoint [**here**](https://docs.meshconnect.com/api-reference/managed-transfers/get-transfers-initiated-by-mesh). **➡️ Learn More** For detailed information on webhook security, payload structure, and how to respond to events, see the [webhooks](https://docs.meshconnect.com/testing/webhooks) guide. To get more information about our SDKs, refer to the respective Github repository:  
| [React Native](https://github.com/FrontFin/mesh-react-native-sdk)  |  
| --- |  
##  Productionize
When you are ready to move from testing to production, follow these steps: **Switch API Keys** : In your Mesh Dashboard, generate Production API keys and use them in your backend environment variables. **Update API Endpoint** : Change the base URL in your backend from the sandbox endpoint to the production endpoint (<https://integration-api.meshconnect.com>). **Configure Production Webhooks** : In the Mesh Dashboard, add your production webhook URL to receive real-time transfer status updates. **Add Allowed Callback URLs** : Ensure your production domain (e.g., <https://yourapp.com>) is added to the “Allowed callback URLs” list in your dashboard settings to allow the Link SDK to load correctly.
Was this page helpful?
YesNo
[ Overview Previous ](https://docs.meshconnect.com/overview)[Next](https://docs.meshconnect.com/supported-tokens)
Ctrl+I
On this page
  * [Setting up your developer dashboard (team members, API keys, and Link customization)](https://docs.meshconnect.com/manual#setting-up-your-developer-dashboard-team-members-api-keys-and-link-customization)
  * [Create Link Token (Backend)](https://docs.meshconnect.com/manual#create-link-token-backend)
  * [Configuring the Link Token](https://docs.meshconnect.com/manual#configuring-the-link-token)
  * [Setting up a Transfer](https://docs.meshconnect.com/manual#setting-up-a-transfer)
  * [Finding the networkId](https://docs.meshconnect.com/manual#finding-the-networkid)
  * [Configuring Destination Addresses (toAddresses)](https://docs.meshconnect.com/manual#configuring-destination-addresses-toaddresses)
  * [Enabling SmartFunding](https://docs.meshconnect.com/manual#enabling-smartfunding)
  * [Controlling the User Flow](https://docs.meshconnect.com/manual#controlling-the-user-flow)
  * [Using Paylinks](https://docs.meshconnect.com/manual#using-paylinks)
  * [Open Link UI (Client-Side)](https://docs.meshconnect.com/manual#open-link-ui-client-side)


Assistant
Responses are generated using AI and may contain mistakes.
