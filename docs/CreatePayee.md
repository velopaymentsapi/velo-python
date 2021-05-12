# CreatePayee

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRefV3]**](PayeePayorRefV3.md) |  | [optional] 
**email** | **str** |  | 
**remote_id** | **str** |  | 
**type** | [**PayeeType**](PayeeType.md) |  | 
**address** | [**CreatePayeeAddress**](CreatePayeeAddress.md) |  | 
**payment_channel** | [**CreatePaymentChannel**](CreatePaymentChannel.md) |  | [optional] 
**challenge** | [**Challenge**](Challenge.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**individual** | [**CreateIndividual**](CreateIndividual.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


