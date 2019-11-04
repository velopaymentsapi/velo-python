# PaymentResponseV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** |  | 
**payee_id** | **str** |  | 
**payor_id** | **str** | Deprecated in v2.16. Will be populated with submitting payor ID until removed in a later release. | 
**payor_name** | **str** |  | [optional] 
**quote_id** | **str** |  | 
**source_account_id** | **str** |  | 
**source_account_name** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**source_amount** | **int** |  | [optional] 
**source_currency** | [**PaymentAuditCurrencyV4**](PaymentAuditCurrencyV4.md) |  | [optional] 
**payment_amount** | **int** |  | 
**payment_currency** | [**PaymentAuditCurrencyV4**](PaymentAuditCurrencyV4.md) |  | [optional] 
**rate** | **float** |  | [optional] 
**inverted_rate** | **float** |  | [optional] 
**submitted_date_time** | **datetime** |  | 
**status** | **str** |  | 
**funding_status** | **str** |  | 
**routing_number** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**iban** | **str** |  | [optional] 
**payment_memo** | **str** |  | [optional] 
**filename_reference** | **str** |  | [optional] 
**individual_identification_number** | **str** |  | [optional] 
**trace_number** | **str** |  | [optional] 
**payor_payment_id** | **str** |  | [optional] 
**payment_channel_id** | **str** |  | [optional] 
**payment_channel_name** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**rails_id** | **str** |  | 
**country_code** | **str** |  | [optional] 
**events** | [**list[PaymentEventResponseV4]**](PaymentEventResponseV4.md) |  | 
**return_cost** | **int** |  | [optional] 
**return_reason** | **str** |  | [optional] 
**payout** | [**PaymentResponseV4Payout**](PaymentResponseV4Payout.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


