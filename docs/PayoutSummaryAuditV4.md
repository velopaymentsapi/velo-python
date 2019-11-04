# PayoutSummaryAuditV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** |  | 
**payor_id** | **str** | Deprecated in v2.16. Will be populated with submitting payor ID until removed in a later release. | [optional] 
**status** | [**PayoutStatusV4**](PayoutStatusV4.md) |  | 
**date_time** | **datetime** |  | [optional] 
**submitted_date_time** | **str** |  | 
**instructed_date_time** | **str** |  | [optional] 
**withdrawn_date_time** | **datetime** |  | [optional] 
**total_payments** | **int** |  | [optional] 
**total_incomplete_payments** | **int** |  | [optional] 
**total_returned_payments** | **int** |  | [optional] 
**source_account_summary** | [**list[SourceAccountSummaryV4]**](SourceAccountSummaryV4.md) |  | [optional] 
**fx_summaries** | [**list[FxSummaryV4]**](FxSummaryV4.md) |  | [optional] 
**payout_memo** | **str** |  | [optional] 
**payout_type** | [**PayoutTypeV4**](PayoutTypeV4.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


