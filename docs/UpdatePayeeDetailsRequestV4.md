# UpdatePayeeDetailsRequestV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PayeeAddressV4**](PayeeAddressV4.md) |  | [optional] 
**individual** | [**IndividualV4**](IndividualV4.md) |  | [optional] 
**company** | [**CompanyV4**](CompanyV4.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**payee_type** | [**PayeeTypeEnum**](PayeeTypeEnum.md) |  | [optional] 
**challenge** | [**ChallengeV4**](ChallengeV4.md) |  | [optional] 
**email** | **str** |  | [optional] 
**contact_sms_number** | **str** | The phone number of a device that the payee wishes to receive sms messages on  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


