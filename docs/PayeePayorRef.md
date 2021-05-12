# PayeePayorRef

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payor_id** | **str** |  | [optional] 
**remote_id** | **str** |  | [optional] 
**invitation_status** | [**InvitationStatus**](InvitationStatus.md) |  | [optional] 
**invitation_status_timestamp** | **datetime** | The timestamp when the invitation status is updated | [optional] 
**payment_channel_id** | **str** |  | [optional] 
**payable_status** | **bool** | Indicates if the payee is payable for this payor | [optional] 
**payable_issues** | [**list[PayableIssue2]**](PayableIssue2.md) | Indicates any conditions which prevent the payee from being payable for this payor | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


