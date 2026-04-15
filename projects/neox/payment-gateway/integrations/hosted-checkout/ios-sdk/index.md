<!-- Source: https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/ios-sdk -->

## 
IOS SDK for NeoX Payment Gateway
**Use**
Copy
```
importSwiftUI
importNeoPaySDK
structPayment:View {
@Environment(\.presentationMode)var presentationMode: Binding<PresentationMode>
var method: String
@Bindingvar showingAlert:Bool
@Bindingvar alert:String
var amount: Int64
var body: some View {
let request =NeoRequest(
            neo_MerchantCode:"HUYEN1",
            neo_PaymentMethod:self.method,
            neo_Amount: amount,
            neo_MerchantTxnID:"T"+String(Int.random(in:0..<9999)),
            neo_OrderID:"DH"+String(Int(Date().timeIntervalSince1970)),
            neo_OrderInfo:"123",
            secureHash:"123456", 
            neo_ENV: .uat
let customHeader =NeoCustomHeader()
let customButton =NeoCustomButton(
//            title: "Thanh toán",
//            textColor: "#fff",
//            background: "blue"
let params =NeoParams(request: request,  backHandler:{
self.presentationMode.wrappedValue.dismiss()
}, customHeader: customHeader,customButton: customButton){ success, failure in
iflet success = success {
print("success  \(success)")
iflet failure = failure {
print("failure  \(failure)")
VStack{
NeoSDKView(params:params)
}.hiddenNavigationBarStyle()

```

Swift
Objective-C
Copy
```
import SwiftUI 
import NeoPaySDK
struct Payment: View {
    @Environment(\.presentationMode) var presentationMode: Binding<PresentationMode>
    var method: String
    @Binding var showingAlert:Bool
    @Binding var alert:String
    var amount: Int64
    var body: some View {
        let request = NeoRequest(
            neo_MerchantCode: "HUYEN1",
            neo_PaymentMethod: self.method,
            neo_Amount: amount,
            neo_MerchantTxnID:"T" + String(Int.random(in: 0..<9999)),
            neo_OrderID: "DH" + String(Int(Date().timeIntervalSince1970)),
            neo_OrderInfo:"123",
            secureHash: "123456", 
            neo_ENV: .uat
        let customHeader = NeoCustomHeader() 
        let customButton = NeoCustomButton(
//            title: "Thanh toán",
//            textColor: "#fff",
//            background: "blue"
        let params = NeoParams(request: request,  backHandler: {
            self.presentationMode.wrappedValue.dismiss()
        }, customHeader: customHeader,customButton: customButton) { success, failure in
            if let success = success {
                print("success  \(success)")
            if let failure = failure {
                print("failure  \(failure)")
        VStack{
            NeoSDKView(params:params)
        }.hiddenNavigationBarStyle()

```

Copy
```
//  ViewController.m
#import "ViewController.h"
#import "DemoObjectiveC-Swift.h"
@interface ViewController ()
@end
@implementation ViewController
- (void)viewDidLoad {
    [super viewDidLoad];
//    NSLog(@"The code runs through here!");
    // Do any additional setup after loading the view.
- (IBAction)buttonTapped:(id)sender {
    NSInteger *amount = 10000;
    NSTimeInterval timeInSeconds = [[NSDate date] timeIntervalSince1970];
    NSString *timeInSecondsString = [NSString stringWithFormat:@"%d",timeInSeconds];
    NSString *orderID = [@"DH"  stringByAppendingString:timeInSecondsString];
    NSLog(orderID);
    [self displayNeoPaySDKWithAmount:amount orderID:orderID];
@end

```

