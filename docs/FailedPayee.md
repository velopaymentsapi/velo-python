# FailedPayee


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**[PayeePayorRefV3], none_type**](PayeePayorRefV3.md) |  | [optional] [readonly] 
**email** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**type** | [**PayeeType2**](PayeeType2.md) |  | [optional] 
**address** | [**CreatePayeeAddress**](CreatePayeeAddress.md) |  | [optional] 
**payment_channel** | [**CreatePaymentChannel**](CreatePaymentChannel.md) |  | [optional] 
**challenge** | [**Challenge**](Challenge.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**individual** | [**CreateIndividual**](CreateIndividual.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


