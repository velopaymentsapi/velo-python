# velo_payments.PayorsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payor_by_id_v2**](PayorsApi.md#get_payor_by_id_v2) | **GET** /v2/payors/{payorId} | Get Payor
[**payor_add_payor_logo_v1**](PayorsApi.md#payor_add_payor_logo_v1) | **POST** /v1/payors/{payorId}/branding/logos | Add Logo
[**payor_create_api_key_v1**](PayorsApi.md#payor_create_api_key_v1) | **POST** /v1/payors/{payorId}/applications/{applicationId}/keys | Create API Key
[**payor_create_application_v1**](PayorsApi.md#payor_create_application_v1) | **POST** /v1/payors/{payorId}/applications | Create Application
[**payor_email_opt_out**](PayorsApi.md#payor_email_opt_out) | **POST** /v1/payors/{payorId}/reminderEmailsUpdate | Reminder Email Opt-Out
[**payor_get_branding**](PayorsApi.md#payor_get_branding) | **GET** /v1/payors/{payorId}/branding | Get Branding


# **get_payor_by_id_v2**
> PayorV2 get_payor_by_id_v2(payor_id)

Get Payor

Get a Single Payor by Id. 

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
api_instance = velo_payments.PayorsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID

try:
    # Get Payor
    api_response = api_instance.get_payor_by_id_v2(payor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayorsApi->get_payor_by_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 

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

# **payor_add_payor_logo_v1**
> payor_add_payor_logo_v1(payor_id, logo=logo)

Add Logo

<p>Add Payor Logo</p> <p>Logo file is used in your branding and emails sent to payees</p> 

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
api_instance = velo_payments.PayorsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
logo = '/path/to/file' # file |  (optional)

try:
    # Add Logo
    api_instance.payor_add_payor_logo_v1(payor_id, logo=logo)
except ApiException as e:
    print("Exception when calling PayorsApi->payor_add_payor_logo_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **logo** | **file**|  | [optional] 

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

# **payor_create_api_key_v1**
> PayorCreateApiKeyResponse payor_create_api_key_v1(payor_id, application_id, payor_create_api_key_request)

Create API Key

<p>Create an an API key for the given payor Id and application Id</p> <p>You can create multiple API Keys for a given application</p> <p>API Keys are programmatic users for integrating your application with the Velo platform</p> <p>The response will return the API Key and the secret. This is the only time you will be able to see the secret</p> 

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
api_instance = velo_payments.PayorsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
application_id = 'application_id_example' # str | Application ID
payor_create_api_key_request = velo_payments.PayorCreateApiKeyRequest() # PayorCreateApiKeyRequest | Details of application API key to create

try:
    # Create API Key
    api_response = api_instance.payor_create_api_key_v1(payor_id, application_id, payor_create_api_key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayorsApi->payor_create_api_key_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **application_id** | [**str**](.md)| Application ID | 
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

# **payor_create_application_v1**
> payor_create_application_v1(payor_id, payor_create_application_request)

Create Application

<p>Create an application for the given Payor ID.</p> <p>Applications provide a means to group your API Keys</p> <p>For example you might have an SAP application that you wish to integrate with Velo</p> <p>You can create an application and then create one or more API keys for the application</p> 

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
api_instance = velo_payments.PayorsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
payor_create_application_request = velo_payments.PayorCreateApplicationRequest() # PayorCreateApplicationRequest | Details of application to create

try:
    # Create Application
    api_instance.payor_create_application_v1(payor_id, payor_create_application_request)
except ApiException as e:
    print("Exception when calling PayorsApi->payor_create_application_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
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
**201** | Success |  * Location - location <br>  |
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
api_instance = velo_payments.PayorsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
payor_email_opt_out_request = velo_payments.PayorEmailOptOutRequest() # PayorEmailOptOutRequest | Reminder Emails Opt-Out Request

try:
    # Reminder Email Opt-Out
    api_instance.payor_email_opt_out(payor_id, payor_email_opt_out_request)
except ApiException as e:
    print("Exception when calling PayorsApi->payor_email_opt_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
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
api_instance = velo_payments.PayorsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID

try:
    # Get Branding
    api_response = api_instance.payor_get_branding(payor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayorsApi->payor_get_branding: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 

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

