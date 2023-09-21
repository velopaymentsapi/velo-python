# PayorV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payor_id** | **str** |  | 
**payor_name** | **str** | The name of the payor. | 
**payor_xid** | **str** | A unique identifier that an external system uses to reference the payor in their system | [optional] 
**provider** | **str** | The source of the payorXid, default is null which means Velo | [optional] 
**address** | [**PayorAddressV2**](PayorAddressV2.md) |  | [optional] 
**primary_contact_name** | **str** | Name of primary contact for the payor. | [optional] 
**primary_contact_phone** | **str** | Primary contact phone number for the payor. | [optional] 
**primary_contact_email** | **str** | Primary contact email for the payor. | [optional] 
**kyc_state** | **str** | The kyc state of the payor. One of the following values: FAILED_KYC, PASSED_KYC, REQUIRES_KYC | [optional] 
**manual_lockout** | **bool** | Whether or not the payor has been manually locked by the backoffice. | [optional] 
**open_banking_enabled** | **bool** | Is Open Banking supported for this payor | [optional] 
**payee_grace_period_processing_enabled** | **bool** | Whether grace period processing is enabled. | [optional] 
**payee_grace_period_days** | **int** | The grace period for paying payees in days. | [optional] 
**collective_alias** | **str** | How the payor has chosen to refer to payees. | [optional] 
**support_contact** | **str** | The payor’s support contact email address. | [optional] 
**dba_name** | **str** | The payor’s &#39;Doing Business As&#39; name. | [optional] 
**allows_language_choice** | **bool** | Whether or not the payor allows language choice in the UI. | [optional] 
**reminder_emails_opt_out** | **bool** | Whether or not the payor has opted-out of reminder emails being sent. | [optional] 
**language** | **str** | The payor’s language preference. Must be one of [EN, FR] | [optional] 
**includes_reports** | **bool** |  | [optional] 
**wu_customer_id** | **str** |  | [optional] 
**max_master_payor_admins** | **int** |  | [optional] 
**payment_rails** | **str** | The id of the payment rails | [optional] 
**transmission_types** | [**TransmissionTypes2**](TransmissionTypes2.md) |  | [optional] 
**remote_system_ids** | **list[str]** | The payor’s supported remote systems by id | [optional] 
**usd_txn_value_reporting_threshold** | **int** | USD in minor units | [optional] 
**managing_payees** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


