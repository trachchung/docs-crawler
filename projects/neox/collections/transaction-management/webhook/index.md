<!-- Source: https://docs.neox.vn/docs/collections/transaction-management/webhook -->

### 
**Sequence Diagram**
**Event data**
Parameter
Data Type
Description
transId
String
The ID of transaction.
type
String
TRANSACTION
merchantCode
String
Merchant Code
transDate
String
The time of transaction.
virtualAccountRequestId
String
The ID of seller/business is provided by merchant.
virtualAccountId
String
The ID of virtual account.
accountName
String
The account name.
amount
Number
The amount of collection transaction.
note
String
Note.
serviceInformation
Object
Extra data includes "code", "groupId", "desc"
debitorInformation
Object
Debitor info object include: "bankName": Debit fom bank name "bankAccountNumber": Debitor bank account "bankAccountName": Debitor bank account name "bankRemark": Transaction remark received from debitor's bank.
secureHash
String
(Base64)
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the Collection service menu)
### 
Sample data
Copy
```
    "transId": "FT246560944209",
    "type": "TRANSACTION",
    "merchantCode": "UFLIYL",
    "transDate": "2023-10-10T07:06:37.436Z",
    "virtualAccountRequestId": "54f35db9-553b-4078-8271-7863162903c0",
    "virtualAccountId": "NEO0001675",
    "accountName": "HIEP HOANG",
    "amount": 20000,
    "note": "NEO1696918592059",
    "serviceInformation": {
        "code": "GRAB",
        "desc": "testtttt",
        "groupId": "DRIVER"
    "debitorInformation": {
        "bankName": "Simulator connector",
        "bankAccountNumber": "09874732621",
        "bankAccountName": "Simulator account",
        "bankRemark": "691079-CTY TNHH TMDT HIEP HOANG payment for order 123456 NEO188879_NEO0001675"
    "secureHash": "dXNENfQTIa9KgImBXJu2qFRprAcPhYydbBY8AlnmvgY="

```

With the secretKey "SUMTING", the string used to create secureHash will be:
Copy
```
HIEP HOANG20000Simulator account09874732621Simulator connector691079-CTY TNHH TMDT HIEP HOANG payment for order 123456 NEO188879_NEO0001675UFLIYLNEO1696918592059GRABtestttttDRIVER2023-10-10T07:06:37.436ZFT246560944209TRANSACTIONNEO000167554f35db9-553b-4078-8271-7863162903c0SUMTING
```

[PreviousTransaction Managementchevron-left](https://docs.neox.vn/docs/collections/transaction-management)[NextTransaction Status Managementchevron-right](https://docs.neox.vn/docs/collections/transaction-status-management)
Last updated 1 year ago
Was this helpful?
