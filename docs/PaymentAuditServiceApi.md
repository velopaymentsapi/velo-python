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
> PayorAmlTransaction export_transactions_csvv4()

Export Transactions

Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.payor_aml_transaction import PayorAmlTransaction
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payor_id = "payorId_example" # str | <p>The Payor ID for whom you wish to run the report.</p> <p>For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.</p>  (optional)
    start_date = dateutil_parser('1970-01-01').date() # date | Start date, inclusive. Format is YYYY-MM-DD (optional)
    end_date = dateutil_parser('1970-01-01').date() # date | End date, inclusive. Format is YYYY-MM-DD (optional)
    include = "payorOnly" # str | <p>Mode to determine whether to include other Payor's data in the results.</p> <p>May only be used if payorId is specified.</p> <p>Can be omitted or set to 'payorOnly' or 'payorAndDescendants'.</p> <p>payorOnly: Only include results for the specified Payor. This is the default if 'include' is omitted.</p> <p>payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.</p> <p>Note when a Payor requests the report and include=payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id</p>  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Transactions
        api_response = api_instance.export_transactions_csvv4(payor_id=payor_id, start_date=start_date, end_date=end_date, include=include)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->export_transactions_csvv4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| &lt;p&gt;The Payor ID for whom you wish to run the report.&lt;/p&gt; &lt;p&gt;For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.&lt;/p&gt;  | [optional]
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
> GetFundingsResponse get_fundings_v4(payor_id)

Get Fundings for Payor

