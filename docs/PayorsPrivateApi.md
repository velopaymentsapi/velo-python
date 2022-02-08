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
import time
import velo_payments
from velo_payments.api import payors_private_api
from velo_payments.model.create_payor_link_request import CreatePayorLinkRequest
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

# Configure OAuth2 access token for authorization: oAuthVeloBackOffice
configuration = velo_payments.Configuration(
    host = "https://api.sandbox.velopayments.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = payors_private_api.PayorsPrivateApi(api_client)
    create_payor_link_request = CreatePayorLinkRequest(
        from_payor_id="from_payor_id_example",
        link_type="PARENT_OF",
        to_payor_id="to_payor_id_example",
    ) # CreatePayorLinkRequest | Request to create a payor link

    # example passing only required values which don't have defaults set
    try:
        # Create a Payor Link
        api_instance.create_payor_links(create_payor_link_request)
    except velo_payments.ApiException as e:
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
**404** | The resource was not found or is no longer available  |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

