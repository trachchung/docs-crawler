<!-- Source: https://docs.payram.com/onboarding-guide/hot-wallet-setup -->

## 
**Prerequisites**
Before setting up a hot wallet, ensure the following steps are completed:
  * Install the PayRam server and complete the setup.
  * Successfully configure the blockchain node where you will accept payments.
  * Verify that your wallets are set up and ready to receive payments.


## 
Understanding key concepts
Before proceeding with the setup steps, please ensure you are familiar with the following concepts, as they are important for managing your wallets effectively:
### 
**Hot wallet**
A hot wallet is the wallet used to cover transaction fees (gas) when sweeping funds from deposit wallets to the cold wallet. Because blockchain transactions require gas, the hot wallet holds the funds needed to pay these fees and enable transfers during the sweep process. Hot wallets are EOA (Externally Owned Account) wallets.
circle-info
**NOTE****: It is important to always maintain a minimum balance in the hot wallet, otherwise sweep operations will fail**.
### 
**SmartSweep**
The **Smart-sweep** feature helps you automatically move funds from your customer deposit wallets to your main wallet. This reduces manual transfers and ensures funds are consolidated efficiently. Our objective is to simplify daily operations while keeping security on top. For most blockchains, this is done with a family of smart contracts, such that you don’t have to expose keys to sweep funds while PayRam takes care of all the orchestration.
#### 
SmartSweep eligibility
To enable smart-sweeps, a customer's deposit wallet must first meet a **one-time minimum balance requirement**.
  * When this balance is reached, PayRam deploys a **smart wallet contract** to the blockchain.
  * If the balance is not reached, the wallet remains **dormant** and no sweeps will occur.
  * Also note, you can configure these default requirements; the default is $5 USD worth of assets.


#### 
How SmartSweep works
Once a wallet is activated, PayRam can sweep funds automatically based on three configurable settings:
  1. **Amount:** Smart-sweep is triggered when either,
     * An individual deposit wallet’s balance reaches the set amount, or,
     * The total balance across multiple wallets in a batch reaches the set amount.
  2. **Address count:** The sweep occurs after a set number of deposit addresses have received funds.
  3. **Time:** The sweep occurs after a set time period has elapsed.


## 
Hot wallet configuration 
You only need to add hot wallets for the following blockchains 
  * Tron
  * EVM Family


Tron
EVM Family
### 
**Step 1**
  * Select Wallet Management to expand the section, and then select Hot Wallet. From here, you can manage your hot wallets.


### 
Step 2 
  * Now click on Add button on Tron section


### 
Step 3 
  * Select the **Add** button. A pop-up screen appears.
  * In the pop-up screen, you see two options: **Add an existing wallet** or **Create a new wallet**.
    1. If this is your first time, the **Create a new wallet** option is disabled.
    2. Select **Add an existing wallet**.
    3. Select **Continue to add hot wallet**.


### 
Step 4
  * Enter the private key of one of your Tron wallets. Make sure the wallet has enough funds to cover transaction fees so the sweep mechanism works correctly.


### 
Step 5
  * After you enter the private key, select Add Wallet. This adds the wallet as the hot wallet for the Tron blockchain.


  * You have now set up the hot wallet for Tron. When you receive deposits on the Tron chain to your deposit addresses, this hot wallet pays the gas fees for sweeping funds to your cold wallet address.


circle-info
**Note** : In the EVM family, configuring an Ethereum hot wallet covers all networks in the family. In this case, Base, Polygon, and Ethereum.
### 
**Step 1**
  * Select Wallet Management to expand the section, and then select Hot Wallet. From here, you can manage your hot wallets.


### 
Step 2 
  * Now click on Add button on EVM Family section


### 
Step 3 
  * Select the **Add** button. A pop-up screen appears.
  * In the pop-up screen, you see two options: **Add an existing wallet** or **Create a new wallet**.
    1. If this is your first time, the **Create a new wallet** option is disabled.
    2. Select **Add an existing wallet**.
    3. Select **Continue to add hot wallet**.


### 
Step 4
  * Enter the private key of one of your EVM wallets. Make sure the wallet has enough funds to cover transaction fees so the sweep mechanism works correctly.


### 
Step 5
  * After you enter the private key, select Add Wallet. This adds the wallet as the hot wallet for the EVM blockchain.


  * You have now set up the hot wallet for EVM Family. When you receive deposits on the EVM chain to your deposit addresses, this hot wallet pays the gas fees for sweeping funds to your cold wallet address.


You’ve successfully completed the hot wallet setup for both the EVM Family and Tron, which enables smart sweeping. If you are also receiving payments in BTC, note that the sweeping process works slightly differently. You can learn more about it [here].
[PreviousTesting Payment Linkschevron-left](https://docs.payram.com/onboarding-guide/testing-payment-links)[NextFunds Sweepingchevron-right](https://docs.payram.com/onboarding-guide/funds-sweeping)
This site uses cookies to deliver its service and to analyze traffic. By browsing this site, you accept the [privacy policy](http://payram.com/privacy-policy).
close
AcceptReject
