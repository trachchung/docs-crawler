<!-- Source: https://docs.meshconnect.com/advanced/best-ux-practices -->

[Skip to main content](https://docs.meshconnect.com/advanced/best-ux-practices#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Best UX Practices & Examples
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


Mesh provides a faster, safer, and more reliable way for users to move funds from exchanges and wallets directly into your platform. By replacing error-prone QR codes and manual address entry with a seamless, embedded flow, you can significantly increase conversion and user satisfaction. **Key Advantages:**
  * **Fast and Easy:** One-click payments and deposits from Binance, Coinbase, MetaMask, and 300+ other sources.
  * **Error-Free:** Prevents wrong addresses, wrong networks, and address poisoning scams.
  * **Higher Conversion:** Reduces user drop-off compared to manual flows.
  * **Customer-Friendly:** A familiar, secure connection process, similar to linking an account with Plaid or PayPal.


###  **Placement Best Practices**
How you present the Mesh option in your UI is critical for adoption.
  * **Prioritize the Embedded Flow:** Place the “Pay with Crypto” or “Deposit with Crypto” button prominently in your checkout or wallet UI, above any manual QR code options.
  * **Use QR Codes as a Backup:** Maintain the manual/QR code option as a secondary choice for users who prefer it.
  * **Use Action-Oriented Labels:** Highlight Mesh as the recommended option with labels like **Smart Pay** , **Easy Deposit** , or **Instant Transfer**.
  * **Lead with Trusted Brands:** Instead of “Pay with Mesh,” use the logos of top exchanges and wallets your users trust, like Binance, Coinbase, and MetaMask.


###  **The User Journey: A Phased Approach**
The goal is to move users from a simple first-time setup to a frictionless, one-click experience.
####  **1. First-Time User Experience (Smart Pay / Smart Deposit)**
For a new user connecting an account, the flow is simple and builds trust.
  * The user selects “Pay with Crypto” or “Deposit from Exchange/Wallet.”
  * Mesh securely authenticates their account once.
  * The user chooses an asset, previews the transaction, and confirms.

This is equivalent to adding a card to Apple Pay: a small, one-time setup that unlocks a seamless experience for all future use. **📸 Example (Payment Use Case): A “Pay with Crypto” button in a checkout flow.** **📸 Example (Deposit Use Case): “Deposit from Wallet” with trusted brand options.**
####  **2. Returning User Experience (Easy Pay / Easy Deposit)**
This is where the power of Mesh becomes clear. Once an account is connected, returning users get a one-click experience.
  * You use the stored `auth_token` to initialize Mesh.
  * The user is taken **directly to the confirmation screen** , skipping the login steps.
  * You can create dedicated, personalized buttons like **“Pay with your Binance account”** or **“Deposit from MetaMask.”**

**📸 Example: A personalized deposit button for a return user.**
####  **3. Power User Experience (Fast Pay / Fast Deposit)**
For frequent users, you can create an even faster flow by pre-selecting the token and network.
  * The `linkToken` is configured with a single, pre-defined asset.
  * The user is taken directly into the transfer flow, bypassing all selection steps.
  * This is ideal for high-frequency use cases like iGaming platforms.


###  **Key Feature for Payments: SmartFunding**
For all use cases, enabling SmartFunding is the most effective way to maximize conversion.
  * **What it is:** SmartFunding allows users to complete a payment even if they don’t have enough of the required token by **auto-converting** their other assets in the background.
  * **Why it’s critical for payments:** It prevents transaction failures due to insufficient funds of a specific asset, turning a potential “failed payment” into a successful one.


###  **Technical Integration Tips**
  * **Token Management:** Always store and refresh the user’s `auth_token` to enable the “Easy Pay/Deposit” return user experience.
  * **Use **`integrationId` **s:** Deep-link directly to specific providers (e.g., Binance, Coinbase) to create shortcuts in your UI.
  * **Support Multi-Asset Arrays:** In your `linkToken` request, pass an array of all the tokens/networks you support to give users maximum flexibility.


###  **Business Impact**
By adopting this UX strategy, our partners see measurable improvements:
  * **Higher Conversion Rates (20-30% lift):** Users complete payments and deposits more often.
  * **Increased Volume:** Faster flows encourage more frequent and larger transactions.
  * **Reduced Support Tickets:** Eliminates user errors like sending to the wrong address or network.
  * **Stronger Retention (2-6x repeat conversions):** Account-linked flows keep users engaged on your platform.


Was this page helpful?
YesNo
[Previous](https://docs.meshconnect.com/supported-tokens)[ Configuring Transfer Options Next ](https://docs.meshconnect.com/advanced/configuring-transfer-options)
Ctrl+I
On this page
  * [Placement Best Practices](https://docs.meshconnect.com/advanced/best-ux-practices#placement-best-practices)
  * [The User Journey: A Phased Approach](https://docs.meshconnect.com/advanced/best-ux-practices#the-user-journey-a-phased-approach)
  * [1. First-Time User Experience (Smart Pay / Smart Deposit)](https://docs.meshconnect.com/advanced/best-ux-practices#1-first-time-user-experience-smart-pay-%2F-smart-deposit)
  * [2. Returning User Experience (Easy Pay / Easy Deposit)](https://docs.meshconnect.com/advanced/best-ux-practices#2-returning-user-experience-easy-pay-%2F-easy-deposit)
  * [3. Power User Experience (Fast Pay / Fast Deposit)](https://docs.meshconnect.com/advanced/best-ux-practices#3-power-user-experience-fast-pay-%2F-fast-deposit)
  * [Key Feature for Payments: SmartFunding](https://docs.meshconnect.com/advanced/best-ux-practices#key-feature-for-payments-smartfunding)
  * [Technical Integration Tips](https://docs.meshconnect.com/advanced/best-ux-practices#technical-integration-tips)
  * [Business Impact](https://docs.meshconnect.com/advanced/best-ux-practices#business-impact)


Assistant
Responses are generated using AI and may contain mistakes.
