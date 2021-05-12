# CreatePayee2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRef]**](PayeePayorRef.md) |  | [optional] 
**email** | **str** |  | 
**remote_id** | **str** |  | 
**type** | [**PayeeType**](PayeeType.md) |  | 
**address** | [**CreatePayeeAddress2**](CreatePayeeAddress2.md) |  | 
**payment_channel** | [**CreatePaymentChannel2**](CreatePaymentChannel2.md) |  | [optional] 
**challenge** | [**Challenge2**](Challenge2.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**Company2**](Company2.md) |  | [optional] 
**individual** | [**CreateIndividual2**](CreateIndividual2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


