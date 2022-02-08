# velo_payments.PayeeInvitationApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payees_invitation_status_v3**](PayeeInvitationApi.md#get_payees_invitation_status_v3) | **GET** /v3/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
[**get_payees_invitation_status_v4**](PayeeInvitationApi.md#get_payees_invitation_status_v4) | **GET** /v4/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
[**query_batch_status_v3**](PayeeInvitationApi.md#query_batch_status_v3) | **GET** /v3/payees/batch/{batchId} | Query Batch Status
[**query_batch_status_v4**](PayeeInvitationApi.md#query_batch_status_v4) | **GET** /v4/payees/batch/{batchId} | Query Batch Status
[**resend_payee_invite_v3**](PayeeInvitationApi.md#resend_payee_invite_v3) | **POST** /v3/payees/{payeeId}/invite | Resend Payee Invite
[**resend_payee_invite_v4**](PayeeInvitationApi.md#resend_payee_invite_v4) | **POST** /v4/payees/{payeeId}/invite | Resend Payee Invite
[**v3_create_payee**](PayeeInvitationApi.md#v3_create_payee) | **POST** /v3/payees | Initiate Payee Creation
[**v4_create_payee**](PayeeInvitationApi.md#v4_create_payee) | **POST** /v4/payees | Initiate Payee Creation


# **get_payees_invitation_status_v3**
> PagedPayeeInvitationStatusResponse get_payees_invitation_status_v3(payor_id)

Get Payee Invitation Status

<p>Use v4 instead</p> <p>Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.paged_payee_invitation_status_response import PagedPayeeInvitationStatusResponse
from velo_payments.model.invitation_status import InvitationStatus
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    payor_id = "9ac75325-5dcd-42d5-b992-175d7e0a035e" # str | The account owner Payor ID
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee. (optional)
    invitation_status = InvitationStatus("ACCEPTED") # InvitationStatus | The invitation status of the payees. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get Payee Invitation Status
        api_response = api_instance.get_payees_invitation_status_v3(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payee Invitation Status
        api_response = api_instance.get_payees_invitation_status_v3(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID |
 **payee_id** | **str**| The UUID of the payee. | [optional]
 **invitation_status** | **InvitationStatus**| The invitation status of the payees. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] if omitted the server will use the default value of 25

### Return type

[**PagedPayeeInvitationStatusResponse**](PagedPayeeInvitationStatusResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Payees with Invitaion status - filters of payeeId and invitationStatus |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payees_invitation_status_v4**
> PagedPayeeInvitationStatusResponse2 get_payees_invitation_status_v4(payor_id)

Get Payee Invitation Status

Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.invitation_status import InvitationStatus
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.paged_payee_invitation_status_response2 import PagedPayeeInvitationStatusResponse2
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    payor_id = "9ac75325-5dcd-42d5-b992-175d7e0a035e" # str | The account owner Payor ID
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee. (optional)
    invitation_status = InvitationStatus("ACCEPTED") # InvitationStatus | The invitation status of the payees. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) if omitted the server will use the default value of 25

    # example passing only required values which don't have defaults set
    try:
        # Get Payee Invitation Status
        api_response = api_instance.get_payees_invitation_status_v4(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payee Invitation Status
        api_response = api_instance.get_payees_invitation_status_v4(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID |
 **payee_id** | **str**| The UUID of the payee. | [optional]
 **invitation_status** | **InvitationStatus**| The invitation status of the payees. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] if omitted the server will use the default value of 25

### Return type

[**PagedPayeeInvitationStatusResponse2**](PagedPayeeInvitationStatusResponse2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Payees with Invitaion status - filters of payeeId and invitationStatus |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_batch_status_v3**
> QueryBatchResponse query_batch_status_v3(batch_id)

Query Batch Status

<p>Use v4 instead</p> Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.query_batch_response import QueryBatchResponse
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    batch_id = "batchId_example" # str | Batch Id

    # example passing only required values which don't have defaults set
    try:
        # Query Batch Status
        api_response = api_instance.query_batch_status_v3(batch_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->query_batch_status_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Batch Id |

### Return type

[**QueryBatchResponse**](QueryBatchResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Batch Status |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_batch_status_v4**
> QueryBatchResponse2 query_batch_status_v4(batch_id)

Query Batch Status

Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.query_batch_response2 import QueryBatchResponse2
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    batch_id = "batchId_example" # str | Batch Id

    # example passing only required values which don't have defaults set
    try:
        # Query Batch Status
        api_response = api_instance.query_batch_status_v4(batch_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->query_batch_status_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| Batch Id |

### Return type

[**QueryBatchResponse2**](QueryBatchResponse2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Batch Status |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_payee_invite_v3**
> resend_payee_invite_v3(payee_id, invite_payee_request)

Resend Payee Invite

<p>Use v4 instead</p> <p>Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined</p> <p>Any previous invites to the payee by this Payor will be invalidated</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.invite_payee_request import InvitePayeeRequest
from velo_payments.model.inline_response403 import InlineResponse403
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    invite_payee_request = InvitePayeeRequest(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
    ) # InvitePayeeRequest | Provide Payor Id in body of request

    # example passing only required values which don't have defaults set
    try:
        # Resend Payee Invite
        api_instance.resend_payee_invite_v3(payee_id, invite_payee_request)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->resend_payee_invite_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **invite_payee_request** | [**InvitePayeeRequest**](InvitePayeeRequest.md)| Provide Payor Id in body of request |

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
**200** | the request was accepted |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_payee_invite_v4**
> resend_payee_invite_v4(payee_id, invite_payee_request2)

Resend Payee Invite

<p>Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined</p> <p>Any previous invites to the payee by this Payor will be invalidated</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.invite_payee_request2 import InvitePayeeRequest2
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    invite_payee_request2 = InvitePayeeRequest2(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
    ) # InvitePayeeRequest2 | Provide Payor Id in body of request

    # example passing only required values which don't have defaults set
    try:
        # Resend Payee Invite
        api_instance.resend_payee_invite_v4(payee_id, invite_payee_request2)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->resend_payee_invite_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **invite_payee_request2** | [**InvitePayeeRequest2**](InvitePayeeRequest2.md)| Provide Payor Id in body of request |

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
**200** | the request was accepted |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_payee**
> CreatePayeesCSVResponse v3_create_payee()

Initiate Payee Creation

<p>Use v4 instead</p> Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body. In addition to standard semantic validations, a 400 will also result if there is a duplicate remote id within the batch / if there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch). The validation at this stage is intra-batch only. Validation against payees who have already been invited occurs subsequently during processing of the batch. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.create_payees_csv_response import CreatePayeesCSVResponse
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.create_payees_csv_request import CreatePayeesCSVRequest
from velo_payments.model.create_payees_request import CreatePayeesRequest
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    create_payees_request = CreatePayeesRequest(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
        payees=[
            CreatePayee(
                email="bob@example.com",
                remote_id="Remote ID",
                type=PayeeType2("Individual"),
                address=CreatePayeeAddress(
                    line1="500 Duval St",
                    line2="line2_example",
                    line3="line3_example",
                    line4="line4_example",
                    city="Key West",
                    county_or_province="FL",
                    zip_or_postcode="33945",
                    country="US",
                ),
                payment_channel=CreatePaymentChannel(
                    payment_channel_name="My Payment Channel",
                    iban="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234",
                    account_number="XXXXXX5678",
                    routing_number="XXXXX6789",
                    country_code="US",
                    currency="USD",
                    account_name="My account",
                ),
                challenge=Challenge(
                    value="challenge test",
                    description="challenge description",
                ),
                language="en-US",
                company=Company(
                    name="ABC Group Plc",
                    tax_id="123123123",
                    operating_name="ABC Co",
                ),
                individual=CreateIndividual(
                    name=CreateIndividualName(None),
                    national_identification="SA211123K",
                    date_of_birth=dateutil_parser('Wed May 20 00:00:00 UTC 1970').date(),
                ),
            ),
        ],
    ) # CreatePayeesRequest | Post payees to create. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Payee Creation
        api_response = api_instance.v3_create_payee(create_payees_request=create_payees_request)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->v3_create_payee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payees_request** | [**CreatePayeesRequest**](CreatePayeesRequest.md)| Post payees to create. | [optional]

### Return type

[**CreatePayeesCSVResponse**](CreatePayeesCSVResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | HTTP Created. Body created only on CSV requests |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_create_payee**
> CreatePayeesCSVResponse2 v4_create_payee()

Initiate Payee Creation

Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body. In addition to standard semantic validations, a 400 will also result if there is a duplicate remote id within the batch / if there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch). The validation at this stage is intra-batch only. Validation against payees who have already been invited occurs subsequently during processing of the batch. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.create_payees_csv_request2 import CreatePayeesCSVRequest2
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.create_payees_csv_response2 import CreatePayeesCSVResponse2
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.create_payees_request2 import CreatePayeesRequest2
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
    api_instance = payee_invitation_api.PayeeInvitationApi(api_client)
    create_payees_request2 = CreatePayeesRequest2(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
        payees=[
            CreatePayee2(
                email="bob@example.com",
                remote_id="Remote ID",
                type=PayeeType2("Individual"),
                address=CreatePayeeAddress2(
                    line1="500 Duval St",
                    line2="line2_example",
                    line3="line3_example",
                    line4="line4_example",
                    city="Key West",
                    county_or_province="FL",
                    zip_or_postcode="33945",
                    country="US",
                ),
                payment_channel=CreatePaymentChannel2(
                    payment_channel_name="My Payment Channel",
                    iban="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234",
                    account_number="XXXXXX5678",
                    routing_number="XXXXX6789",
                    country_code="US",
                    currency="USD",
                    account_name="My account",
                ),
                challenge=Challenge2(
                    value="11984567",
                    description="challenge description",
                ),
                language="en-US",
                company=Company2(
                    name="ABC Group Plc",
                    tax_id="123123123",
                    operating_name="ABC Co",
                ),
                individual=CreateIndividual2(
                    name=CreateIndividualName(None),
                    national_identification="SA211123K",
                    date_of_birth=dateutil_parser('Wed May 20 00:00:00 UTC 1970').date(),
                ),
            ),
        ],
    ) # CreatePayeesRequest2 | Post payees to create. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Payee Creation
        api_response = api_instance.v4_create_payee(create_payees_request2=create_payees_request2)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->v4_create_payee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payees_request2** | [**CreatePayeesRequest2**](CreatePayeesRequest2.md)| Post payees to create. | [optional]

### Return type

[**CreatePayeesCSVResponse2**](CreatePayeesCSVResponse2.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | HTTP Created. Body created only on CSV requests |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

