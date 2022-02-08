# Notification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version of the notification schema | 
**sequence_number** | **int** | This is a payor specific sequence number starting at 1 for the first notification sent | 
**category** | **str** | The category that the notification relates to. One of \&quot;payment\&quot;, \&quot;payee\&quot;, \&quot;debit\&quot; or \&quot;system\&quot; | 
**event_name** | **str** | The name of event that led to this notification | 
**source** | **bool, date, datetime, dict, float, int, list, str, none_type** | One of the available set of source event payloads | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


