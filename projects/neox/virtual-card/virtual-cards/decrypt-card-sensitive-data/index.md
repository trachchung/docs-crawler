<!-- Source: https://docs.neox.vn/docs/virtual-card/virtual-cards/decrypt-card-sensitive-data -->

This document explains the **algorithmic process** to decrypt the `cardEncryptedData` object.
## 
1. Hybrid Encryption Structure
The encryption uses a **hybrid approach** :
  * **RSA (asymmetric)** : Protects the AES key, IV, and Auth Tag.
  * **AES-GCM (symmetric)** : Encrypts the actual card data.


## 
2. Decryption Steps
### 
Step 1: RSA Decryption
  * The `encryptedKey` is a base64-encoded string.
  * It contains the AES key, IV, and Auth Tag, all encrypted with the merchant's RSA public key.
  * The private RSA key is used to decrypt `encryptedKey`, yielding a buffer with:
    * **AES Key** : First 32 bytes (256 bits)
    * **IV** : Next 12 bytes (96 bits)
    * **Auth Tag** : Last 16 bytes (128 bits)


### 
Step 2: Extract AES Parameters
  * **AES Key** : Used for AES-256-GCM decryption.
  * **IV (Initialization Vector)** : Required for AES-GCM.
  * **Auth Tag** : Used to verify data integrity in AES-GCM.


### 
Step 3: AES-GCM Decryption
  * The `encryptedData` is a base64-encoded string, encrypted with AES-256-GCM.
  * Using the extracted AES key, IV, and Auth Tag, the data is decrypted.
  * The output is the original card data in JSON string format.


## 
3. Security Notes
  * RSA ensures only the intended recipient can access the AES key.
  * AES-GCM provides both confidentiality and integrity for the card data.


## 
4. Sample codes (in NodeJS)
Copy
```
import * as crypto from "crypto";
import * as fs from "fs";
const PRIVATE_KEY = fs.readFileSync(`path/to/your/private-key.pem`, "utf8");
const AES_KEY_LENGTH = 32; // 256 bits
const IV_LENGTH = 12; // 96 bits
const AUTH_TAG_LENGTH = 16; // 128 bits
function hybridDecrypt(cardEncryptedData) {
  const { encryptedData, encryptedKey } = cardEncryptedData;
  try {
    // 1. RSA Decryption
    const decryptedKeyBuf = crypto.privateDecrypt(
        key: PRIVATE_KEY,
        padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
        oaepHash: "sha256"
      encryptedKey
    // 2. Extract AES Parameters
    const aesKey = decryptedKeyBuf.subarray(0, AES_KEY_LENGTH);
    const iv = decryptedKeyBuf.subarray(AES_KEY_LENGTH, AES_KEY_LENGTH + IV_LENGTH);
    const authTag = decryptedKeyBuf.subarray(-AUTH_TAG_LENGTH);
    // 3. AES-GCM Decryption
    const decipher = crypto.createDecipheriv("aes-256-gcm", aesKey, iv);
    decipher.setAuthTag(authTag);
    let decrypted = decipher.update(encryptedData, "base64", "utf8");
    decrypted += decipher.final("utf8");
    return decrypted;
  } catch (error) {
    console.log(`call to hybridDecrypt failed with error: ${error.message}`);
    return "{}";
// Test with NeoX virtual card encrypted data. Replace with actual encrypted data
const cardEncryptedData = {
  encryptedData:
    "Some encryptedData data here that is base64 encoded",
  encryptedKey:
    "Some encryptedKey data here that is base64 encoded"
const result = hybridDecrypt(cardEncryptedData);
console.log("result", JSON.parse(result));

```

[PreviousWebhookchevron-left](https://docs.neox.vn/docs/virtual-card/virtual-cards/webhook)[NextMerchant Portalchevron-right](https://docs.neox.vn/docs/merchant-portal)
Last updated 10 months ago
Was this helpful?
