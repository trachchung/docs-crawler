<!-- Source: https://docs.neox.vn/docs/collections/integration/sftp-upload-document-file-of-collection-transaction -->

  * NeoX will build an SFTP server for the merchant to upload the document file of the collection transaction.
  * The format of file name: _DSTH_[Merchant Code]_[Transaction Code]_[version upload]._
    * [Merchant Code]: is obtained on the Merchant portal, in the _“My Profile”_ menu.
    * [Transaction Code]: is obtained on the Merchant portal, in the _“Collection management”_ menu → _“Transactions management”_ menu.
  * The SFTP server information will be provided to the merchant upon actual connection.
  * Sequence Diagram:


  * The merchant uploads the document file of the transaction via the SFTP protocol (Step1), before NeoX do the settlement (Step 3).


[PreviousEvent Notificationchevron-left](https://docs.neox.vn/docs/collections/integration/event-notification)[NextError Codeschevron-right](https://docs.neox.vn/docs/collections/integration/error-codes)
Last updated 2 years ago
Was this helpful?
