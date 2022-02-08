# CreatePaymentChannel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Two character country code | 
**currency** | **str** |  | 
**account_name** | **str** |  | 
**payment_channel_name** | **str** |  | [optional] 
**iban** | **str** | Must match the regular expression &#x60;&#x60;&#x60;^[A-Za-z0-9]+$&#x60;&#x60;&#x60;. Either routing number and account number or only iban must be set | [optional] 
**account_number** | **str** | Either routing number and account number or only iban must be set | [optional] 
**routing_number** | **str** | Either routing number and account number or only iban must be set | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


