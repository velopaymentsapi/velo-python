# Payee2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**list[PayeePayorRefV2]**](PayeePayorRefV2.md) |  | [optional] [readonly] 
**email** | **str** |  | [optional] 
**address** | [**PayeeAddress**](PayeeAddress.md) |  | [optional] 
**country** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**payment_channel** | [**PayeePaymentChannel2**](PayeePaymentChannel2.md) |  | [optional] 
**challenge** | [**Challenge**](Challenge.md) |  | [optional] 
**language** | [**Language2**](Language2.md) |  | [optional] 
**accept_terms_and_conditions_timestamp** | **datetime** | The timestamp when the payee last accepted T&amp;Cs | [optional] [readonly] 
**cellphone_number** | **str** |  | [optional] 
**payee_type** | [**PayeeType**](PayeeType.md) |  | [optional] 
**company** | [**CompanyV1**](CompanyV1.md) |  | [optional] 
**individual** | [**IndividualV1**](IndividualV1.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**grace_period_end_date** | **date** |  | [optional] [readonly] 
**watchlist_status_updated_timestamp** | **str** |  | [optional] [readonly] 
**marketing_opt_ins** | [**list[MarketingOptIn]**](MarketingOptIn.md) |  | [optional] 
**onboarded_status** | [**OnboardedStatus**](OnboardedStatus.md) |  | [optional] 
**remote_id** | **str** | Remote Id must be between 1 and 100 characters long | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


