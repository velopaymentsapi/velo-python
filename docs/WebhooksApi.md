# velo_payments.WebhooksApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_webhook_v1**](WebhooksApi.md#create_webhook_v1) | **POST** /v1/webhooks | Create Webhook
[**get_webhook_v1**](WebhooksApi.md#get_webhook_v1) | **GET** /v1/webhooks/{webhookId} | Get details about the given webhook.
[**list_webhooks_v1**](WebhooksApi.md#list_webhooks_v1) | **GET** /v1/webhooks | List the details about the webhooks for the given payor.
[**ping_webhook_v1**](WebhooksApi.md#ping_webhook_v1) | **POST** /v1/webhooks/{webhookId}/ping | 
[**update_webhook_v1**](WebhooksApi.md#update_webhook_v1) | **POST** /v1/webhooks/{webhookId} | Update Webhook


# **create_webhook_v1**
> create_webhook_v1()

Create Webhook

Create Webhook

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import webhooks_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.create_webhook_request import CreateWebhookRequest
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    create_webhook_request = CreateWebhookRequest(
        payor_id="payor_id_example",
        webhook_url="webhook_url_example",
        authorization_header="/",
        enabled=True,
        categories=[
            Category("payment"),
        ],
    ) # CreateWebhookRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Webhook
        api_instance.create_webhook_v1(create_webhook_request=create_webhook_request)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->create_webhook_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_webhook_request** | [**CreateWebhookRequest**](CreateWebhookRequest.md)|  | [optional]

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
**201** | Webhook Created |  * Location - Reference to Webhook object <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_webhook_v1**
> WebhookResponse get_webhook_v1(webhook_id)

Get details about the given webhook.

Get details about the given webhook.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import webhooks_api
from velo_payments.model.webhook_response import WebhookResponse
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhook_id = "webhookId_example" # str | Webhook id

    # example passing only required values which don't have defaults set
    try:
        # Get details about the given webhook.
        api_response = api_instance.get_webhook_v1(webhook_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->get_webhook_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook id |

### Return type

[**WebhookResponse**](WebhookResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook response |  -  |
**400** | Bad Request, Invalid path parameter |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_webhooks_v1**
> WebhooksResponse list_webhooks_v1(payor_id)

List the details about the webhooks for the given payor.

List the details about the webhooks for the given payor.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import webhooks_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.webhooks_response import WebhooksResponse
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    payor_id = "payorId_example" # str | The Payor ID
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # List the details about the webhooks for the given payor.
        api_response = api_instance.list_webhooks_v1(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->list_webhooks_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the details about the webhooks for the given payor.
        api_response = api_instance.list_webhooks_v1(payor_id, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->list_webhooks_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor ID |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25

### Return type

[**WebhooksResponse**](WebhooksResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Webhook response |  -  |
**400** | Invalid Request Parameters |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ping_webhook_v1**
> PingResponse ping_webhook_v1(webhook_id)



### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import webhooks_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.ping_response import PingResponse
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhook_id = "webhookId_example" # str | Webhook id

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.ping_webhook_v1(webhook_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->ping_webhook_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook id |

### Return type

[**PingResponse**](PingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Send ping |  -  |
**400** | Bad Request, Invalid path parameter |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_webhook_v1**
> update_webhook_v1(webhook_id)

Update Webhook

Update Webhook

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import webhooks_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.update_webhook_request import UpdateWebhookRequest
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
    api_instance = webhooks_api.WebhooksApi(api_client)
    webhook_id = "webhookId_example" # str | Webhook id
    update_webhook_request = UpdateWebhookRequest(
        webhook_url="webhook_url_example",
        authorization_header="/",
        enabled=True,
        categories=[
            Category("payment"),
        ],
    ) # UpdateWebhookRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Webhook
        api_instance.update_webhook_v1(webhook_id)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->update_webhook_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Webhook
        api_instance.update_webhook_v1(webhook_id, update_webhook_request=update_webhook_request)
    except velo_payments.ApiException as e:
        print("Exception when calling WebhooksApi->update_webhook_v1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **webhook_id** | **str**| Webhook id |
 **update_webhook_request** | [**UpdateWebhookRequest**](UpdateWebhookRequest.md)|  | [optional]

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
**204** | Webhook Updated |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

