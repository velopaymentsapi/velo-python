# PaymentV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The id of the payment | 
**remote_id** | **str** | The remoteId supplied by the payor that identifies the payee | [optional] 
**currency** | **str** | The currency that the payment was made in | [optional] 
**amount** | **int** | The amount of the payment in minor units | [optional] 
**source_account_name** | **str** | The identifier of the source account to debit the payment from | [optional] 
**payor_payment_id** | **str** | A reference identifier for the payor for the given payee payment | [optional] 
**payment_memo** | **str** | &lt;p&gt;Any value here will override the memo value in the parent payout&lt;/p&gt; &lt;p&gt;This should be the reference field on the statement seen by the payee (but not via ACH)&lt;/p&gt;  | [optional] 
**payee** | [**PayoutPayeeV3**](PayoutPayeeV3.md) |  | [optional] 
**withdrawable** | **bool** | Can this paynent be withdrawn | [optional] 
**status** | **str** | Current status of payment. One of the following values: SUBMITTED, ACCEPTED, REJECTED, WITHDRAWN, RETURNED, AWAITING_FUNDS, FUNDED, UNFUNDED, CANCELLED, BANK_PAYMENT_REQUESTED | [optional] 
**transmission_type** | **str** | &lt;p&gt;The transmission method of the payment.&lt;/p&gt; &lt;p&gt;Valid values for transmissionType can be found attached to the Source Account&lt;/p&gt;  | [optional] 
**remote_system_id** | **str** | &lt;p&gt;The identifier for the remote payments system if not Velo&lt;/p&gt;  | [optional] 
**payment_metadata** | **str** | &lt;p&gt;Metadata about the payment that may be relevant to the specific rails or remote system making the payout&lt;/p&gt; &lt;p&gt;The structure of the data will be dictated by the requirements of the payment rails&lt;/p&gt;  | [optional] 
**auto_withdrawn_reason_code** | **str** | Populated only if the payment was automatically withdrawn during instruction for being invalid | [optional] 
**rails_id** | **str** | Indicates the 3rd party system involved in making this payment | [optional] 
**transaction_id** | **str** | The id of the transaction associated with this payment if there was one | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


