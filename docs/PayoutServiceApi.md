# velo_payments.PayoutServiceApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quote_for_payout_v3**](PayoutServiceApi.md#create_quote_for_payout_v3) | **POST** /v3/payouts/{payoutId}/quote | Create a quote for the payout
[**deschedule_payout**](PayoutServiceApi.md#deschedule_payout) | **DELETE** /v3/payouts/{payoutId}/schedule | Deschedule a payout
[**get_payments_for_payout_v3**](PayoutServiceApi.md#get_payments_for_payout_v3) | **GET** /v3/payouts/{payoutId}/payments | Retrieve payments for a payout
[**get_payout_summary_v3**](PayoutServiceApi.md#get_payout_summary_v3) | **GET** /v3/payouts/{payoutId} | Get Payout Summary
[**instruct_payout_v3**](PayoutServiceApi.md#instruct_payout_v3) | **POST** /v3/payouts/{payoutId} | Instruct Payout
[**schedule_for_payout**](PayoutServiceApi.md#schedule_for_payout) | **POST** /v3/payouts/{payoutId}/schedule | Schedule a payout
[**submit_payout_v3**](PayoutServiceApi.md#submit_payout_v3) | **POST** /v3/payouts | Submit Payout
[**withdraw_payment**](PayoutServiceApi.md#withdraw_payment) | **POST** /v1/payments/{paymentId}/withdraw | Withdraw a Payment
[**withdraw_payout_v3**](PayoutServiceApi.md#withdraw_payout_v3) | **DELETE** /v3/payouts/{payoutId} | Withdraw Payout


# **create_quote_for_payout_v3**
> QuoteResponseV3 create_quote_for_payout_v3(payout_id)

Create a quote for the payout

Create quote for a payout

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.quote_response_v3 import QuoteResponseV3
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.inline_response409 import InlineResponse409
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout

    # example passing only required values which don't have defaults set
    try:
        # Create a quote for the payout
        api_response = api_instance.create_quote_for_payout_v3(payout_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->create_quote_for_payout_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |

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
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.inline_response409 import InlineResponse409
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout

    # example passing only required values which don't have defaults set
    try:
        # Deschedule a payout
        api_instance.deschedule_payout(payout_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->deschedule_payout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |

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
> PagedPaymentsResponseV3 get_payments_for_payout_v3(payout_id)

Retrieve payments for a payout

Retrieve payments for a payout

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.paged_payments_response_v3 import PagedPaymentsResponseV3
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout
    status = "ACCEPTED" # str | Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal  (optional)
    remote_id = "remoteId_example" # str | The remote id of the payees. (optional)
    payor_payment_id = "payorPaymentId_example" # str | Payor's Id of the Payment (optional)
    source_account_name = "sourceAccountName_example" # str | Physical Account Name (optional)
    transmission_type = "ACH" # str | Transmission Type * ACH * SAME_DAY_ACH * WIRE  (optional)
    payment_memo = "paymentMemo_example" # str | Payment Memo of the Payment (optional)
    page_size = 25 # int | The number of results to return in a page (optional) if omitted the server will use the default value of 25
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1

    # example passing only required values which don't have defaults set
    try:
        # Retrieve payments for a payout
        api_response = api_instance.get_payments_for_payout_v3(payout_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->get_payments_for_payout_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve payments for a payout
        api_response = api_instance.get_payments_for_payout_v3(payout_id, status=status, remote_id=remote_id, payor_payment_id=payor_payment_id, source_account_name=source_account_name, transmission_type=transmission_type, payment_memo=payment_memo, page_size=page_size, page=page)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->get_payments_for_payout_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |
 **status** | **str**| Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal  | [optional]
 **remote_id** | **str**| The remote id of the payees. | [optional]
 **payor_payment_id** | **str**| Payor&#39;s Id of the Payment | [optional]
 **source_account_name** | **str**| Physical Account Name | [optional]
 **transmission_type** | **str**| Transmission Type * ACH * SAME_DAY_ACH * WIRE  | [optional]
 **payment_memo** | **str**| Payment Memo of the Payment | [optional]
 **page_size** | **int**| The number of results to return in a page | [optional] if omitted the server will use the default value of 25
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1

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
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.payout_summary_response_v3 import PayoutSummaryResponseV3
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout

    # example passing only required values which don't have defaults set
    try:
        # Get Payout Summary
        api_response = api_instance.get_payout_summary_v3(payout_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->get_payout_summary_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |

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
> instruct_payout_v3(payout_id)

Instruct Payout

Instruct a payout to be made for the specified payoutId.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.instruct_payout_request import InstructPayoutRequest
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.inline_response409 import InlineResponse409
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout
    instruct_payout_request = InstructPayoutRequest(
        fx_rate_degredation_threshold_percentage=3.14,
    ) # InstructPayoutRequest | Additional instruct payout parameters (optional)

    # example passing only required values which don't have defaults set
    try:
        # Instruct Payout
        api_instance.instruct_payout_v3(payout_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->instruct_payout_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Instruct Payout
        api_instance.instruct_payout_v3(payout_id, instruct_payout_request=instruct_payout_request)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->instruct_payout_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |
 **instruct_payout_request** | [**InstructPayoutRequest**](InstructPayoutRequest.md)| Additional instruct payout parameters | [optional]

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
> schedule_for_payout(payout_id)

Schedule a payout

<p>Schedule a payout for auto-instruction in the future or update existing payout schedule if the payout has been scheduled before.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.schedule_payout_request import SchedulePayoutRequest
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.inline_response409 import InlineResponse409
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout
    schedule_payout_request = SchedulePayoutRequest(
        scheduled_for=dateutil_parser('2025-01-01T10:00:00Z'),
        notifications_enabled=True,
    ) # SchedulePayoutRequest | schedule payout parameters (optional)

    # example passing only required values which don't have defaults set
    try:
        # Schedule a payout
        api_instance.schedule_for_payout(payout_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->schedule_for_payout: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Schedule a payout
        api_instance.schedule_for_payout(payout_id, schedule_payout_request=schedule_payout_request)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->schedule_for_payout: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |
 **schedule_payout_request** | [**SchedulePayoutRequest**](SchedulePayoutRequest.md)| schedule payout parameters | [optional]

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

<p>Create a new payout and return a location header with a link to get the payout.</p> <p>Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously.</p> <p>The results can be obtained by issuing a HTTP GET to the URL returned in the location header.</p> <p>**NOTE:** amount values in payments must be in 'minor units' format. E.g. cents for USD, pence for GBP etc.</p>  with no decimal places. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.create_payout_request_v3 import CreatePayoutRequestV3
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.payment_instruction_v3 import PaymentInstructionV3
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    create_payout_request_v3 = CreatePayoutRequestV3(
        payout_from_payor_id="c4261044-13df-4a6c-b1d4-fa8be2b46f5a",
        payout_to_payor_id="9afc6b39-de12-466a-a9ca-07c7a23b312d",
        payout_memo="Monthly Payment",
        payments=[
            PaymentInstructionV3(
                remote_id="remoteId1234",
                currency="USD",
                amount=1299,
                payment_memo="my memo",
                source_account_name="MyAccountName",
                payor_payment_id="123211321ABSD",
                transmission_type=TransmissionType("ACH"),
                remote_system_id="remote_system_id_example",
                payment_metadata="invoiceeId_123|abc001:12345|xyz002:4567",
            ),
        ],
    ) # CreatePayoutRequestV3 | Post amount to transfer using stored funding account details.

    # example passing only required values which don't have defaults set
    try:
        # Submit Payout
        api_instance.submit_payout_v3(create_payout_request_v3)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->submit_payout_v3: %s\n" % e)
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
**202** | Detailed response of payout instructions |  * Location - Reference to created payout <br>  |
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
import time
import velo_payments
from velo_payments.api import payout_service_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.withdraw_payment_request import WithdrawPaymentRequest
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payment_id = "paymentId_example" # str | Id of the Payment
    withdraw_payment_request = WithdrawPaymentRequest(
        reason="Payment submitted in error",
    ) # WithdrawPaymentRequest | details for withdrawal

    # example passing only required values which don't have defaults set
    try:
        # Withdraw a Payment
        api_instance.withdraw_payment(payment_id, withdraw_payment_request)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->withdraw_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_id** | **str**| Id of the Payment |
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
import time
import velo_payments
from velo_payments.api import payout_service_api
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
    api_instance = payout_service_api.PayoutServiceApi(api_client)
    payout_id = "payoutId_example" # str | Id of the payout

    # example passing only required values which don't have defaults set
    try:
        # Withdraw Payout
        api_instance.withdraw_payout_v3(payout_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayoutServiceApi->withdraw_payout_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | **str**| Id of the payout |

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

