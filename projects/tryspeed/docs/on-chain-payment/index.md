<!-- Source: https://docs.tryspeed.com/docs/on-chain-payment -->

## On-chain payments
Speed provides the essential elements for seamless on-chain transactions. Unlike involving a secondary layer like the Lightning Network, on-chain transactions are broadcasted to the entire network for verification, are public, and can be found on the digital ledger known as the 'blockchain.’
#### [Lifecycle of an on-chain transactionCopied!](https://docs.tryspeed.com/docs/on-chain-payment#lifecycle-of-an-on-chain-transaction)
The steps involved in an on-chain transaction typically include:
  1. **Initiation:** The process begins with a user initiating a transaction, specifying the recipient, amount, and any additional details required.
  2. **Transaction Creation:** A transaction is created, containing information about the sender, receiver, and the amount to be transferred. This transaction is broadcast to the network.
  3. **Validation:** The network's nodes validate the transaction to ensure it adheres to the rules of the blockchain protocol. This involves confirming that the sender has the necessary funds and that the transaction is properly formatted.
  4. **Inclusion in a Block:** Validated transactions are grouped into a block by miners. This block is then added to the blockchain through a process known as consensus, which varies depending on the specific blockchain protocol (e.g., proof-of-work or proof-of-stake).
  5. **Block Confirmation:** The transaction is considered confirmed when the block containing it is added to the blockchain. The number of confirmations required may vary depending on the blockchain and the level of security desired.
  6. **Completion:** Once the transaction is confirmed, it is considered complete, and the recipient can access and utilize the received funds.


#### [How on-chain transactions differ from the lightning/traditional transactionsCopied!](https://docs.tryspeed.com/docs/on-chain-payment#how-on-chain-transactions-differ-from-the-lightning/traditional-transactions)
On-chain transactions can take some time (minutes to hours) for block confirmations. The process involves waiting for block confirmations to validate payments, a duration that can range from minutes to hours.
Importantly, on-chain payments consistently involve higher transaction fees compared to Lightning payments. As a result, on-chain payments are generally recommended for bigger transactions and are not supported for smaller transactions.
In the on-chain method, the payment which is received can be of either two types -
  1. Full Payment: Opting for full payment results in the transaction being marked as paid immediately upon completion, covering the entire invoice amount.
  2. Partial Payments: When customers choose partial payments, the invoice will only be considered paid if the combined value of transactions equals or exceeds the total invoice amount. Upon each payment, customers have the ability to review the breakdown of their payments, including the amount paid and the outstanding balance yet to be settled.


On-chain transactions are typically accessible to anyone with an internet connection, providing global reach.
#### [Benefits of on-chain networkCopied!](https://docs.tryspeed.com/docs/on-chain-payment#benefits-of-on-chain-network)
  1. **Security** : The underlying blockchain protocol provides a strong and well-established security framework, which is used to secure on-chain payments.
  2. **Decentralization:** On-chain transactions directly interact with the blockchain, contributing to the overall decentralization of the network**.**
  3. **Global Accessibility:** Bitcoin transactions can be conducted globally, providing financial services to individuals who may not have access to traditional banking systems.
  4. **Reduced Transaction Costs:** Bitcoin transactions often have lower fees compared to traditional financial systems, especially for international transfers.


# Table of contents
[Lifecycle of an on-chain transaction](https://docs.tryspeed.com/docs/on-chain-payment#lifecycle-of-an-on-chain-transaction)[How on-chain transactions differ from the lightning/traditional transactions](https://docs.tryspeed.com/docs/on-chain-payment#how-on-chain-transactions-differ-from-the-lightning/traditional-transactions)[Benefits of on-chain network](https://docs.tryspeed.com/docs/on-chain-payment#benefits-of-on-chain-network)
/docs/on-chain-payment
