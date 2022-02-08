# PaymentEventResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | The id of the event. | 
**event_date_time** | **datetime** | The date/time at which the event occurred. | 
**event_type** | **str** | The type of the event. | 
**source_currency** | [**PaymentAuditCurrency**](PaymentAuditCurrency.md) |  | [optional] 
**source_amount** | **int** | The source amount exposed by the event. | [optional] 
**payment_currency** | [**PaymentAuditCurrency**](PaymentAuditCurrency.md) |  | [optional] 
**payment_amount** | **int** | The destination amount exposed by the event. | [optional] 
**account_number** | **str** | The account number attached to the event. | [optional] 
**routing_number** | **str** | The routing number attached to the event. | [optional] 
**iban** | **str** |  | [optional] 
**account_name** | **str** |  | [optional] 
**principal** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


