# SourceAccountResponseV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Source Account Id | 
**balance** | **int** | Decimal implied | [optional] 
**currency** | **str** |  | [optional] 
**funding_ref** | **str** | The funding reference (will not be set for DECOUPLED accounts). | [optional] 
**physical_account_name** | **str** | The physical account name (will not be set for DECOUPLED accounts). | [optional] 
**rails_id** | **str** |  | 
**payor_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**pooled** | **bool** | The pooled account flag (will not be set for DECOUPLED accounts). | [optional] 
**customer_id** | **str** |  | [optional] 
**physical_account_id** | **str** | The physical account id (will not be set for DECOUPLED accounts). | [optional] 
**notifications** | [**Notifications2**](Notifications2.md) |  | [optional] 
**auto_top_up_config** | [**AutoTopUpConfig2**](AutoTopUpConfig2.md) |  | [optional] 
**type** | **str** |  | 
**country** | **str** | The two character ISO country code for the associated account | [optional] 
**archived** | **bool** | A flag for whether the source account has been archived.  Only present in the response if true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


