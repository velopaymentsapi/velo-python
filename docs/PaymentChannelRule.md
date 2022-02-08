# PaymentChannelRule

Rules that will get applied when creating or updating a payment channel for the given country

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**element** | **str** | &lt;p&gt;the rule element&lt;/p&gt; &lt;p&gt;will match a given element name for a payment channel configuration  | 
**required** | **bool** | is this element required | 
**display_name** | **str** | User friendly name | 
**validation** | **str** | a regex to validate the element data | 
**min_length** | **int** | mininum length of the element data | [optional] 
**max_length** | **int** | maximum length of the element data | [optional] 
**display_order** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


