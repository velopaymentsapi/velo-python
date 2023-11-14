# PaymentChannelSummaryV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_channel_id** | **str** |  | 
**name** | **str** | The payment channel name | 
**country_code** | **str** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**currency** | **str** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**last4_digits** | **str** | The last 4 digits of the account number or IBAN | [optional] 
**enabled** | **bool** | Usually true. False if an associated payment is returned | 
**disabled_reason** | **str** | Indicates why the payment channel was disabled | [optional] 
**disabled_reason_code** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


