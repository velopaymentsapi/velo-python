# velo_payments.PayorsPrivateApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payor_links**](PayorsPrivateApi.md#create_payor_links) | **POST** /v1/payorLinks | Create a Payor Link


# **create_payor_links**
> create_payor_links(create_payor_link_request)

Create a Payor Link

This endpoint allows you to create a payor link.

### Example

* OAuth Authentication (oAuthVeloBackOffice):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint
configuration = velo_payments.Configuration()
# Configure OAuth2 access token for authorization: oAuthVeloBackOffice
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.sandbox.velopayments.com
configuration.host = "https://api.sandbox.velopayments.com"

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.PayorsPrivateApi(api_client)
    create_payor_link_request = velo_payments.CreatePayorLinkRequest() # CreatePayorLinkRequest | Request to create a payor link

    try:
        # Create a Payor Link
        api_instance.create_payor_links(create_payor_link_request)
    except ApiException as e:
        print("Exception when calling PayorsPrivateApi->create_payor_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payor_link_request** | [**CreatePayorLinkRequest**](CreatePayorLinkRequest.md)| Request to create a payor link | 

### Return type

void (empty response body)

### Authorization

[oAuthVeloBackOffice](../README.md#oAuthVeloBackOffice)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | HTTP Creeated |  * Location - URI to location of created resource <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**404** | Resource not found |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

