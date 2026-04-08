<!-- Source: https://docs.meshconnect.com/advanced/manual-deposits -->

[Skip to main content](https://docs.meshconnect.com/advanced/manual-deposits#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Manual Deposits
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
Mesh’s flagship product is our **Direct Connection** experience. The Direct flow allows users to securely connect their exchange accounts or wallets to your platform through Mesh, enabling seamless, programmatic transfers. With the Direct Flow:
  * Users connect their exchange or wallet directly
  * Mesh can read account details (balances, addresses, transaction history)
  * Transfers are initiated programmatically
  * Mesh can help prevent user misconfiguration
  * SmartFunding can be applied to optimize conversion

However, to ensure broader coverage and higher conversion, Mesh also supports **Manual Deposits** through wallet address/QR code. Manual Deposits allow users to transfer funds by scanning a QR code or copying a wallet address—while still enabling you to receive confirmation and webhook updates from Mesh.
##  What Are Manual Deposits?
Manual Deposits support the traditional crypto transfer flow:
  1. The user is shown a QR code and destination address.
  2. The token and network are clearly specified.
  3. Any required instructions (e.g., memo/tag, minimum deposit amount) are displayed.
  4. The user initiates the transfer directly from their wallet or exchange.
  5. Mesh monitors the blockchain for the transfer.
  6. Once detected, Mesh sends a webhook event confirming the deposit.

To support this flow, clients provide destination addresses at the start of each user session via the `linkToken` request. When Mesh detects a valid onchain transfer matching the provided address, token, and network, we send a webhook with:

```
status: succeeded

```

This indicates a successful Mesh deposit.
##  When Is Manual Used?
Manual Deposits appear in two primary ways:
###  1. Front-Door Option
Mesh supports a landing experience where users can choose their preferred deposit method:
  * Connect account (Direct)
  * Deposit manually (QR code)

This gives users flexibility and can improve overall conversion by meeting different comfort levels.
###  2. Backup Experience (Enabled by Default)
If a user cannot complete a direct transfer—for example:
  * Their exchange or wallet is not supported
  * They cannot find their integration in the catalog
  * They choose to exit the direct flow
  * They run into terminal errors during direct flow

Mesh automatically presents the Manual Deposit option. This backup flow is **enabled by default for all deposit sessions**.
##  How Attribution Works
For Direct transfers, attribution is straightforward: Mesh initiates the transfer and receives confirmation from the connected account. Manual transfers require a different approach. When a user views a Mesh-generated QR code, we monitor for onchain activity and apply the following attribution logic: A transfer is attributed to Mesh if:
  * The specified token and network
  * Are sent to the exact destination address provided
  * Within 15 minutes of the user viewing the Mesh QR code
  * And there is no existing successful or pending direct deposit event

If these conditions are met, Mesh attributes the transfer as a **successful Mesh QR code deposit** and sends the corresponding webhook event. This attribution window ensures reliable detection while maintaining a clear and consistent standard across clients.
##  When Manual Deposits May Not Be Appropriate
Manual Deposits are not recommended in the following scenarios:
###  1. Non-Unique Deposit Addresses
If your platform does not provide unique wallet addresses per user session, Manual Deposits may not be suitable. Exceptions:
  * Networks like XLM or XRP that use memo/tag identifiers (which Mesh supports and displays to users)


###  2. Source-of-Funds Verification Requirements
If your compliance framework requires verification of the source of funds, Manual Deposits may not meet those requirements, as funds are sent externally without account-level connectivity.
###  3. Exact Payment Amount Requirements
If your use case requires receiving a precise amount (e.g., invoice or payment flows), Manual Deposits may introduce variability that needs additional handling.
###  4. Preference Not to Support Manual Transfers
Manual Deposits are currently enabled by default. If your business model requires restricting transfers to direct-only flows, please contact the Mesh team.
Was this page helpful?
YesNo
[ Foreign Currency Support Previous ](https://docs.meshconnect.com/advanced/foreign-currency-support)[ Overview Next ](https://docs.meshconnect.com/testing/sandbox)
Ctrl+I
On this page
  * [What Are Manual Deposits?](https://docs.meshconnect.com/advanced/manual-deposits#what-are-manual-deposits)
  * [When Is Manual Used?](https://docs.meshconnect.com/advanced/manual-deposits#when-is-manual-used)
  * [1. Front-Door Option](https://docs.meshconnect.com/advanced/manual-deposits#1-front-door-option)
  * [2. Backup Experience (Enabled by Default)](https://docs.meshconnect.com/advanced/manual-deposits#2-backup-experience-enabled-by-default)
  * [How Attribution Works](https://docs.meshconnect.com/advanced/manual-deposits#how-attribution-works)
  * [When Manual Deposits May Not Be Appropriate](https://docs.meshconnect.com/advanced/manual-deposits#when-manual-deposits-may-not-be-appropriate)
  * [1. Non-Unique Deposit Addresses](https://docs.meshconnect.com/advanced/manual-deposits#1-non-unique-deposit-addresses)
  * [2. Source-of-Funds Verification Requirements](https://docs.meshconnect.com/advanced/manual-deposits#2-source-of-funds-verification-requirements)
  * [3. Exact Payment Amount Requirements](https://docs.meshconnect.com/advanced/manual-deposits#3-exact-payment-amount-requirements)
  * [4. Preference Not to Support Manual Transfers](https://docs.meshconnect.com/advanced/manual-deposits#4-preference-not-to-support-manual-transfers)


Assistant
Responses are generated using AI and may contain mistakes.
