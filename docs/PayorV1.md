# PayorV1

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payor_id** | **str** |  | [optional] [readonly] 
**payor_name** | **str** | The name of the payor. | 
**address** | [**PayorAddress**](PayorAddress.md) |  | [optional] 
**primary_contact_name** | **str** | Name of primary contact for the payor. | [optional] 
**primary_contact_phone** | **str** | Primary contact phone number for the payor. | [optional] 
**primary_contact_email** | **str** | Primary contact email for the payor. | [optional] 
**funding_account_routing_number** | **str** | The funding account routing number to be used for the payor. | [optional] 
**funding_account_account_number** | **str** | The funding account number to be used for the payor. | [optional] 
**funding_account_account_name** | **str** | The funding account name to be used for the payor. | [optional] 
**kyc_state** | [**KycState**](KycState.md) |  | [optional] 
**manual_lockout** | **bool** | Whether or not the payor has been manually locked by the backoffice. | [optional] 
**payee_grace_period_processing_enabled** | **bool** | Whether grace period processing is enabled. | [optional] [readonly] 
**payee_grace_period_days** | **int** | The grace period for paying payees in days. | [optional] [readonly] 
**collective_alias** | **str** | How the payor has chosen to refer to payees. | [optional] 
**support_contact** | **str** | The payor’s support contact email address. | [optional] 
**dba_name** | **str** | The payor’s &#39;Doing Business As&#39; name. | [optional] 
**allows_language_choice** | **bool** | Whether or not the payor allows language choice in the UI. | [optional] 
**reminder_emails_opt_out** | **bool** | Whether or not the payor has opted-out of reminder emails being sent. | [optional] [readonly] 
**language** | **str** | The payor’s language preference. Must be one of [EN, FR]. | [optional] 
**includes_reports** | **bool** |  | [optional] 
**max_master_payor_admins** | **int** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


