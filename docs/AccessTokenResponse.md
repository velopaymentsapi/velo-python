# AccessTokenResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** | Bearer token used in headers to access secure endpoints  | [optional] 
**token_type** | **str** | the type of the token | [optional] [default to 'bearer']
**refresh_token** | **str** | can be used to obtain a new access token | [optional] 
**expires_in** | **int** | The lifetime in seconds of the access token | [optional] 
**scope** | **str** | the scope of the access token | [optional] 
**user_info** | [**UserInfo**](UserInfo.md) |  | [optional] 
**entity_ids** | **list[str]** | If the user is a payee then the payeeId&lt;P&gt; If the user is a payor then the payorId  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


