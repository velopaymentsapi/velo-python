# velo_payments.FundingApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_funding_request_v2**](FundingApi.md#create_funding_request_v2) | **POST** /v2/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request
[**create_funding_request_v3**](FundingApi.md#create_funding_request_v3) | **POST** /v3/sourceAccounts/{sourceAccountId}/fundingRequest | Create Funding Request
[**get_funding_account_v2**](FundingApi.md#get_funding_account_v2) | **GET** /v2/fundingAccounts/{fundingAccountId} | Get Funding Account
[**get_funding_accounts_v2**](FundingApi.md#get_funding_accounts_v2) | **GET** /v2/fundingAccounts | Get Funding Accounts
[**get_funding_by_id_v1**](FundingApi.md#get_funding_by_id_v1) | **GET** /v1/fundings/{fundingId} | Get Funding
[**list_funding_audit_deltas**](FundingApi.md#list_funding_audit_deltas) | **GET** /v1/deltas/fundings | Get Funding Audit Delta


# **create_funding_request_v2**
> create_funding_request_v2(source_account_id, funding_request_v2)

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
api_instance = velo_payments.FundingApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
funding_request_v2 = velo_payments.FundingRequestV2() # FundingRequestV2 | Body to included amount to be funded

try:
    # Create Funding Request
    api_instance.create_funding_request_v2(source_account_id, funding_request_v2)
except ApiException as e:
    print("Exception when calling FundingApi->create_funding_request_v2: %s\n" % e)
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

<p>Instruct a funding request to transfer funds from the payor’s funding bank to the payor’s balance held within Velo</p> 

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
api_instance = velo_payments.FundingApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
funding_request_v3 = velo_payments.FundingRequestV3() # FundingRequestV3 | Body to included amount to be funded

try:
    # Create Funding Request
    api_instance.create_funding_request_v3(source_account_id, funding_request_v3)
except ApiException as e:
    print("Exception when calling FundingApi->create_funding_request_v3: %s\n" % e)
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
**202** | Request Accepted |  * Location - Reference to created Funding Request <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_funding_account_v2**
> FundingAccountResponseV2 get_funding_account_v2(funding_account_id, sensitive=sensitive)

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
api_instance = velo_payments.FundingApi(velo_payments.ApiClient(configuration))
funding_account_id = 'funding_account_id_example' # str | 
sensitive = False # bool |  (optional) (default to False)

try:
    # Get Funding Account
    api_response = api_instance.get_funding_account_v2(funding_account_id, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingApi->get_funding_account_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funding_account_id** | [**str**](.md)|  | 
 **sensitive** | **bool**|  | [optional] [default to False]

### Return type

[**FundingAccountResponseV2**](FundingAccountResponseV2.md)

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

# **get_funding_accounts_v2**
> ListFundingAccountsResponseV2 get_funding_accounts_v2(payor_id=payor_id, name=name, country=country, currency=currency, type=type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

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
api_instance = velo_payments.FundingApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str |  (optional)
name = 'name_example' # str | The descriptive funding account name (optional)
country = 'US' # str | The 2 letter ISO 3166-1 country code (upper case) (optional)
currency = 'USD' # str | The ISO 4217 currency code (optional)
type = 'type_example' # str | The type of funding account. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'accountName:asc' # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. (optional) (default to 'accountName:asc')
sensitive = False # bool |  (optional) (default to False)

try:
    # Get Funding Accounts
    api_response = api_instance.get_funding_accounts_v2(payor_id=payor_id, name=name, country=country, currency=currency, type=type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingApi->get_funding_accounts_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)|  | [optional] 
 **name** | **str**| The descriptive funding account name | [optional] 
 **country** | **str**| The 2 letter ISO 3166-1 country code (upper case) | [optional] 
 **currency** | **str**| The ISO 4217 currency code | [optional] 
 **type** | **str**| The type of funding account. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. | [optional] [default to &#39;accountName:asc&#39;]
 **sensitive** | **bool**|  | [optional] [default to False]

### Return type

[**ListFundingAccountsResponseV2**](ListFundingAccountsResponseV2.md)

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

# **get_funding_by_id_v1**
> FundingResponse get_funding_by_id_v1(funding_id)

Get Funding

Get Funding by Id

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
api_instance = velo_payments.FundingApi(velo_payments.ApiClient(configuration))
funding_id = 'funding_id_example' # str | 

try:
    # Get Funding
    api_response = api_instance.get_funding_by_id_v1(funding_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingApi->get_funding_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **funding_id** | [**str**](.md)|  | 

### Return type

[**FundingResponse**](FundingResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Funding response |  -  |
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
api_instance = velo_payments.FundingApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | 
updated_since = '2013-10-20T19:20:30+01:00' # datetime | 
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)

try:
    # Get Funding Audit Delta
    api_response = api_instance.list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FundingApi->list_funding_audit_deltas: %s\n" % e)
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

