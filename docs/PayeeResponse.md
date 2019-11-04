# PayeeResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payee_id** | **str** |  | [optional] [readonly] 
**payor_refs** | [**list[PayeePayorRef]**](PayeePayorRef.md) |  | [optional] [readonly] 
**email** | **str** |  | [optional] 
**address** | [**PayeeAddress**](PayeeAddress.md) |  | [optional] 
**country** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**payment_channel** | [**PayeePaymentChannel**](PayeePaymentChannel.md) |  | [optional] 
**challenge** | [**Challenge**](Challenge.md) |  | [optional] 
**language** | [**Language**](Language.md) |  | [optional] 
**accept_terms_and_conditions_timestamp** | **datetime** | The timestamp when the payee last accepted T&amp;Cs | [optional] [readonly] 
**cellphone_number** | **str** |  | [optional] 
**payee_type** | [**PayeeType**](PayeeType.md) |  | [optional] 
**company** | [**CompanyResponse**](CompanyResponse.md) |  | [optional] 
**individual** | [**IndividualResponse**](IndividualResponse.md) |  | [optional] 
**created** | **datetime** |  | [optional] 
**grace_period_end_date** | **date** |  | [optional] [readonly] 
**last_ofac_check_timestamp** | **str** |  | [optional] [readonly] 
**marketing_opt_ins** | [**list[MarketingOptIn]**](MarketingOptIn.md) |  | [optional] 
**ofac_status** | [**OfacStatus**](OfacStatus.md) |  | [optional] 
**onboarded_status** | [**OnboardedStatus**](OnboardedStatus.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


