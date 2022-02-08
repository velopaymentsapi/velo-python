# GetPaymentsForPayoutResponseV4Summary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_status** | [**PayoutStatus**](PayoutStatus.md) |  | [optional] 
**submitted_date_time** | **datetime** | The date/time at which the payout was submitted. | [optional] 
**instructed_date_time** | **datetime** | The date/time at which the payout was instructed. | [optional] 
**withdrawn_date_time** | **datetime** |  | [optional] 
**quoted_date_time** | **datetime** | The date/time at which the payout was quoted. | [optional] 
**payout_memo** | **str** | The memo attached to the payout. | [optional] 
**total_payments** | **int** | The count of payments within the payout. | [optional] 
**confirmed_payments** | **int** | The count of payments within the payout which have been confirmed. | [optional] 
**released_payments** | **int** | The count of payments within the payout which have been released. | [optional] 
**incomplete_payments** | **int** | The count of payments within the payout which are incomplete. | [optional] 
**returned_payments** | **int** | The count of payments within the payout which have been returned. | [optional] 
**withdrawn_payments** | **int** | The count of payments within the payout which have been withdrawn. | [optional] 
**payout_type** | [**PayoutType**](PayoutType.md) |  | [optional] 
**submitting** | [**PayoutPayor**](PayoutPayor.md) |  | [optional] 
**payout_from** | [**PayoutPayor**](PayoutPayor.md) |  | [optional] 
**payout_to** | [**PayoutPayor**](PayoutPayor.md) |  | [optional] 
**quoted** | [**PayoutPrincipal**](PayoutPrincipal.md) |  | [optional] 
**instructed** | [**PayoutPrincipal**](PayoutPrincipal.md) |  | [optional] 
**withdrawn** | [**PayoutPrincipal**](PayoutPrincipal.md) |  | [optional] 
**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


