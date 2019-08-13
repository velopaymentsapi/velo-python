# velo_payments.PayorApplicationsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payor_create_api_key_request**](PayorApplicationsApi.md#payor_create_api_key_request) | **POST** /v1/payors/{payorId}/applications/{applicationId}/keys | Create API Key
[**payor_create_application_request**](PayorApplicationsApi.md#payor_create_application_request) | **POST** /v1/payors/{payorId}/applications | Create Application


# **payor_create_api_key_request**
> PayorCreateApiKeyResponse payor_create_api_key_request(payor_id, application_id, payor_create_api_key_request)

Create API Key

Create an an API key for the given payor Id and application Id

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
api_instance = velo_payments.PayorApplicationsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
application_id = 'application_id_example' # str | Application ID
payor_create_api_key_request = velo_payments.PayorCreateApiKeyRequest() # PayorCreateApiKeyRequest | Details of application API key to create

try:
    # Create API Key
    api_response = api_instance.payor_create_api_key_request(payor_id, application_id, payor_create_api_key_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayorApplicationsApi->payor_create_api_key_request: %s\n" % e)
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
**400** | Invalid Request Body or Payor in Invalid State |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payor_create_application_request**
> payor_create_application_request(payor_id, payor_create_application_request)

Create Application

Create an application for the given Payor ID. Applications are programatic users which can be assigned unique keys.

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
api_instance = velo_payments.PayorApplicationsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
payor_create_application_request = velo_payments.PayorCreateApplicationRequest() # PayorCreateApplicationRequest | Details of application to create

try:
    # Create Application
    api_instance.payor_create_application_request(payor_id, payor_create_application_request)
except ApiException as e:
    print("Exception when calling PayorApplicationsApi->payor_create_application_request: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  * Location - location <br>  |
**400** | invalid request body or payor in invalid state |  -  |
**404** | Payor not found. |  -  |
**409** | Application name conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

