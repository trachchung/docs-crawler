<!-- Source: https://docs.meshconnect.com/testing/webhooks -->

[Skip to main content](https://docs.meshconnect.com/testing/webhooks#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Testing
Transfer Webhooks
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


If your business relies on transfer status updates to make business decisions (releasing inventory, dispersing funds, etc.), then polling Mesh’s managed transfers endpoint is an inefficient and ineffective solution. Mesh offers webhooks to solve this problem. A webhook is a callback function that allows lightweight, event-driven communication between 2 systems. The events that trigger communications from Mesh’s webhooks are updates to transfer statuses. Instead of polling a Mesh endpoint, you can provide Mesh (via the Dashboard) with a unique callback URL which will automatically receive transfer status updates as Mesh learns about them.
##  Secure Data Transmission
  * Mesh uses HMAC (Hash-based Message Authentication Code)
  * When clients register their Webhook URI, they receive a Secret from Mesh which will be used in signing the request.
  * Mesh signs each webhook request using a secret key. The receiver can verify the signature using the same secret key to ensure the data has not been tampered with.
  * Mesh will include a signature header (e.g., **`X-Mesh-Signature-256`**) that the receiver can use to validate the integrity and authenticity of the payload.

This is the function we use for creating HMAC signature that is used in the request header:

```
 public string GenerateHmacSignature(string payload, string webhookSecret)

        using var hmac = new HMACSHA256(Encoding.UTF8.GetBytes(webhookSecret));
        byte[] hash = hmac.ComputeHash(Encoding.UTF8.GetBytes(payload));
        return Convert.ToBase64String(hash);


```

#  Whitelist IP
All the webhook calls from Mesh side will come from this static IP:

```
20.22.113.37

```

##  Webhook Event Model
The webhook payload contains the core information related to a transfer update, and also includes additional fields specific to the webhook event.
###  Transfer data
  * **`TransferId`**(`Guid`): The unique identifier of the transfer related to this event.
  * **`Timestamp`**(`long`): The timestamp indicating when the event occurred.
  * **`TransferStatus`**(`string`): The status of the transfer at the time of the event. This is an enumeration representing various possible states of the transfer.
  * **`TransactionId`**(`string`): The unique identifier for the transaction associated with the transfer.
  * **`TxHash`**(`string`): The unique identifier for the blockchain transaction associated with the transfer.
  * **`UserId`**(`string`): The unique identifier of the user associated with the transfer.
  * **`Token`**(`string`): The token associated with the transfer.
  * **`Chain`**(`string`): The chain associated with the transfer.
  * **`SourceAmount`**(`decimal?`): The amount of token that has left the source account.
  * **`SourceAccountProvider`**(`string`): The account provider that has been used to send the token.
  * **`DestinationAmount`**(`decimal?`): The amount of token that has received by the destination account.
  * **`DestinationAddress`**(`string`): The destination account address.
  * **`RefundAddress`**(`string`): The refund address (optional).


###  Webhook call data
  * **`EventId`**(`Guid`): A unique identifier for the event. This event identifies each message sent to clients. This ID will remain same even in case of retries.
  * **`Id`**(`Guid`): A unique identifier for the webhook event. This is considered as SentID, there maybe multiple retries for any event pushed into the queue. For each try for sending a specific event there is a different Id.
  * **`SentTimestamp`**(`long`): The timestamp indicating when the webhook event was sent.


###  Payload
The payload format is JSON. Here is an example of payload.

```

  "Id": "358c6ab7-4518-416b-9266-c680fda3a8dd",
  "EventId": "56713e70-be74-4a37-0036-08da97f5941a",
  "SentTimestamp": 1720532648,
  "UserId": "user_id_provided_by_client",
  "TransactionId": "transaction_id_provided_by_client",
  "TransferId": "dd4063e5-f317-441c-3f07-08dc7353b6f8",
  "TransferStatus": "Pending",
  "TxHash": "0x7d4ec1ce50952a377452c95fdf5a787ff551f08c0343093f866c84f57c473495",
  "Chain":"Ethereum",
  "Token":"ETH",
  "DestinationAddress":"0x0Ff0000f0A0f0000F0F000000000ffFf00f0F0f0",
  "SourceAccountProvider" :"Binance",
  "SourceAmount":0.004786046226555188,
  "DestinationAmount":0.004786046226555188,
  "RefundAddress": "0x0Ff0000f0A0f0000F0F000000000ffFf00f0F0f0",
  "Timestamp": 1715175519038


```

###  Transfer Status Values
  * **`pending`**: The transfer has been initiated via Mesh, but has not yet reached a final state. Mesh does not yet have a Transfer Hash for this transfer.
  * **`succeeded`**: A final state that indicates the transfer was successfully delivered to the destination address. Mesh has a Transfer Hash for this transfer.
  * **`failed`**: A final state that indicates the transfer has failed. No transfer hash available.


###  Create and register your callback URI
  * Create an endpoint that can receive a POST request with application/json content.
  * Go to [Account —> API Keys](https://dashboard.meshconnect.com/company/keys) in your Mesh Dashboard.
  * Scroll down to “Production Transfer Webhook URI” and “Sandbox Transfer Webhook URI”


  * When registering an endpoint, you’ll be prompted to store your secret key, as you won’t be able to view it again.


  * You can only save one production URI and one Sandbox URI, but you can deactivate one and save a new one at any time.


###  How to respond to a Mesh webhook event
  * Please respond with a **`200`**response in < 200ms to confirm receipt of the event.
  * If Mesh does not receive a **`200`**response in < 200ms, the webhook will retry (you will receive the event again with all duplicate information except for a different **`Id`**).


Was this page helpful?
YesNo
Ctrl+I
On this page
  * [Secure Data Transmission](https://docs.meshconnect.com/testing/webhooks#secure-data-transmission)
  * [Webhook Event Model](https://docs.meshconnect.com/testing/webhooks#webhook-event-model)
  * [Webhook call data](https://docs.meshconnect.com/testing/webhooks#webhook-call-data)
  * [Transfer Status Values](https://docs.meshconnect.com/testing/webhooks#transfer-status-values)
  * [Create and register your callback URI](https://docs.meshconnect.com/testing/webhooks#create-and-register-your-callback-uri)
  * [How to respond to a Mesh webhook event](https://docs.meshconnect.com/testing/webhooks#how-to-respond-to-a-mesh-webhook-event)


Assistant
Responses are generated using AI and may contain mistakes.
