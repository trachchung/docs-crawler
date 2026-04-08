<!-- Source: https://docs.payram.com/faqs/fund-management-faqs -->

### 
Fund Management
  * [What is Smart Consolidation (Fund Sweep)?](https://docs.payram.com/faqs/fund-management-faqs#what-is-smart-consolidation-fund-sweep)
  * [What is a Gas Station in PayRam?](https://docs.payram.com/faqs/fund-management-faqs#what-is-smart-consolidation-fund-sweep)


#### 
What is Smart Consolidation (Fund Sweep)?
**Smart Consolidation** (a.k.a. fund sweep) is PayRam’s on-chain fund aggregation feature. It uses a smart contract (on EVM networks) to automatically collect funds from all your deposit addresses into a single cold wallet you control. To use it, you deploy a “sweep” contract for each supported EVM network, specifying your cold-wallet address as the collector. Then you run two transactions: first **approve** the sweep contract to spend funds (signed with your wallet seed), then **execute** the sweep contract to transfer the balances. These can be done manually or scheduled periodically. The PayRam docs outline these steps – deploy the sweep contract, provide the collector address, approve the contract, and then execute the sweep. In summary, Smart Consolidation automates gathering all crypto from customer deposit addresses into one wallet for easier management.
#### 
What is a Gas Station in PayRam?
A **Gas Station** in PayRam is a dedicated wallet funded with native cryptocurrency to pay blockchain transaction fees (gas). For example, an ETH Gas Station holds Ether, a TON Gas Station holds TON, etc. While normal deposit processing doesn’t require a Gas Station, features like smart sweeps **do**. Whenever PayRam needs to deploy contracts, approve the sweep contract, or execute a fund sweep, the Gas Station wallet provides the gas fees. If the Gas Station runs out of funds for a given chain, those transactions will fail. Therefore, you should **top up your Gas Station wallet regularly** with enough native tokens. In practice, deploy one Gas Station per protocol and ensure it has enough balance to cover operations like contract deployment, approval, sweeping, withdrawals, or refunds.
[PreviousGeneral FAQ'schevron-left](https://docs.payram.com/faqs/general-faqs)[NextReferral FAQ'schevron-right](https://docs.payram.com/faqs/referral-faqs)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
