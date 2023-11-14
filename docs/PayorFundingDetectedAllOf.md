# PayorFundingDetectedAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rails_id** | **str** | the identifier of the payment rail from which funding was received | [optional] 
**payor_id** | **str** | ID of the payor within the Velo platform | 
**funding_request_id** | **str** | ID of this funding transaction within the Velo platform | 
**funding_ref** | **str** | the external identity reference for this funding transaction | [optional] 
**currency** | **str** | the ISO-4217 code for the currency in which the funding was made | [optional] 
**amount** | **int** | the received funding amount in currency minor units | [optional] 
**physical_account_name** | **str** | the name of the account as registered with the payment rail | [optional] 
**source_account_name** | **str** | the name of the account as registered with the Velo platform | [optional] 
**source_account_id** | **str** | the ID of the account as registered with the Velo platform | [optional] 
**additional_information** | **str** | any additional information received from the payment rail | [optional] 
**transaction_id** | **str** | The Id of the related transaction | [optional] 
**transaction_reference** | **str** | The payors own reference for the related transaction | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


