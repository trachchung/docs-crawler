<!-- Source: https://docs.payram.com/support/change-log -->

These release notes document changes and updates to the API and functionalities. Ensure you are using the latest Docker file for optimal performance.
## 
PayRam — What's New
> 30 Releases | 241+ Changes Shipped
### 
March 25, 2026
#### 
PayRam Core `v1.9.3`
**Fixed**
  * BTC transaction receipt now surfaces real errors (timeout, auth failure, rate limit) instead of silently marking transactions as not found
  * Deposit verification correctly distinguishes missing transactions from transient RPC failures — nil receipts are retried on next cycle
  * Removed exponential retry backoff from confirming sweeps — now processed every cycle without age-based delays
  * Refresh token endpoint returns correct HTTP status codes (401 for invalid JWT, 404 for deleted members) instead of generic 500
  * Database errors in token refresh no longer collapse into incorrect 404 — real DB failures propagate as 500


#### 
PayRam Frontend `v0.4.2`
**Added**
  * System Updater page with version management, upgrade planning, and real-time upgrade monitoring
  * Debug panel wallet URL override for testing payments page against custom backends


**Fixed**
  * Remove authenticated config call from public payments page and add checkout suffix to wallet URLs
  * Improve error handling and type safety in updater API functions
  * Normalize upgrade failure state check and fix import paths in updater module


#### 
PayRam MCP Server `v1.2.0`
**Fixed**
  * Auto-discover platform ID so agents no longer need to ask for it during setup


### 
March 21, 2026
#### 
PayRam MCP Server `v1.2.0`
**Added**
  * MCP server discovery tool for agents to find and connect to PayRam instances
  * Authentication skill for secure agent access to PayRam APIs
  * Authenticated data-fetching MCP tools for merchant dashboards


**Changed**
  * Rewritten analytics skill with direct API access for real-time data


### 
March 20, 2026
#### 
PayRam Core `v1.9.2`
**Added**
  * Batch BTC DB queries — reduces ~22,000 queries per block down to 2 using two-pass batch pattern for UTXO and sweep detection


**Changed**
  * RPC pool composite node identity uses URL + credential hash as key — fixes credential loss for same-URL nodes with different API keys
  * Existing RPC nodes re-hashed via migration for consistency with new hashing scheme
  * Processor shutdown changed to graceful termination via context cancellation


**Fixed**
  * BTC UTXO batch fallback — on DB error, falls back to per-item lookup instead of dropping sweep detections
  * `Stop()` now unblocks correctly by listening on both context and stop channel
  * BTC unauthenticated RPC nodes filtered out for remote connections
  * Empty batch returns consistent empty slice instead of nil for JSON safety


### 
March 19, 2026
#### 
PayRam Frontend `v0.4.1`
**Fixed**
  * Remove authenticated config API call from public payments page to prevent auth errors
  * Use plain axios (unauthenticated) for `reportMissedDeposit` on public payments page


#### 
PayRam Frontend `v0.4.0`
**Added**
  * Default configuration integration for dynamic backend and wallet URLs
  * Unified page headers with `PageHeader` component across all screens
  * Sidebar logo now clickable to navigate home
  * RPC pool frontend alignment with updated backend API changes


**UI**
  * Fixed alert bar transparency in page headers
  * UI polish for payment links, chart legends, alert bar, and sponsorship copy
  * Addressed loading flash, overflow, and accessibility issues in RPC pool


**Fixed**
  * Guard against null analytics cells crashing dashboard on login
  * Fix `defaultValue` sync issue in RPC pool settings
  * Update `PAYMENTS_APP_CONFIG` with new backend and web wallet URLs


#### 
PayRam Core `v1.9.1`
**Fixed**
  * BTC batch size reduced to 2 for per-block height updates to improve stability


#### 
PayRam Core `v1.9.0`
**Added**
  * RPC connection pool with health-based routing, priority ranking, and 60 seed nodes across all supported chains
  * RPC node management APIs — create, update, delete, and per-node live connection testing
  * ARM64 Docker build and publish workflow for multi-platform image support
  * Automatic releases and tag builds via CI pipeline
  * Computed `webhookStatus` field in payment search results
  * Deposit sponsorship retry timeout configuration
  * `CONFIRMING` payment status exposed in API; analytics tightened to processed-only deposits
  * Computed `priority` field in RPCNode API response
  * Hash-based RPC node gatekeeper (`ConnectionHash`) to prevent duplicate node registration
  * BTC fallback node support in RPC pool


