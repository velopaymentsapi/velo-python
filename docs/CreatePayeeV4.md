# CreatePayeeV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**remote_id** | **str** |  | 
**type** | [**PayeeType2**](PayeeType2.md) |  | 
**address** | [**CreatePayeeAddressV4**](CreatePayeeAddressV4.md) |  | 
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**[PayeePayorRefV4], none_type**](PayeePayorRefV4.md) |  | [optional] [readonly] 
**payment_channel** | [**CreatePaymentChannelV4**](CreatePaymentChannelV4.md) |  | [optional] 
**challenge** | [**ChallengeV4**](ChallengeV4.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**CompanyV4**](CompanyV4.md) |  | [optional] 
**individual** | [**CreateIndividualV4**](CreateIndividualV4.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


