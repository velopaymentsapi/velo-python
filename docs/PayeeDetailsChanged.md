# PayeeDetailsChanged

Base type for all payee details changed events

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly | 
**event_id** | **str** | UUID id of the source event in the Velo platform | 
**created_at** | **datetime** | ISO8601 timestamp indicating when the source event was created | 
**payee_id** | **str** | ID of this payee within the Velo platform | 
**reasons** | [**[PayeeEventAllOfReasons]**](PayeeEventAllOfReasons.md) | The reasons for the event notification. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


