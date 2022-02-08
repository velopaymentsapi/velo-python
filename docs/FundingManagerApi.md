# velo_payments.FundingManagerApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ach_funding_request**](FundingManagerApi.md#create_ach_funding_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/achFundingRequest | Create Funding Request
[**create_funding_request**](FundingManagerApi.md#create_funding_request) | **POST** /v2/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request
[**create_funding_request_v3**](FundingManagerApi.md#create_funding_request_v3) | **POST** /v3/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request
[**get_funding_account**](FundingManagerApi.md#get_funding_account) | **GET** /v1/fundingAccounts/{fundingAccountId} | Get Funding Account
[**get_funding_account_v2**](FundingManagerApi.md#get_funding_account_v2) | **GET** /v2/fundingAccounts/{fundingAccountId} | Get Funding Account
[**get_funding_accounts**](FundingManagerApi.md#get_funding_accounts) | **GET** /v1/fundingAccounts | Get Funding Accounts
[**get_funding_accounts_v2**](FundingManagerApi.md#get_funding_accounts_v2) | **GET** /v2/fundingAccounts | Get Funding Accounts
[**get_source_account**](FundingManagerApi.md#get_source_account) | **GET** /v1/sourceAccounts/{sourceAccountId} | Get details about given source account.
[**get_source_account_v2**](FundingManagerApi.md#get_source_account_v2) | **GET** /v2/sourceAccounts/{sourceAccountId} | Get details about given source account.
[**get_source_account_v3**](FundingManagerApi.md#get_source_account_v3) | **GET** /v3/sourceAccounts/{sourceAccountId} | Get details about given source account.
[**get_source_accounts**](FundingManagerApi.md#get_source_accounts) | **GET** /v1/sourceAccounts | Get list of source accounts
[**get_source_accounts_v2**](FundingManagerApi.md#get_source_accounts_v2) | **GET** /v2/sourceAccounts | Get list of source accounts
[**get_source_accounts_v3**](FundingManagerApi.md#get_source_accounts_v3) | **GET** /v3/sourceAccounts | Get list of source accounts
[**list_funding_audit_deltas**](FundingManagerApi.md#list_funding_audit_deltas) | **GET** /v1/deltas/fundings | Get Funding Audit Delta
[**set_notifications_request**](FundingManagerApi.md#set_notifications_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/notifications | Set notifications
[**transfer_funds**](FundingManagerApi.md#transfer_funds) | **POST** /v2/sourceAccounts/{sourceAccountId}/transfers | Transfer Funds between source accounts
[**transfer_funds_v3**](FundingManagerApi.md#transfer_funds_v3) | **POST** /v3/sourceAccounts/{sourceAccountId}/transfers | Transfer Funds between source accounts


# **create_ach_funding_request**
> create_ach_funding_request(source_account_id, funding_request_v1)

Create Funding Request

Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.funding_request_v1 import FundingRequestV1
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id
    funding_request_v1 = FundingRequestV1(
        amount=1,
    ) # FundingRequestV1 | Body to included amount to be funded

    # example passing only required values which don't have defaults set
    try:
        # Create Funding Request
        api_instance.create_ach_funding_request(source_account_id, funding_request_v1)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->create_ach_funding_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |
 **funding_request_v1** | [**FundingRequestV1**](FundingRequestV1.md)| Body to included amount to be funded |

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
**202** | Request Accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_funding_request**
> create_funding_request(source_account_id, funding_request_v2)

Create Funding Request

Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo  (202 - accepted, 400 - invalid request body, 404 - source account not found).

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.funding_request_v2 import FundingRequestV2
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id
    funding_request_v2 = FundingRequestV2(
        amount=1,
    ) # FundingRequestV2 | Body to included amount to be funded

    # example passing only required values which don't have defaults set
    try:
        # Create Funding Request
        api_instance.create_funding_request(source_account_id, funding_request_v2)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->create_funding_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |
 **funding_request_v2** | [**FundingRequestV2**](FundingRequestV2.md)| Body to included amount to be funded |

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
**202** | Request Accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_funding_request_v3**
> create_funding_request_v3(source_account_id, funding_request_v3)

Create Funding Request

Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo  (202 - accepted, 400 - invalid request body, 404 - source account not found).

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.funding_request_v3 import FundingRequestV3
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id
    funding_request_v3 = FundingRequestV3(
        funding_account_id="funding_account_id_example",
        amount=1,
    ) # FundingRequestV3 | Body to included amount to be funded

    # example passing only required values which don't have defaults set
    try:
        # Create Funding Request
        api_instance.create_funding_request_v3(source_account_id, funding_request_v3)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->create_funding_request_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |
 **funding_request_v3** | [**FundingRequestV3**](FundingRequestV3.md)| Body to included amount to be funded |

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
**202** | Request Accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_funding_account**
> FundingAccountResponse get_funding_account(funding_account_id)

Get Funding Account

Get Funding Account by ID

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.funding_account_response import FundingAccountResponse
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    funding_account_id = "fundingAccountId_example" # str | 
    sensitive = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Funding Account
        api_response = api_instance.get_funding_account(funding_account_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_funding_account: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Funding Account
        api_response = api_instance.get_funding_account(funding_account_id, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_funding_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funding_account_id** | **str**|  |
 **sensitive** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**FundingAccountResponse**](FundingAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Funding Account Response |  -  |
**400** | Bad Request |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_funding_account_v2**
> FundingAccountResponse2 get_funding_account_v2(funding_account_id)

Get Funding Account

Get Funding Account by ID

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.funding_account_response2 import FundingAccountResponse2
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    funding_account_id = "fundingAccountId_example" # str | 
    sensitive = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get Funding Account
        api_response = api_instance.get_funding_account_v2(funding_account_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_funding_account_v2: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Funding Account
        api_response = api_instance.get_funding_account_v2(funding_account_id, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_funding_account_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funding_account_id** | **str**|  |
 **sensitive** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**FundingAccountResponse2**](FundingAccountResponse2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Funding Account Response |  -  |
**400** | Bad Request |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_funding_accounts**
> ListFundingAccountsResponse get_funding_accounts()

Get Funding Accounts

Get the funding accounts.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.list_funding_accounts_response import ListFundingAccountsResponse
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    payor_id = "payorId_example" # str |  (optional)
    source_account_id = "sourceAccountId_example" # str |  (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "accountName:asc" # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name and currency. (optional) if omitted the server will use the default value of "accountName:asc"
    sensitive = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Funding Accounts
        api_response = api_instance.get_funding_accounts(payor_id=payor_id, source_account_id=source_account_id, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_funding_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**|  | [optional]
 **source_account_id** | **str**|  | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name and currency. | [optional] if omitted the server will use the default value of "accountName:asc"
 **sensitive** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**ListFundingAccountsResponse**](ListFundingAccountsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Funding Accounts Response |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_funding_accounts_v2**
> ListFundingAccountsResponse2 get_funding_accounts_v2()

Get Funding Accounts

Get the funding accounts.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.list_funding_accounts_response2 import ListFundingAccountsResponse2
from velo_payments.model.funding_account_type import FundingAccountType
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    payor_id = "payorId_example" # str |  (optional)
    name = "name_example" # str | The descriptive funding account name (optional)
    country = "US" # str | The 2 letter ISO 3166-1 country code (upper case) (optional)
    currency = "USD" # str | The ISO 4217 currency code (optional)
    type = FundingAccountType("FBO") # FundingAccountType | The type of funding account. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "accountName:asc" # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. (optional) if omitted the server will use the default value of "accountName:asc"
    sensitive = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Funding Accounts
        api_response = api_instance.get_funding_accounts_v2(payor_id=payor_id, name=name, country=country, currency=currency, type=type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_funding_accounts_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**|  | [optional]
 **name** | **str**| The descriptive funding account name | [optional]
 **country** | **str**| The 2 letter ISO 3166-1 country code (upper case) | [optional]
 **currency** | **str**| The ISO 4217 currency code | [optional]
 **type** | **FundingAccountType**| The type of funding account. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. | [optional] if omitted the server will use the default value of "accountName:asc"
 **sensitive** | **bool**|  | [optional] if omitted the server will use the default value of False

### Return type

[**ListFundingAccountsResponse2**](ListFundingAccountsResponse2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Funding Accounts Response |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_account**
> SourceAccountResponse get_source_account(source_account_id)

Get details about given source account.

Get details about given source account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.source_account_response import SourceAccountResponse
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id

    # example passing only required values which don't have defaults set
    try:
        # Get details about given source account.
        api_response = api_instance.get_source_account(source_account_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_source_account: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |

### Return type

[**SourceAccountResponse**](SourceAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source account response |  -  |
**400** | Bad Request, Invalid path parameter |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_account_v2**
> SourceAccountResponseV2 get_source_account_v2(source_account_id)

Get details about given source account.

Get details about given source account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.source_account_response_v2 import SourceAccountResponseV2
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id

    # example passing only required values which don't have defaults set
    try:
        # Get details about given source account.
        api_response = api_instance.get_source_account_v2(source_account_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_source_account_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |

### Return type

[**SourceAccountResponseV2**](SourceAccountResponseV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source account response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_account_v3**
> SourceAccountResponseV3 get_source_account_v3(source_account_id)

Get details about given source account.

Get details about given source account.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.source_account_response_v3 import SourceAccountResponseV3
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id

    # example passing only required values which don't have defaults set
    try:
        # Get details about given source account.
        api_response = api_instance.get_source_account_v3(source_account_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_source_account_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |

### Return type

[**SourceAccountResponseV3**](SourceAccountResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Source account response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_accounts**
> ListSourceAccountResponse get_source_accounts()

Get list of source accounts

List source accounts.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.list_source_account_response import ListSourceAccountResponse
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    physical_account_name = "physicalAccountName_example" # str | Physical Account Name (optional)
    payor_id = "payorId_example" # str | The account owner Payor ID (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "fundingRef:asc" # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef  (optional) if omitted the server will use the default value of "fundingRef:asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of source accounts
        api_response = api_instance.get_source_accounts(physical_account_name=physical_account_name, payor_id=payor_id, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_source_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional]
 **payor_id** | **str**| The account owner Payor ID | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef  | [optional] if omitted the server will use the default value of "fundingRef:asc"

### Return type

[**ListSourceAccountResponse**](ListSourceAccountResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Source Account response |  -  |
**400** | Invalid Request Parameters |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_accounts_v2**
> ListSourceAccountResponseV2 get_source_accounts_v2()

Get list of source accounts

List source accounts.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.list_source_account_response_v2 import ListSourceAccountResponseV2
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    physical_account_name = "physicalAccountName_example" # str | Physical Account Name (optional)
    physical_account_id = "physicalAccountId_example" # str | The physical account ID (optional)
    payor_id = "payorId_example" # str | The account owner Payor ID (optional)
    funding_account_id = "fundingAccountId_example" # str | The funding account ID (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "fundingRef:asc" # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) if omitted the server will use the default value of "fundingRef:asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of source accounts
        api_response = api_instance.get_source_accounts_v2(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_source_accounts_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional]
 **physical_account_id** | **str**| The physical account ID | [optional]
 **payor_id** | **str**| The account owner Payor ID | [optional]
 **funding_account_id** | **str**| The funding account ID | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  | [optional] if omitted the server will use the default value of "fundingRef:asc"

### Return type

[**ListSourceAccountResponseV2**](ListSourceAccountResponseV2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Source Account response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_accounts_v3**
> ListSourceAccountResponseV3 get_source_accounts_v3()

Get list of source accounts

List source accounts.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.list_source_account_response_v3 import ListSourceAccountResponseV3
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.source_account_type import SourceAccountType
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    physical_account_name = "physicalAccountName_example" # str | Physical Account Name (optional)
    physical_account_id = "physicalAccountId_example" # str | The physical account ID (optional)
    payor_id = "payorId_example" # str | The account owner Payor ID (optional)
    funding_account_id = "fundingAccountId_example" # str | The funding account ID (optional)
    include_user_deleted = "includeUserDeleted_example" # bool | A filter for retrieving both active accounts and user deleted ones (optional)
    type = SourceAccountType("FBO") # SourceAccountType | The type of source account. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "fundingRef:asc" # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) if omitted the server will use the default value of "fundingRef:asc"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get list of source accounts
        api_response = api_instance.get_source_accounts_v3(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, include_user_deleted=include_user_deleted, type=type, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->get_source_accounts_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional]
 **physical_account_id** | **str**| The physical account ID | [optional]
 **payor_id** | **str**| The account owner Payor ID | [optional]
 **funding_account_id** | **str**| The funding account ID | [optional]
 **include_user_deleted** | **bool**| A filter for retrieving both active accounts and user deleted ones | [optional]
 **type** | **SourceAccountType**| The type of source account. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  | [optional] if omitted the server will use the default value of "fundingRef:asc"

### Return type

[**ListSourceAccountResponseV3**](ListSourceAccountResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Source Account response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_funding_audit_deltas**
> PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse list_funding_audit_deltas(payor_id, updated_since)

Get Funding Audit Delta

Get funding audit deltas for a payor

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.page_resource_funding_payor_status_audit_response_funding_payor_status_audit_response import PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    payor_id = "payorId_example" # str | 
    updated_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | 
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get Funding Audit Delta
        api_response = api_instance.list_funding_audit_deltas(payor_id, updated_since)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->list_funding_audit_deltas: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Funding Audit Delta
        api_response = api_instance.list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->list_funding_audit_deltas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**|  |
 **updated_since** | **datetime**|  |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25

### Return type

[**PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse**](PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Funding Account Deltas |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_notifications_request**
> set_notifications_request(source_account_id, set_notifications_request)

Set notifications

Set notifications for a given source account

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.set_notifications_request import SetNotificationsRequest
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | Source account id
    set_notifications_request = SetNotificationsRequest(
        minimum_balance=0,
    ) # SetNotificationsRequest | Body to included minimum balance to set

    # example passing only required values which don't have defaults set
    try:
        # Set notifications
        api_instance.set_notifications_request(source_account_id, set_notifications_request)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->set_notifications_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| Source account id |
 **set_notifications_request** | [**SetNotificationsRequest**](SetNotificationsRequest.md)| Body to included minimum balance to set |

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
**204** | Request Fulfilled |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_funds**
> transfer_funds(source_account_id, transfer_request)

Transfer Funds between source accounts

Transfer funds between source accounts for a Payor. The 'from' source account is identified in the URL, and is the account which will be debited. The 'to' (destination) source account is in the body, and is the account which will be credited. Both source accounts must belong to the same Payor. There must be sufficient balance in the 'from' source account, otherwise the transfer attempt will fail.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.transfer_request import TransferRequest
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | The 'from' source account id, which will be debited
    transfer_request = TransferRequest(
        to_source_account_id="to_source_account_id_example",
        amount=1,
        currency="USD",
    ) # TransferRequest | Body

    # example passing only required values which don't have defaults set
    try:
        # Transfer Funds between source accounts
        api_instance.transfer_funds(source_account_id, transfer_request)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->transfer_funds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| The &#39;from&#39; source account id, which will be debited |
 **transfer_request** | [**TransferRequest**](TransferRequest.md)| Body |

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
**204** | Request Processed |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_funds_v3**
> transfer_funds_v3(source_account_id, transfer_request2)

Transfer Funds between source accounts

Transfer funds between source accounts for a Payor. The 'from' source account is identified in the URL, and is the account which will be debited. The 'to' (destination) source account is in the body, and is the account which will be credited. Both source accounts must belong to the same Payor. There must be sufficient balance in the 'from' source account, otherwise the transfer attempt will fail.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import funding_manager_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.transfer_request2 import TransferRequest2
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
    api_instance = funding_manager_api.FundingManagerApi(api_client)
    source_account_id = "sourceAccountId_example" # str | The 'from' source account id, which will be debited
    transfer_request2 = TransferRequest2(
        to_source_account_id="to_source_account_id_example",
        amount=1,
        currency="USD",
    ) # TransferRequest2 | Body

    # example passing only required values which don't have defaults set
    try:
        # Transfer Funds between source accounts
        api_instance.transfer_funds_v3(source_account_id, transfer_request2)
    except velo_payments.ApiException as e:
        print("Exception when calling FundingManagerApi->transfer_funds_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | **str**| The &#39;from&#39; source account id, which will be debited |
 **transfer_request2** | [**TransferRequest2**](TransferRequest2.md)| Body |

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
**204** | Request Processed |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

