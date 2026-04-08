<!-- Source: https://docs.meshconnect.com/advanced/configuring-transfer-options -->

[Skip to main content](https://docs.meshconnect.com/advanced/configuring-transfer-options#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Configuring Transfer Options
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


The `transferOptions` object is the core of any payment or deposit flow in Mesh. By passing this object in your server-side `POST /api/v1/linktoken` request, you can precisely control the user’s experience in the Link UI, from the assets they can transfer to the fees they are charged.
#  Core Components of `transferOptions`  
| Parameter  | Type  | Description  |  
| --- | --- | --- |  
| `toAddresses`  | Array  |  **Required.** An array of objects defining the destination for the funds.  |  
| `transferType`  | String  | The type of transfer, either `payment` or `deposit`.  |  
| `fundingOptions`  | Object  | An object to enable features like SmartFunding.  |  
| `transactionId`  | String  | A unique identifier for the transaction from your system, crucial for reconciliation.  |  
| `ClientFee`  | Number  | A decimal representing a fee you can add to the transaction (e.g., `0.025` for 2.5%).  |  
#  **`Configuring Destination Addresses (toAddresses)`**
The `toAddresses` array is the most critical part of the configuration. Each object in this array defines a specific asset, network, and destination address.
  * **Key Requirement:** You must use the Mesh-specific Unique Identifier (`NetworkId`) for each network. You can find these by calling the `GET /api/v1/transfers/managed/networks` endpoint.


#  **Single Address (Streamlined UX)**
Providing a single object in the `toAddresses` array creates the most direct user experience. The Link UI will skip the asset and network selection screens, taking the user directly to the amount and confirmation steps. **Example:**

```
"transferOptions": {
  "toAddresses": [

      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "ETH",
      "address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"




```

#  **Multiple Addresses (Flexibility)**
To give your users more choice, you can provide an array with multiple destination objects. This will allow the user to select their preferred asset and network within the Link UI. **Example:**

```
"transferOptions": {
  "toAddresses": [

      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "ETH",
      "address": "0xYourAddress..."
    },

      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "USDC",
      "address": "0xYourAddress..."
    },

      "networkId": "7436e9d0-ba42-4d2b-b4c0-8e4e606b2c12",
      "symbol": "MATIC",
      "address": "0xYourAddress..."




```

#  **Configuring a Specific Amount**
For payment use cases, you can pre-fill the amount the user needs to send.
  * **Amount in Crypto:** To specify an amount in a specific cryptocurrency, add the `Amount` key to an object within the `toAddresses` array.
  * **Amount in Fiat:** To specify an amount in fiat (e.g., USD) that will be converted to the crypto equivalent at the time of the transaction, add the `AmountInFiat` key directly within the `transferOptions` object.

**`Example (AmountInFiat):`**

```
"transferOptions": {
  "toAddresses": [

      "networkId": "e3c7fdd8-b1fc-4e51-85ae-bb276e075611",
      "symbol": "ETH",
      "address": "0x9Bf6207f8A3f4278E0C989527015deFe10e5D7c6"

  ],
  "AmountInFiat": 10,
  "TransactionId": "YOUR_UNIQUE_TRANSACTION_ID"


```

#  **Enabling SmartFunding**
To maximize conversion, we strongly recommend enabling SmartFunding. This allows users to complete a payment even if they don’t have enough of the required asset by auto-converting their other tokens.
  * **How to Enable:** Set `enabled: true` within the `fundingOptions` object.

**Example:**

```
"transferOptions": {
  "toAddresses": [ /* ... */ ],
  "AmountInFiat": 10,
  "fundingOptions": {
    "enabled": true



```

Was this page helpful?
YesNo
[ Best UX Practices & Examples Previous ](https://docs.meshconnect.com/advanced/best-ux-practices)[ Mesh Managed Tokens (MMT) Next ](https://docs.meshconnect.com/advanced/mesh-managed-tokens)
Ctrl+I
On this page
  * [Core Components of transferOptions](https://docs.meshconnect.com/advanced/configuring-transfer-options#core-components-of-transferoptions)
  * [Configuring Destination Addresses (toAddresses)](https://docs.meshconnect.com/advanced/configuring-transfer-options#configuring-destination-addresses-toaddresses)
  * [Single Address (Streamlined UX)](https://docs.meshconnect.com/advanced/configuring-transfer-options#single-address-streamlined-ux)
  * [Multiple Addresses (Flexibility)](https://docs.meshconnect.com/advanced/configuring-transfer-options#multiple-addresses-flexibility)
  * [Configuring a Specific Amount](https://docs.meshconnect.com/advanced/configuring-transfer-options#configuring-a-specific-amount)
  * [Enabling SmartFunding](https://docs.meshconnect.com/advanced/configuring-transfer-options#enabling-smartfunding)


Assistant
Responses are generated using AI and may contain mistakes.
