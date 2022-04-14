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
import time
import velo_payments
from velo_payments.api import login_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.velopayments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout
        api_instance.logout()
    except velo_payments.ApiException as e:
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
import time
import velo_payments
from velo_payments.api import login_api
from velo_payments.model.reset_password_request import ResetPasswordRequest
from velo_payments.model.inline_response400 import InlineResponse400
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.velopayments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)


# Enter a context with an instance of the API client
with velo_payments.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    reset_password_request = ResetPasswordRequest(
        email="foo@example.com",
    ) # ResetPasswordRequest | An Email address to send the reset password link to

    # example passing only required values which don't have defaults set
    try:
        # Reset password
        api_instance.reset_password(reset_password_request)
    except velo_payments.ApiException as e:
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
> AccessTokenResponse validate_access_token(access_token_validation_request)

validate

<p>The second part of login involves validating using an MFA device</p> <p>An access token with PRE_AUTH authorities is required</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import login_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.access_token_validation_request import AccessTokenValidationRequest
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.access_token_response import AccessTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.velopayments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    access_token_validation_request = AccessTokenValidationRequest(
        otp="123456",
    ) # AccessTokenValidationRequest | An OTP from the user's registered MFA Device 
    authorization = "Authorization_example" # str | Bearer token authorization leg of validate (optional)

    # example passing only required values which don't have defaults set
    try:
        # validate
        api_response = api_instance.validate_access_token(access_token_validation_request)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling LoginApi->validate_access_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # validate
        api_response = api_instance.validate_access_token(access_token_validation_request, authorization=authorization)
        pprint(api_response)
    except velo_payments.ApiException as e:
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
> AuthResponse velo_auth()

Authentication endpoint

<p>Use this endpoint to obtain an access token for calling Velo Payments APIs. </p> <p>You need your API key and API secret issued by Velo</p> <p>To login and get an access token the API key and API secret must be Base64 encoded by concatenating them with a colon between them</p> <p>e.g. Given an ApiKey: 44a9537d-d55d-4b47-8082-14061c2bcdd8 and ApiSecret: c396b26b-137a-44fd-87f5-34631f8fd529</p> <p>Using a Base64 encode function Base64Encoder().encode(\"44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529\")</p> <p>Included as a Basic Authorization header: -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" </p> 

### Example

* Basic Authentication (basicAuth):

```python
import time
import velo_payments
from velo_payments.api import login_api
from velo_payments.model.auth_response import AuthResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.sandbox.velopayments.com
# See configuration.py for a list of all supported configuration parameters.
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = velo_payments.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    grant_type = "client_credentials" # str | OAuth grant type. Should use 'client_credentials' (optional) if omitted the server will use the default value of "client_credentials"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Authentication endpoint
        api_response = api_instance.velo_auth(grant_type=grant_type)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling LoginApi->velo_auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| OAuth grant type. Should use &#39;client_credentials&#39; | [optional] if omitted the server will use the default value of "client_credentials"

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

