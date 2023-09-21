# velo_payments.PayoutsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote_for_payout_v3**](PayoutsApi.md#create_quote_for_payout_v3) | **POST** /v3/payouts/{payoutId}/quote | Create a quote for the payout
[**deschedule_payout**](PayoutsApi.md#deschedule_payout) | **DELETE** /v3/payouts/{payoutId}/schedule | Deschedule a payout
[**get_payments_for_payout_v3**](PayoutsApi.md#get_payments_for_payout_v3) | **GET** /v3/payouts/{payoutId}/payments | Retrieve payments for a payout
[**get_payout_summary_v3**](PayoutsApi.md#get_payout_summary_v3) | **GET** /v3/payouts/{payoutId} | Get Payout Summary
[**instruct_payout_v3**](PayoutsApi.md#instruct_payout_v3) | **POST** /v3/payouts/{payoutId} | Instruct Payout
[**schedule_for_payout**](PayoutsApi.md#schedule_for_payout) | **POST** /v3/payouts/{payoutId}/schedule | Schedule a payout
[**submit_payout_v3**](PayoutsApi.md#submit_payout_v3) | **POST** /v3/payouts | Submit Payout
[**withdraw_payment**](PayoutsApi.md#withdraw_payment) | **POST** /v1/payments/{paymentId}/withdraw | Withdraw a Payment
[**withdraw_payout_v3**](PayoutsApi.md#withdraw_payout_v3) | **DELETE** /v3/payouts/{payoutId} | Withdraw Payout


# **create_quote_for_payout_v3**
> QuoteResponseV3 create_quote_for_payout_v3(payout_id)

Create a quote for the payout

Create quote for a payout

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout

try:
    # Create a quote for the payout
    api_response = api_instance.create_quote_for_payout_v3(payout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutsApi->create_quote_for_payout_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 

### Return type

[**QuoteResponseV3**](QuoteResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quote for payout |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deschedule_payout**
> deschedule_payout(payout_id)

Deschedule a payout

Remove the schedule for a scheduled payout

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout

try:
    # Deschedule a payout
    api_instance.deschedule_payout(payout_id)
except ApiException as e:
    print("Exception when calling PayoutsApi->deschedule_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 

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
**204** | Descheduled payout successfully |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_for_payout_v3**
> PagedPaymentsResponseV3 get_payments_for_payout_v3(payout_id, status=status, remote_id=remote_id, payor_payment_id=payor_payment_id, source_account_name=source_account_name, transmission_type=transmission_type, payment_memo=payment_memo, page_size=page_size, page=page)

Retrieve payments for a payout

Retrieve payments for a payout

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout
status = 'status_example' # str | Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal  (optional)
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
payor_payment_id = 'payor_payment_id_example' # str | Payor's Id of the Payment (optional)
source_account_name = 'source_account_name_example' # str | Physical Account Name (optional)
transmission_type = 'transmission_type_example' # str | Transmission Type * ACH * SAME_DAY_ACH * WIRE  (optional)
payment_memo = 'payment_memo_example' # str | Payment Memo of the Payment (optional)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)

try:
    # Retrieve payments for a payout
    api_response = api_instance.get_payments_for_payout_v3(payout_id, status=status, remote_id=remote_id, payor_payment_id=payor_payment_id, source_account_name=source_account_name, transmission_type=transmission_type, payment_memo=payment_memo, page_size=page_size, page=page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutsApi->get_payments_for_payout_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 
 **status** | **str**| Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal  | [optional] 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **payor_payment_id** | **str**| Payor&#39;s Id of the Payment | [optional] 
 **source_account_name** | **str**| Physical Account Name | [optional] 
 **transmission_type** | **str**| Transmission Type * ACH * SAME_DAY_ACH * WIRE  | [optional] 
 **payment_memo** | **str**| Payment Memo of the Payment | [optional] 
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]

### Return type

[**PagedPaymentsResponseV3**](PagedPaymentsResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payments for payout |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_summary_v3**
> PayoutSummaryResponseV3 get_payout_summary_v3(payout_id)

Get Payout Summary

Get payout summary - returns the current state of the payout.

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout

try:
    # Get Payout Summary
    api_response = api_instance.get_payout_summary_v3(payout_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutsApi->get_payout_summary_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 

### Return type

[**PayoutSummaryResponseV3**](PayoutSummaryResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payout |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instruct_payout_v3**
> instruct_payout_v3(payout_id, instruct_payout_request_v3=instruct_payout_request_v3)

Instruct Payout

Instruct a payout to be made for the specified payoutId.

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout
instruct_payout_request_v3 = velo_payments.InstructPayoutRequestV3() # InstructPayoutRequestV3 | Additional instruct payout parameters (optional)

try:
    # Instruct Payout
    api_instance.instruct_payout_v3(payout_id, instruct_payout_request_v3=instruct_payout_request_v3)
except ApiException as e:
    print("Exception when calling PayoutsApi->instruct_payout_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 
 **instruct_payout_request_v3** | [**InstructPayoutRequestV3**](InstructPayoutRequestV3.md)| Additional instruct payout parameters | [optional] 

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
**202** | HTTP 202 Accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schedule_for_payout**
> schedule_for_payout(payout_id, schedule_payout_request_v3=schedule_payout_request_v3)

Schedule a payout

<p>Schedule a payout for auto-instruction in the future or update existing payout schedule if the payout has been scheduled before.</p> 

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout
schedule_payout_request_v3 = velo_payments.SchedulePayoutRequestV3() # SchedulePayoutRequestV3 | schedule payout parameters (optional)

try:
    # Schedule a payout
    api_instance.schedule_for_payout(payout_id, schedule_payout_request_v3=schedule_payout_request_v3)
except ApiException as e:
    print("Exception when calling PayoutsApi->schedule_for_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 
 **schedule_payout_request_v3** | [**SchedulePayoutRequestV3**](SchedulePayoutRequestV3.md)| schedule payout parameters | [optional] 

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
**204** | Payout is scheduled successfully |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_payout_v3**
> submit_payout_v3(create_payout_request_v3)

Submit Payout

<p>Create a new payout and return a location header with a link to the payout</p> <p>Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously</p> <p>The results can be obtained by issuing a HTTP GET to the URL returned in the location header</p> <p>**NOTE:** amount values in payments must be in 'minor units' format. E.g. cents for USD, pence for GBP etc with no decimal places</p> 

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
create_payout_request_v3 = velo_payments.CreatePayoutRequestV3() # CreatePayoutRequestV3 | Post amount to transfer using stored funding account details.

try:
    # Submit Payout
    api_instance.submit_payout_v3(create_payout_request_v3)
except ApiException as e:
    print("Exception when calling PayoutsApi->submit_payout_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payout_request_v3** | [**CreatePayoutRequestV3**](CreatePayoutRequestV3.md)| Post amount to transfer using stored funding account details. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Successful submission of the payout |  * Location - Reference to created payout <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_payment**
> withdraw_payment(payment_id, withdraw_payment_request)

Withdraw a Payment

<p>withdraw a payment </p> <p>There are a variety of reasons why this can fail</p> <ul>     <li>the payment must be in a state of 'accepted' or 'unfunded'</li>     <li>the payout must not be in a state of 'instructed'</li> </ul> 

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payment_id = 'payment_id_example' # str | Id of the Payment
withdraw_payment_request = velo_payments.WithdrawPaymentRequest() # WithdrawPaymentRequest | details for withdrawal

try:
    # Withdraw a Payment
    api_instance.withdraw_payment(payment_id, withdraw_payment_request)
except ApiException as e:
    print("Exception when calling PayoutsApi->withdraw_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Id of the Payment | 
 **withdraw_payment_request** | [**WithdrawPaymentRequest**](WithdrawPaymentRequest.md)| details for withdrawal | 

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
**204** | The payment was withdrawn |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_payout_v3**
> withdraw_payout_v3(payout_id)

Withdraw Payout

Withdraw Payout will remove the payout details from the rails but the payout will still be accessible in payout service in WITHDRAWN status.

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
api_instance = velo_payments.PayoutsApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout

try:
    # Withdraw Payout
    api_instance.withdraw_payout_v3(payout_id)
except ApiException as e:
    print("Exception when calling PayoutsApi->withdraw_payout_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 

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
**202** | HTTP 202 Accepted |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

