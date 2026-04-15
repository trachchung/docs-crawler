<!-- Source: https://docs.neox.vn/docs/collections/integration/event-notification -->

This is the API that should be created by platform to receive notifications from NeoX including created virtual accounts and transaction events.
## 
Configuration
Webhook configuration
#### 
Config to receive notification about created accounts and successful transaction events.
Create new configuration
#### 
Parameters description
  * URL: Webhook URL
  * Secret key: Use to verify data from NeoX
  * Authorization type: No Auth or Basic Auth
  * Type: ACCOUNT | TRANSACTION | TRANSACTION_STATUS
  * Code: Optional, mapping to "serviceInfomation.code" in creating a [_virtual account_ arrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/api-create-list-of-virtual-accounts.md) request. If you fill in the "Code", the URL will be received transaction notifications of that virtual accounts having the same "Code".
  * Group id: Optional, mapping to "serviceInfomation.groupId" in creating a [_virtual account_ arrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/api-create-list-of-virtual-accounts.md) request. If you fill in the "Group id", the URL will be received transaction notifications of that virtual accounts having the same "Group id".


> "Code" and "Group id" are $and conditions
For example, merchant create a [_virtual account_ arrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/integration/api-create-list-of-virtual-accounts.md) with "serviceInfomation.code" = "001" and "serviceInfomation.groupId" = "GR01". There are four configuration ways to receive the transaction notifications:
No
Code
Group id
001
GR01
001
_empty_
_empty_
GR01
_empty_
_empty_
## 
Notification
NeoX will send a POST request to configured URL whenever there is an event happen.
  1. **Notification of collection transaction happened**


View event object data of type "TRANSACTION". 
  1. **Notification of virtual accounts created**


View event object data of type "ACCOUNT". 
  1. **Notification when transaction (reconcile) status changed**


View event object data of type "TRANSACTION_STATUS". [_**Click here**_ arrow-up-right](https://docs.neox.vn/docs/collections/transaction-status-management/webhook)
  1. **Notification when refund request status changed**


View event object data of type "REFUND". [_**Click here**_ arrow-up-right](https://docs.neox.vn/docs/collections/refund-request-management/webhook)
  1. **Notification when withdraw request status changed**


View event object data of type "PAYOUT". [_**Click here**_ arrow-up-right](https://docs.neox.vn/docs/collections/withdraw-request-management/webhook)
[PreviousAPI get detail withdraw requestchevron-left](https://docs.neox.vn/docs/collections/integration/apis-for-withdraw-requests-management/get-detail-withdraw-request)[NextSFTP upload document file of collection transactionchevron-right](https://docs.neox.vn/docs/collections/integration/sftp-upload-document-file-of-collection-transaction)
Last updated 1 year ago
Was this helpful?
