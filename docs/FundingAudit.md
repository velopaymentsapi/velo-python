# FundingAudit

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The amount funded | [optional] 
**currency** | **str** | The currency of the funding | [optional] 
**date_time** | **datetime** |  | [optional] 
**status** | **str** | Status of the funding. One of the following values: PENDING, FAILED, CREDIT, DEBIT | [optional] 
**source_account_name** | **str** |  | [optional] 
**funding_account_name** | **str** |  | [optional] 
**funding_type** | **str** | Funding type. One of the following values: ACH, WIRE, EMBEDDED, BANK_TRANSFER | [optional] 
**events** | [**list[FundingEvent]**](FundingEvent.md) |  | [optional] 
**topup_type** | **str** | Type of top up. One of the following values: AUTOMATIC, MANUAL | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


