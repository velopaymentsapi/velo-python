# SubmitPayoutV3Request


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payor_id** | **str** | Deprecated in v2.16. Any value supplied here will be ignored. | [optional] 
**payout_from_payor_id** | **str** | The id of the payor whose source account(s) will be debited. payoutFromPayorId and payoutToPayorId must be both supplied or both omitted. | [optional] 
**payout_to_payor_id** | **str** | The id of the payor whose payees will be paid. payoutFromPayorId and payoutToPayorId must be both supplied or both omitted. | [optional] 
**file** | [**[PaymentInstructionV3]**](PaymentInstructionV3.md) | Create a new payout from a CSV source file and return a location header with a link to get the payout | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


