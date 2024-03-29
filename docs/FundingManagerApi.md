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
funding_request_v1 = velo_payments.FundingRequestV1() # FundingRequestV1 | Body to included amount to be funded

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
funding_request_v2 = velo_payments.FundingRequestV2() # FundingRequestV2 | Body to included amount to be funded

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
funding_request_v3 = velo_payments.FundingRequestV3() # FundingRequestV3 | Body to included amount to be funded

try:
    # Create Funding Request
    api_instance.create_funding_request_v3(source_account_id, funding_request_v3)
except ApiException as e:
    print("Exception when calling FundingManagerApi->create_funding_request_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 
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
> FundingAccountResponse get_funding_account(funding_account_id, sensitive=sensitive)

Get Funding Account

Get Funding Account by ID

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
funding_account_id = 'funding_account_id_example' # str | 
sensitive = False # bool |  (optional) (default to False)

try:
    # Get Funding Account
    api_response = api_instance.get_funding_account(funding_account_id, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_funding_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funding_account_id** | [**str**](.md)|  | 
 **sensitive** | **bool**|  | [optional] [default to False]

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
> FundingAccountResponse2 get_funding_account_v2(funding_account_id, sensitive=sensitive)

Get Funding Account

Get Funding Account by ID

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
funding_account_id = 'funding_account_id_example' # str | 
sensitive = False # bool |  (optional) (default to False)

try:
    # Get Funding Account
    api_response = api_instance.get_funding_account_v2(funding_account_id, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_funding_account_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funding_account_id** | [**str**](.md)|  | 
 **sensitive** | **bool**|  | [optional] [default to False]

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
> ListFundingAccountsResponse get_funding_accounts(payor_id=payor_id, source_account_id=source_account_id, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

Get Funding Accounts

Get the funding accounts.

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
payor_id = 'payor_id_example' # str |  (optional)
source_account_id = 'source_account_id_example' # str |  (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'accountName:asc' # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name and currency. (optional) (default to 'accountName:asc')
sensitive = False # bool |  (optional) (default to False)

try:
    # Get Funding Accounts
    api_response = api_instance.get_funding_accounts(payor_id=payor_id, source_account_id=source_account_id, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_funding_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)|  | [optional] 
 **source_account_id** | [**str**](.md)|  | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name and currency. | [optional] [default to &#39;accountName:asc&#39;]
 **sensitive** | **bool**|  | [optional] [default to False]

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
> ListFundingAccountsResponse2 get_funding_accounts_v2(payor_id=payor_id, name=name, country=country, currency=currency, type=type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

Get Funding Accounts

Get the funding accounts.

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
payor_id = 'payor_id_example' # str |  (optional)
name = 'name_example' # str | The descriptive funding account name (optional)
country = 'US' # str | The 2 letter ISO 3166-1 country code (upper case) (optional)
currency = 'USD' # str | The ISO 4217 currency code (optional)
type = velo_payments.FundingAccountType() # FundingAccountType | The type of funding account. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'accountName:asc' # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. (optional) (default to 'accountName:asc')
sensitive = False # bool |  (optional) (default to False)

try:
    # Get Funding Accounts
    api_response = api_instance.get_funding_accounts_v2(payor_id=payor_id, name=name, country=country, currency=currency, type=type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_funding_accounts_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)|  | [optional] 
 **name** | **str**| The descriptive funding account name | [optional] 
 **country** | **str**| The 2 letter ISO 3166-1 country code (upper case) | [optional] 
 **currency** | **str**| The ISO 4217 currency code | [optional] 
 **type** | [**FundingAccountType**](.md)| The type of funding account. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. | [optional] [default to &#39;accountName:asc&#39;]
 **sensitive** | **bool**|  | [optional] [default to False]

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
    api_response = api_instance.get_source_account_v3(source_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_account_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 

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
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef  (optional) (default to 'fundingRef:asc')

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
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef  | [optional] [default to &#39;fundingRef:asc&#39;]

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
> ListSourceAccountResponseV2 get_source_accounts_v2(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, page=page, page_size=page_size, sort=sort)

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
physical_account_id = 'physical_account_id_example' # str | The physical account ID (optional)
payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
funding_account_id = 'funding_account_id_example' # str | The funding account ID (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) (default to 'fundingRef:asc')

try:
    # Get list of source accounts
    api_response = api_instance.get_source_accounts_v2(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_accounts_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional] 
 **physical_account_id** | [**str**](.md)| The physical account ID | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor ID | [optional] 
 **funding_account_id** | [**str**](.md)| The funding account ID | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  | [optional] [default to &#39;fundingRef:asc&#39;]

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
> ListSourceAccountResponseV3 get_source_accounts_v3(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, include_user_deleted=include_user_deleted, type=type, page=page, page_size=page_size, sort=sort)

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
physical_account_id = 'physical_account_id_example' # str | The physical account ID (optional)
payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
funding_account_id = 'funding_account_id_example' # str | The funding account ID (optional)
include_user_deleted = True # bool | A filter for retrieving both active accounts and user deleted ones (optional)
type = velo_payments.SourceAccountType() # SourceAccountType | The type of source account. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) (default to 'fundingRef:asc')

try:
    # Get list of source accounts
    api_response = api_instance.get_source_accounts_v3(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, include_user_deleted=include_user_deleted, type=type, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->get_source_accounts_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional] 
 **physical_account_id** | [**str**](.md)| The physical account ID | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor ID | [optional] 
 **funding_account_id** | [**str**](.md)| The funding account ID | [optional] 
 **include_user_deleted** | **bool**| A filter for retrieving both active accounts and user deleted ones | [optional] 
 **type** | [**SourceAccountType**](.md)| The type of source account. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields e.g. ?sort&#x3D;name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  | [optional] [default to &#39;fundingRef:asc&#39;]

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
> PageResourceFundingPayorStatusAuditResponseFundingPayorStatusAuditResponse list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)

Get Funding Audit Delta

Get funding audit deltas for a payor

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
payor_id = 'payor_id_example' # str | 
updated_since = '2013-10-20T19:20:30+01:00' # datetime | 
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)

try:
    # Get Funding Audit Delta
    api_response = api_instance.list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingManagerApi->list_funding_audit_deltas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)|  | 
 **updated_since** | **datetime**|  | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]

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
source_account_id = 'source_account_id_example' # str | The 'from' source account id, which will be debited
transfer_request = velo_payments.TransferRequest() # TransferRequest | Body

try:
    # Transfer Funds between source accounts
    api_instance.transfer_funds(source_account_id, transfer_request)
except ApiException as e:
    print("Exception when calling FundingManagerApi->transfer_funds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| The &#39;from&#39; source account id, which will be debited | 
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
source_account_id = 'source_account_id_example' # str | The 'from' source account id, which will be debited
transfer_request2 = velo_payments.TransferRequest2() # TransferRequest2 | Body

try:
    # Transfer Funds between source accounts
    api_instance.transfer_funds_v3(source_account_id, transfer_request2)
except ApiException as e:
    print("Exception when calling FundingManagerApi->transfer_funds_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| The &#39;from&#39; source account id, which will be debited | 
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

