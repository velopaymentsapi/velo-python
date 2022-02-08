# ValidatePasswordResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **int** | More secure passwords are given a higher score. &lt;P&gt; For a password to be acceptable for use in Velo, it must score at least 3  | [optional] 
**valid** | **bool** | if true then the password can be accepted | [optional] 
**warning** | **str** | Any warning message as a reason for the given score. | [optional] 
**suggestions** | **[str]** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


