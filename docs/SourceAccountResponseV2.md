# SourceAccountResponseV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Source Account Id | 
**funding_ref** | **str** |  | 
**physical_account_name** | **str** |  | 
**rails_id** | **str** |  | 
**pooled** | **bool** |  | 
**balance_visible** | **bool** |  | 
**account_type** | **str** |  | 
**balance** | **int** | Decimal implied | [optional] 
**currency** | **str** |  | [optional]  if omitted the server will use the default value of "USD"
**payor_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**customer_id** | **str, none_type** |  | [optional] 
**physical_account_id** | **str** |  | [optional] 
**notifications** | [**Notifications**](Notifications.md) |  | [optional] 
**funding_account_id** | **str, none_type** |  | [optional] 
**auto_top_up_config** | [**AutoTopUpConfig**](AutoTopUpConfig.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


