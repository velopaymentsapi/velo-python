# UserResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the user | [optional] 
**status** | **str** | The status of the user when the user has been invited but not yet enrolled they will have a PENDING status  | [optional] 
**email** | **str** | the email address of the user | [optional] 
**sms_number** | **str** | The phone number of a device that the user can receive sms messages on  | [optional] 
**primary_contact_number** | **str** | The main contact number for the user  | [optional] 
**secondary_contact_number** | **str** | The secondary contact number for the user  | [optional] 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**entity_id** | **str** | The payorId or payeeId or null if the user is not a payor or payee user  | [optional] 
**company_name** | **str** | The payor or payee company name or null if the user is not a payor or payee user  | [optional] 
**roles** | [**list[Role]**](Role.md) | The role(s) for the user  | [optional] 
**user_type** | **str** | Indicates the type of user. Could be BACKOFFICE, PAYOR or PAYEE. | [optional] 
**mfa_type** | **str** | The type of the MFA device | [optional] 
**mfa_status** | **str** | The status of the MFA device | [optional] 
**locked_out** | **bool** | If true the user is currently locked out and unable to log in | [optional] 
**locked_out_timestamp** | **datetime** | A timestamp showing when the user was locked out If null then the user is not currently locked out  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


