# velo_payments.PaymentAuditServiceApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_transactions_csvv4**](PaymentAuditServiceApi.md#export_transactions_csvv4) | **GET** /v4/paymentaudit/transactions | Export Transactions
[**get_fundings_v4**](PaymentAuditServiceApi.md#get_fundings_v4) | **GET** /v4/paymentaudit/fundings | Get Fundings for Payor
[**get_payment_details_v4**](PaymentAuditServiceApi.md#get_payment_details_v4) | **GET** /v4/paymentaudit/payments/{paymentId} | Get Payment
[**get_payments_for_payout_v4**](PaymentAuditServiceApi.md#get_payments_for_payout_v4) | **GET** /v4/paymentaudit/payouts/{payoutId} | Get Payments for Payout
[**get_payout_stats_v4**](PaymentAuditServiceApi.md#get_payout_stats_v4) | **GET** /v4/paymentaudit/payoutStatistics | Get Payout Statistics
[**get_payouts_for_payor_v4**](PaymentAuditServiceApi.md#get_payouts_for_payor_v4) | **GET** /v4/paymentaudit/payouts | Get Payouts for Payor
[**list_payment_changes_v4**](PaymentAuditServiceApi.md#list_payment_changes_v4) | **GET** /v4/payments/deltas | List Payment Changes
[**list_payments_audit_v4**](PaymentAuditServiceApi.md#list_payments_audit_v4) | **GET** /v4/paymentaudit/payments | Get List of Payments


# **export_transactions_csvv4**
> PayorAmlTransaction export_transactions_csvv4(payor_id=payor_id, start_date=start_date, end_date=end_date, include=include)

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
# Create an instance of the API class
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | <p>The Payor ID for whom you wish to run the report.</p> <p>For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.</p>  (optional)
start_date = '2013-10-20' # date | Start date, inclusive. Format is YYYY-MM-DD (optional)
end_date = '2013-10-20' # date | End date, inclusive. Format is YYYY-MM-DD (optional)
include = 'include_example' # str | <p>Mode to determine whether to include other Payor's data in the results.</p> <p>May only be used if payorId is specified.</p> <p>Can be omitted or set to 'payorOnly' or 'payorAndDescendants'.</p> <p>payorOnly: Only include results for the specified Payor. This is the default if 'include' is omitted.</p> <p>payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.</p> <p>Note when a Payor requests the report and include=payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id</p>  (optional)

try:
    # Export Transactions
    api_response = api_instance.export_transactions_csvv4(payor_id=payor_id, start_date=start_date, end_date=end_date, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentAuditServiceApi->export_transactions_csvv4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| &lt;p&gt;The Payor ID for whom you wish to run the report.&lt;/p&gt; &lt;p&gt;For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.&lt;/p&gt;  | [optional] 
 **start_date** | **date**| Start date, inclusive. Format is YYYY-MM-DD | [optional] 
 **end_date** | **date**| End date, inclusive. Format is YYYY-MM-DD | [optional] 
 **include** | **str**| &lt;p&gt;Mode to determine whether to include other Payor&#39;s data in the results.&lt;/p&gt; &lt;p&gt;May only be used if payorId is specified.&lt;/p&gt; &lt;p&gt;Can be omitted or set to &#39;payorOnly&#39; or &#39;payorAndDescendants&#39;.&lt;/p&gt; &lt;p&gt;payorOnly: Only include results for the specified Payor. This is the default if &#39;include&#39; is omitted.&lt;/p&gt; &lt;p&gt;payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.&lt;/p&gt; &lt;p&gt;Note when a Payor requests the report and include&#x3D;payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id&lt;/p&gt;  | [optional] 

### Return type

[**PayorAmlTransaction**](PayorAmlTransaction.md)

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

# **get_fundings_v4**
> GetFundingsResponse get_fundings_v4(payor_id, page=page, page_size=page_size, sort=sort)

Get Fundings for Payor

<p>Get a list of Fundings for a payor.</p> 

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
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount.  (optional)

try:
    # Get Fundings for Payor
    api_response = api_instance.get_fundings_v4(payor_id, page=page, page_size=page_size, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentAuditServiceApi->get_fundings_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
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
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

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
# Create an instance of the API class
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
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
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_for_payout_v4**
> GetPaymentsForPayoutResponseV4 get_payments_for_payout_v4(payout_id, remote_id=remote_id, remote_system_id=remote_system_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, transmission_type=transmission_type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

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
# Create an instance of the API class
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | The id (UUID) of the payout.
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
remote_system_id = 'remote_system_id_example' # str | The id of the remote system that is orchestrating payments (optional)
status = 'status_example' # str | Payment Status (optional)
source_amount_from = 56 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
source_amount_to = 56 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
payment_amount_from = 56 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
payment_amount_to = 56 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
transmission_type = 'transmission_type_example' # str | Transmission Type * ACH * SAME_DAY_ACH * WIRE  (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

try:
    # Get Payments for Payout
    api_response = api_instance.get_payments_for_payout_v4(payout_id, remote_id=remote_id, remote_system_id=remote_system_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, transmission_type=transmission_type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentAuditServiceApi->get_payments_for_payout_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| The id (UUID) of the payout. | 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **remote_system_id** | **str**| The id of the remote system that is orchestrating payments | [optional] 
 **status** | **str**| Payment Status | [optional] 
 **source_amount_from** | **int**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional] 
 **source_amount_to** | **int**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional] 
 **payment_amount_from** | **int**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional] 
 **payment_amount_to** | **int**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional] 
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional] 
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional] 
 **transmission_type** | **str**| Transmission Type * ACH * SAME_DAY_ACH * WIRE  | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
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
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_stats_v4**
> GetPayoutStatistics get_payout_stats_v4(payor_id=payor_id)

Get Payout Statistics

<p>Get payout statistics for a payor.</p> 

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
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The account owner Payor ID. Required for external users. (optional)

try:
    # Get Payout Statistics
    api_response = api_instance.get_payout_stats_v4(payor_id=payor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentAuditServiceApi->get_payout_stats_v4: %s\n" % e)
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
**200** | Payout Statistics response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payouts_for_payor_v4**
> GetPayoutsResponse get_payouts_for_payor_v4(payor_id=payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, from_payor_name=from_payor_name, page=page, page_size=page_size, sort=sort)

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
# Create an instance of the API class
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The id (UUID) of the payor funding the payout or the payor whose payees are being paid. (optional)
payout_memo = 'payout_memo_example' # str | Payout Memo filter - case insensitive sub-string match (optional)
status = 'status_example' # str | Payout Status (optional)
submitted_date_from = '2013-10-20' # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
submitted_date_to = '2013-10-20' # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
from_payor_name = 'from_payor_name_example' # str | The name of the payor whose payees are being paid. This filters via a case insensitive substring match. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
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
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId  | [optional] 

### Return type

[**GetPayoutsResponse**](GetPayoutsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Payor data found |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_changes_v4**
> PaymentDeltaResponse list_payment_changes_v4(payor_id, updated_since, page=page, page_size=page_size)

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
# Create an instance of the API class
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payor_id = 'payor_id_example' # str | The Payor ID to find associated Payments
updated_since = '2013-10-20T19:20:30+01:00' # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 100 # int | The number of results to return in a page (optional) (default to 100)

try:
    # List Payment Changes
    api_response = api_instance.list_payment_changes_v4(payor_id, updated_since, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PaymentAuditServiceApi->list_payment_changes_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID to find associated Payments | 
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 100]

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

# **list_payments_audit_v4**
> ListPaymentsResponseV4 list_payments_audit_v4(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, remote_system_id=remote_system_id, status=status, transmission_type=transmission_type, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

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
# Create an instance of the API class
api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))
payee_id = 'payee_id_example' # str | The UUID of the payee. (optional)
payor_id = 'payor_id_example' # str | The account owner Payor Id. Required for external users. (optional)
payor_name = 'payor_name_example' # str | The payor’s name. This filters via a case insensitive substring match. (optional)
remote_id = 'remote_id_example' # str | The remote id of the payees. (optional)
remote_system_id = 'remote_system_id_example' # str | The id of the remote system that is orchestrating payments (optional)
status = 'status_example' # str | Payment Status (optional)
transmission_type = 'transmission_type_example' # str | Transmission Type * ACH * SAME_DAY_ACH * WIRE  (optional)
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
page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
sort = 'sort_example' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId  (optional)
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

try:
    # Get List of Payments
    api_response = api_instance.list_payments_audit_v4(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, remote_system_id=remote_system_id, status=status, transmission_type=transmission_type, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
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
 **remote_system_id** | **str**| The id of the remote system that is orchestrating payments | [optional] 
 **status** | **str**| Payment Status | [optional] 
 **transmission_type** | **str**| Transmission Type * ACH * SAME_DAY_ACH * WIRE  | [optional] 
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
 **page_size** | **int**| The number of results to return in a page | [optional] [default to 25]
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
**200** | Paginated list of payments |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

