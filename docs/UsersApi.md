# velo_payments.UsersApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_by_id_v2**](UsersApi.md#delete_user_by_id_v2) | **DELETE** /v2/users/{userId} | Delete a User
[**disable_user_v2**](UsersApi.md#disable_user_v2) | **POST** /v2/users/{userId}/disable | Disable a User
[**enable_user_v2**](UsersApi.md#enable_user_v2) | **POST** /v2/users/{userId}/enable | Enable a User
[**get_self**](UsersApi.md#get_self) | **GET** /v2/users/self | Get Self
[**get_user_by_id_v2**](UsersApi.md#get_user_by_id_v2) | **GET** /v2/users/{userId} | Get User
[**invite_user**](UsersApi.md#invite_user) | **POST** /v2/users/invite | Invite a User
[**list_users**](UsersApi.md#list_users) | **GET** /v2/users | List Users
[**register_sms**](UsersApi.md#register_sms) | **POST** /v2/users/registration/sms | Register SMS Number
[**resend_token**](UsersApi.md#resend_token) | **POST** /v2/users/{userId}/tokens | Resend a token
[**role_update**](UsersApi.md#role_update) | **POST** /v2/users/{userId}/roleUpdate | Update User Role
[**unlock_user_v2**](UsersApi.md#unlock_user_v2) | **POST** /v2/users/{userId}/unlock | Unlock a User
[**unregister_mfa**](UsersApi.md#unregister_mfa) | **POST** /v2/users/{userId}/mfa/unregister | Unregister MFA for the user
[**unregister_mfa_for_self**](UsersApi.md#unregister_mfa_for_self) | **POST** /v2/users/self/mfa/unregister | Unregister MFA for Self
[**update_password_self**](UsersApi.md#update_password_self) | **POST** /v2/users/self/password | Update Password for self
[**user_details_update**](UsersApi.md#user_details_update) | **POST** /v2/users/{userId}/userDetailsUpdate | Update User Details
[**user_details_update_for_self**](UsersApi.md#user_details_update_for_self) | **POST** /v2/users/self/userDetailsUpdate | Update User Details for self
[**validate_password_self**](UsersApi.md#validate_password_self) | **POST** /v2/users/self/password/validate | Validate the proposed password


# **delete_user_by_id_v2**
> delete_user_by_id_v2(user_id)

Delete a User

Delete User by Id. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response404 import InlineResponse404
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.

    # example passing only required values which don't have defaults set
    try:
        # Delete a User
        api_instance.delete_user_by_id_v2(user_id)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->delete_user_by_id_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |

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
**204** | request completed okay |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_user_v2**
> disable_user_v2(user_id)

Disable a User

<p>If a user is enabled this endpoint will disable them </p> <p>The invoker must have the appropriate permission </p> <p>A user cannot disable themself </p> <p>When a user is disabled any active access tokens will be revoked and the user will not be able to log in</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.

    # example passing only required values which don't have defaults set
    try:
        # Disable a User
        api_instance.disable_user_v2(user_id)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->disable_user_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |

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
**204** | Success the user was disabled or was already disabled |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_user_v2**
> enable_user_v2(user_id)

Enable a User

<p>If a user has been disabled this endpoints will enable them </p> <p>The invoker must have the appropriate permission </p> <p>A user cannot enable themself </p> <p>If the user is a payor user and the payor is disabled this operation is not allowed</p> <p>If enabling a payor user would breach the limit for master admin payor users the request will be rejected </p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.

    # example passing only required values which don't have defaults set
    try:
        # Enable a User
        api_instance.enable_user_v2(user_id)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->enable_user_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |

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
**204** | Success the user was enabled or was already enabled |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self**
> UserResponse get_self()

Get Self

Get the user's details 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Self
        api_response = api_instance.get_self()
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->get_self: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get User Details |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_id_v2**
> UserResponse get_user_by_id_v2(user_id)

Get User

Get a Single User by Id. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.user_response import UserResponse
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.

    # example passing only required values which don't have defaults set
    try:
        # Get User
        api_response = api_instance.get_user_by_id_v2(user_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->get_user_by_id_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get User Details |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_user**
> invite_user(invite_user_request)

Invite a User

Create a User and invite them to the system 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.invite_user_request import InviteUserRequest
from velo_payments.model.inline_response409 import InlineResponse409
from velo_payments.model.inline_response412 import InlineResponse412
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
    api_instance = users_api.UsersApi(api_client)
    invite_user_request = InviteUserRequest(
        email="foo@example.com",
        mfa_type="TOTP",
        sms_number="11235555555",
        primary_contact_number="11235555555",
        secondary_contact_number="11235555550",
        roles=["velo.payor.admin"],
        first_name="John",
        last_name="Doe",
        entity_id="7fffa261-ac68-49e6-b605-d24a444d9206",
        user_type="PAYEE",
        verification_code="123456",
    ) # InviteUserRequest | Details of User to invite

    # example passing only required values which don't have defaults set
    try:
        # Invite a User
        api_instance.invite_user(invite_user_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->invite_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_user_request** | [**InviteUserRequest**](InviteUserRequest.md)| Details of User to invite |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content. The user was invited successfully |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |
**412** | The request could not be completed as a precondition was not met  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> PagedUserResponse list_users()

List Users

Get a paginated response listing the Users

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.user_type import UserType
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.user_status import UserStatus
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.payee_type import PayeeType
from velo_payments.model.paged_user_response import PagedUserResponse
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
    api_instance = users_api.UsersApi(api_client)
    type = UserType("PAYOR") # UserType | The Type of the User. (optional)
    status = UserStatus("ENABLED") # UserStatus | The status of the User. (optional)
    entity_id = "entityId_example" # str | The entityId of the User. (optional)
    payee_type = PayeeType("COMPANY") # PayeeType | The Type of the Payee entity. Either COMPANY or INDIVIDUAL. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "email:asc" # str | List of sort fields (e.g. ?sort=email:asc,lastName:asc) Default is email:asc 'name' The supported sort fields are - email, lastNmae.  (optional) if omitted the server will use the default value of "email:asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Users
        api_response = api_instance.list_users(type=type, status=status, entity_id=entity_id, payee_type=payee_type, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **UserType**| The Type of the User. | [optional]
 **status** | **UserStatus**| The status of the User. | [optional]
 **entity_id** | **str**| The entityId of the User. | [optional]
 **payee_type** | **PayeeType**| The Type of the Payee entity. Either COMPANY or INDIVIDUAL. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;email:asc,lastName:asc) Default is email:asc &#39;name&#39; The supported sort fields are - email, lastNmae.  | [optional] if omitted the server will use the default value of "email:asc"

### Return type

[**PagedUserResponse**](PagedUserResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paginated list of Users filtered by query parameters |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_sms**
> register_sms(register_sms_request)

Register SMS Number

<p>Register an Sms number and send an OTP to it </p> <p>Used for manual verification of a user </p> <p>The backoffice user initiates the request to send the OTP to the user's sms </p> <p>The user then reads back the OTP which the backoffice user enters in the verifactionCode property for requests that require it</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.register_sms_request import RegisterSmsRequest
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = users_api.UsersApi(api_client)
    register_sms_request = RegisterSmsRequest(
        sms_number="11235555555",
    ) # RegisterSmsRequest | a SMS Number to send an OTP to

    # example passing only required values which don't have defaults set
    try:
        # Register SMS Number
        api_instance.register_sms(register_sms_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->register_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_sms_request** | [**RegisterSmsRequest**](RegisterSmsRequest.md)| a SMS Number to send an OTP to |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | request completed okay |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_token**
> resend_token(user_id, resend_token_request)

Resend a token

<p>Resend the specified token </p> <p>The token to resend must already exist for the user </p> <p>It will be revoked and a new one issued</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.resend_token_request import ResendTokenRequest
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.
    resend_token_request = ResendTokenRequest(
        token_type="INVITE_MFA_USER",
        verification_code="123456",
    ) # ResendTokenRequest | The type of token to resend

    # example passing only required values which don't have defaults set
    try:
        # Resend a token
        api_instance.resend_token(user_id, resend_token_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->resend_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |
 **resend_token_request** | [**ResendTokenRequest**](ResendTokenRequest.md)| The type of token to resend |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | request completed okay |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **role_update**
> role_update(user_id, role_update_request)

Update User Role

<p>Update the user's Role</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.role_update_request import RoleUpdateRequest
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.
    role_update_request = RoleUpdateRequest(
        roles=["payor.admin"],
        verification_code="123456",
    ) # RoleUpdateRequest | The Role to change to

    # example passing only required values which don't have defaults set
    try:
        # Update User Role
        api_instance.role_update(user_id, role_update_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->role_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |
 **role_update_request** | [**RoleUpdateRequest**](RoleUpdateRequest.md)| The Role to change to |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | request completed okay |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlock_user_v2**
> unlock_user_v2(user_id)

Unlock a User

If a user is locked this endpoint will unlock them 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.

    # example passing only required values which don't have defaults set
    try:
        # Unlock a User
        api_instance.unlock_user_v2(user_id)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->unlock_user_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |

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
**204** | Success the user was unlocked or was already unlocked |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_mfa**
> unregister_mfa(user_id, unregister_mfa_request)

Unregister MFA for the user

<p>Unregister the MFA device for the user </p> <p>If the user does not require further verification then a register new MFA device token will be sent to them via their email address</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.unregister_mfa_request import UnregisterMFARequest
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.
    unregister_mfa_request = UnregisterMFARequest(
        mfa_type="TOTP",
        verification_code="123456",
    ) # UnregisterMFARequest | The MFA Type to unregister

    # example passing only required values which don't have defaults set
    try:
        # Unregister MFA for the user
        api_instance.unregister_mfa(user_id, unregister_mfa_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->unregister_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |
 **unregister_mfa_request** | [**UnregisterMFARequest**](UnregisterMFARequest.md)| The MFA Type to unregister |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the MFA Type to unregister |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_mfa_for_self**
> unregister_mfa_for_self(self_mfa_type_unregister_request)

Unregister MFA for Self

<p>Unregister the MFA device for the user </p> <p>If the user does not require further verification then a register new MFA device token will be sent to them via their email address</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.self_mfa_type_unregister_request import SelfMFATypeUnregisterRequest
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = users_api.UsersApi(api_client)
    self_mfa_type_unregister_request = SelfMFATypeUnregisterRequest(
        mfa_type="TOTP",
    ) # SelfMFATypeUnregisterRequest | The MFA Type to unregister
    authorization = "Authorization_example" # str | Bearer token authorization leg of validate (optional)

    # example passing only required values which don't have defaults set
    try:
        # Unregister MFA for Self
        api_instance.unregister_mfa_for_self(self_mfa_type_unregister_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->unregister_mfa_for_self: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Unregister MFA for Self
        api_instance.unregister_mfa_for_self(self_mfa_type_unregister_request, authorization=authorization)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->unregister_mfa_for_self: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_mfa_type_unregister_request** | [**SelfMFATypeUnregisterRequest**](SelfMFATypeUnregisterRequest.md)| The MFA Type to unregister |
 **authorization** | **str**| Bearer token authorization leg of validate | [optional]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the MFA Type to unregister |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_self**
> update_password_self(self_update_password_request)

Update Password for self

Update password for self 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.self_update_password_request import SelfUpdatePasswordRequest
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = users_api.UsersApi(api_client)
    self_update_password_request = SelfUpdatePasswordRequest(
        old_password="My_current_password",
        new_password="My_new_password",
    ) # SelfUpdatePasswordRequest | The password

    # example passing only required values which don't have defaults set
    try:
        # Update Password for self
        api_instance.update_password_self(self_update_password_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->update_password_self: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **self_update_password_request** | [**SelfUpdatePasswordRequest**](SelfUpdatePasswordRequest.md)| The password |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | the password was submitted and accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_details_update**
> user_details_update(user_id, user_details_update_request)

Update User Details

<p>Update the profile details for the given user</p> <p>When updating Payor users with the role of payor.master_admin a verificationCode is required</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.user_details_update_request import UserDetailsUpdateRequest
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.inline_response409 import InlineResponse409
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
    api_instance = users_api.UsersApi(api_client)
    user_id = "userId_example" # str | The UUID of the User.
    user_details_update_request = UserDetailsUpdateRequest(
        primary_contact_number="11235555555",
        secondary_contact_number="11235555550",
        first_name="John",
        last_name="Doe",
        email="foo@example.com",
        sms_number="11235555555",
        mfa_type=MFAType("TOTP"),
        verification_code="123456",
    ) # UserDetailsUpdateRequest | The details of the user to update

    # example passing only required values which don't have defaults set
    try:
        # Update User Details
        api_instance.user_details_update(user_id, user_details_update_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->user_details_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| The UUID of the User. |
 **user_details_update_request** | [**UserDetailsUpdateRequest**](UserDetailsUpdateRequest.md)| The details of the user to update |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | request completed okay |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_details_update_for_self**
> user_details_update_for_self(payee_user_self_update_request)

Update User Details for self

<p>Update the profile details for the given user</p> <p>Only Payee user types are supported</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.payee_user_self_update_request import PayeeUserSelfUpdateRequest
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response409 import InlineResponse409
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
    api_instance = users_api.UsersApi(api_client)
    payee_user_self_update_request = PayeeUserSelfUpdateRequest(
        primary_contact_number="11235555555",
        secondary_contact_number="11235555550",
        first_name="John",
        last_name="Doe",
        email="foo@example.com",
        sms_number="11235555555",
    ) # PayeeUserSelfUpdateRequest | The details of the user to update

    # example passing only required values which don't have defaults set
    try:
        # Update User Details for self
        api_instance.user_details_update_for_self(payee_user_self_update_request)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->user_details_update_for_self: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_user_self_update_request** | [**PayeeUserSelfUpdateRequest**](PayeeUserSelfUpdateRequest.md)| The details of the user to update |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | request completed okay |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_password_self**
> ValidatePasswordResponse validate_password_self(password_request)

Validate the proposed password

validate the password and return a score 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import users_api
from velo_payments.model.validate_password_response import ValidatePasswordResponse
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.password_request import PasswordRequest
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = users_api.UsersApi(api_client)
    password_request = PasswordRequest(
        password="My_strong_password",
    ) # PasswordRequest | The password

    # example passing only required values which don't have defaults set
    try:
        # Validate the proposed password
        api_response = api_instance.validate_password_self(password_request)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling UsersApi->validate_password_self: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_request** | [**PasswordRequest**](PasswordRequest.md)| The password |

### Return type

[**ValidatePasswordResponse**](ValidatePasswordResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the password was checked and a score returned |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

