# PaymentResponseV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | The id of the payment | 
**payee_id** | **str** | The id of the paymeee | 
**payor_id** | **str** | The id of the payor | 
**quote_id** | **str** | The quote Id used for the FX | 
**source_account_id** | **str** | The id of the source account from which the payment was taken | 
**payment_amount** | **int** | The amount which the payee will receive | 
**submitted_date_time** | **datetime** |  | 
**status** | **str** |  | 
**funding_status** | **str** | The funding status of the payment | 
**events** | [**[PaymentEventResponse]**](PaymentEventResponse.md) |  | 
**rails_id** | **str** | The rails ID. Default value is RAILS ID UNAVAILABLE when not populated. | defaults to "RAILS ID UNAVAILABLE"
**payor_name** | **str** | The name of the payor | [optional] 
**source_account_name** | **str** | The name of the source account from which the payment was taken | [optional] 
**remote_id** | **str** | The remote id by which the payor refers to the payee. Only populated once payment is confirmed | [optional] 
**remote_system_id** | **str** | The velo id of the remote system orchestrating the payment. Not populated for normal Velo payments. | [optional] 
**remote_system_payment_id** | **str** | The id of the payment in the remote system. Not populated for normal Velo payments. | [optional] 
**source_amount** | **int** | The source amount for the payment (amount debited to make the payment) | [optional] 
**source_currency** | [**PaymentAuditCurrency**](PaymentAuditCurrency.md) |  | [optional] 
**payment_currency** | [**PaymentAuditCurrency**](PaymentAuditCurrency.md) |  | [optional] 
**rate** | **float** | The FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed | [optional] 
**inverted_rate** | **float** | The inverted FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed | [optional] 
**is_payment_ccy_base_ccy** | **bool** |  | [optional] 
**routing_number** | **str** | The routing number for the payment. | [optional] 
**account_number** | **str** | The account number for the account which will receive the payment. | [optional] 
**iban** | **str** | The iban for the payment. | [optional] 
**payment_memo** | **str** | The payment memo set by the payor | [optional] 
**filename_reference** | **str** | ACH file payment was submitted in, if applicable | [optional] 
**individual_identification_number** | **str** | Individual Identification Number assigned to the payment in the ACH file, if applicable | [optional] 
**trace_number** | **str** | Trace Number assigned to the payment in the ACH file, if applicable | [optional] 
**payor_payment_id** | **str** |  | [optional] 
**payment_channel_id** | **str** |  | [optional] 
**payment_channel_name** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**country_code** | **str** | The country code of the payment channel. | [optional] 
**return_cost** | **int** | The return cost if a returned payment. | [optional] 
**return_reason** | **str** |  | [optional] 
**rails_payment_id** | **str** |  | [optional] 
**rails_batch_id** | **str** |  | [optional] 
**rejection_reason** | **str** |  | [optional] 
**withdrawn_reason** | **str** |  | [optional] 
**withdrawable** | **bool** |  | [optional] 
**auto_withdrawn_reason_code** | **str** | Populated with rejection reason code if the payment was withdrawn automatically at instruct time | [optional] 
**transmission_type** | **str** | The transmission type of the payment, e.g. ACH, SAME_DAY_ACH, WIRE | [optional] 
**payment_tracking_reference** | **str** |  | [optional] 
**payment_metadata** | **str** | Metadata for the payment | [optional] 
**schedule** | [**PayoutSchedule**](PayoutSchedule.md) |  | [optional] 
**payout** | [**PaymentResponseV4Payout**](PaymentResponseV4Payout.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


