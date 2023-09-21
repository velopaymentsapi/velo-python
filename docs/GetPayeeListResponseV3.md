# GetPayeeListResponseV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRefV3]**](PayeePayorRefV3.md) |  | [optional] 
**email** | **str** |  | [optional] 
**onboarded_status** | **str** | Onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED | [optional] 
**watchlist_status** | **str** | Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED | [optional] 
**watchlist_status_updated_timestamp** | **str** |  | [optional] 
**watchlist_override_comment** | **str** |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**created** | **datetime** |  | [optional] 
**country** | **str** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**display_name** | **str** |  | [optional] 
**payee_type** | **str** | Type of Payee. One of the following values: Individual, Company | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_comment** | **str** |  | [optional] 
**disabled_updated_timestamp** | **datetime** |  | [optional] 
**individual** | [**GetPayeeListResponseIndividualV3**](GetPayeeListResponseIndividualV3.md) |  | [optional] 
**company** | [**GetPayeeListResponseCompanyV3**](GetPayeeListResponseCompanyV3.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


