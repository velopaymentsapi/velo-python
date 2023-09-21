# CreatePayeesCSVRequestV4

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PayeeTypeEnum**](PayeeTypeEnum.md) |  | 
**remote_id** | **str** |  | 
**email** | **str** |  | 
**address_line1** | **str** |  | 
**address_line2** | **str** |  | [optional] 
**address_line3** | **str** |  | [optional] 
**address_line4** | **str** |  | [optional] 
**address_city** | **str** |  | 
**address_county_or_province** | **str** |  | [optional] 
**address_zip_or_postcode** | **str** |  | 
**address_country** | **str** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | 
**individual_national_identification** | **str** |  | [optional] 
**individual_date_of_birth** | **date** | Must not be date in future. Example - 1970-05-20 | [optional] 
**individual_title** | **str** |  | [optional] 
**individual_first_name** | **str** |  | [optional] 
**individual_other_names** | **str** |  | [optional] 
**individual_last_name** | **str** |  | [optional] 
**company_name** | **str** |  | [optional] 
**company_ein** | **str** |  | [optional] 
**company_operating_name** | **str** |  | [optional] 
**payment_channel_account_number** | **str** | Either routing number and account number or only iban must be set | [optional] 
**payment_channel_routing_number** | **str** | Either routing number and account number or only iban must be set | [optional] 
**payment_channel_account_name** | **str** |  | [optional] 
**payment_channel_iban** | **str** | Must match the regular expression &#x60;&#x60;&#x60;^[A-Za-z0-9]+$&#x60;&#x60;&#x60;. | [optional] 
**payment_channel_country_code** | **str** | Valid ISO 3166 2 character country code. See the &lt;a href&#x3D;\&quot;https://www.iso.org/iso-3166-country-codes.html\&quot; target&#x3D;\&quot;_blank\&quot; a&gt;ISO specification&lt;/a&gt; for details. | [optional] 
**payment_channel_currency** | **str** |  | [optional] 
**challenge_description** | **str** |  | [optional] 
**challenge_value** | **str** |  | [optional] 
**payee_language** | **str** | An IETF BCP 47 language code which has been configured for use within this Velo environment.&lt;BR&gt; See the /v1/supportedLanguages endpoint to list the available codes for an environment.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


