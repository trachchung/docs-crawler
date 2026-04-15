<!-- Source: https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/android-sdk -->

### 
Before using SDK, these setup must be completed
  * A verified account on NeoX Merchant Portal. Register at this link <https://portal.neopay.vn/merchant/portal/user/register>[arrow-up-right](https://portal.neopay.vn/merchant/portal/user/register).
  * Taking the developer credentials (instruction here).
  * Initialize payment request at order payment step.


### 
Process to integrate NeoX Payment Gateway 
#### 
Implement permissions in AndroidManifest.xml
Copy
```
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <application
        ...
        android:requestLegacyExternalStorage="true"
        ...
    </application>
</manifest>
```

#### 
**Implement NeoX SDK library in app/build.gradle**
Download package here
Copy
```
dependencies {
    implementation(files("libs/neox-release.aar"))
    ...

```

#### 
Method to initialize payment request
Kotlin
Java
Copy
```
import com.android.neox.*
...
class YOUR_ACTIVITY: AppCompatActivity() {
   private lateinit var yourPaymentBtn: Button
   override fun onCreate(savedInstanceState: Bundle?) {
      ...
      yourPaymentBtn.setOnClickListener {
         val paymentRequest = NeoXPaymentRequest(
             neo_ENV = "development environment" // Default is production. Supported sandbox|production. Ex: NeoXEnvironment.SANDBOX.env
             neo_MerchantCode = "merchant code",
             neo_SecureHash = "secret key",
             neo_Amount = "payment amount", // 10000
             neo_PaymentMethod = arrayOf("payment channel"), // Default is all channel. Payment methods WALLET|ATM|CC|QC
             neo_MerchantTxnID = "your transaction id", // size <= 36.
             neo_OrderID = "order_id || order_code",
             neo_OrderInfo = "order description", // size <= 256
             neo_Command = "command", // Supported commands are PAY, QUERY. Default is PAY. 
             neo_Currency = "payment currency", // Supported currencies are VND, USD. Default is VND.
             neo_Locale = "locale", // Supported locales are vi, en. Default is vi,
             neo_Version = "version", // Default is 1.
             neo_ReturnURL = "url address" // URL to return payment result.
         NeoXPaymentHandler.paymentInitialize(this, paymentRequest)
  ...

```

Copy
```
import com.android.neox.*;
...
public class YOUR_ACTIVITY extends AppCompatActivity {
   private Button paymentButton;
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      ...
      paymentButton.setOnClickListener(view -> {
            String[] paymentMethods = {};
            NeoXPaymentRequest paymentRequest = new NeoXPaymentRequest(
                "env", // NeoXEnvironment.SANDBOX.getEnv()
                "merchant_code",
                "secret_key",
                "amount",
                paymentMethods,
                "merchant_txn_id",
                "order_id",
                "order_info",
                "command",
                "currency",
                "locale",
                "version",
                "return_url"
            NeoXPaymentHandler.INSTANCE.paymentInitialize(YOUR_ACTIVITY.this, paymentRequest);
       });
   ...

```

#### 
**Method to listen payment event**
Kotlin
Java
Copy
```
import com.android.neox.*
...
class YOUR_ACTIVITY: AppCompatActivity() {
   ...
   override fun onCreate(savedInstanceState: Bundle?) {
       ...
       NeoXPaymentHandler.setNeoXPaymentListener(object: NeoXPaymentListener {
            override fun onPaymentClose() {
                    // Your implementation
            override fun onPaymentError(result: NeoXPaymentResult) {
                    // Your implementation
            override fun onPaymentSuccess(result: NeoXPaymentResult) {
                    // Your implementation
  ...

```

Copy
```
import com.android.neox.*;
...
public class YOUR_ACTIVITY extends AppCompatActivity {
   ...
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      ...
      NeoXPaymentHandler.INSTANCE.setNeoXPaymentListener(new NeoXPaymentListener() {
            @Override
            public void onPaymentSuccess(@NonNull NeoXPaymentResult neoXPaymentResult) {
                // Your implementation
            @Override
            public void onPaymentError(@NonNull NeoXPaymentResult neoXPaymentResult) {
                // Your implementation
            @Override
            public void onPaymentClose() {
                // Your implementation
       });
   ...

```

#### 
Method to custom Payment Gateway UI
Kotlin
Java
Copy
```
import com.android.neox.*
...
class YOUR_ACTIVITY: AppCompatActivity() {
   ...
   override fun onCreate(savedInstanceState: Bundle?) {
      ...
      with(NeoXPaymentUtils) {
            useNeoXToolbar = false
            finishActivityOnComplete = true
            overridePaymentButton(NeoXPaymentButton(
                label = "Pay now",
                backgroundColor = "#fed07f",
                textColor = "#000",
                fontSize = 16,
                borderRadius = 24
            overridePaymentViewTitles(NeoXTitles(
                paymentGatewayTitle = "NeoX Payment Gateway",
                bankPaymentTitle = "Bank transfer",
                cardPaymentTitle = "ATM/Card payment",
                resultTitle = "Payment result"
  ...

```

Copy
```
import com.android.neox.*;
...
public class YOUR_ACTIVITY extends AppCompatActivity {
   ...
   @Override
   protected void onCreate(Bundle savedInstanceState) {
      ...
      NeoXPaymentUtils.setUseNeoXToolbar(true);
      NeoXPaymentUtils.setFinishActivityOnComplete(true);
      NeoXPaymentUtils.INSTANCE.overridePaymentButton(new NeoXPaymentButton(
          "Pay now", // label
          "#fed07f", // background color
          "#000", // text color
          16, // text size
          24 // border radius
      ));
      NeoXPaymentUtils.INSTANCE.overridePaymentViewTitles(new NeoXTitles(
          "NeoX Payment Gateway",
          "Bank transfer",
          "ATM/Card payment",
          "Payment result"
      ));
   ...

```

[PreviousiOS SDKchevron-left](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/ios-sdk)[NextReact Native SDKchevron-right](https://docs.neox.vn/docs/payment-gateway/integrations/hosted-checkout/react-native-sdk)
Last updated 3 years ago
Was this helpful?
