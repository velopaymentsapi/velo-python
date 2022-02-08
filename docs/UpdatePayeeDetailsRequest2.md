# UpdatePayeeDetailsRequest2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PayeeAddress2**](PayeeAddress2.md) |  | [optional] 
**individual** | [**Individual2**](Individual2.md) |  | [optional] 
**company** | [**Company2**](Company2.md) |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**payee_type** | [**PayeeType2**](PayeeType2.md) |  | [optional] 
**challenge** | [**Challenge2**](Challenge2.md) |  | [optional] 
**email** | **str, none_type** |  | [optional] 
**contact_sms_number** | **str** | The phone number of a device that the payee wishes to receive sms messages on  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


