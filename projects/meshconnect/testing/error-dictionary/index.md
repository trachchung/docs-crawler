<!-- Source: https://docs.meshconnect.com/testing/error-dictionary -->

[Skip to main content](https://docs.meshconnect.com/testing/error-dictionary#content-area)
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


##  Possible Ineligibility Reasons
Here are the reasons why holdings cannot be transferred in some cases.
##  Configure Transfer Errors  
| Error Code  | Description  | Level Found  |  
| --- | --- | --- |  
| NoEligibleNetworks  | None of the networks supported by Source and Target accounts can be used for the transfer. Individual reasons specifying why a particular network cannot be used may vary.  | Holdings  |  
| SymbolDoesNotMatch  | The symbol that was requested for the transfer is different from the holding’s symbol  | Holdings  |  
| NotSupportedForTransferByTarget  | None of the networks for that token are eligible to transfer TO the source. This is often due to the **client** not supporting the token for transfer.  | Holdings  |  
| NotSupportedForTransferBySource  | None of the networks for that token are eligible to transfer FROM the source. This is often due to **Mesh or the integration** not supporting the token for transfer.  | Holdings  |  
| AmountNotSufficient  | The (amount to be transferred + the gas fee) is more than the available balance  | Network  |  
| NoTargetNetworkFound  | Target addresses/institution do not contain the corresponding network, so this network cannot be used for the transfer  | Network  |  
| GasFeeAssetBalanceNotEnough  | The amount of the asset is sufficient, but there’s not enough balance of the gas fee’s asset (e.g. not enough ETH to send USDC)  | Network  |  
##  Preview Transfer Errors
Statuses:
  * Succeeded
  * Failed


###  Error messages (when status = failed)  
| Error Code  | Error Message  |  
| --- | --- |  
| NetworkIdMissing  | (TransferToAddress.NetworkId) field was not provided.  |  
| AddressMissing  | (TransferToAddress.Address) field was not provided.  |  
| SymbolMissing  | (TransferToAddress.Symbol) field was not provided.  |  
| UnsupportedSymbolByNetwork  | Network does not currently support the requested symbol.  |  
| InvalidAddressPattern  | Target address does not match network '0' address pattern.  |  
| NetworkNotFound  | Network not found.  |  
| NetworkDisabled  | Network '0' is currently disabled and cannot be used.  |  
| InsufficientFunds  | Insufficient '0' funds.  |  
| InsufficientFeeFunds  | Insufficient '0' funds for transfer fees.  |  
| EmptyWalletSymbolBalance  | Source wallet '0' balance is empty.  |  
| KycRequired  | The provided '0' account requires KYC to be completed to perform transfers.  |  
| DepositAmountTooLow  | The requested amount is lower than the minimum amount that can be accepted by the target institution.  |  
| WrongPreviewRequestFromAuthTokenMissing  | (PreviewTransferRequest.FromAuthToken) is a mandatory field and should be provided.  |  
| WrongPreviewRequestNoSymbol  | (PreviewTransferRequest.Symbol) is a mandatory field and should be provided.  |  
| WrongPreviewRequestInvalidToAuthToken  | (PreviewTransferRequest.ToAuthToken) is invalid.  |  
| WrongPreviewRequestToData  | Either (PreviewTransferRequest.ToAuthToken) with (PreviewTransferRequest.ToType) or (PreviewTransferRequest.ToAddress) should be provided.  |  
| WrongPreviewRequestAmount  | Both (PreviewTransferRequest.AmountInFiat) and (PreviewTransferRequest.Amount) can not be provided.  |  
| WrongPreviewRequestNoAmount  | Either (PreviewTransferRequest.AmountInFiat) or (PreviewTransferRequest.Amount) should be provided.  |  
| WrongPreviewRequestUnsupportedSymbolBySourceWallet  | Symbol to transfer not supported by the source wallet over the requested network.  |  
| WrongPreviewRequestUnsupportedSymbolByTargetWallet  | Symbol to transfer not supported by the target wallet over the requested network.  |  
| WrongPreviewRequestNetwork  | Requested network is not supported by the source wallet.  |  
| PriceNotFound  | Could not fetch '0' price.  |  
| AmountMoreThanWithdrawMaximum  | Could not preview the transfer. The requested amount (previewRequest.Amount) (requestDto.Request.Symbol) is greater than the maximum allowed amount (minimumMaximumAmount.WithdrawMaximumAmount requestDto.Request.Symbol).  |  
| AmountLessThanWithdrawMinimum  | Could not preview the transfer. The requested amount (previewRequest.Amount) (requestDto.Request.Symbol) is below the minimum allowable threshold (minimumMaximumAmount.WithdrawMinimumAmount requestDto.Request.Symbol).  |  
##  Execute Transfer Errors
Statuses:
  * Succeeded
  * Failed
  * MfaRequired
  * EmailConfirmationRequired
  * DeviceConfirmationRequired
  * MfaFailed
  * AddressWhitelistRequired


###  Error messages (when status = failed)  
| Error Code  | Error Message  |  
| --- | --- |  
| PreviewExpired  | The preview is expired.  |  
| TransferIsRequested  | The transfer is already requested.  |  
| PreviewNotFound  | Could not find the preview.  |  
| AddressNotRegistered  | The target address is not registered.  |  
Was this page helpful?
YesNo
[ Testnets Previous ](https://docs.meshconnect.com/testing/testnets)[Next](https://docs.meshconnect.com/testing/troubleshooting-link)
Ctrl+I
On this page
  * [Possible Ineligibility Reasons](https://docs.meshconnect.com/testing/error-dictionary#possible-ineligibility-reasons)
  * [Configure Transfer Errors](https://docs.meshconnect.com/testing/error-dictionary#configure-transfer-errors)
  * [Preview Transfer Errors](https://docs.meshconnect.com/testing/error-dictionary#preview-transfer-errors)
  * [Error messages (when status = failed)](https://docs.meshconnect.com/testing/error-dictionary#error-messages-when-status-%3D-failed)
  * [Execute Transfer Errors](https://docs.meshconnect.com/testing/error-dictionary#execute-transfer-errors)
  * [Error messages (when status = failed)](https://docs.meshconnect.com/testing/error-dictionary#error-messages-when-status-%3D-failed-2)


Assistant
Responses are generated using AI and may contain mistakes.
