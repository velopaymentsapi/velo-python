# PaymentInstructionV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_id** | **str** | Your identifier for the payee | 
**currency** | **str** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**amount** | **int** | &lt;p&gt;Amount to send to Payee&lt;/p&gt; &lt;p&gt;The maximum payment amount is dependent on the currency&lt;/p&gt;  | 
**payment_memo** | **str** | &lt;p&gt;Any value here will override the memo value in the parent payout&lt;/p&gt; &lt;p&gt;This should be the reference field on the statement seen by the payee (but not via ACH)&lt;/p&gt;  | [optional] 
**source_account_name** | **str** | Must match a valid source account name belonging to the payor. Exactly one of sourceAccountName or transactionId is required. | [optional] 
**transaction_id** | **str** | Must match a valid transaction id previously created by the payor. Exactly one of sourceAccountName or transactionId is required. | [optional] 
**payor_payment_id** | **str** | A reference identifier for the payor for the given payee payment | [optional] 
**transmission_type** | **str** | &lt;p&gt;Optionally choose a specific transmission method for the payment.&lt;/p&gt; &lt;p&gt;Valid values for transmissionType can be found attached to the Source Account&lt;/p&gt;  | [optional] 
**remote_system_id** | **str** | &lt;p&gt;The identifier for the remote payments system if not Velo&lt;/p&gt; &lt;p&gt;Should only be used after consultation with Velo Payments&lt;/p&gt;  | [optional] 
**payment_metadata** | **str** | &lt;p&gt;Metadata about the payment that may be relevant to the specific rails or remote system making the payout&lt;/p&gt; &lt;p&gt;The structure of the data will be dictated by the requirements of the payment rails&lt;/p&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


