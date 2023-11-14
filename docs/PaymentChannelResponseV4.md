# PaymentChannelResponseV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**payee_id** | **str** |  | [optional] 
**payment_channel_name** | **str** |  | 
**account_name** | **str** |  | 
**channel_type** | **str** | Payment channel type. One of the following values: CHANNEL_BANK | 
**country_code** | **str** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**routing_number** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**iban** | **str** | Must match the regular expression &#x60;&#x60;&#x60;^[A-Za-z0-9]+$&#x60;&#x60;&#x60;. | [optional] 
**currency** | **str** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**payor_ids** | **list[str]** |  | [optional] 
**payee_name** | **str** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_swift_bic** | **str** |  | [optional] 
**bank_address** | [**AddressV4**](AddressV4.md) |  | [optional] 
**deleted** | **bool** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**disabled_reason_code** | **str** |  | [optional] 
**disabled_reason** | **str** |  | [optional] 
**payable** | **bool** | Whether this payment channel is payable | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


