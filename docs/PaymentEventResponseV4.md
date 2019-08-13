# PaymentEventResponseV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The id of the event. | 
**event_date_time** | **datetime** | The date/time at which the event occurred. | 
**event_type** | **str** | The type of the event. | 
**source_currency** | [**PaymentAuditCurrencyV4**](PaymentAuditCurrencyV4.md) |  | [optional] 
**source_amount** | **int** | The source amount exposed by the event. | [optional] 
**payment_currency** | [**PaymentAuditCurrencyV4**](PaymentAuditCurrencyV4.md) |  | [optional] 
**payment_amount** | **int** | The destination amount exposed by the event. | [optional] 
**account_number** | **str** | The account number attached to the event. | [optional] 
**routing_number** | **str** | The routing number attached to the event. | [optional] 
**iban** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


