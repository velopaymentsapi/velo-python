# PayoutSummaryAudit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** |  | [optional] 
**payor_id** | **str** |  | [optional] 
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**date_time** | **datetime** |  | [optional] 
**submitted_date_time** | **str** |  | 
**instructed_date_time** | **str** |  | [optional] 
**withdrawn_date_time** | **datetime** |  | [optional] 
**total_payments** | **int** |  | [optional] 
**total_incomplete_payments** | **int** |  | [optional] 
**total_returned_payments** | **int** |  | [optional] 
**total_withdrawn_payments** | **int** |  | [optional] 
**source_account_summary** | [**list[SourceAccountSummary]**](SourceAccountSummary.md) |  | [optional] 
**fx_summaries** | [**list[FxSummary]**](FxSummary.md) |  | [optional] 
**payout_memo** | **str** |  | [optional] 
**payout_type** | [**PayoutType**](PayoutType.md) |  | 
**payor_name** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


