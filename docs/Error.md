# Error


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | English language message indicating the nature of the error | [optional] 
**error_code** | **str** | Unique numeric code that can be used for switching client behavior or to drive translated or customised error messages | [optional] 
**localisation_details** | [**LocalisationDetails**](LocalisationDetails.md) |  | [optional] 
**location** | **str** | the property or object that caused the error | [optional] 
**location_type** | **str** | the location type in the request that was the cause of the error  | [optional] 
**reason_code** | **str** | a camel-cased string that can be used by clients to localise client error messages (deprecated) | [optional] 
**error_data** | [**ErrorData**](ErrorData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


