# GetPayeeListResponse2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] 
**payor_refs** | [**list[PayeePayorRef]**](PayeePayorRef.md) |  | [optional] 
**email** | **str** |  | [optional] 
**onboarded_status** | [**OnboardedStatus**](OnboardedStatus.md) |  | [optional] 
**watchlist_status** | [**WatchlistStatus2**](WatchlistStatus2.md) |  | [optional] 
**watchlist_status_updated_timestamp** | **str** |  | [optional] 
**watchlist_override_comment** | **str** |  | [optional] 
**language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 
**created** | **datetime** |  | [optional] 
**country** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**payee_type** | [**PayeeType**](PayeeType.md) |  | [optional] 
**disabled** | **bool** |  | [optional] 
**disabled_comment** | **str** |  | [optional] 
**disabled_updated_timestamp** | **datetime** |  | [optional] 
**individual** | [**GetPayeeListResponseIndividual2**](GetPayeeListResponseIndividual2.md) |  | [optional] 
**company** | [**GetPayeeListResponseCompany2**](GetPayeeListResponseCompany2.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


