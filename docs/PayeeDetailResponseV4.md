# PayeeDetailResponseV4


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**[PayeePayorRefV4], none_type**](PayeePayorRefV4.md) |  | [optional] [readonly] 
**email** | **str, none_type** |  | [optional] 
**onboarded_status** | [**OnboardedStatusV4**](OnboardedStatusV4.md) |  | [optional] 
**watchlist_status** | [**WatchlistStatusV4**](WatchlistStatusV4.md) |  | [optional] 
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
**address** | [**PayeeAddressV4**](PayeeAddressV4.md) |  | [optional] 
**individual** | [**IndividualV4**](IndividualV4.md) |  | [optional] 
**company** | [**CompanyV4**](CompanyV4.md) |  | [optional] 
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
**challenge** | [**ChallengeV4**](ChallengeV4.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


