<!-- Source: https://docs.neox.vn/docs/collections/integration/api-upload-kyc-file -->

  * This is the API used to upload KYC files
  * API:
    * Path: _v2/col/files/upload_
    * Method: POST
    * Request: body, form-data


**Request Parameter**
Parameter
Data Type
Required
Description
file
File
File upload
**Response Data**
Parameter
Data Type
Descriptions
code
Number
Error code, refer to .
message
String
Error description.
data
Object
Refer to 
#### 
UploadFileResponse
Parameter
Data Type
Description
fileName
String
The name of the file which is uploaded
path
String
The path to the file
[PreviousAPI authenPlatformchevron-left](https://docs.neox.vn/docs/collections/integration/api-authenplatform)[NextAPIs for virtual accounts managementchevron-right](https://docs.neox.vn/docs/collections/integration/virtual-accounts)
Last updated 2 years ago
Was this helpful?
