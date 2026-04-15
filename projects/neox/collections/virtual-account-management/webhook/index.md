<!-- Source: https://docs.neox.vn/docs/collections/virtual-account-management/webhook -->

### 
**Sequence Diagram**
### 
**Event data**
Parameter
Data Type
Description
requestId
String
The ID of the request.
type
String
“ _ACCOUNT_ ”
merchantId
String
The ID of merchant.
virtualAccounts
Array
The array contains the list of created virtual accounts.
Refer to below
createdAt
String
The time of creating account.
secureHash
String
(Base64)
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the Collection service menu)
#### 
VirtualAccount
Parameter
Data Type
Description
accountName
String
The ID of seller/business is provided by merchant.
receiver
String
The name of receiver.
bankId
String
The Swift Code of the bank.
bankName
String
Bank name
serviceInfomation
Object
Refer to 
bankAccountNumber
String
The bank account number.
qrText
String
QR Code
virtualAccountRequestId
String
The ID of seller/business is provided by merchant
transferNote
String
Transfer Contents
code
Number
Refer to 
status
String
Status of virtual account creation: SUCCESS FAILED PROCESSING
#### 
Service Information
Parameter
Data Type
Required
Description
code
String (up to 10 latin chars)
Service code which is defined by the merchants. This code will be used to filter the VAs and grouped Reconciliations on Merchant Portal
groupId
String (up to 10 latin chars)
Id of VA group which is defined by the merchants. This id will be used to filter the VAs on Merchant Portal
desc
String (up to 256 latin chars)
Description of VA
### 
Sample data
Copy
```
  "requestId": "63ea2832-8448-4993-8bff-9748cd3aed64",
  "merchantId": "62aa8e8311c8360019132856",
  "type": "ACCOUNT",
  "createdAt": "2023-11-15T02:27:18.241Z",
  "virtualAccounts": [
      "virtualAccountRequestId": "5029e5b0-5824-4a0c-bd7a-808439cced22",
      "bankAccountNumber": "NEO0003044",
      "bankId": "MSCBVNVX",
      "bankName": "Military Commercial Joint stock Bank",
      "transferNote": "NEO1700015238057",
      "receiver": "ACC SBX 001",
      "accountName": "ACC SBX 001",
      "qrText": "00020101021238540010A000000727012400069704220110NEO00030440208QRIBFTTA53037045802VN5911ACC SBX 00162200816NEO17000152380576304FA4E",
      "serviceInformation": {
        "code": "code1",
        "desc": " test",
        "groupId": "group1"
      "code": 1,
      "status": "SUCCESS"
  "secureHash": "vpE2KAJ78GTrIXUkdxp8m3WOeR8rBRPAeth1/mP3sWE="

```

With the secretKey "123", the string used to create secureHash will be:
Copy
```
2023-11-15T02:27:18.241Z62aa8e8311c836001913285663ea2832-8448-4993-8bff-9748cd3aed64ACCOUNTACC SBX 001NEO0003044MSCBVNVXMilitary Commercial Joint stock Bank100020101021238540010A000000727012400069704220110NEO00030440208QRIBFTTA53037045802VN5911ACC SBX 00162200816NEO17000152380576304FA4EACC SBX 001code1 testgroup1SUCCESSNEO17000152380575029e5b0-5824-4a0c-bd7a-808439cced22123
```

[PreviousVirtual Account Statuschevron-left](https://docs.neox.vn/docs/collections/virtual-account-management/virtual-account-status)[NextTransaction Managementchevron-right](https://docs.neox.vn/docs/collections/transaction-management)
Last updated 1 year ago
Was this helpful?
