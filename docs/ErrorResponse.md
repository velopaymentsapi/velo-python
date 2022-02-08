# ErrorResponse

Error response returned by all error conditions in Velo Services

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**[Error]**](Error.md) | one or more errors | [optional] 
**correlation_id** | **str** | a unique identifier to track a request or related sequence of requests | [optional] 
**http_status_code** | **int** | this will mirror the Status-Code part of the Status-Line http response header and is included for extra clarity | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


