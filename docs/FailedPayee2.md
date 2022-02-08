# FailedPayee2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**[PayeePayorRef], none_type**](PayeePayorRef.md) |  | [optional] [readonly] 
**email** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**type** | [**PayeeType2**](PayeeType2.md) |  | [optional] 
**address** | [**CreatePayeeAddress2**](CreatePayeeAddress2.md) |  | [optional] 
**payment_channel** | [**CreatePaymentChannel2**](CreatePaymentChannel2.md) |  | [optional] 
**challenge** | [**Challenge2**](Challenge2.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**Company2**](Company2.md) |  | [optional] 
**individual** | [**CreateIndividual2**](CreateIndividual2.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


