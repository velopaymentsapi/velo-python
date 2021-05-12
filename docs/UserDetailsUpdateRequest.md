# UserDetailsUpdateRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_contact_number** | **str** | The main contact number for the user  | [optional] 
**secondary_contact_number** | **str** | The secondary contact number for the user  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** | the email address of the user | [optional] 
**sms_number** | **str** | The phone number of a device that the user can receive sms messages on  | [optional] 
**mfa_type** | [**MFAType**](MFAType.md) |  | [optional] 
**verification_code** | **str** | &lt;p&gt;Optional property that MUST be suppied when manually verifying a user&lt;/p&gt; &lt;p&gt;The user&#39;s smsNumber is registered via a separate endpoint and an OTP sent to them&lt;/p&gt;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