**Changed**
  * Centralized `BLOCKCHAIN_NETWORK_TYPE` environment reads into `models.GetNetworkType()`
  * Removed redundant `network_type` column from `rpc_nodes` table
  * Chain ID retrieval refactored — TRX JSON-RPC probe separated into a dedicated function
  * Seeder now uses `OnConflict{DoNothing}` for idempotency; syncs non-key fields on duplicate key
  * Batch address checking for ETH/BASE blocks for improved performance
  * Chain ID cached via `sync.Once` for Received events matching


**Fixed**
  * TRX chain ID retrieval — enhanced error handling for unsupported endpoints and improved JSON-RPC probe
  * TRX multi API key support — per-node API key used for gRPC calls instead of single client-level key
  * TRX URL parsing and pool integration
  * TRX timestamp handling
  * RPC pool poisoning from "not found" errors — errors no longer incorrectly evict healthy nodes
  * RPC pool: removed silent `DefaultFreeNodes` fallback to surface configuration issues explicitly
  * Tron node mapping fix — nodes slice initialized to empty instead of nil
  * BTC missed deposit flow improved
  * BTC testnet connectivity fix
  * Sweep retry logic — sweeps no longer incorrectly marked as `not_found` on transient errors
  * Dashboard confirming deposits filter accuracy
  * `FetchTransactionSponsorship` error handling and logging improvements
  * Deposit pipeline stability — prevents silent deposit loss and unsafe height advancement
  * External platform blockchain currency approval logic corrected
  * Chain ID validation skipped on non-connection RPC node updates
  * Signed transaction payload stored for safe re-broadcast on withdrawal failure
  * Race condition and goroutine leak fixes in RPC pool management
  * Worker restart error handling fixed


#### 
PayRam Payments App `v1.2.0`
**Added**
  * Withdraw transactions support
  * Sponsorship calculation endpoint and handler
  * Fiat currency and country data integration
  * Automated CI/CD release pipeline


#### 
PayRam Wallet `v2.4.0`
**Changed**
  * TypeScript migration and ESLint configuration


**Fixed**
  * Improved installation check logic and login redirect on token expiry


### 
March 11, 2026
#### 
PayRam Frontend `v0.3.1`
**Added**
  * Activity Log in settings with breadcrumb navigation
  * Missed payments reporting feature with UI components, validation, and error handling
  * `excludeActionStatusPairs` filter support for activity logs API and hooks
  * `UserMultiSelect` component improvements for activity log filtering


**UI**
  * Quick filter style updates with high value filter option removed


**Fixed**
  * Update `WEB_WALLET_URL` in `PAYMENTS_APP_CONFIG` to new production URL
  * Handle 403 Forbidden separately from 401 to prevent unintended logout
  * Update activity log API routes for correctness


#### 
PayRam Core `v1.8.3`
**Added**
  * Polygon listener and broadcast processor registered in system service
  * Webhook retry mechanism with exponential backoff — failed webhook deliveries are automatically retried at 30m, 1h, 2h, 4h, 8h, 24h, and 48h intervals before being marked as failed; retry intervals are configurable via system configuration


**Fixed**
  * BTC missed deposit flow — improved handling in BTC client
  * Sweep approval: temporarily disabled fee transfer and signature broadcasting in run method


#### 
PayRam Payments App `v1.1.0`
**Changed**
  * Country selector and default payment method configuration


**Fixed**
  * Card onramp parameter handling improvements


### 
March 5, 2026
#### 
PayRam Core `v1.8.2`
**Fixed**
  * Polygon mainnet RPC connectivity


#### 
PayRam Payments App `v1.0.0`
**Added**
  * Address book service with Ethereum address validation and normalization
  * Sponsorship calculation logic with user payable amount computation
  * Network fee support for payment calculations


### 
March 1, 2026
#### 
PayRam Core `v1.8.1`
**Fixed**
  * Batch DB query for calldata address checking to fix slow block processing
  * Nil guard for `IdentifyOurAddresses` to prevent panic
  * Error logging in `identifyOurAddresses` for silent DB failures
  * Remove `MaxBlocksPerBatch` cap in polling to eliminate inter-batch sleep
  * Prevent genuine deposits from being marked stale on transient RPC errors
  * Log error from `MarkStaleConfirmingDeposits` instead of discarding


### 
February 28, 2026
#### 
PayRam Frontend `v0.3.0`
**Added**
  * OnRamp Payments: new `OnrampPaymentsScreen` component integrated into OnrampPayments page
  * `ErrorBoundary` for `OnrampPaymentsScreen` to handle rendering errors gracefully
  * Confirmation state logic with debug mode and animated transitions for payment flows
  * Legacy QR toggle with improved dropdown overflow handling and payment UI enhancements
  * PayRam logo embedded in QR codes
  * Restart Nodes button in integrations settings
  * Refresh icon added to icon components
  * Configure MCP nav item with icons in sidebar


