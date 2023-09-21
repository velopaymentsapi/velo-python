# GetPaymentsForPayoutResponseV3Summary

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_status** | **str** | The current status of the payout. One of the following values: ACCEPTED, REJECTED, SUBMITTED, QUOTED, INSTRUCTED, COMPLETED, INCOMPLETE, CONFIRMED, WITHDRAWN | [optional] 
**submitted_date_time** | **datetime** | The date/time at which the payout was submitted. | [optional] 
**instructed_date_time** | **datetime** | The date/time at which the payout was instructed. | [optional] 
**withdrawn_date_time** | **datetime** | The date/time at which the payout was withdrawn. | [optional] 
**payout_memo** | **str** | The memo attached to the payout. | [optional] 
**total_payments** | **int** | The count of payments within the payout. | [optional] 
**confirmed_payments** | **int** | The count of payments within the payout which have been confirmed. | [optional] 
**released_payments** | **int** | The count of payments within the payout which have been released. | [optional] 
**incomplete_payments** | **int** | The count of payments within the payout which are incomplete. | [optional] 
**failed_payments** | **int** | The count of payments within the payout which have failed or been returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