<p>Get a list of Fundings for a payor.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.get_fundings_response import GetFundingsResponse
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Fundings for Payor
        api_response = api_instance.get_fundings_v4(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_fundings_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Fundings for Payor
        api_response = api_instance.get_fundings_v4(payor_id, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_fundings_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
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
> PaymentResponseV4 get_payment_details_v4(payment_id)

Get Payment

Get the payment with the given id. This contains the payment history. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.payment_response_v4 import PaymentResponseV4
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payment_id = "paymentId_example" # str | Payment Id
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payment
        api_response = api_instance.get_payment_details_v4(payment_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payment_details_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payment
        api_response = api_instance.get_payment_details_v4(payment_id, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payment_details_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Payment Id |
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
> GetPaymentsForPayoutResponseV4 get_payments_for_payout_v4(payout_id)

Get Payments for Payout

Get List of payments for Payout, allowing for RETURNED status 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.get_payments_for_payout_response_v4 import GetPaymentsForPayoutResponseV4
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payout_id = "payoutId_example" # str | The id (UUID) of the payout.
    remote_id = "remoteId_example" # str | The remote id of the payees. (optional)
    remote_system_id = "remoteSystemId_example" # str | The id of the remote system that is orchestrating payments (optional)
    status = "ACCEPTED" # str | Payment Status (optional)
    source_amount_from = 1 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
    source_amount_to = 1 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
    payment_amount_from = 1 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
    payment_amount_to = 1 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
    submitted_date_from = dateutil_parser('1970-01-01').date() # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
    submitted_date_to = dateutil_parser('1970-01-01').date() # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
    transmission_type = "ACH" # str | Transmission Type * ACH * SAME_DAY_ACH * WIRE  (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payments for Payout
        api_response = api_instance.get_payments_for_payout_v4(payout_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payments_for_payout_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payments for Payout
        api_response = api_instance.get_payments_for_payout_v4(payout_id, remote_id=remote_id, remote_system_id=remote_system_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, transmission_type=transmission_type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payments_for_payout_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The id (UUID) of the payout. |
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
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
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
> GetPayoutStatistics get_payout_stats_v4()

Get Payout Statistics

<p>Get payout statistics for a payor.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.get_payout_statistics import GetPayoutStatistics
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID. Required for external users. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payout Statistics
        api_response = api_instance.get_payout_stats_v4(payor_id=payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payout_stats_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID. Required for external users. | [optional]

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
> GetPayoutsResponse get_payouts_for_payor_v4()

Get Payouts for Payor

Get List of payouts for payor 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.get_payouts_response import GetPayoutsResponse
from velo_payments.model.inline_response401 import InlineResponse401
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payor_id = "payorId_example" # str | The id (UUID) of the payor funding the payout or the payor whose payees are being paid. (optional)
    payout_memo = "payoutMemo_example" # str | Payout Memo filter - case insensitive sub-string match (optional)
    status = "ACCEPTED" # str | Payout Status (optional)
    submitted_date_from = dateutil_parser('1970-01-01').date() # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
    submitted_date_to = dateutil_parser('1970-01-01').date() # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
    from_payor_name = "fromPayorName_example" # str | The name of the payor whose payees are being paid. This filters via a case insensitive substring match. (optional)
    scheduled_for_date_from = dateutil_parser('1970-01-01').date() # date | Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd. (optional)
    scheduled_for_date_to = dateutil_parser('1970-01-01').date() # date | Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd. (optional)
    schedule_status = "ANY" # str | Payout Schedule Status (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payouts for Payor
        api_response = api_instance.get_payouts_for_payor_v4(payor_id=payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, from_payor_name=from_payor_name, scheduled_for_date_from=scheduled_for_date_from, scheduled_for_date_to=scheduled_for_date_to, schedule_status=schedule_status, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->get_payouts_for_payor_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The id (UUID) of the payor funding the payout or the payor whose payees are being paid. | [optional]
 **payout_memo** | **str**| Payout Memo filter - case insensitive sub-string match | [optional]
 **status** | **str**| Payout Status | [optional]
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional]
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional]
 **from_payor_name** | **str**| The name of the payor whose payees are being paid. This filters via a case insensitive substring match. | [optional]
 **scheduled_for_date_from** | **date**| Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd. | [optional]
 **scheduled_for_date_to** | **date**| Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd. | [optional]
 **schedule_status** | **str**| Payout Schedule Status | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor  | [optional]

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
> PaymentDeltaResponse list_payment_changes_v4(payor_id, updated_since)

List Payment Changes

Get a paginated response listing payment changes.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.payment_delta_response import PaymentDeltaResponse
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payor_id = "payorId_example" # str | The Payor ID to find associated Payments
    updated_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 100 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # List Payment Changes
        api_response = api_instance.list_payment_changes_v4(payor_id, updated_since)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->list_payment_changes_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payment Changes
        api_response = api_instance.list_payment_changes_v4(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->list_payment_changes_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor ID to find associated Payments |
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 100

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
> ListPaymentsResponseV4 list_payments_audit_v4()

Get List of Payments

Get payments for the given payor Id

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.list_payments_response_v4 import ListPaymentsResponseV4
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
    api_instance = payment_audit_service_api.PaymentAuditServiceApi(api_client)
    payee_id = "payeeId_example" # str | The UUID of the payee. (optional)
    payor_id = "payorId_example" # str | The account owner Payor Id. Required for external users. (optional)
    payor_name = "payorName_example" # str | The payor’s name. This filters via a case insensitive substring match. (optional)
    remote_id = "remoteId_example" # str | The remote id of the payees. (optional)
    remote_system_id = "remoteSystemId_example" # str | The id of the remote system that is orchestrating payments (optional)
    status = "ACCEPTED" # str | Payment Status (optional)
    transmission_type = "ACH" # str | Transmission Type * ACH * SAME_DAY_ACH * WIRE  (optional)
    source_account_name = "sourceAccountName_example" # str | The source account name filter. This filters via a case insensitive substring match. (optional)
    source_amount_from = 1 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
    source_amount_to = 1 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
    source_currency = "sourceCurrency_example" # str | The source currency filter. Filters based on an exact match on the currency. (optional)
    payment_amount_from = 1 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
    payment_amount_to = 1 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
    payment_currency = "paymentCurrency_example" # str | The payment currency filter. Filters based on an exact match on the currency. (optional)
    submitted_date_from = dateutil_parser('1970-01-01').date() # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
    submitted_date_to = dateutil_parser('1970-01-01').date() # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
    payment_memo = "paymentMemo_example" # str | The payment memo filter. This filters via a case insensitive substring match. (optional)
    scheduled_for_date_from = dateutil_parser('1970-01-01').date() # date | Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd. (optional)
    scheduled_for_date_to = dateutil_parser('1970-01-01').date() # date | Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd. (optional)
    schedule_status = "ANY" # str | Payout Schedule Status (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId  (optional)
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get List of Payments
        api_response = api_instance.list_payments_audit_v4(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, remote_system_id=remote_system_id, status=status, transmission_type=transmission_type, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, scheduled_for_date_from=scheduled_for_date_from, scheduled_for_date_to=scheduled_for_date_to, schedule_status=schedule_status, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceApi->list_payments_audit_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. | [optional]
 **payor_id** | **str**| The account owner Payor Id. Required for external users. | [optional]
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
 **scheduled_for_date_from** | **date**| Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd. | [optional]
 **scheduled_for_date_to** | **date**| Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd. | [optional]
 **schedule_status** | **str**| Payout Schedule Status | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
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

