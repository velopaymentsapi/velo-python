# FundingResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**funding_id** | **str** |  | 
**payor_id** | **str** |  | 
**allocation_date** | **datetime** |  | 
**detected_funding_ref** | **str** |  | [optional] 
**amount** | **int** |  | 
**currency** | **str** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**text** | **str** |  | [optional] 
**physical_account_name** | **str** |  | [optional] 
**source_account_id** | **str** |  | [optional] 
**allocation_type** | **str** | Funding Allocation Type. One of the following values: AUTOMATIC, MANUAL | [optional] 
**reason** | **str** |  | [optional] 
**hidden_date** | **datetime** |  | [optional] 
**funding_account_type** | **str** | Funding Account Type. One of the following values: FBO, WUBS_DECOUPLED, PRIVATE | 
**status** | **str** | Current status of the funding. One of the follwing values: PENDING, UNALLOCATED, ALLOCATED, HIDDEN, RETURNED, RETURNING, BULK_RETURN, OTHER | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


