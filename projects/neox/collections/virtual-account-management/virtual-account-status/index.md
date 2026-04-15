<!-- Source: https://docs.neox.vn/docs/collections/virtual-account-management/virtual-account-status -->

### 
**Sequence Diagram**
**Event data**
Parameter
Data Type
Description
type
String
ACCOUNT_STATUS
merchantCode
String
Merchant Code
requestId
String
The requestId when creating virtual account.
virtualAccountRequestId
String
The ID of seller/business is provided by merchant.
bankAccountNumber
String
Virtual Account number.
accountName
String
Virtual Account name.
accountAddress
String
Virtual Account address.
bankId
String
The bank swiftcode of virtual account.
bankName
String
The bank name of virtual account.
qrText
String
Napas QR Code plain data for virtual account.
status
String
Virtual account active status, include: ACTIVE: Virtual account has been actived and can be used. INACTIVE: Virtual account has been inactived and can not be used.
authorizeStatus
String
Virtual account authorize status, Include: UNAUTHORIZED: KYC/KYB documents for VA were not uploaded. PENDING: KYC/KYB documents for VA were uploaded, waiting to verify. AUTHORIZED: KYC/KYB documents for VA have been approved. REJECTED: KYC/KYB documents for VA have been rejected.
serviceInfomation
Object
Refer to [ServiceInformationData.arrow-up-right](https://github.com/neopayvn/neox-gitbook-documents-v1/blob/main/collections/virtual-account-management/api-upload-kyc-file.md#uploadfileresponse)
note
String
Note for current virtual account.
createdAt
Datetime String (ISO 8601)
Record created time
updatedAt
Datetime String (ISO 8601)
Record last updated time
secureHash
String
(Base64)
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the Collection service menu)
### Sample data
Copy
```
  "type": "ACCOUNT_STATUS",
  "merchantCode": "MSFEAF",
  "requestId": "d7fd1438-1c30-46c9-8ba1-bceeafc5198a",
  "virtualAccountRequestId": "4c3ad2bd-a910-4c9b-96ca-77fd46e69239",
  "bankAccountNumber": "M9629245",
  "accountName": "YHTEACR1",
  "accountAddress": "48172 Myrtis Views",
  "bankId": "VTCBVNVX",
  "bankName": "Vietnam Technological and Commercial Joint stock Bank",
  "qrText": "00020101021238520010A000000727012200069704070108M96292450208QRIBFTTA53037045802VN62090805NEO4563040CA8",
  "status": "ACTIVE",
  "authorizeStatus": "UNAUTHORIZED",
  "serviceInformation": {
    "id": "4953df2a-0477-44ac-b615-88aea5eb9070",
    "code": "AMD",
    "desc": "portals",
    "groupId": "Garden"
  "note": "",
  "createdAt": "2025-04-23T14:43:06.883Z",
  "updatedAt": "2025-04-23T14:55:58.497Z",
  "secureHash": "1l5kbr2tzqsAwPTq+0Ol8y4TRNReld8gamrp2KPevQc="

```

With the secretKey "SOME_secret_123", the string used to create secureHash will be:
Copy
```
48172 Myrtis ViewsYHTEACR1UNAUTHORIZEDM9629245VTCBVNVXVietnam Technological and Commercial Joint stock Bank2025-04-23T14:43:06.883ZMSFEAF00020101021238520010A000000727012200069704070108M96292450208QRIBFTTA53037045802VN62090805NEO4563040CA8d7fd1438-1c30-46c9-8ba1-bceeafc5198aAMDportalsGarden4953df2a-0477-44ac-b615-88aea5eb9070ACTIVEACCOUNT_STATUS2025-04-23T14:55:58.497Z4c3ad2bd-a910-4c9b-96ca-77fd46e69239SOME_secret_123
```

[PreviousVirtual Accountchevron-left](https://docs.neox.vn/docs/collections/virtual-account-management/virtual-account)[NextWebhookchevron-right](https://docs.neox.vn/docs/collections/virtual-account-management/webhook)
Last updated 9 months ago
Was this helpful?
