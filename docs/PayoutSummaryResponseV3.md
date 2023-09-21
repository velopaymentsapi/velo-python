# PayoutSummaryResponseV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_id** | **str** | The id of the payout | [optional] 
**status** | **str** | The status of the payout (one of SUBMITTED, ACCEPTED, REJECTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, WITHDRAWN) | [optional] 
**payments_submitted** | **int** | The number of payments that were submitted in the payout | [optional] 
**payments_accepted** | **int** | The number of payments that were accepted in the payout | [optional] 
**payments_rejected** | **int** | The number of payments that were rejected in the payout | [optional] 
**payments_withdrawn** | **int** | The number of payments that were withdrawn in the payout | 
**fx_summaries** | [**list[QuoteFxSummaryV3]**](QuoteFxSummaryV3.md) |  | 
**accounts** | [**list[SourceAccountV3]**](SourceAccountV3.md) |  | 
**accepted_payments** | [**list[AcceptedPaymentV3]**](AcceptedPaymentV3.md) |  | 
**rejected_payments** | [**list[RejectedPaymentV3]**](RejectedPaymentV3.md) |  | 
**schedule** | [**PayoutScheduleV3**](PayoutScheduleV3.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


