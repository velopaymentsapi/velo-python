# UserDetailsUpdateRequest

<p>All properties are optional</p> <p>Only provided properties will be updated</p> <p>Use null to null out a property that is allowed to be nullable</p> 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_contact_number** | **str, none_type** | The main contact number for the user  | [optional] 
**secondary_contact_number** | **str, none_type** | The secondary contact number for the user  | [optional] 
**first_name** | **str, none_type** |  | [optional] 
**last_name** | **str, none_type** |  | [optional] 
**email** | **str, none_type** | the email address of the user | [optional] 
**sms_number** | **str, none_type** | The phone number of a device that the user can receive sms messages on  | [optional] 
**mfa_type** | [**MFAType**](MFAType.md) |  | [optional] 
**verification_code** | **str, none_type** | &lt;p&gt;Optional property that MUST be suppied when manually verifying a user&lt;/p&gt; &lt;p&gt;The user&#39;s smsNumber is registered via a separate endpoint and an OTP sent to them&lt;/p&gt;  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