**displayNeoPaySDKWithAmount (function in SDKView file)**
Copy
```
// SDKView
import Foundation
import NeoPaySDK
import SwiftUI
@objc extension ViewController {
    func displayNeoPaySDK(amount:Int64 = 0,orderID:String){
         let host = UIHostingController(rootView: SDKView(amount:amount,orderID: orderID))
        host.modalPresentationStyle = .fullScreen
        self.present(host, animated: true)
struct SDKView: View{
    public init(amount :Int64 = 0,orderID:String) {
//          print("Vo day may lan")
        self.amount = amount
        self.orderID = orderID
    var amount:Int64 = 0
    var orderID:String = ""
    @Environment(\.dismiss) var dismiss
    @State private var showingAlert = false
    @State private var alert = ""
    var body:some View {
        let request = NeoRequest(
            neo_MerchantCode: "HUYEN1",
            neo_PaymentMethod: "",
            neo_Amount: self.amount,
            neo_MerchantTxnID:"T" + String(Int.random(in: 0..<9999)),
            neo_OrderID:  self.orderID ?? "DH" + String(Int(Date().timeIntervalSince1970)),
            neo_OrderInfo:"123",
            secureHash: "123456",
            neo_ENV: .uat
        let params = NeoParams(request: request,  backHandler: {
            self.dismiss()
        }) { success, failure in
            if let success = success {
                print("success ne \(success)")
                self.showingAlert = true
                self.alert = "Thanh toán thành công"
//                self.dismiss()
            if let failure = failure {
                print("failure ne \(failure)")
                self.showingAlert = true
                self.alert = "Thanh toán thất bại"
        VStack{
            if self.showingAlert == false && self.alert == ""{
                NeoSDKView(params:params)
            else{
                Button(action: {
                            }) {
                                Text("")
                            }.alert(isPresented: $showingAlert) {
                    Alert(title: Text("Thông báo"), message: Text(alert), dismissButton: .destructive(Text("Đồng ý")) {
                        self.dismiss()

```

#### 
Methods
Method
Description
init
Initialize the necessary configurations for the SDK and UI
NeoSDKView**(** params:NeoParams**)**
NeoParams(request,backHandler,customHeader)
Parammetter
Data Type
Description
request
Input params 
customHeader
Allows header customization
customButton
Allows Button customization
## 
NeoRequest 
Parammetter
Data Type
Default Value
Description
neo_MerchantCode
String
Merchant code is provided by NeoX
neo_Currency
String
VND
Transaction currency, VND as default
neo_Locale
String
vi
Language will display on the checkout page. Support: “vi”, “en”.
neo_Version
string
Payment gateway version, “1” as default
neo_PaymentMethod
String
["WALLET", "ATM", "CC", "QR"]
Allows to choose to display direct or list payment channels. If this field is not transmitted, all channels will be displayed.
neo_Amount
number
Payment amount
neo_MerchantTxnID
String
Unique - Transaction ID is provided by merchant
neo_OrderID
String
Oder ID
neo_ENV
Enum
[dev,uat,prod]
Environment
### 
**NeoCustomHeader**
Parammetter
Data Type
Default Value
title
Font
Thanh toán
textColor
Color
Color.black
background
Color
Color.white
font
Font
Font.system(size:20, design: .default)
fontWeight
Font.Weight
Font.Weight.bold
imgLeft
AnyView
AnyView(Image(systemName: "chevron.backward").padding(sides: [.left], value: 16))
### 
NeoCustomButton
Parammetter
Data Type
Default Value
title
String
Thanh toán
textColor
String
#000
background
String
#fed07f
fontSize
String
14px
fontWeight
String
bold
borderRadius
String
25px
**Callback**
Event
Description
onSuccess
The event occurs when payment is successful.
onFailure
The event occurs when payment fails.
**Callback data from onSuccess and onFailure**
Parameter
Data Type
Description
neo_MerchantCode
string
Merchant code is provided by NeoX
neo_Currency
string
Transaction currency, VND as default
neo_Locale
string
Language will display on the checkout page. Support: “vi”, “en”.
neo_Version
string
Payment gateway version, “1” as default
neo_Command
string
“PAY” as default
neo_Amount
string
Payment amount
neo_MerchantTxnID
string
Unique - Transaction ID is provided by merchant
neo_OrderID
string
Oder ID
neo_OrderInfo
string
Oder Information
neo_TransactionID
string
Unique - Transaction ID is generated by the NeoX system, for reconciling.
neo_ResponseCode
string
The error code is returned by NeoX, indicates the transaction result.
neo_ResponseMsg
string
Error description.
neo_CustomerID
string
The customer ID on the merchant system.
neo_ResponseData
string
The data response of customer's payment.
neo_SecureHash
string
Use SHA256 to hash the above parameters (sort the key by Alphabet order) + Secret Key (will be provided by NeoX after actual integration)
[PreviousPlugin/Extenstionchevron-left](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/plugin-extenstion)[NextAndroid SDKchevron-right](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/android-sdk)
Last updated 1 year ago
Was this helpful?
