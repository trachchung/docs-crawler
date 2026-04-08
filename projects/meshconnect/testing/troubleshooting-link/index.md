<!-- Source: https://docs.meshconnect.com/testing/troubleshooting-link -->

[Skip to main content](https://docs.meshconnect.com/testing/troubleshooting-link#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
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


##  Link UI is not displaying in your webpage
**Symptoms:**
  * When initializing the Link UI, you see a grey box instead of the Link UI
  * An error in the browser’s console that says `Refused to frame 'https://web.meshconnect.com/' because an ancestor violates the following Content Security Policy directive...`

**Causes:**
  * When using the Link Web SDK in your page, Mesh SDK loads the Link UI using an iFrame component. Due to security reasons, we allow loading the Link UI only on a predefined set of URLs.
  * If you are using a Content Security Policy (CSP) directives on your website, they might block loading an external iFrame into your page.

**Troubleshooting:**
  * Add your website’s URL to the list of **Allowed Link URLs** in our [dashboard](https://dashboard.meshconnect.com/company/keys).
  * Add the following CSP directives to your site: `frame-src: *.meshconnect.com`


#  Unable to connect an OAuth integration
**Symptoms:**
  * When authenticating on a third party integration’s side (e.g., Coinbase or Gemini), the user gets stuck on a page displaying a loading spinner

**Causes:**
  * Ad-blocking software is not officially supported with Link UI, and some ad-blockers have been known to cause issues with Link.
  * Some browsers have built-in ad-blocking service (Brave Browser) which prevents Link UI from using the browser’s storage.

**Troubleshooting:**
  * Disable all ad-blockers in your browser


Was this page helpful?
YesNo
[Previous](https://docs.meshconnect.com/testing/error-dictionary)[ Transfer Webhooks Next ](https://docs.meshconnect.com/testing/webhooks)
Ctrl+I
On this page
  * [Link UI is not displaying in your webpage](https://docs.meshconnect.com/testing/troubleshooting-link#link-ui-is-not-displaying-in-your-webpage)
  * [Unable to connect an OAuth integration](https://docs.meshconnect.com/testing/troubleshooting-link#unable-to-connect-an-oauth-integration)


Assistant
Responses are generated using AI and may contain mistakes.