**Changed**
  * Rolled back Next.js 15 to 14 for stability
  * Upgraded CSS and UI dependencies to latest compatible versions
  * Cleaned up global CSS, removed redundant configs and duplicate imports
  * Refactored icon imports and added new OnrampPayments API


**UI**
  * Global design unification — slate color palette, stat strip, settings and payments redesign
  * Dashboard design audit — slate color scheme, table redesign, mobile filters, chart theming
  * Redesigned dashboard metric cards and updated sidebar color theme
  * Mobile hamburger menu, neon green theme, and dashboard polish
  * Instant sidebar highlight on navigation click
  * Fixed dropdown flash by defaulting to desktop positioning
  * Restored credit card icon next to Cards payment method label
  * Aligned Crypto icon layout to match Cards payment method
  * Settings list layout, sweep-in header and info block reorder


**Fixed**
  * Update wallet URL to production domain
  * Handle 403 Forbidden separately from 401 to prevent unintended logout
  * Prevent automatic logout on transient errors during token refresh
  * Improve logic to check availability of USDC token and BASE blockchain in ChannelSelector
  * Remove duplicate blockchain case showing incorrect card icons
  * Add QR code containers to prevent SVG overflow and fix wallet chain detection race condition
  * Revert build optimizations and remove deprecated Next.js 15 config


#### 
PayRam Core `v1.8.0`
**Added**
  * Deposit confirming state support — frontend can now track confirmation progress before deposits are fully confirmed
  * Blockchain node validation with mainnet detection (`IsMainnet` method)
  * Support for missed deposit webhook approval workflow


**Changed**
  * Consolidated webhook processing into single method to prevent duplicate webhook sends
  * Improved OnramperPayments API with better pagination, date filtering, and sorting validation
  * Refactored blockchain client methods for consistency (`ChainIDUint64` renamed to `GetChainID`)
  * Standardized error responses with correct HTTP status codes


**Fixed**
  * Context deadline/cancellation handling in blockchain processors
  * `EnsureTxConfirmed` polling behavior on `NotFound` status
  * TRX sweep transaction field population (Token/From/To/Amount/EventType)
  * BTC sweep UTXO processing to include "confirming" status
  * Analytics graph colors for New/Recurring metrics
  * Payment channel seeder to set Payments App status to active


### 
February 17, 2026
#### 
PayRam MCP Server `v1.1.0`
**Added**
  * Headless setup guide retrieval tool with formatted checklist
  * Agent onboarding skill for automated deployment
  * Analytics references integrated across all existing skills
  * Google Analytics integration on MCP landing page


**Changed**
  * Renamed headless setup to agent onboarding for clarity


**UI**
  * Integration card layout split into 2-column grid


### 
February 14, 2026
#### 
PayRam Frontend `v0.2.8`
**Added**
  * Added Payments App Channel
  * Update Payments Page to support Payments App


**Fixed**
  * Payments Page UI fixes


#### 
PayRam Core `v1.7.9`
**Added**
  * Integration of Payments App


### 
February 10, 2026
#### 
PayRam Frontend `v0.2.7`
**Added**
  * Payments page Disclaimer


**Fixed**
  * QR code styles and UI improvements
  * Recommended token fix
  * Dashboard UI fixes


#### 
PayRam Core `v1.7.8`
**Added**
  * Tracking of user activity in the dashboard
  * Improved polling logic for the blockchain network processors


### 
January 15, 2026
#### 
PayRam Frontend `v0.2.6`
**Added**
  * Added support for Polygon


**Fixed**
  * Recommended token fix in payments page


#### 
PayRam Core `v1.7.7`
**Added**
  * Polygon integration


**Fixed**
  * Minor bug fixes


### 
January 6, 2026
#### 
PayRam Frontend `v0.2.5`
**Fixed**
  * Add disclaimer text regarding PayRam software usage and liability
  * Add disclaimer text regarding software usage and liability in PaymentScreen


#### 
PayRam Core `v1.7.6`
**Fixed**
  * Bug fix for deposits coming through smart contracts
  * Improvement in Tron sweep


### 
December 26, 2025
#### 
PayRam Frontend `v0.2.4`
**Fixed**
  * TRON QR scan fix
  * Update precision of amount on scanning QR code on Payments Page
  * Filter inactive recipient while creating Payout


#### 
PayRam Core `v1.7.5`
**Fixed**
  * Fix for JWT token based authentication
  * Minor fix in Ethereum blockchain listener


### 
December 9, 2025
#### 
PayRam Frontend `v0.2.3`
**Added**
  * Payment channels (TransFi)
  * Added support for JWT based authentication


#### 
PayRam Core `v1.7.4`
**Added**
  * JWT token based authentication for all the dashboard APIs
  * Swagger documentation for all APIs


