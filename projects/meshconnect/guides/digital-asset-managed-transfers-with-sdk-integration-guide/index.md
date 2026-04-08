<!-- Source: https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide -->

[Skip to main content](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Link Transfers Guide
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
One of the unique features with Mesh is enabling clients to build embedded experiences that enables retail users to transfer digital assets from either centralized exchanges or self-custody wallets to the client application without needing to copy and paste a target address on a separate platform. This document will guide you through integrating with our Link + Transfer SDKs and **drop-in UI** to transfer from **either centralized exchanges or self-custody wallets** for your users. Mesh APIs handle credential validation, multi-factor authentication, and error handling when connecting to each account. After an end user authenticates with their account credentials, clients will be passed authentication tokens to provide access to the account which allows client applications to initiate transfers on behalf of the user on the originating platform. Clients have the option of using Mesh’s pre-built transfer UI or building the experience natively using server-side calls. You can test the authentication and transfers functionality for yourself in our [interactive demos](https://dashboard.meshconnect.com/demos). Using Mesh APIs, you can easily connect and transfer digital from the following types of accounts:
  * Centralized exchanges
  * Self-custody wallets 
    * Transfers for self-custody wallets **must** use the Mesh SDKs

Using the Link + Transfer SDKs, you can leverage Mesh’s pre-built transfer UI to easily enable transfers on your platform. Alternatively, you can use Mesh [Transfer APIs](https://docs.meshconnect.com/api-reference/managed-transfers/configure-transfer) directly for transfers from centralized exchanges to build the experience natively on your platform.
##  Introduction
The fastest to get started with Mesh’s Transfers product is by testing the functionality via our [interactive demos](https://dashboard.meshconnect.com/demos). Then, you’ll need to generate [API keys](https://dashboard.meshconnect.com/company/keys), which are accessible after [signing up](https://dashboard.meshconnect.com/signup) for Mesh. You can generate two different API keys (one for Sandbox and another for Production), you should store the API keys immediately after generating them as they will no longer be viewable after leaving the page. You should add any ‘Allowed callback URLs’ for your local, staging and production environments, this will enable the Link SDK to correctly load. Note: you should add full URLs (e.g., <http://localhost:3000/settings/user>).
#  How the Link + Transfer SDKs works
You will use both server and client-side components to facilitate a transfer with Mesh APIs.
  1. Call [Get Networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks) to get the network IDs and token symbols that you want to make available to receive assets.
  2. Call [/api/v1/linkToken](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters) with a POST that includes the network IDs, token symbol and the target addresses that you want to make available to receive assets to create a link + Transfer URL. Make sure to include the parameter enableTransfers=true.
  3. Pass the iFrameURL to the appropriate SDK
    1. [Web Link SDK](https://docs.meshconnect.com/guides/web-sdk)
    2. [iOS Link SDK](https://docs.meshconnect.com/guides/ios-sdk)
    3. [Android Link SDK](https://docs.meshconnect.com/guides/android-sdk)
    4. [React Native SDK](https://docs.meshconnect.com/guides/react-native-sdk)
    5. [Flutter SDK](https://docs.meshconnect.com/guides/flutter-sdk)
  4. Your user will be able to filter and search for the account they want to connect. Mesh will manage the authentication flow and handle MFAs for all integrations that support transfers v2.
  5. After your user successfully enters their credentials, in the return method you will receive an auth_token.
  6. Your user initiates a transfer by selecting the eligible assets
  7. Your user configures a transfer by inputting amount to transfer
  8. Your user is given preview of transfer details (including origin account, destination address, symbol, network, amount, estimated gas fee)
  9. Your user submits the transfer
    1. If user is transferring from self-custody wallet, then the user is redirected to wallet platform to execute transfer
    2. If user is transferring from centralized exchange, then Mesh sends instructions to exchange to execute the transfer
  10. Your user will be returned to a transfer confirmation screen after the transfer has been successfully confirmed by the origin account

A pre-requisite step is to call [/api/v1/transfers/managed/networks](https://docs.meshconnect.com/api-reference/managed-transfers/get-networks)` to get the list of networks supported by Mesh in order to supply the list of addresses to Mesh.

```

    "content": {
        "networks": [

                "id": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
                "name": "Polygon",
                "chainId": "137",
                "supportedTokens": [
                    "MATIC",
                    "USDC"

                "supportedBrokerTypes": [
                    "binanceInternational",
                    "kraken",
                    "robinhood"



                "id": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
                "name": "Ethereum",
                "chainId": "1",
                "supportedTokens": [
                    "ETH",
                    "USDC"

                "supportedBrokerTypes": [
                    "binanceInternational",
                    "kraken",
                    "robinhood"



                "id": "0291810a-5947-424d-9a59-e88bb33e999d",
                "name": "Solana",
                "chainId": "101",
                "supportedTokens": [
                    "SOL",
                    "USDC"

                "supportedBrokerTypes": [
                    "binanceInternational",
                    "kraken"



    },
    "status": "ok",
    "message": ""


```

The initial step is to generate a link URL by posting a request to
###  Request

```

curl --request POST \
     --url https://integration-api.meshconnect.com/api/v1/linktoken \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'X-Client-Id: CLIENT_ID' \
-H 'X-Client-Secret: CLIENT_SECRET' \
     --data '

  "transferOptions": {
    "toAddresses": [

        "networkId": "0291810a-5947-424d-9a59-e88bb33e999d",
        "symbol": "SOL",
        "address": "DVifyLEUVxCAUTdi8rPHX9fmi1tCwv7hciut4BErskZ8"


  },
  "restrictMultipleAccounts": true,
  "userId": "123456"




```

###  Response

```

    "content": {
        "linkToken": "aHR0cHM6Ly93ZWIuZ2V0ZnJvbnQuY29tL2IyYi1pZnJhbWUvZTE4ODBjNmQtNWFmOC00NjM0LTMxODItMDhkYmE1OGE5OWE1L2Jyb2tlci1jb25uZWN0P2F1dGhfY29kZT12NkJMT2tkMF84cUhLbXZNa2FWdGVMTGo2WnRBcGpjQVpCNE50S091MllnQV9ZcW5OSkVROE9Lck1Hd3E1akFjNU1Tb0drNDVpdEZzN1MtZ19lWFdwQSZyZXN0cmljdE11bHRpcGxlQWNjb3VudHM9dHJ1ZSZ0cmFuc2Zlcl90b2tlbj0wUDlENHNLV2Q5VFRXdGh3bHlTSzVRJTNkJTNkLmFHWldJcjdsN2tjZXp3cVVzWUQ0JTJiRG5kSE1NcmNGNXVZYnkyWDdCVDMwS2VEdm5hZkcxaXJKY0NUbE5BNUp6WWRLWVlDRXQxOWpxSkJsdTd5WlVFTkxBOHBFNTNLdkNGRVpIVWtob2p4TlhSdEpKVDN3MGdKWHdwR3VaQ2RHakUlMmZWZDBzMUZpdnlPJTJicEM0ZEVIdFFlUSUzZCUzZCZsaW5rX3N0eWxlPWV5SndZeUk2SWlNd016ZEdSa1lpTENKd2RDSTZJaU5HUmtaR1JrWWlMQ0p6WXlJNklpTkdOME16TmpZaUxDSnpkQ0k2SWlNd01EQXdNREFpTENKaWNpSTZOUzR3TUN3aWFYSWlPakF1TURBc0ltbHZJam93TGpNM01EQXdNREF3TENKMElqb2liR0ZpWld3aUxDSm9ZeUk2Wm1Gc2MyVjk="
    },
    "status": "ok",
    "message": "",
    "errorType": ""


```

Once you have the `linkToken`, you can use it to initialize the Mesh Link SDK. Mesh Link SDKs are a drop-in client-side module available for web, iOS, and Android that handles the authentication process and facilitate transfers. This is what your users use to connect to their accounts, configure and execute their transfers.

```
import React, { useEffect, useState } from 'react'
import {
  FrontConnection,
  FrontPayload,
  createFrontConnection
} from '@front-finance/link'
import { clientId } from '../utility/config'

export const FrontComponent: React.FC<{
  iframeLink?: string | null
  onSuccess: (authData: FrontPayload) => void
  onExit?: (error?: string) => void
}> = ({ iframeLink, onSuccess, onExit }) => {
  const [frontConnection, setFrontConnection] =
    useState<FrontConnection | null>(null)

  useEffect(() => {
    setFrontConnection(
      createFrontConnection({
        clientId: clientId,
        onBrokerConnected: authData => {
          console.info('[MESH SUCCESS]', authData)
          onSuccess(authData)
        },
        onExit: (error?: string) => {
          if (error) {
            console.error(`[MESH ERROR] ${error}`)


          onExit?.()
        },
				onTransferFinished: data => {
          console.info('[MESH TRANSFER SUCCESS]', data)
          onTransferFinished?.(data)

      })

  }, [])

  useEffect(() => {
    if (iframeLink) {
      frontConnection?.openPopup(iframeLink)


    return () => {
      if (iframeLink) {
        frontConnection?.closePopup()


  }, [frontConnection, iframeLink])

  return <></>


```

On successful authentication, you will be provided the auth_token (and in most cases refresh_token) that can be used for future calls. Your users will be able to configure, preview and execute transfers with the Drop-In Transfer UI. We will provide events that you can subscribe to that provide details on progress and any errors that might be encountered. On successful completion of the transfer, you will be provided a transaction data of the type `TransferFinishedPayload`, that’s content can be the following:

```

	"type": "transferFinished",
	"payload": {
		"status": "success",
		"amount": 0.005,
		"fromAddress": "0x9bf6207f8a3f4278e0c989527015defe10e5d7c6",
		"toAddress":  "0x9bf6207f8a3f4278e0c989527015defe10e5d7c6",
		"networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
		"symbol": "ETH",
		"txId": "0x458f3d8bd6c9ea3c9f1fe831d7444e4a6f4525e40c87179796350cc426aa020c",




	"type": "transferFinished",
	"payload": {
		"status": "error",
		"errorMessage": "The specified amount is greater than the maximum amount allowed."



```

#  How to initiate a transfer after a user has previously authenticated
  1. Generate a new Link token with payload providing `transferOptions` along with `toAddresses` as shown below and described in [API reference](https://docs.meshconnect.com/api-reference/managed-account-authentication/get-link-token-with-parameters)



```

curl --request POST \
     --url https://integration-api.meshconnect.com/api/v1/linktoken \
     --header 'accept: application/json' \
     --header 'content-type: application/json' \
     --header 'X-Client-Id: CLIENT_ID' \
-H 'X-Client-Secret: CLIENT_SECRET' \
     --data '

  "transferOptions": {
    "toAddresses": [

        "networkId": "0291810a-5947-424d-9a59-e88bb33e999d",
        "symbol": "SOL",
        "address": "DVifyLEUVxCAUTdi8rPHX9fmi1tCwv7hciut4BErskZ8"


  },
  "restrictMultipleAccounts": true,
  "userId": "123456"




```

  1. Initiate the web SDK using `createFrontConnection` function and provide the `accessTokens` parameters that was obtained previously (**Note** : Only provide `accessTokens` as shown below). The type of the access tokens object is exported as `IntegrationAccessToken` type from the `@meshconnect/link` package



```
  createFrontConnection({
    clientId: clientId,
    onBrokerConnected: authData => {
      console.info('[MESH SUCCESS]', authData)
      onSuccess(authData)
    },
    onExit: (error?: string) => {
      if (error) {
        console.error(`[MESH ERROR] ${error}`)


      onExit?.()
    },
    accessTokens: [

        accountId: '739376630',
        accountName: 'Margin account',
        accessToken: '..............',
        brokerType: 'robinhood',
        brokerName: 'Robinhood'


  })

```

  1. Open the transfers UI using the `frontConnection.openPopup` function as you would on account connection flow described in the [quickstart guide](https://docs.meshconnect.com/docs/web-sdks#getting-tokens). This should take you straight to the Transfers UI using previously authenticated integration.

Notes:
  * In step 2, you can provide multiple integration access tokens. However, only the first account will be used as an origin account for transfers.
  * If you provide an access token that is not supported by managed transfers, the user will see an error message stating that there are no eligible assets to transfer from the origin account. A list of supported integrations can be found [here](https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations).
  * If you provide an access token that belongs to a DeFi wallet, the user is prompted to connect that account again and then redirected to the crypto transfers flow.


#  Flow Diagrams
##  CEX Flow Diagram
Was this page helpful?
YesNo
Ctrl+I
On this page
  * [How the Link + Transfer SDKs works](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide#how-the-link-%2B-transfer-sdks-works)
  * [How to initiate a transfer after a user has previously authenticated](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide#how-to-initiate-a-transfer-after-a-user-has-previously-authenticated)
  * [CEX Flow Diagram](https://docs.meshconnect.com/guides/digital-asset-managed-transfers-with-sdk-integration-guide#cex-flow-diagram)


Assistant
Responses are generated using AI and may contain mistakes.
