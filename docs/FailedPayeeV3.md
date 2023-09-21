# FailedPayeeV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRefV3]**](PayeePayorRefV3.md) |  | [optional] 
**email** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**type** | **str** | Type of Payee. One of the following values: Individual, Company | [optional] 
**address** | [**CreatePayeeAddressV3**](CreatePayeeAddressV3.md) |  | [optional] 
**payment_channel** | [**CreatePaymentChannelV3**](CreatePaymentChannelV3.md) |  | [optional] 
**challenge** | [**ChallengeV3**](ChallengeV3.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**CompanyV3**](CompanyV3.md) |  | [optional] 
**individual** | [**CreateIndividualV3**](CreateIndividualV3.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


