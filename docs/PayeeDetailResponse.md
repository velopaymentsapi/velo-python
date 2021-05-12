# PayeeDetailResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRefV3]**](PayeePayorRefV3.md) |  | [optional] 
**email** | **str** |  | [optional] 
**onboarded_status** | [**OnboardedStatus2**](OnboardedStatus2.md) |  | [optional] 
**watchlist_status** | [**WatchlistStatus**](WatchlistStatus.md) |  | [optional] 
**watchlist_override_expires_at_timestamp** | **datetime** |  | [optional] 
**watchlist_override_comment** | **str** |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**created** | **datetime** |  | [optional] 
**country** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**payee_type** | [**PayeeType**](PayeeType.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_comment** | **str** |  | [optional] 
**disabled_updated_timestamp** | **datetime** |  | [optional] 
**address** | [**PayeeAddress**](PayeeAddress.md) |  | [optional] 
**individual** | [**Individual**](Individual.md) |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**cellphone_number** | **str** |  | [optional] 
**watchlist_status_updated_timestamp** | **str** |  | [optional] 
**grace_period_end_date** | **date** |  | [optional] 
**enhanced_kyc_completed** | **bool** |  | [optional] 
**kyc_completed_timestamp** | **str** |  | [optional] 
**pause_payment** | **bool** |  | [optional] 
**pause_payment_timestamp** | **str** |  | [optional] 
**marketing_opt_in_decision** | **bool** |  | [optional] 
**marketing_opt_in_timestamp** | **str** |  | [optional] 
**accept_terms_and_conditions_timestamp** | **datetime** | The timestamp when the payee last accepted T&amp;Cs | [optional] 
**challenge** | [**Challenge**](Challenge.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


