# PayoutSchedule

Details relating to a payout that was executed via a schedule or is still waiting to be executed

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schedule_status** | [**ScheduleStatus**](ScheduleStatus.md) |  | 
**scheduled_at** | **datetime** |  | 
**scheduled_for** | **datetime** |  | 
**scheduled_by_principal_id** | **str** | ID of the user or application that scheduled the payout | 
**notifications_enabled** | **bool** |  | 
**scheduled_by** | **str** | Optional display name as a hint for who scheduled the payout. Not populated if payout was scheduled by an application. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


