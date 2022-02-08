# velo_payments.PayorsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payor_by_id**](PayorsApi.md#get_payor_by_id) | **GET** /v1/payors/{payorId} | Get Payor
[**get_payor_by_id_v2**](PayorsApi.md#get_payor_by_id_v2) | **GET** /v2/payors/{payorId} | Get Payor
[**payor_add_payor_logo**](PayorsApi.md#payor_add_payor_logo) | **POST** /v1/payors/{payorId}/branding/logos | Add Logo
[**payor_create_api_key_request**](PayorsApi.md#payor_create_api_key_request) | **POST** /v1/payors/{payorId}/applications/{applicationId}/keys | Create API Key
[**payor_create_application_request**](PayorsApi.md#payor_create_application_request) | **POST** /v1/payors/{payorId}/applications | Create Application
[**payor_email_opt_out**](PayorsApi.md#payor_email_opt_out) | **POST** /v1/payors/{payorId}/reminderEmailsUpdate | Reminder Email Opt-Out
[**payor_get_branding**](PayorsApi.md#payor_get_branding) | **GET** /v1/payors/{payorId}/branding | Get Branding
[**payor_links**](PayorsApi.md#payor_links) | **GET** /v1/payorLinks | List Payor Links


# **get_payor_by_id**
> PayorV1 get_payor_by_id(payor_id)

Get Payor

Get a Single Payor by Id. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.payor_v1 import PayorV1
from velo_payments.model.error_response import ErrorResponse
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id

    # example passing only required values which don't have defaults set
    try:
        # Get Payor
        api_response = api_instance.get_payor_by_id(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->get_payor_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |

### Return type

[**PayorV1**](PayorV1.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Payor Details |  -  |
**404** | Payor Id Not Found |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payor_by_id_v2**
> PayorV2 get_payor_by_id_v2(payor_id)

Get Payor

Get a Single Payor by Id. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.payor_v2 import PayorV2
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.error_response import ErrorResponse
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id

    # example passing only required values which don't have defaults set
    try:
        # Get Payor
        api_response = api_instance.get_payor_by_id_v2(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->get_payor_by_id_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |

### Return type

[**PayorV2**](PayorV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Payor Details |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_add_payor_logo**
> payor_add_payor_logo(payor_id)

Add Logo

Add Payor Logo. Logo file is used in your branding, and emails sent to payees.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id
    logo = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Logo
        api_instance.payor_add_payor_logo(payor_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_add_payor_logo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Logo
        api_instance.payor_add_payor_logo(payor_id, logo=logo)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_add_payor_logo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |
 **logo** | **file_type**|  | [optional]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_create_api_key_request**
> PayorCreateApiKeyResponse payor_create_api_key_request(payor_id, application_id, payor_create_api_key_request)

Create API Key

Create an an API key for the given payor Id and application Id

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.payor_create_api_key_request import PayorCreateApiKeyRequest
from velo_payments.model.payor_create_api_key_response import PayorCreateApiKeyResponse
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id
    application_id = "applicationId_example" # str | Application ID
    payor_create_api_key_request = PayorCreateApiKeyRequest(
        name="iOS Key",
        description="Key for iOS mobile application",
        roles=["payor.admin"],
    ) # PayorCreateApiKeyRequest | Details of application API key to create

    # example passing only required values which don't have defaults set
    try:
        # Create API Key
        api_response = api_instance.payor_create_api_key_request(payor_id, application_id, payor_create_api_key_request)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_create_api_key_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |
 **application_id** | **str**| Application ID |
 **payor_create_api_key_request** | [**PayorCreateApiKeyRequest**](PayorCreateApiKeyRequest.md)| Details of application API key to create |

### Return type

[**PayorCreateApiKeyResponse**](PayorCreateApiKeyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Ok, key created |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_create_application_request**
> payor_create_application_request(payor_id, payor_create_application_request)

Create Application

Create an application for the given Payor ID. Applications are programatic users which can be assigned unique keys.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.payor_create_application_request import PayorCreateApplicationRequest
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id
    payor_create_application_request = PayorCreateApplicationRequest(
        name="SAP",
        description="SAP Application integration",
    ) # PayorCreateApplicationRequest | Details of application to create

    # example passing only required values which don't have defaults set
    try:
        # Create Application
        api_instance.payor_create_application_request(payor_id, payor_create_application_request)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_create_application_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |
 **payor_create_application_request** | [**PayorCreateApplicationRequest**](PayorCreateApplicationRequest.md)| Details of application to create |

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
**201** | Success |  * Location - Reference to Webhook object <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_email_opt_out**
> payor_email_opt_out(payor_id, payor_email_opt_out_request)

Reminder Email Opt-Out

Update the emailRemindersOptOut field for a Payor. This API can be used to opt out or opt into Payor Reminder emails. These emails are typically around payee events such as payees registering and onboarding. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.error_response import ErrorResponse
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.payor_email_opt_out_request import PayorEmailOptOutRequest
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id
    payor_email_opt_out_request = PayorEmailOptOutRequest(
        reminder_emails_opt_out=True,
    ) # PayorEmailOptOutRequest | Reminder Emails Opt-Out Request

    # example passing only required values which don't have defaults set
    try:
        # Reminder Email Opt-Out
        api_instance.payor_email_opt_out(payor_id, payor_email_opt_out_request)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_email_opt_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |
 **payor_email_opt_out_request** | [**PayorEmailOptOutRequest**](PayorEmailOptOutRequest.md)| Reminder Emails Opt-Out Request |

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
**202** | HTTP Accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_get_branding**
> PayorBrandingResponse payor_get_branding(payor_id)

Get Branding

Get the payor branding details.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.error_response import ErrorResponse
from velo_payments.model.payor_branding_response import PayorBrandingResponse
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
    api_instance = payors_api.PayorsApi(api_client)
    payor_id = "payorId_example" # str | The Payor Id

    # example passing only required values which don't have defaults set
    try:
        # Get Branding
        api_response = api_instance.payor_get_branding(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_get_branding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor Id |

### Return type

[**PayorBrandingResponse**](PayorBrandingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | HTTP Ok, key created |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_links**
> PayorLinksResponse payor_links()

List Payor Links

This endpoint allows you to list payor links

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payors_api
from velo_payments.model.payor_links_response import PayorLinksResponse
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
    api_instance = payors_api.PayorsApi(api_client)
    descendants_of_payor = "descendantsOfPayor_example" # str | The Payor ID from which to start the query to show all descendants (optional)
    parent_of_payor = "parentOfPayor_example" # str | Look for the parent payor details for this payor id (optional)
    fields = "fields_example" # str | List of additional Payor fields to include in the response for each Payor. The values of payorId and payorName and always included for each Payor - 'fields' allows you to add to this. Example: ```fields=primaryContactEmail,kycState``` - will include payorId+payorName+primaryContactEmail+kycState for each Payor Default if not specified is to include only payorId and payorName. The supported fields are any combination of: primaryContactEmail,kycState  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payor Links
        api_response = api_instance.payor_links(descendants_of_payor=descendants_of_payor, parent_of_payor=parent_of_payor, fields=fields)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayorsApi->payor_links: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descendants_of_payor** | **str**| The Payor ID from which to start the query to show all descendants | [optional]
 **parent_of_payor** | **str**| Look for the parent payor details for this payor id | [optional]
 **fields** | **str**| List of additional Payor fields to include in the response for each Payor. The values of payorId and payorName and always included for each Payor - &#39;fields&#39; allows you to add to this. Example: &#x60;&#x60;&#x60;fields&#x3D;primaryContactEmail,kycState&#x60;&#x60;&#x60; - will include payorId+payorName+primaryContactEmail+kycState for each Payor Default if not specified is to include only payorId and payorName. The supported fields are any combination of: primaryContactEmail,kycState  | [optional]

### Return type

[**PayorLinksResponse**](PayorLinksResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payor Links |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

