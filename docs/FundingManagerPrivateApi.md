# velo_payments.FundingManagerPrivateApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_funding_account_v2**](FundingManagerPrivateApi.md#create_funding_account_v2) | **POST** /v2/fundingAccounts | Create Funding Account
[**delete_source_account_v3**](FundingManagerPrivateApi.md#delete_source_account_v3) | **DELETE** /v3/sourceAccounts/{sourceAccountId} | Delete a source account by ID


# **create_funding_account_v2**
> create_funding_account_v2()

Create Funding Account

Create Funding Account

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_private_api
from velo_payments.model.create_funding_account_request_v2 import CreateFundingAccountRequestV2
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
    api_instance = funding_manager_private_api.FundingManagerPrivateApi(api_client)
    create_funding_account_request_v2 = CreateFundingAccountRequestV2(
        type="FBO",
        name="name_example",
        payor_id="payor_id_example",
        account_name="account_name_example",
        account_number="account_number_example",
        routing_number="routing_number_example",
        currency="USD",
    ) # CreateFundingAccountRequestV2 |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Funding Account
        api_instance.create_funding_account_v2(create_funding_account_request_v2=create_funding_account_request_v2)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerPrivateApi->create_funding_account_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_funding_account_request_v2** | [**CreateFundingAccountRequestV2**](CreateFundingAccountRequestV2.md)|  | [optional]

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
**202** | Funding Account Creation Request Accepted |  * Location - Reference to created payout <br>  * Retry-After - How long the user agent should wait before making a follow-up request (seconds) <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_account_v3**
> delete_source_account_v3(source_account_id)

Delete a source account by ID

Mark a source account as deleted by ID

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_private_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = funding_manager_private_api.FundingManagerPrivateApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id

    # example passing only required values which don't have defaults set
    try:
        # Delete a source account by ID
        api_instance.delete_source_account_v3(source_account_id)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerPrivateApi->delete_source_account_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |

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
**204** | No Content - Source account is deleted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

