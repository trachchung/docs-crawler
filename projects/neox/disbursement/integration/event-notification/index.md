<!-- Source: https://docs.neox.vn/docs/disbursement/integration/event-notification -->

## 
Usage
  * This is the API that the Platform should create to receive notifications of events that occur from NeoX. 
  * Sequence Diagram
    * Notifies about balance amount
    * Notifies about disbursement transaction


## 
API
  * Path: the URL(_https:// <<yourdomain.com/api/notifi>>_) Webhook is created and configured by Platform on Merchant Portal, in the “Disbursement service” menu 
  * Method: POST 
  * Request: Body 


## 
Notification type
### 
**Notifies about balance amount**
Parameter
Data Type 
Description
service 
String 
“ _DISBURSEMENT_ ” 
type 
String 
“ _BALANCE_ ” 
value 
Number 
The current amount. 
time 
String 
The time of the event. 
secureHash 
String 
(Base64) 
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the “Disbursement service” menu) 
### 
**Notifies about disbursement transaction happened**
Parameter
Data Type 
Description
service 
String 
“ _DISBURSEMENT_ ” 
type 
String 
“ _TRANSACTION_ ” 
data 
Object 
Data response, refer to [DisbursementTransactionItem](https://docs.neox.vn/docs/disbursement/integration/response-data-structure)
time 
String 
The time of the event. 
secureHash 
String 
(Base64) 
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the “Disbursement service” menu) 
### 
**Notifies about currency exchanged**
Parameter
Data Type 
Description
service 
String 
“ _DISBURSEMENT_ ” 
type 
String 
“ _EXCHANGE_ ” 
data 
Object 
Data response, refer to 
time 
String 
The time of the event. 
secureHash 
String 
(Base64) 
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (configured on Merchant Portal, in the “Disbursement service” menu) 
[PreviousCurrency conversion APIchevron-left](https://docs.neox.vn/docs/disbursement/integration/currency-conversion-api)[NextResponse Data Structurechevron-right](https://docs.neox.vn/docs/disbursement/integration/response-data-structure)
Last updated 2 years ago
Was this helpful?
