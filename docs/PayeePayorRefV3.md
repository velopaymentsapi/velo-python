# PayeePayorRefV3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payor_id** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**invitation_status** | **str** |  | [optional] 
**invitation_status_timestamp** | **datetime** | The timestamp when the invitation status is updated | [optional] 
**payment_channel_id** | **str** |  | [optional] 
**payable_status** | **bool** | Indicates if the payee is payable for this payor | [optional] 
**payable_issues** | [**list[PayableIssueV3]**](PayableIssueV3.md) | Indicates any conditions which prevent the payee from being payable for this payor | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


