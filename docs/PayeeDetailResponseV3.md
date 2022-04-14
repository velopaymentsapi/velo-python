# PayeeDetailResponseV3


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**[PayeePayorRefV3], none_type**](PayeePayorRefV3.md) |  | [optional] [readonly] 
**email** | **str, none_type** |  | [optional] 
**onboarded_status** | [**OnboardedStatusV3**](OnboardedStatusV3.md) |  | [optional] 
**watchlist_status** | [**WatchlistStatusV3**](WatchlistStatusV3.md) |  | [optional] 
**watchlist_override_expires_at_timestamp** | **datetime, none_type** |  | [optional] 
**watchlist_override_comment** | **str** |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**created** | **datetime** |  | [optional] 
**country** | **str** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**display_name** | **str** |  | [optional] 
**payee_type** | [**PayeeType2**](PayeeType2.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_comment** | **str** |  | [optional] 
**disabled_updated_timestamp** | **datetime** |  | [optional] 
**address** | [**PayeeAddressV3**](PayeeAddressV3.md) |  | [optional] 
**individual** | [**IndividualV3**](IndividualV3.md) |  | [optional] 
**company** | [**CompanyV3**](CompanyV3.md) |  | [optional] 
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
**challenge** | [**ChallengeV3**](ChallengeV3.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


