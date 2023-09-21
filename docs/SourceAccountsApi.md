# velo_payments.SourceAccountsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_source_account_v2**](SourceAccountsApi.md#get_source_account_v2) | **GET** /v2/sourceAccounts/{sourceAccountId} | Get Source Account
[**get_source_account_v3**](SourceAccountsApi.md#get_source_account_v3) | **GET** /v3/sourceAccounts/{sourceAccountId} | Get details about given source account.
[**get_source_accounts_v2**](SourceAccountsApi.md#get_source_accounts_v2) | **GET** /v2/sourceAccounts | Get list of source accounts
[**get_source_accounts_v3**](SourceAccountsApi.md#get_source_accounts_v3) | **GET** /v3/sourceAccounts | Get list of source accounts
[**set_notifications_request**](SourceAccountsApi.md#set_notifications_request) | **POST** /v1/sourceAccounts/{sourceAccountId}/notifications | Set notifications
[**set_notifications_request_v3**](SourceAccountsApi.md#set_notifications_request_v3) | **POST** /v3/sourceAccounts/{sourceAccountId}/notifications | Set notifications
[**transfer_funds_v2**](SourceAccountsApi.md#transfer_funds_v2) | **POST** /v2/sourceAccounts/{sourceAccountId}/transfers | Transfer Funds between source accounts
[**transfer_funds_v3**](SourceAccountsApi.md#transfer_funds_v3) | **POST** /v3/sourceAccounts/{sourceAccountId}/transfers | Transfer Funds between source accounts


# **get_source_account_v2**
> SourceAccountResponseV2 get_source_account_v2(source_account_id)

Get Source Account

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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id

try:
    # Get Source Account
    api_response = api_instance.get_source_account_v2(source_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->get_source_account_v2: %s\n" % e)
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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id

try:
    # Get details about given source account.
    api_response = api_instance.get_source_account_v3(source_account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->get_source_account_v3: %s\n" % e)
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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
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
    print("Exception when calling SourceAccountsApi->get_source_accounts_v2: %s\n" % e)
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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
physical_account_name = 'physical_account_name_example' # str | Physical Account Name (optional)
physical_account_id = 'physical_account_id_example' # str | The physical account ID (optional)
payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
funding_account_id = 'funding_account_id_example' # str | The funding account ID (optional)
include_user_deleted = True # bool | A filter for retrieving both active accounts and user deleted ones (optional)
type = 'type_example' # str | The type of source account. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) (default to 'fundingRef:asc')

try:
    # Get list of source accounts
    api_response = api_instance.get_source_accounts_v3(physical_account_name=physical_account_name, physical_account_id=physical_account_id, payor_id=payor_id, funding_account_id=funding_account_id, include_user_deleted=include_user_deleted, type=type, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->get_source_accounts_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **physical_account_name** | **str**| Physical Account Name | [optional] 
 **physical_account_id** | [**str**](.md)| The physical account ID | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor ID | [optional] 
 **funding_account_id** | [**str**](.md)| The funding account ID | [optional] 
 **include_user_deleted** | **bool**| A filter for retrieving both active accounts and user deleted ones | [optional] 
 **type** | **str**| The type of source account. | [optional] 
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

# **set_notifications_request**
> set_notifications_request(source_account_id, set_notifications_request)

Set notifications

<p>Set notifications for a given source account</p> <p>deprecated since 2.34 (use v3 version)</p> 

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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
set_notifications_request = velo_payments.SetNotificationsRequest() # SetNotificationsRequest | Body to included minimum balance to set

try:
    # Set notifications
    api_instance.set_notifications_request(source_account_id, set_notifications_request)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->set_notifications_request: %s\n" % e)
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

# **set_notifications_request_v3**
> set_notifications_request_v3(source_account_id, set_notifications_request2)

Set notifications

<p>Set notifications for a given source account</p> <p>If the balance falls below the amount set in the request an email notification will be sent to the email address registered in the payor profile</p> 

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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | Source account id
set_notifications_request2 = velo_payments.SetNotificationsRequest2() # SetNotificationsRequest2 | Body to included minimum balance to set

try:
    # Set notifications
    api_instance.set_notifications_request_v3(source_account_id, set_notifications_request2)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->set_notifications_request_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| Source account id | 
 **set_notifications_request2** | [**SetNotificationsRequest2**](SetNotificationsRequest2.md)| Body to included minimum balance to set | 

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

# **transfer_funds_v2**
> transfer_funds_v2(source_account_id, transfer_request_v2)

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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | The 'from' source account id, which will be debited
transfer_request_v2 = velo_payments.TransferRequestV2() # TransferRequestV2 | Body

try:
    # Transfer Funds between source accounts
    api_instance.transfer_funds_v2(source_account_id, transfer_request_v2)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->transfer_funds_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| The &#39;from&#39; source account id, which will be debited | 
 **transfer_request_v2** | [**TransferRequestV2**](TransferRequestV2.md)| Body | 

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
> transfer_funds_v3(source_account_id, transfer_request_v3)

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
api_instance = velo_payments.SourceAccountsApi(velo_payments.ApiClient(configuration))
source_account_id = 'source_account_id_example' # str | The 'from' source account id, which will be debited
transfer_request_v3 = velo_payments.TransferRequestV3() # TransferRequestV3 | Body

try:
    # Transfer Funds between source accounts
    api_instance.transfer_funds_v3(source_account_id, transfer_request_v3)
except ApiException as e:
    print("Exception when calling SourceAccountsApi->transfer_funds_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_account_id** | [**str**](.md)| The &#39;from&#39; source account id, which will be debited | 
 **transfer_request_v3** | [**TransferRequestV3**](TransferRequestV3.md)| Body | 

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

