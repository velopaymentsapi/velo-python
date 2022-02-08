# PayeeDetailResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**[PayeePayorRefV3], none_type**](PayeePayorRefV3.md) |  | [optional] [readonly] 
**email** | **str, none_type** |  | [optional] 
**onboarded_status** | [**OnboardedStatus2**](OnboardedStatus2.md) |  | [optional] 
**watchlist_status** | [**WatchlistStatus**](WatchlistStatus.md) |  | [optional] 
**watchlist_override_expires_at_timestamp** | **datetime, none_type** |  | [optional] 
**watchlist_override_comment** | **str** |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**created** | **datetime** |  | [optional] 
**country** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**payee_type** | [**PayeeType2**](PayeeType2.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_comment** | **str** |  | [optional] 
**disabled_updated_timestamp** | **datetime** |  | [optional] 
**address** | [**PayeeAddress**](PayeeAddress.md) |  | [optional] 
**individual** | [**Individual**](Individual.md) |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**cellphone_number** | **str** |  | [optional] 
**watchlist_status_updated_timestamp** | **str, none_type** |  | [optional] [readonly] 
**grace_period_end_date** | **date, none_type** |  | [optional] [readonly] 
**enhanced_kyc_completed** | **bool** |  | [optional] 
**kyc_completed_timestamp** | **str, none_type** |  | [optional] 
**pause_payment** | **bool** |  | [optional] 
**pause_payment_timestamp** | **str, none_type** |  | [optional] 
**marketing_opt_in_decision** | **bool** |  | [optional] 
**marketing_opt_in_timestamp** | **str, none_type** |  | [optional] 
**accept_terms_and_conditions_timestamp** | **datetime, none_type** | The timestamp when the payee last accepted T&amp;Cs | [optional] [readonly] 
**challenge** | [**Challenge**](Challenge.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


