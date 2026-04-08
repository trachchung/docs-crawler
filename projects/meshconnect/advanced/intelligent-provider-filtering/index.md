<!-- Source: https://docs.meshconnect.com/advanced/intelligent-provider-filtering -->

[Skip to main content](https://docs.meshconnect.com/advanced/intelligent-provider-filtering#content-area)
[Mesh home page](https://docs.meshconnect.com/)
Search...
Ctrl KAsk AICTRLI


[Mesh home page](https://docs.meshconnect.com/)
Search or ask...
Navigation
Advanced
Intelligent Provider Filtering in Mesh Link
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


Mesh automatically applies intelligent filtering during Link initialization to ensure users only see compatible, compliant, and viable providers (wallets, exchanges, brokers). This improves success rates, avoids regulatory blockers, and enhances user experience. Below is a complete breakdown of the filters we apply, categorized by use case and user type.
##  **1. Token & Network Compatibility**
**Applies to: All clients** Mesh only displays providers that support the exact asset and network combination requested in the transfer. **How it works:**
  * If a user selects USDC on Solana, only providers that support USDC _on Solana_ will be shown.
  * If the selected token or network is not supported by a provider, that provider is excluded.

**Why this matters:** Prevents failed transfers due to unsupported configurations and ensures a seamless experience.
##  **2. Travel Rule Filters – VASP ID Requirement**
**Applies to: Custodial platforms (e.g. neobanks, exchanges, fintechs)** In certain jurisdictions, Coinbase requires the sending platform to provide a valid **VASP ID**. If Mesh does not have a VASP ID on file for your client and the user is in a restricted country, **Coinbase will not appear**. **Countries affected:** AE, AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, JE, KR, LI, LT, LU, LV, MT, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK **Logic:**
  * IP address is in an affected country
  * Mesh does not have a VASP ID for your client → Coinbase is excluded from the provider list


##  **3. Travel Rule Filters – Wallet Ownership Verification**
**Applies to: Self-custody wallets (e.g. MetaMask, Zengo, Trust Wallet)** When a user is connecting via a self-hosted wallet, Coinbase enforces wallet ownership verification in certain jurisdictions. Because self-custody wallets cannot provide ownership proof, Mesh filters Coinbase out in these scenarios. **Logic:**
  * If the **transfer amount exceeds 1000 EUR** and the user’s IP is in one of the following countries, Coinbase will **not be shown** : **AE, AT, BE, BG, CH, CY, CZ, DE, DK, EE, ES, FI, FR, GB, GR, HR, HU, IE, IS, IT, JE, KR, LI, LT, LU, LV, MT, NL, NO, NZ, PL, PT, RO, SE, SG, SI, SK**
  * If the user’s IP is in one of the following **Southeast and East Asian countries** , Coinbase will also be **filtered regardless of amount** : **SG (Singapore), HK (Hong Kong), PH (Philippines), KR (South Korea)**

This enforcement is based on Coinbase’s jurisdiction-specific compliance policies and is dynamically applied by Mesh at runtime.
##  **4. Travel Rule Filters – Use Case Restrictions**
**Applies to: Gaming platforms using custodial or exchange accounts** Some providers restrict transfers based on the **type of platform** initiating the request. **Example:**
  * **Binance (Japan):** Does not allow Japanese accounts to transfer to gaming platforms. → If a user is on a gaming platform and their IP is in Japan, Binance will not be shown.

Mesh applies this logic automatically when the client metadata indicates the platform is categorized as “gaming.”
##  **5. Broker Geography Restrictions**
**Applies to: All clients** Mesh enforces IP-based restrictions at the provider level to reflect each broker’s supported regions. **Rules:**
  * **Binance:** Not shown to users with IPs in **US, Canada, or Netherlands**
  * **Robinhood:** Only shown to users with **US IPs** ; filtered out otherwise

These rules are enforced directly based on provider policies and automatically reflected in the Link session.
##  **Summary**  
| **Filter Type**  | **Applies To**  | **Example Outcome**  |  
| --- | --- | --- |  
| Token/Network Compatibility  | All clients  | Only show providers that support USDT on Arbitrum  |  
| Coinbase VASP ID  | Custodial clients  | Coinbase not shown if no VASP ID for client in DE  |  
| Coinbase Wallet Ownership  | Self-custody wallets  | Coinbase hidden for >1000 EUR from FR via Zengo  |  
| Broker Geography  | All clients  | Binance not shown to user in US  |  
| Use Case Travel Rule  | Gaming platforms  | Binance filtered for JP IPs on gaming platform  |  
If you need help validating provider coverage for specific asset/network combinations or regions, please reach out to your Mesh account manager or visit the [Mesh Developer Docs](https://docs.meshconnect.com/).
Was this page helpful?
YesNo
[ Mesh Managed Tokens (MMT) Previous ](https://docs.meshconnect.com/advanced/mesh-managed-tokens)[ Enabling Multi-Language Support for Link Next ](https://docs.meshconnect.com/advanced/language)
Ctrl+I
On this page
  * [1. Token & Network Compatibility](https://docs.meshconnect.com/advanced/intelligent-provider-filtering#1-token-%26-network-compatibility)
  * [2. Travel Rule Filters – VASP ID Requirement](https://docs.meshconnect.com/advanced/intelligent-provider-filtering#2-travel-rule-filters-%E2%80%93-vasp-id-requirement)
  * [3. Travel Rule Filters – Wallet Ownership Verification](https://docs.meshconnect.com/advanced/intelligent-provider-filtering#3-travel-rule-filters-%E2%80%93-wallet-ownership-verification)
  * [4. Travel Rule Filters – Use Case Restrictions](https://docs.meshconnect.com/advanced/intelligent-provider-filtering#4-travel-rule-filters-%E2%80%93-use-case-restrictions)
  * [5. Broker Geography Restrictions](https://docs.meshconnect.com/advanced/intelligent-provider-filtering#5-broker-geography-restrictions)


Assistant
Responses are generated using AI and may contain mistakes.
