<!-- Source: https://docs.meshconnect.com/advanced/foreign-currency-support -->

[Skip to main content](https://docs.meshconnect.com/advanced/foreign-currency-support#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Foreign Currency Support
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


You can now display balances and amounts in multiple currencies outside of USD to better serve your global user base.
##  Supported Currencies
The following currencies are currently supported:
  * **USD** - US Dollar
  * **GBP** - British Pound
  * **EUR** - Euro


##  How to Enable
To enable foreign currency support, set the `displayFiatCurrency` parameter in your Web SDK configuration to one of the three supported currency codes listed above. Please **ensure you pass one of these three values** when initializing the SDK. Example:

```
useEffect(() => {
    setLinkConnection(
      createLink({
        clientId: clientId,
        language: 'en',
        theme: 'system',
        displaycurrency: 'eur'

```

**Note** : `displayAmountInFiat` and other fiat fields will be fully compatible with this new feature
##  UI Behaviour
By specifying a non-USD currency, **all fiat amounts** in Mesh Link will display in the specified currency. Examples:
Was this page helpful?
YesNo
[ Mesh Link SDK Events Previous ](https://docs.meshconnect.com/advanced/link-ui-events)[ Manual Deposits Next ](https://docs.meshconnect.com/advanced/manual-deposits)
Ctrl+I
On this page
  * [Supported Currencies](https://docs.meshconnect.com/advanced/foreign-currency-support#supported-currencies)
  * [How to Enable](https://docs.meshconnect.com/advanced/foreign-currency-support#how-to-enable)


Assistant
Responses are generated using AI and may contain mistakes.
