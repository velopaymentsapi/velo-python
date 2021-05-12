# PaymentEvent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_type** | **str** | OA3 Schema type name for the source info which is used as the discriminator value to ensure that data binding works correctly | 
**event_id** | **str** | UUID id of the source event in the Velo platform | 
**created_at** | **datetime** | ISO8601 timestamp indicating when the source event was created | 
**payment_id** | **str** | ID of this payment within the Velo platform | 
**payout_payor_ids** | [**PayoutPayorIds**](PayoutPayorIds.md) |  | [optional] 
**payor_payment_id** | **str** | ID of this payment in the payors system | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


