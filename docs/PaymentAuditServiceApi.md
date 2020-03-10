# velo_payments.PaymentAuditServiceApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_transactions_csvv3**](PaymentAuditServiceApi.md#export_transactions_csvv3) | **GET** /v3/paymentaudit/transactions | Export Transactions
[**export_transactions_csvv4**](PaymentAuditServiceApi.md#export_transactions_csvv4) | **GET** /v4/paymentaudit/transactions | Export Transactions
[**get_fundings_v1**](PaymentAuditServiceApi.md#get_fundings_v1) | **GET** /v1/paymentaudit/fundings | Get Fundings for Payor
[**get_payment_details**](PaymentAuditServiceApi.md#get_payment_details) | **GET** /v3/paymentaudit/payments/{paymentId} | Get Payment
[**get_payment_details_v4**](PaymentAuditServiceApi.md#get_payment_details_v4) | **GET** /v4/paymentaudit/payments/{paymentId} | Get Payment
[**get_payments_for_payout**](PaymentAuditServiceApi.md#get_payments_for_payout) | **GET** /v3/paymentaudit/payouts/{payoutId} | Get Payments for Payout
[**get_payments_for_payout_v4**](PaymentAuditServiceApi.md#get_payments_for_payout_v4) | **GET** /v4/paymentaudit/payouts/{payoutId} | Get Payments for Payout
[**get_payouts_for_payor_v3**](PaymentAuditServiceApi.md#get_payouts_for_payor_v3) | **GET** /v3/paymentaudit/payouts | Get Payouts for Payor
[**get_payouts_for_payor_v4**](PaymentAuditServiceApi.md#get_payouts_for_payor_v4) | **GET** /v4/paymentaudit/payouts | Get Payouts for Payor
[**list_payment_changes**](PaymentAuditServiceApi.md#list_payment_changes) | **GET** /v1/deltas/payments | List Payment Changes
[**list_payments_audit**](PaymentAuditServiceApi.md#list_payments_audit) | **GET** /v3/paymentaudit/payments | Get List of Payments
[**list_payments_audit_v4**](PaymentAuditServiceApi.md#list_payments_audit_v4) | **GET** /v4/paymentaudit/payments | Get List of Payments


# **export_transactions_csvv3**
> PayorAmlTransactionV3 export_transactions_csvv3(payor_id=payor_id, start_date=start_date, end_date=end_date)

Export Transactions

Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payor_id = 'payor_id_example' # str | The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  (optional)
start_date = '2013-10-20' # date | Start date, inclusive. Format is YYYY-MM-DD (optional)
end_date = '2013-10-20' # date | End date, inclusive. Format is YYYY-MM-DD (optional)

    try:
        # Export Transactions
        api_response = api_instance.export_transactions_csvv3(payor_id=payor_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->export_transactions_csvv3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  | [optional] 
 **start_date** | **date**| Start date, inclusive. Format is YYYY-MM-DD | [optional] 
 **end_date** | **date**| End date, inclusive. Format is YYYY-MM-DD | [optional] 

### Return type

[**PayorAmlTransactionV3**](PayorAmlTransactionV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export Transactions response |  -  |
**400** | invalid Request |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_transactions_csvv4**
> PayorAmlTransactionV4 export_transactions_csvv4(payor_id=payor_id, start_date=start_date, submitted_date_from=submitted_date_from, include=include)

Export Transactions

Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payor_id = 'payor_id_example' # str | The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  (optional)
start_date = '2013-10-20' # date | Start date, inclusive. Format is YYYY-MM-DD (optional)
submitted_date_from = '2013-10-20' # date | Start date, inclusive. Format is YYYY-MM-DD (optional)
include = 'include_example' # str | Mode to determine whether to include other Payor's data in the results. May only be used if payorId is specified. Can be omitted or set to 'payorOnly' or 'payorAndDescendants'. payorOnly: Only include results for the specified Payor. This is the default if 'include' is omitted. payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.                      Note when a Payor requests the report and include=payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id  (optional)

    try:
        # Export Transactions
        api_response = api_instance.export_transactions_csvv4(payor_id=payor_id, start_date=start_date, submitted_date_from=submitted_date_from, include=include)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->export_transactions_csvv4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  | [optional] 
 **start_date** | **date**| Start date, inclusive. Format is YYYY-MM-DD | [optional] 
 **submitted_date_from** | **date**| Start date, inclusive. Format is YYYY-MM-DD | [optional] 
 **include** | **str**| Mode to determine whether to include other Payor&#39;s data in the results. May only be used if payorId is specified. Can be omitted or set to &#39;payorOnly&#39; or &#39;payorAndDescendants&#39;. payorOnly: Only include results for the specified Payor. This is the default if &#39;include&#39; is omitted. payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.                      Note when a Payor requests the report and include&#x3D;payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id  | [optional] 

### Return type

[**PayorAmlTransactionV4**](PayorAmlTransactionV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export Transactions response |  -  |
**400** | invalid Request |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fundings_v1**
> GetFundingsResponse get_fundings_v1(payor_id=payor_id, page=page, page_size=page_size, sort=sort)

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

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payor_id = 'payor_id_example' # str | The account owner Payor ID (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount.  (optional)

    try:
        # Get Fundings for Payor
        api_response = api_instance.get_fundings_v1(payor_id=payor_id, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_fundings_v1: %s\n" % e)
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

# **get_payment_details**
> PaymentResponseV3 get_payment_details(payment_id, sensitive=sensitive)

Get Payment

Get the payment with the given id. This contains the payment history. 

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payment_id = 'payment_id_example' # str | Payment Id
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payment
        api_response = api_instance.get_payment_details(payment_id, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payment_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Payment Id | 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**PaymentResponseV3**](PaymentResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response, request completed okay |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Payment Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_details_v4**
> PaymentResponseV4 get_payment_details_v4(payment_id, sensitive=sensitive)

Get Payment

Get the payment with the given id. This contains the payment history. 

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payment_id = 'payment_id_example' # str | Payment Id
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payment
        api_response = api_instance.get_payment_details_v4(payment_id, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payment_details_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | [**str**](.md)| Payment Id | 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**PaymentResponseV4**](PaymentResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response, request completed okay |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Payment Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
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
        print("Exception when calling PaymentAuditServiceApi->get_payments_for_payout: %s\n" % e)
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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
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
        print("Exception when calling PaymentAuditServiceApi->get_payments_for_payout_v4: %s\n" % e)
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

# **get_payouts_for_payor_v3**
> GetPayoutsResponseV3 get_payouts_for_payor_v3(payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort)

Get Payouts for Payor

Get List of payouts for payor 

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payor_id = 'payor_id_example' # str | The account owner Payor ID
payout_memo = 'payout_memo_example' # str | Payout Memo filter - case insensitive sub-string match (optional)
status = 'status_example' # str | Payout Status (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status.  (optional)

    try:
        # Get Payouts for Payor
        api_response = api_instance.get_payouts_for_payor_v3(payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payouts_for_payor_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **payout_memo** | **str**| Payout Memo filter - case insensitive sub-string match | [optional] 
 **status** | **str**| Payout Status | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status.  | [optional] 

### Return type

[**GetPayoutsResponseV3**](GetPayoutsResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payor data found |  -  |
**400** | Invalid Request Parameter |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payouts_for_payor_v4**
> GetPayoutsResponseV4 get_payouts_for_payor_v4(payor_id=payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, from_payor_name=from_payor_name, page=page, page_size=page_size, sort=sort)

Get Payouts for Payor

Get List of payouts for payor 

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payor_id = 'payor_id_example' # str | The id (UUID) of the payor funding the payout or the payor whose payees are being paid. (optional)
payout_memo = 'payout_memo_example' # str | Payout Memo filter - case insensitive sub-string match (optional)
status = 'status_example' # str | Payout Status (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
from_payor_name = 'from_payor_name_example' # str | The name of the payor whose payees are being paid. This filters via a case insensitive substring match. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId  (optional)

    try:
        # Get Payouts for Payor
        api_response = api_instance.get_payouts_for_payor_v4(payor_id=payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, from_payor_name=from_payor_name, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payouts_for_payor_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The id (UUID) of the payor funding the payout or the payor whose payees are being paid. | [optional] 
 **payout_memo** | **str**| Payout Memo filter - case insensitive sub-string match | [optional] 
 **status** | **str**| Payout Status | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **from_payor_name** | **str**| The name of the payor whose payees are being paid. This filters via a case insensitive substring match. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId  | [optional] 

### Return type

[**GetPayoutsResponseV4**](GetPayoutsResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payor data found |  -  |
**400** | Invalid Request Parameter |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |
**404** | Payor Id Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_changes**
> PaymentDeltaResponse list_payment_changes(payor_id, updated_since, page=page, page_size=page_size)

List Payment Changes

Get a paginated response listing payment changes.

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payor_id = 'payor_id_example' # str | The Payor ID to find associated Payments
updated_since = '2013-10-20T19:20:30+01:00' # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 100 # int | Page size. Default is 100. Max allowable is 1000. (optional) (default to 100)

    try:
        # List Payment Changes
        api_response = api_instance.list_payment_changes(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->list_payment_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID to find associated Payments | 
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 100. Max allowable is 1000. | [optional] [default to 100]

### Return type

[**PaymentDeltaResponse**](PaymentDeltaResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payment Changes |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments_audit**
> ListPaymentsResponse list_payments_audit(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

Get List of Payments

Get payments for the given payor Id

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payee_id = 'payee_id_example' # str | The UUID of the payee. (optional)
payor_id = 'payor_id_example' # str | The account owner Payor Id. Required for external users. (optional)
payor_name = 'payor_name_example' # str | The payor’s name. This filters via a case insensitive substring match. (optional)
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
status = 'status_example' # str | Payment Status (optional)
source_account_name = 'source_account_name_example' # str | The source account name filter. This filters via a case insensitive substring match. (optional)
source_amount_from = 56 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
source_amount_to = 56 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
source_currency = 'source_currency_example' # str | The source currency filter. Filters based on an exact match on the currency. (optional)
payment_amount_from = 56 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
payment_amount_to = 56 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
payment_currency = 'payment_currency_example' # str | The payment currency filter. Filters based on an exact match on the currency. (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
payment_memo = 'payment_memo_example' # str | The payment memo filter. This filters via a case insensitive substring match. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get List of Payments
        api_response = api_instance.list_payments_audit(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->list_payments_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor Id. Required for external users. | [optional] 
 **payor_name** | **str**| The payor’s name. This filters via a case insensitive substring match. | [optional] 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **status** | **str**| Payment Status | [optional] 
 **source_account_name** | **str**| The source account name filter. This filters via a case insensitive substring match. | [optional] 
 **source_amount_from** | **int**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] 
 **source_amount_to** | **int**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] 
 **source_currency** | **str**| The source currency filter. Filters based on an exact match on the currency. | [optional] 
 **payment_amount_from** | **int**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] 
 **payment_amount_to** | **int**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] 
 **payment_currency** | **str**| The payment currency filter. Filters based on an exact match on the currency. | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **payment_memo** | **str**| The payment memo filter. This filters via a case insensitive substring match. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  | [optional] 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**ListPaymentsResponse**](ListPaymentsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee |  -  |
**400** | Bad Request Parameter |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payments_audit_v4**
> ListPaymentsResponseV4 list_payments_audit_v4(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

Get List of Payments

Get payments for the given payor Id

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
    api_instance = velo_payments.PaymentAuditServiceApi(api_client)
    payee_id = 'payee_id_example' # str | The UUID of the payee. (optional)
payor_id = 'payor_id_example' # str | The account owner Payor Id. Required for external users. (optional)
payor_name = 'payor_name_example' # str | The payor’s name. This filters via a case insensitive substring match. (optional)
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
status = 'status_example' # str | Payment Status (optional)
source_account_name = 'source_account_name_example' # str | The source account name filter. This filters via a case insensitive substring match. (optional)
source_amount_from = 56 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
source_amount_to = 56 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
source_currency = 'source_currency_example' # str | The source currency filter. Filters based on an exact match on the currency. (optional)
payment_amount_from = 56 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
payment_amount_to = 56 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
payment_currency = 'payment_currency_example' # str | The payment currency filter. Filters based on an exact match on the currency. (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
payment_memo = 'payment_memo_example' # str | The payment memo filter. This filters via a case insensitive substring match. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId  (optional)
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get List of Payments
        api_response = api_instance.list_payments_audit_v4(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->list_payments_audit_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | [optional] 
 **payor_id** | [**str**](.md)| The account owner Payor Id. Required for external users. | [optional] 
 **payor_name** | **str**| The payor’s name. This filters via a case insensitive substring match. | [optional] 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **status** | **str**| Payment Status | [optional] 
 **source_account_name** | **str**| The source account name filter. This filters via a case insensitive substring match. | [optional] 
 **source_amount_from** | **int**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] 
 **source_amount_to** | **int**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] 
 **source_currency** | **str**| The source currency filter. Filters based on an exact match on the currency. | [optional] 
 **payment_amount_from** | **int**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] 
 **payment_amount_to** | **int**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] 
 **payment_currency** | **str**| The payment currency filter. Filters based on an exact match on the currency. | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **payment_memo** | **str**| The payment memo filter. This filters via a case insensitive substring match. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId  | [optional] 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**ListPaymentsResponseV4**](ListPaymentsResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee |  -  |
**400** | Bad Request Parameter |  -  |
**401** | Not Authorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

