# NotificationSource

One of the available set of source event payloads

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly | 
**payout_payor_ids** | [**PayoutPayorIds**](PayoutPayorIds.md) |  | [optional] 
**payor_payment_id** | **str** | ID of this payment in the payors system | [optional] 
**reasons** | [**[PayeeEventAllOfReasons]**](PayeeEventAllOfReasons.md) | The reasons for the event notification. | [optional] 
**event_id** | **str** | UUID id of the source event in the Velo platform | [optional] 
**created_at** | **datetime** | ISO8601 timestamp indicating when the source event was created | [optional] 
**payment_id** | **str** | ID of this payment within the Velo platform | [optional] 
**status** | **str** | The new status of the debit. One of \&quot;PENDING\&quot; \&quot;PROCESSING\&quot; \&quot;REJECTED\&quot; \&quot;RELEASED\&quot; | [optional] 
**reason_code** | **str** | The Velo code that indicates why the payment was rejected or returned | [optional] 
**reason_message** | **str** | The description of why the payment was rejected or returned | [optional] 
**payee_id** | **str** | ID of this payee within the Velo platform | [optional] 
**debit_transaction_id** | **str** | ID of this debit transaction within the Velo platform | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


