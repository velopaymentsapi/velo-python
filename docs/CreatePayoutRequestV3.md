# CreatePayoutRequestV3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments** | [**[PaymentInstructionV3]**](PaymentInstructionV3.md) |  | 
**payout_from_payor_id** | **str** | &lt;p&gt;The id of the payor whose source account(s) will be debited&lt;/p&gt; &lt;p&gt;payoutFromPayorId and payoutToPayorId must be both supplied or both omitted&lt;/p&gt;  | [optional] 
**payout_to_payor_id** | **str** | &lt;p&gt;The id of the payor whose payees will be paid&lt;/p&gt; &lt;p&gt;payoutFromPayorId and payoutToPayorId must be both supplied or both omitted&lt;/p&gt;  | [optional] 
**payout_memo** | **str** | &lt;p&gt;Text applied to all payment memos unless specified explicitly on a payment&lt;/p&gt; &lt;p&gt;This should be the reference field on the statement seen by the payee (but not via ACH)&lt;/p&gt;  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


