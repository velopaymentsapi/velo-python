# velo_payments.PaymentAuditServiceDeprecatedApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_transactions_csvv3**](PaymentAuditServiceDeprecatedApi.md#export_transactions_csvv3) | **GET** /v3/paymentaudit/transactions | V3 Export Transactions
[**get_fundings_v1**](PaymentAuditServiceDeprecatedApi.md#get_fundings_v1) | **GET** /v1/paymentaudit/fundings | V1 Get Fundings for Payor
[**get_payment_details_v3**](PaymentAuditServiceDeprecatedApi.md#get_payment_details_v3) | **GET** /v3/paymentaudit/payments/{paymentId} | V3 Get Payment
[**get_payments_for_payout_pav3**](PaymentAuditServiceDeprecatedApi.md#get_payments_for_payout_pav3) | **GET** /v3/paymentaudit/payouts/{payoutId} | V3 Get Payments for Payout
[**get_payout_stats_v1**](PaymentAuditServiceDeprecatedApi.md#get_payout_stats_v1) | **GET** /v1/paymentaudit/payoutStatistics | V1 Get Payout Statistics
[**get_payouts_for_payor_v3**](PaymentAuditServiceDeprecatedApi.md#get_payouts_for_payor_v3) | **GET** /v3/paymentaudit/payouts | V3 Get Payouts for Payor
[**list_payment_changes**](PaymentAuditServiceDeprecatedApi.md#list_payment_changes) | **GET** /v1/deltas/payments | V1 List Payment Changes
[**list_payments_audit_v3**](PaymentAuditServiceDeprecatedApi.md#list_payments_audit_v3) | **GET** /v3/paymentaudit/payments | V3 Get List of Payments


# **export_transactions_csvv3**
> PayorAmlTransactionV3 export_transactions_csvv3()

V3 Export Transactions

Deprecated (use /v4/paymentaudit/transactions instead)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.payor_aml_transaction_v3 import PayorAmlTransactionV3
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payor_id = "payorId_example" # str | The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  (optional)
    start_date = dateutil_parser('1970-01-01').date() # date | Start date, inclusive. Format is YYYY-MM-DD (optional)
    end_date = dateutil_parser('1970-01-01').date() # date | End date, inclusive. Format is YYYY-MM-DD (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V3 Export Transactions
        api_response = api_instance.export_transactions_csvv3(payor_id=payor_id, start_date=start_date, end_date=end_date)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->export_transactions_csvv3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor ID for whom you wish to run the report. For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.  | [optional]
 **start_date** | **date**| Start date, inclusive. Format is YYYY-MM-DD | [optional]
 **end_date** | **date**| End date, inclusive. Format is YYYY-MM-DD | [optional]

### Return type

[**PayorAmlTransactionV3**](PayorAmlTransactionV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/csv, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Export Transactions response |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fundings_v1**
> GetFundingsResponse get_fundings_v1(payor_id)

V1 Get Fundings for Payor

Deprecated (use /v4/paymentaudit/fundings)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # V1 Get Fundings for Payor
        api_response = api_instance.get_fundings_v1(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_fundings_v1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V1 Get Fundings for Payor
        api_response = api_instance.get_fundings_v1(payor_id, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_fundings_v1: %s\n" % e)
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

# **get_payment_details_v3**
> PaymentResponseV3 get_payment_details_v3(payment_id)

V3 Get Payment

Deprecated (use /v4/paymentaudit/payments/<paymentId> instead)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.payment_response_v3 import PaymentResponseV3
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payment_id = "paymentId_example" # str | Payment Id
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # V3 Get Payment
        api_response = api_instance.get_payment_details_v3(payment_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payment_details_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V3 Get Payment
        api_response = api_instance.get_payment_details_v3(payment_id, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payment_details_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Payment Id |
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
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payments_for_payout_pav3**
> GetPaymentsForPayoutResponseV3 get_payments_for_payout_pav3(payout_id)

V3 Get Payments for Payout

Deprecated (use /v4/paymentaudit/payouts/<payoutId> instead)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.get_payments_for_payout_response_v3 import GetPaymentsForPayoutResponseV3
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payout_id = "payoutId_example" # str | The id (UUID) of the payout.
    remote_id = "remoteId_example" # str | The remote id of the payees. (optional)
    status = "ACCEPTED" # str | Payment Status (optional)
    source_amount_from = 1 # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
    source_amount_to = 1 # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
    payment_amount_from = 1 # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
    payment_amount_to = 1 # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
    submitted_date_from = dateutil_parser('1970-01-01').date() # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
    submitted_date_to = dateutil_parser('1970-01-01').date() # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | <p>List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId</p> <p>The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status</p>  (optional)
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # V3 Get Payments for Payout
        api_response = api_instance.get_payments_for_payout_pav3(payout_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payments_for_payout_pav3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V3 Get Payments for Payout
        api_response = api_instance.get_payments_for_payout_pav3(payout_id, remote_id=remote_id, status=status, source_amount_from=source_amount_from, source_amount_to=source_amount_to, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payments_for_payout_pav3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| The id (UUID) of the payout. |
 **remote_id** | **str**| The remote id of the payees. | [optional]
 **status** | **str**| Payment Status | [optional]
 **source_amount_from** | **int**| The source amount from range filter. Filters for sourceAmount &gt;&#x3D; sourceAmountFrom | [optional]
 **source_amount_to** | **int**| The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo | [optional]
 **payment_amount_from** | **int**| The payment amount from range filter. Filters for paymentAmount &gt;&#x3D; paymentAmountFrom | [optional]
 **payment_amount_to** | **int**| The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo | [optional]
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional]
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| &lt;p&gt;List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId&lt;/p&gt; &lt;p&gt;The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status&lt;/p&gt;  | [optional]
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
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payout_stats_v1**
> GetPayoutStatistics get_payout_stats_v1()

V1 Get Payout Statistics

Deprecated (Use /v4/paymentaudit/payoutStatistics)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID. Required for external users. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V1 Get Payout Statistics
        api_response = api_instance.get_payout_stats_v1(payor_id=payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payout_stats_v1: %s\n" % e)
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

# **get_payouts_for_payor_v3**
> GetPayoutsResponseV3 get_payouts_for_payor_v3(payor_id)

V3 Get Payouts for Payor

Deprecated (use /v4/paymentaudit/payouts instead)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.get_payouts_response_v3 import GetPayoutsResponseV3
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID
    payout_memo = "payoutMemo_example" # str | Payout Memo filter - case insensitive sub-string match (optional)
    status = "ACCEPTED" # str | Payout Status (optional)
    submitted_date_from = dateutil_parser('1970-01-01').date() # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
    submitted_date_to = dateutil_parser('1970-01-01').date() # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # V3 Get Payouts for Payor
        api_response = api_instance.get_payouts_for_payor_v3(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payouts_for_payor_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V3 Get Payouts for Payor
        api_response = api_instance.get_payouts_for_payor_v3(payor_id, payout_memo=payout_memo, status=status, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->get_payouts_for_payor_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID |
 **payout_memo** | **str**| Payout Memo filter - case insensitive sub-string match | [optional]
 **status** | **str**| Payout Status | [optional]
 **submitted_date_from** | **date**| The submitted date from range filter. Format is yyyy-MM-dd. | [optional]
 **submitted_date_to** | **date**| The submitted date to range filter. Format is yyyy-MM-dd. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
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
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_changes**
> PaymentDeltaResponseV1 list_payment_changes(payor_id, updated_since)

V1 List Payment Changes

Deprecated (use /v4/payments/deltas instead)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
from velo_payments.model.payment_delta_response_v1 import PaymentDeltaResponseV1
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payor_id = "payorId_example" # str | The Payor ID to find associated Payments
    updated_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 100 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # V1 List Payment Changes
        api_response = api_instance.list_payment_changes(payor_id, updated_since)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->list_payment_changes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V1 List Payment Changes
        api_response = api_instance.list_payment_changes(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->list_payment_changes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor ID to find associated Payments |
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 100

### Return type

[**PaymentDeltaResponseV1**](PaymentDeltaResponseV1.md)

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

# **list_payments_audit_v3**
> ListPaymentsResponseV3 list_payments_audit_v3()

V3 Get List of Payments

Deprecated (use /v4/paymentaudit/payments instead)

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payment_audit_service_deprecated_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.list_payments_response_v3 import ListPaymentsResponseV3
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
    api_instance = payment_audit_service_deprecated_api.PaymentAuditServiceDeprecatedApi(api_client)
    payee_id = "payeeId_example" # str | The UUID of the payee. (optional)
    payor_id = "payorId_example" # str | The account owner Payor Id. Required for external users. (optional)
    payor_name = "payorName_example" # str | The payor’s name. This filters via a case insensitive substring match. (optional)
    remote_id = "remoteId_example" # str | The remote id of the payees. (optional)
    status = "ACCEPTED" # str | Payment Status (optional)
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
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    sort = "sort_example" # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # V3 Get List of Payments
        api_response = api_instance.list_payments_audit_v3(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PaymentAuditServiceDeprecatedApi->list_payments_audit_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. | [optional]
 **payor_id** | **str**| The account owner Payor Id. Required for external users. | [optional]
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
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  | [optional]
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional]

### Return type

[**ListPaymentsResponseV3**](ListPaymentsResponseV3.md)

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