### 
November 15, 2025
#### 
PayRam Core `v1.7.0`
**Added**
  * Support for smart contract ETH deposits (e.g. deposits from Coinbase)


### 
November 11, 2025
#### 
PayRam Frontend `v0.2.2`
**Added**
  * Merchant payout: merchant can create a payout request


**Fixed**
  * Minor bug fixes and performance improvements


#### 
PayRam Core `v1.6.9`
**Added**
  * APIs for merchant payout (withdrawal)


### 
April 18, 2024
#### 
PayRam Core `v1.2.6`
**Added**
  * APIs to add member
  * APIs to add roles
  * APIs to add permissions
  * APIs to assign roles to members
  * API for signing authentication
  * APIs to add permissions to roles
  * USD adjustment factor of 2%


### 
April 10, 2024
#### 
PayRam Core `v1.2.5`
**Fixed**
  * Removed unwanted log
  * Added defer function to avoid nil pointer error


#### 
PayRam Core `v1.2.4`
**Fixed**
  * Added defer to handle abrupt termination of webhook job due to error at network layer


#### 
PayRam Core `v1.2.3`
**Added**
  * Support for notifying customer through email upon BTC credits
  * Added necessary logs
  * Updated event consumer library


**Fixed**
  * Fixed few bugs related to transaction which was causing database locking


### 
April 9, 2024
#### 
PayRam Core `v1.2.2`
**Added**
  * Support to add multiple platforms for a merchant
  * Migration to add platform table and updates in the database tables
  * Code refactored
  * Payment request API no-ok response structured


### 
April 5, 2024
#### 
PayRam Core `v1.2.1`
**Added**
  * Support for Tron listening
  * Change in routes and handlers for admin APIs to follow REST API guidelines
  * Code refactored


### 
March 29, 2024
#### 
PayRam Core `v1.2.0`
**Added**
  * Feature to send email to merchant on payment request
  * Added open source event emitter library
  * Added open source event consumer library


### 
March 19, 2024
#### 
PayRam Core `v1.1.6`
**Added**
  * Changed USD amount adjustment factor from 0.988 to 0.984
  * Refactored the code
  * Removed unwanted comments


### 
March 15, 2024
#### 
PayRam Core `v1.1.5`
**Added**
  * Accounting processor for Bitcoin sweep (withdrawal)
  * Updated go.mod and go.sum (showing vulnerability in one of the libraries)


### 
March 14, 2024
#### 
PayRam Core `v1.1.4`
**Added**
  * Audit processor for Bitcoin sweep (withdrawal)
  * Changed USD amount adjustment factor from 0.995 to 0.988
  * Updated go.mod and go.sum


### 
March 12, 2024
#### 
PayRam Core `v1.1.3`
**Added**
  * Modified withdraw API to take withdraw hash in param rather than JSON params


### 
March 9, 2024
#### 
PayRam Core `v1.1.2`
**Fixed**
  * Removed unwanted webhook call for cancelled payments in create payment request API call


#### 
PayRam Core `v1.1.1`
**Added**
  * Restructured and added few test cases along with makefile
  * Separate webhook processor for retrying failed webhooks
  * APIs for BTC sweeper (withdrawal)
  * Removed unwanted logs
  * Migration to copy deposits to `withdra_deposits` table for sweeping
  * Migration to mark all cancelled payment requests webhook status to received
  * Migration to add two more tables


**Fixed**
  * Multiple bug fixes in the code while testing


### 
March 3, 2024
#### 
PayRam Core `v1.1.0`
**Added**
  * Support to pay using Bitcoin
  * Bitcoin listener can be run as a separate job
  * Created README.md file with installation, configuration and usage details


**Fixed**
  * Error in Ether and ERC20 subscription stops abruptly


### 
February 24, 2024
#### 
PayRam Core `v1.0.8`
**Added**
  * Welcome message in the home page


#### 
PayRam Core `v1.0.7`
**Fixed**
  * Small bug fix — added missed return statement in payment request API for all users when it is a pre-prod server


### 
February 23, 2024
#### 
PayRam Core `v1.0.6`
**Added**
  * Added code to copy `created_at` and `updated_at` in DB migration


#### 
PayRam Core `v1.0.3`
**Fixed**
  * Bug fix in URL configuration


#### 
PayRam Core `v1.0.2`
**Fixed**
  * Bug fix


#### 
PayRam Core `v1.0.1`
**Fixed**
  * Bug fix


#### 
PayRam Core `v1.0.0`
**Added**
  * First release with new architecture


[PreviousImportant Linkschevron-left](https://docs.payram.com/support/important-links)
Last updated 12 days ago
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
