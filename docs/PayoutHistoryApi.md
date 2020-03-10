# velo_payments.PayoutHistoryApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payments_for_payout**](PayoutHistoryApi.md#get_payments_for_payout) | **GET** /v3/paymentaudit/payouts/{payoutId} | Get Payments for Payout
[**get_payments_for_payout_v4**](PayoutHistoryApi.md#get_payments_for_payout_v4) | **GET** /v4/paymentaudit/payouts/{payoutId} | Get Payments for Payout
[**get_payout_stats_v1**](PayoutHistoryApi.md#get_payout_stats_v1) | **GET** /v1/paymentaudit/payoutStatistics | Get Payout Statistics


# **get_payments_for_payout**
> GetPaymentsForPayoutResponseV3 get_payments_for_payout(payout_id, remote_id=remote_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

Get Payments for Payout

Get List of payments for Payout 

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

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.PayoutHistoryApi(api_client)
    payout_id = 'payout_id_example' # str | The id (UUID) of the payout.
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
status = 'status_example' # str | Payment Status (optional)
source_amount_from = 56 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
source_amount_to = 56 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
payment_amount_from = 56 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
payment_amount_to = 56 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payments for Payout
        api_response = api_instance.get_payments_for_payout(payout_id, remote_id=remote_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayoutHistoryApi->get_payments_for_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| The id (UUID) of the payout. | 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **status** | **str**| Payment Status | [optional] 
 **source_amount_from** | **int**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] 
 **source_amount_to** | **int**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] 
 **payment_amount_from** | **int**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] 
 **payment_amount_to** | **int**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  | [optional] 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**GetPaymentsForPayoutResponseV3**](GetPaymentsForPayoutResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response, data found okay |  -  |
**400** | Invalid Request Parameter |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Payout Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_for_payout_v4**
> GetPaymentsForPayoutResponseV4 get_payments_for_payout_v4(payout_id, remote_id=remote_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

Get Payments for Payout

Get List of payments for Payout, allowing for RETURNED status 

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

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.PayoutHistoryApi(api_client)
    payout_id = 'payout_id_example' # str | The id (UUID) of the payout.
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
status = 'status_example' # str | Payment Status (optional)
source_amount_from = 56 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
source_amount_to = 56 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
payment_amount_from = 56 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
payment_amount_to = 56 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payments for Payout
        api_response = api_instance.get_payments_for_payout_v4(payout_id, remote_id=remote_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayoutHistoryApi->get_payments_for_payout_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| The id (UUID) of the payout. | 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **status** | **str**| Payment Status | [optional] 
 **source_amount_from** | **int**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] 
 **source_amount_to** | **int**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] 
 **payment_amount_from** | **int**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] 
 **payment_amount_to** | **int**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  | [optional] 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**GetPaymentsForPayoutResponseV4**](GetPaymentsForPayoutResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response, data found okay |  -  |
**400** | Invalid Request Parameter |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Payout Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_stats_v1**
> GetPayoutStatistics get_payout_stats_v1(payor_id=payor_id)

Get Payout Statistics

Get payout statistics for a payor.

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

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.PayoutHistoryApi(api_client)
    payor_id = 'payor_id_example' # str | The account owner Payor ID. Required for external users. (optional)

    try:
        # Get Payout Statistics
        api_response = api_instance.get_payout_stats_v1(payor_id=payor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayoutHistoryApi->get_payout_stats_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID. Required for external users. | [optional] 

### Return type

[**GetPayoutStatistics**](GetPayoutStatistics.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Source Account response |  -  |
**400** | Bad Request |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

