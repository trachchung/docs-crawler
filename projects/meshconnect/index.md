<!-- Source: https://docs.meshconnect.com/ -->

[Skip to main content](https://docs.meshconnect.com/overview#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Get Started
Overview
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


Mesh is a global crypto payments network that connects exchanges, wallets, and payment providers, allowing merchants to accept crypto payments and stablecoin conversions easily. It streamlines payments, reduces fees, and offers instant settlement through a suite of APIs and client-side SDKs. The core of the Mesh experience is **Mesh Link** , a collection of client-side SDKs that provide a user-friendly interface for your users to interact with their crypto exchanges and self-custody wallets. It handles credential validation, multi-factor authentication, and error handling for every integration we support. This allows you to build embedded experiences where users can transfer digital assets from centralized exchanges or self-custody wallets without ever needing to leave your application to copy and paste an address.
##  ✨ Capabilities
Mesh is a flexible platform designed to support a variety of use cases through its core product offerings.
###  **Pay**
Configure Link to facilitate cryptocurrency payments within your application. You can define accepted payment assets, amounts, and apply fees for processing. SmartFunding enables automatic conversion of the assets the user has into your payment token of choice.
###  **Deposit**
Enable your users to deposit crypto into specified addresses. You can define single or multiple deposit options and create a seamless experience for returning users by saving their connection information.
###  **Verify**
Confirm ownership of the accounts your users’ interact with.
  * **For Exchanges** : Retrieve basic profile data to get user information directly from their connected exchange account.
  * **For Wallets** : Offer embedded, gasless wallet verification by asking users to sign a message to confirm ownership of a given address.


##  🧱 Basics of a Mesh integration
**Foundational elements**
  * **Backend** : You request a linkToken which will be used to initialize the Mesh Link SDK. The parameters passed configure the user’s experience in that session. These are single use, so you’ll be requesting a new linktoken for every user session.
  * **Frontend** : Download and install the Mesh SDK. This is a modal that overlays your app and facilitates the UX of the entire user journey.

[******The Manual that follows will provide more detail on the basics of building your integration with Mesh******](https://docs.meshconnect.com/manual)
  * Inviting team members to collaborate in your Mesh developer account
  * Generating API keys and managing permissions
  * Configuring the Link SDK for your branding and other needs
  * Configuring the linkToken request to create the appropriate user flow
  * Configuring the SDK initialization to support language and return users
  * Listening for SDK events to properly handle the end of the user journey
  * Subscribing to webhooks for real-time transfer status updates
  * Enabling a seamless return-user experience with token management.
  * General best practices


Was this page helpful?
YesNo
[ Manual Next ](https://docs.meshconnect.com/manual)
Ctrl+I
On this page
  * [🧱 Basics of a Mesh integration](https://docs.meshconnect.com/overview#-basics-of-a-mesh-integration)


Assistant
Responses are generated using AI and may contain mistakes.
