# InviteUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | the email address of the invited user | 
**mfa_type** | **str** | &lt;p&gt;The MFA type that the user will use&lt;/p&gt; &lt;p&gt;The type may be conditional on the role(s) the user has&lt;/p&gt;  | 
**sms_number** | **str** | The phone number of a device that the user can receive sms messages on  | 
**primary_contact_number** | **str** | The main contact number for the user  | 
**secondary_contact_number** | **str** | The secondary contact number for the user  | [optional] 
**roles** | **list[str]** | The role(s) for the user The role must exist The role can be a custom role or a system role but the invoker must have the permissions to assign the role System roles are: velo.backoffice.admin, velo.payor.master_admin, velo.payor.admin, velo.payor.support, velo.payee.admin, velo.payee.support  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**entity_id** | **str** | The payorId or payeeId or null if the user is a backoffice admin  | [optional] 
**user_type** | **str** | Will default to PAYOR if not provided but entityId is provided | [optional] 
**verification_code** | **str** | Optional property that MUST be suppied when manually verifying a user The user&#39;s smsNumber is registered via a separate endpoint and an OTP sent to them  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


