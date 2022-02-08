# PayoutSummaryAudit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**PayoutStatus**](PayoutStatus.md) |  | 
**submitted_date_time** | **str** |  | 
**payout_type** | [**PayoutType**](PayoutType.md) |  | 
**payor_name** | **str** |  | 
**payout_id** | **str** |  | [optional] 
**payor_id** | **str** |  | [optional] 
**date_time** | **datetime** |  | [optional] 
**instructed_date_time** | **str** |  | [optional] 
**withdrawn_date_time** | **datetime** |  | [optional] 
**total_payments** | **int** |  | [optional] 
**total_incomplete_payments** | **int** |  | [optional] 
**total_returned_payments** | **int** |  | [optional] 
**total_withdrawn_payments** | **int** |  | [optional] 
**source_account_summary** | [**[SourceAccountSummary]**](SourceAccountSummary.md) |  | [optional] 
**fx_summaries** | [**[FxSummary]**](FxSummary.md) |  | [optional] 
**payout_memo** | **str** |  | [optional] 
**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


