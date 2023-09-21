# velo_payments.LoginApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logout**](LoginApi.md#logout) | **POST** /v1/logout | Logout
[**reset_password**](LoginApi.md#reset_password) | **POST** /v1/password/reset | Reset password
[**validate_access_token**](LoginApi.md#validate_access_token) | **POST** /v1/validate | validate
[**velo_auth**](LoginApi.md#velo_auth) | **POST** /v1/authenticate | Authentication endpoint


# **logout**
> logout()

Logout

<p>Given a valid access token in the header then log out the authenticated user or client </p> <p>Will revoke the token</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint
configuration = velo_payments.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.sandbox.velopayments.com
configuration.host = "https://api.sandbox.velopayments.com"
# Create an instance of the API class
api_instance = velo_payments.LoginApi(velo_payments.ApiClient(configuration))

try:
    # Logout
    api_instance.logout()
except ApiException as e:
    print("Exception when calling LoginApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User has been logged out |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(reset_password_request)

Reset password

<p>Reset password </p> <p>An email with an embedded link will be sent to the receipient of the email address </p> <p>The link will contain a token to be used for resetting the password </p> 

### Example

```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = velo_payments.LoginApi()
reset_password_request = velo_payments.ResetPasswordRequest() # ResetPasswordRequest | An Email address to send the reset password link to

try:
    # Reset password
    api_instance.reset_password(reset_password_request)
except ApiException as e:
    print("Exception when calling LoginApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)| An Email address to send the reset password link to | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the request was accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_access_token**
> AccessTokenResponse validate_access_token(access_token_validation_request, authorization=authorization)

validate

<p>The second part of login involves validating using an MFA device</p> <p>An access token with PRE_AUTH authorities is required</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint
configuration = velo_payments.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.sandbox.velopayments.com
configuration.host = "https://api.sandbox.velopayments.com"
# Create an instance of the API class
api_instance = velo_payments.LoginApi(velo_payments.ApiClient(configuration))
access_token_validation_request = velo_payments.AccessTokenValidationRequest() # AccessTokenValidationRequest | An OTP from the user's registered MFA Device 
authorization = 'authorization_example' # str | Bearer token authorization leg of validate (optional)

try:
    # validate
    api_response = api_instance.validate_access_token(access_token_validation_request, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->validate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_token_validation_request** | [**AccessTokenValidationRequest**](AccessTokenValidationRequest.md)| An OTP from the user&#39;s registered MFA Device  | 
 **authorization** | **str**| Bearer token authorization leg of validate | [optional] 

### Return type

[**AccessTokenResponse**](AccessTokenResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User request has been validated |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **velo_auth**
> AuthResponse velo_auth(grant_type=grant_type)

Authentication endpoint

<p>Use this endpoint to obtain an access token for calling Velo Payments APIs. </p> <p>You need your API key and API secret issued by Velo</p> <p>To login and get an access token the API key and API secret must be Base64 encoded by concatenating them with a colon between them</p> <p>e.g. Given an ApiKey: 44a9537d-d55d-4b47-8082-14061c2bcdd8 and ApiSecret: c396b26b-137a-44fd-87f5-34631f8fd529</p> <p>Using a Base64 encode function Base64Encoder().encode(\"44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529\")</p> <p>Included as a Basic Authorization header: -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" </p> 

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint
configuration = velo_payments.Configuration()
# Configure HTTP basic authorization: basicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# Defining host is optional and default to https://api.sandbox.velopayments.com
configuration.host = "https://api.sandbox.velopayments.com"
# Create an instance of the API class
api_instance = velo_payments.LoginApi(velo_payments.ApiClient(configuration))
grant_type = 'client_credentials' # str | OAuth grant type. Should use 'client_credentials' (optional) (default to 'client_credentials')

try:
    # Authentication endpoint
    api_response = api_instance.velo_auth(grant_type=grant_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->velo_auth: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| OAuth grant type. Should use &#39;client_credentials&#39; | [optional] [default to &#39;client_credentials&#39;]

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Valid Authenication response |  * Cache-Control - Ensure clients do not cache request <br>  * Pragma - Ensure clients do not cache request <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

