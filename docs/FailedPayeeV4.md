# FailedPayeeV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRefV4]**](PayeePayorRefV4.md) |  | [optional] 
**email** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**type** | **str** | Type of Payee. One of the following values: Individual, Company | [optional] 
**address** | [**CreatePayeeAddressV4**](CreatePayeeAddressV4.md) |  | [optional] 
**payment_channel** | [**CreatePaymentChannelV4**](CreatePaymentChannelV4.md) |  | [optional] 
**challenge** | [**ChallengeV4**](ChallengeV4.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**company** | [**CompanyV4**](CompanyV4.md) |  | [optional] 
**individual** | [**CreateIndividualV4**](CreateIndividualV4.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


