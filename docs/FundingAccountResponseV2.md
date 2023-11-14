# FundingAccountResponseV2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Funding Account Id | [optional] 
**payor_id** | **str** |  | [optional] 
**account_name** | **str** | name on the bank account | [optional] 
**account_number** | **str** | bank account number | [optional] 
**routing_number** | **str** | bank account routing number | [optional] 
**name** | **str** | name of funding account | [optional] 
**currency** | **str** | Valid ISO 4217 3 letter currency code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-4217-currency-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**country_code** | **str** | ISO 3166-1 2 letter country code (upper case) | [optional] 
**type** | **str** | Funding account type. One of the following values: FBO, PRIVATE | [optional] 
**archived** | **bool** | A flag for whether the funding account has been archived.  Only present in the response if true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


