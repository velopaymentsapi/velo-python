# velo_payments.FundingManagerApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ach_funding_request**](FundingManagerApi.md#create_ach_funding_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/achFundingRequest | Create Funding Request
[**create_funding_request**](FundingManagerApi.md#create_funding_request) | **POST** /v2/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request
[**get_fundings**](FundingManagerApi.md#get_fundings) | **GET** /v1/paymentaudit/fundings | Get Fundings for Payor
[**get_source_account**](FundingManagerApi.md#get_source_account) | **GET** /v1/sourceAccounts/{sourceAccountId} | Get details about given source account.
[**get_source_account_v2**](FundingManagerApi.md#get_source_account_v2) | **GET** /v2/sourceAccounts/{sourceAccountId} | Get details about given source account.
[**get_source_accounts**](FundingManagerApi.md#get_source_accounts) | **GET** /v1/sourceAccounts | Get list of source accounts
[**get_source_accounts_v2**](FundingManagerApi.md#get_source_accounts_v2) | **GET** /v2/sourceAccounts | Get list of source accounts
[**list_funding_audit_deltas**](FundingManagerApi.md#list_funding_audit_deltas) | **GET** /v1/deltas/fundings | List Funding changes
[**set_notifications_request**](FundingManagerApi.md#set_notifications_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/notifications | Set notifications


# **create_ach_funding_request**
> create_ach_funding_request(source_account_id, funding_request_v1)

Create Funding Request

Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo  (202 - accepted, 400 - invalid request body, 404 - source account not found).

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
funding_request_v1 = velo_payments.FundingRequestV1() # FundingRequestV1 | Body to included ammount to be funded

try:
    # Create Funding Request
    api_instance.create_ach_funding_request(source_account_id, funding_request_v1)
except ApiException as e:
    print("Exception when calling FundingManagerApi->create_ach_funding_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 
 **funding_request_v1** | [**FundingRequestV1**](FundingRequestV1.md)| Body to included ammount to be funded | 

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
**202** | Request Accepted |  -  |
**400** | Invalid Request Body |  -  |
**404** | Source Account Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_funding_request**
> create_funding_request(source_account_id, funding_request_v2)

Create Funding Request

Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo  (202 - accepted, 400 - invalid request body, 404 - source account not found).

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
funding_request_v2 = velo_payments.FundingRequestV2() # FundingRequestV2 | Body to included ammount to be funded

try:
    # Create Funding Request
    api_instance.create_funding_request(source_account_id, funding_request_v2)
except ApiException as e:
    print("Exception when calling FundingManagerApi->create_funding_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 
 **funding_request_v2** | [**FundingRequestV2**](FundingRequestV2.md)| Body to included ammount to be funded | 

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
**202** | Request Accepted |  -  |
**400** | Invalid Request Body |  -  |
**404** | Source Account Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fundings**
> GetFundingsResponse get_fundings(payor_id=payor_id, page=page, page_size=page_size, sort=sort)

Get Fundings for Payor

Get a list of Fundings for a payor. 

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount.  (optional)

try:
    # Get Fundings for Payor
    api_response = api_instance.get_fundings(payor_id=payor_id, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_fundings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields. Example: &#x60;&#x60;&#x60;?sort&#x3D;destinationCurrency:asc,destinationAmount:asc&#x60;&#x60;&#x60; Default is no sort. The supported sort fields are: dateTime and amount.  | [optional] 

### Return type

[**GetFundingsResponse**](GetFundingsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Fundings normal response |  -  |
**400** | Bad Request |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_account**
> SourceAccountResponse get_source_account(source_account_id)

Get details about given source account.

Get details about given source account.

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id

try:
    # Get details about given source account.
    api_response = api_instance.get_source_account(source_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 

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
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_account_v2**
> SourceAccountResponseV2 get_source_account_v2(source_account_id)

Get details about given source account.

Get details about given source account.

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id

try:
    # Get details about given source account.
    api_response = api_instance.get_source_account_v2(source_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_account_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 

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
**400** | Bad Request, Invalid path parameter |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_accounts**
> ListSourceAccountResponse get_source_accounts(physical_account_name=physical_account_name, payor_id=payor_id, page=page, page_size=page_size, sort=sort)

Get list of source accounts

List source accounts.

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
physical_account_name = 'physical_account_name_example' # str | Physical Account Name (optional)
payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | Sort String (optional)

try:
    # Get list of source accounts
    api_response = api_instance.get_source_accounts(physical_account_name=physical_account_name, payor_id=payor_id, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor ID | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| Sort String | [optional] 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_accounts_v2**
> ListSourceAccountResponseV2 get_source_accounts_v2(physical_account_name=physical_account_name, payor_id=payor_id, page=page, page_size=page_size, sort=sort)

Get list of source accounts

List source accounts.

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
physical_account_name = 'physical_account_name_example' # str | Physical Account Name (optional)
payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | Sort String (optional)

try:
    # Get list of source accounts
    api_response = api_instance.get_source_accounts_v2(physical_account_name=physical_account_name, payor_id=payor_id, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_accounts_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor ID | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| Sort String | [optional] 

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
**400** | Invalid Request Parameters |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_funding_audit_deltas**
> FundingDeltaResponse list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)

List Funding changes

Get a paginated response listing funding changes.

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The Payor ID to find associated funding records
updated_since = '2013-10-20T19:20:30+01:00' # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 100 # int | Page size. Default is 100. Max allowable is 1000. (optional) (default to 100)

try:
    # List Funding changes
    api_response = api_instance.list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->list_funding_audit_deltas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID to find associated funding records | 
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 100. Max allowable is 1000. | [optional] [default to 100]

### Return type

[**FundingDeltaResponse**](FundingDeltaResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Funding changes |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_notifications_request**
> set_notifications_request(source_account_id, set_notifications_request)

Set notifications

Set notifications for a given source account

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
api_instance = velo_payments.FundingManagerApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
set_notifications_request = velo_payments.SetNotificationsRequest() # SetNotificationsRequest | Body to included minimum balance to set

try:
    # Set notifications
    api_instance.set_notifications_request(source_account_id, set_notifications_request)
except ApiException as e:
    print("Exception when calling FundingManagerApi->set_notifications_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 
 **set_notifications_request** | [**SetNotificationsRequest**](SetNotificationsRequest.md)| Body to included minimum balance to set | 

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
**204** | Request Fulfilled |  -  |
**400** | Invalid Request Body |  -  |
**404** | Source Account Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

