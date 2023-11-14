# velo_payments.TransactionsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_transaction_v1**](TransactionsApi.md#create_transaction_v1) | **POST** /v1/transactions | Create a Transaction
[**get_transaction_by_id_v1**](TransactionsApi.md#get_transaction_by_id_v1) | **GET** /v1/transactions/{transactionId} | Get Transaction
[**get_transactions**](TransactionsApi.md#get_transactions) | **GET** /v1/transactions | Get Transactions


# **create_transaction_v1**
> CreateTransactionResponse create_transaction_v1(create_transaction_request=create_transaction_request)

Create a Transaction

Create a new Transaction that can be funded

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
api_instance = velo_payments.TransactionsApi(velo_payments.ApiClient(configuration))
create_transaction_request = velo_payments.CreateTransactionRequest() # CreateTransactionRequest |  (optional)

try:
    # Create a Transaction
    api_response = api_instance.create_transaction_v1(create_transaction_request=create_transaction_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->create_transaction_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_transaction_request** | [**CreateTransactionRequest**](CreateTransactionRequest.md)|  | [optional] 

### Return type

[**CreateTransactionResponse**](CreateTransactionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Transaction Created |  * Location - Reference to created Transaction which can be queried for Balance etc <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction_by_id_v1**
> TransactionResponse get_transaction_by_id_v1(transaction_id)

Get Transaction

Get Transaction by Id

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
api_instance = velo_payments.TransactionsApi(velo_payments.ApiClient(configuration))
transaction_id = 'transaction_id_example' # str | 

try:
    # Get Transaction
    api_response = api_instance.get_transaction_by_id_v1(transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_id** | [**str**](.md)|  | 

### Return type

[**TransactionResponse**](TransactionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Transaction response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transactions**
> PageResourceTransactions get_transactions(payor_id=payor_id, transaction_reference=transaction_reference, page=page, page_size=page_size, sort=sort)

Get Transactions

<P>Get list of Transactions</P> 

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
api_instance = velo_payments.TransactionsApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str |  (optional)
transaction_reference = 'transaction_reference_example' # str |  (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'createdAt:asc' # str |  (optional) (default to 'createdAt:asc')

try:
    # Get Transactions
    api_response = api_instance.get_transactions(payor_id=payor_id, transaction_reference=transaction_reference, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**|  | [optional] 
 **transaction_reference** | **str**|  | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**|  | [optional] [default to &#39;createdAt:asc&#39;]

### Return type

[**PageResourceTransactions**](PageResourceTransactions.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | default response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

