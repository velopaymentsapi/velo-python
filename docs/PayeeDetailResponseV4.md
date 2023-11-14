# PayeeDetailResponseV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRefV4]**](PayeePayorRefV4.md) |  | [optional] 
**payment_channels** | [**list[PaymentChannelSummaryV4]**](PaymentChannelSummaryV4.md) | A list of the Payee&#39;s payment channels in their preferred order | [optional] 
**email** | **str** |  | [optional] 
**onboarded_status** | **str** | Payee onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED | [optional] 
**watchlist_status** | **str** | Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED | [optional] 
**watchlist_override_expires_at_timestamp** | **datetime** |  | [optional] 
**watchlist_override_comment** | **str** |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**created** | **datetime** |  | [optional] 
**country** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**payee_type** | **str** | Type of Payee. One of the following values: Individual, Company | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_comment** | **str** |  | [optional] 
**disabled_updated_timestamp** | **datetime** |  | [optional] 
**address** | [**PayeeAddressV4**](PayeeAddressV4.md) |  | [optional] 
**individual** | [**IndividualV4**](IndividualV4.md) |  | [optional] 
**company** | [**CompanyV4**](CompanyV4.md) |  | [optional] 
**cellphone_number** | **str** |  | [optional] 
**managed_by_payor_id** | **str** | The id of the payor if the payee is managed | [optional] 
**watchlist_status_updated_timestamp** | **str** |  | [optional] 
**grace_period_end_date** | **date** |  | [optional] 
**enhanced_kyc_completed** | **bool** |  | [optional] 
**kyc_completed_timestamp** | **str** |  | [optional] 
**pause_payment** | **bool** |  | [optional] 
**pause_payment_timestamp** | **str** |  | [optional] 
**marketing_opt_in_decision** | **bool** |  | [optional] 
**marketing_opt_in_timestamp** | **str** |  | [optional] 
**accept_terms_and_conditions_timestamp** | **datetime** | The timestamp when the payee last accepted T&amp;Cs | [optional] 
**challenge** | [**ChallengeV4**](ChallengeV4.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


