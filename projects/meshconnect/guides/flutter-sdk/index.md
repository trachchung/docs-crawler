<!-- Source: https://docs.meshconnect.com/guides/flutter-sdk -->

[Skip to main content](https://docs.meshconnect.com/guides/flutter-sdk#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Flutter SDK
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


##  Requirements
  * Dart >= 3.9.2
  * Flutter >= 3.35.7


##  Installation
Add the following dependency to your `pubspec.yaml` file:

```
dependencies:
  mesh_sdk_flutter: <latest_version>

```

You can find the latest version on [pub.dev](https://pub.dev/packages/mesh_sdk_flutter).
###  Localization
Mesh SDK uses the `flutter_localizations` package for localization. For it to work, you need to add `MeshLocalizations.localizationsDelegates` to your `MaterialApp.localizationsDelegates`:

```
import 'package:mesh_sdk_flutter/mesh_sdk_flutter.dart';

@override
Widget build(BuildContext context) {
  return MaterialApp(
    localizationsDelegates: [
      ...
      MeshLocalizations.localizationsDelegates,
    ],
  );


```

##  Get Link Token
Link token should be obtained from the POST `/api/v1/linktoken` endpoint. API reference for this request is available [here](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters). The request must be performed from the server side because it requires the client’s secret. You will get the response in the following format:

```

  "content": {
    "linkToken": "{linkToken}"
  },
  "status": "ok",
  "message": ""


```

##  Launch Link

```
Future<void> _showMeshLinkPage(String linkToken) async {
  final result = await MeshSdk.show(
    context,
    configuration: MeshConfiguration(
      language: 'en',
      linkToken: linkToken,
      onEvent: (event) {
        print('Mesh event: $event');
      },
      onExit: (errorType) {
        print('Mesh exit: $errorType');
      },
      onIntegrationConnected: (integration) {
        print('Integration connected: $integration');
      },
      onTransferFinished: (transfer) {
        print('Transfer finished: $transfer');
      },
    ),
  );

  switch (result) {
    case MeshSuccess():
      print('Mesh link finished successfully');
    case MeshError():
      print('Mesh link error: ${result.type}');



```

See full example app [here](https://github.com/FrontFin/mesh-flutter-sdk/tree/main/example).
##  Configuration
Here’s what you can configure in the `MeshConfiguration`:  
| Parameter  | Type  | Required  | Description  |  
| --- | --- | --- | --- |  
| `linkToken`  | `String`  | Yes  | Link token obtained from the backend.  |  
| `language`  | `String`  | No  | Language, defaults to “en”.  |  
| `isDomainWhitelistEnabled`  | `bool`  | No  | If domain should be checked against our whitelist. Defaults to `true`.  |  
| `integrationAccessTokens`  | `List<IntegrationAccessToken>`  | No  | List of cached `IntegrationAccessToken`s that you can pass, so users don’t need to connect every time.  |  
| `onError`  | `ValueChanged<MeshErrorType>?`  | No  | Error callback with a `MeshErrorType` that describes the error.  |  
| `onSuccess`  | `ValueChanged<MeshSuccess>?`  | No  | Success callback with `SuccessPayload` that contains more info about the transfer or integration.  |  
| `onEvent`  | `ValueChanged<MeshEvent>?`  | No  | Callback for when an event is triggered.  |  
| `onIntegrationConnected`  | `ValueChanged<IntegrationConnectedEvent>?`  | No  | Callback for when an integration is connected. Use this to store the access token.  |  
| `onTransferFinished`  | `ValueChanged<TransferFinishedEvent>?`  | No  | Callback for when a crypto transfer is executed.  |  
###  Callbacks
####  `onIntegrationConnected`
Called when a user successfully connects an integration. The callback receives an `IntegrationConnectedEvent` containing the access token that you should securely store for future use.
####  `onTransferFinished`
Called when a crypto transfer has been executed. The callback receives a `TransferFinishedEvent` containing details about the transfer status and transaction information.
####  `onEvent`
Called to provide details on the user’s progress while interacting with the Link UI. This can be used for analytics and understanding user behavior.
####  `onExit`
Called when a user exits the Link flow. The callback may receive an error type if the exit was due to an error.
###  Using Access Tokens
If the end user has an already connected integration, you can pass the `integrationAccessTokens` to skip re-authentication:

```
final result = await MeshSdk.show(
  context,
  configuration: MeshConfiguration(
    linkToken: linkToken,
    integrationAccessTokens: const [
      IntegrationAccessToken(
        accessToken: 'token',
        accountId: 'id',
        accountName: 'name',
        brokerName: 'broker',
        brokerType: 'type',
      ),
    ],
    onTransferFinished: (transfer) {
      print('Transfer finished: $transfer');
    },
  ),
);

```

###  Whitelist
By default, domain whitelisting is enabled. To disable the whitelist check, set `isDomainWhitelistEnabled: false` in the `MeshConfiguration`.
Was this page helpful?
YesNo
Ctrl+I
On this page
  * [Get Link Token](https://docs.meshconnect.com/guides/flutter-sdk#get-link-token)
  * [onIntegrationConnected](https://docs.meshconnect.com/guides/flutter-sdk#onintegrationconnected)
  * [onTransferFinished](https://docs.meshconnect.com/guides/flutter-sdk#ontransferfinished)
  * [Using Access Tokens](https://docs.meshconnect.com/guides/flutter-sdk#using-access-tokens)


Assistant
Responses are generated using AI and may contain mistakes.
