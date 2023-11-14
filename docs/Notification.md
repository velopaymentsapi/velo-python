# Notification

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | The API version of the notification schema | 
**sequence_number** | **int** | This is a payor specific sequence number starting at 1 for the first notification sent | 
**category** | **str** | The category that the notification relates to. One of \&quot;payment\&quot;, \&quot;payee\&quot;, \&quot;debit\&quot; or \&quot;system\&quot; | 
**event_name** | **str** | The name of event that led to this notification | 
**source** | [**OneOfPingPaymentStatusChangedPaymentRejectedOrReturnedOnboardingStatusChangedPayableStatusChangedPayeeDetailsChangedDebitStatusChangedPayorFundingDetected**](OneOfPingPaymentStatusChangedPaymentRejectedOrReturnedOnboardingStatusChangedPayableStatusChangedPayeeDetailsChangedDebitStatusChangedPayorFundingDetected.md) | One of the available set of source event payloads | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


