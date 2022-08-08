# velo_payments.PayeeInvitationApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payee_v3**](PayeeInvitationApi.md#create_payee_v3) | **POST** /v3/payees | Initiate Payee Creation
[**get_payees_invitation_status_v3**](PayeeInvitationApi.md#get_payees_invitation_status_v3) | **GET** /v3/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
[**get_payees_invitation_status_v4**](PayeeInvitationApi.md#get_payees_invitation_status_v4) | **GET** /v4/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
[**query_batch_status_v3**](PayeeInvitationApi.md#query_batch_status_v3) | **GET** /v3/payees/batch/{batchId} | Query Batch Status
[**query_batch_status_v4**](PayeeInvitationApi.md#query_batch_status_v4) | **GET** /v4/payees/batch/{batchId} | Query Batch Status
[**resend_payee_invite_v3**](PayeeInvitationApi.md#resend_payee_invite_v3) | **POST** /v3/payees/{payeeId}/invite | Resend Payee Invite
[**resend_payee_invite_v4**](PayeeInvitationApi.md#resend_payee_invite_v4) | **POST** /v4/payees/{payeeId}/invite | Resend Payee Invite
[**v4_create_payee**](PayeeInvitationApi.md#v4_create_payee) | **POST** /v4/payees | Initiate Payee Creation


# **create_payee_v3**
> CreatePayeesCSVResponseV3 create_payee_v3()

Initiate Payee Creation

<p>Use v4 instead</p> Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body. In addition to standard semantic validations, a 400 will also result if there is a duplicate remote id within the batch / if there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch). The validation at this stage is intra-batch only. Validation against payees who have already been invited occurs subsequently during processing of the batch. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.create_payees_request_v3 import CreatePayeesRequestV3
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.create_payees_csv_response_v3 import CreatePayeesCSVResponseV3
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.create_payee_v3_request import CreatePayeeV3Request
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
    create_payees_request_v3 = CreatePayeesRequestV3(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
        payees=[
            CreatePayeeV3(
                email="bob@example.com",
                remote_id="Remote ID",
                type=PayeeType2("Individual"),
                address=CreatePayeeAddressV3(
                    line1="500 Duval St",
                    line2="line2_example",
                    line3="line3_example",
                    line4="line4_example",
                    city="Key West",
                    county_or_province="FL",
                    zip_or_postcode="33945",
                    country="US",
                ),
                payment_channel=CreatePaymentChannelV3(
                    payment_channel_name="My Payment Channel",
                    iban="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234",
                    account_number="XXXXXX5678",
                    routing_number="XXXXX6789",
                    country_code="US",
                    currency="USD",
                    account_name="My account",
                ),
                challenge=ChallengeV3(
                    value="challenge test",
                    description="challenge description",
                ),
                language="en-US",
                company=CompanyV3(
                    name="ABC Group Plc",
                    tax_id="123123123",
                    operating_name="ABC Co",
                ),
                individual=CreateIndividualV3(
                    name=CreateIndividualV3Name(None),
                    national_identification="SA211123K",
                    date_of_birth=dateutil_parser('Wed May 20 00:00:00 UTC 1970').date(),
                ),
            ),
        ],
    ) # CreatePayeesRequestV3 | Post payees to create. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Payee Creation
        api_response = api_instance.create_payee_v3(create_payees_request_v3=create_payees_request_v3)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->create_payee_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payees_request_v3** | [**CreatePayeesRequestV3**](CreatePayeesRequestV3.md)| Post payees to create. | [optional]

### Return type

[**CreatePayeesCSVResponseV3**](CreatePayeesCSVResponseV3.md)

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

# **get_payees_invitation_status_v3**
> PagedPayeeInvitationStatusResponseV3 get_payees_invitation_status_v3(payor_id)

Get Payee Invitation Status

<p>Use v4 instead</p> <p>Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.invitation_status_v4 import InvitationStatusV4
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.paged_payee_invitation_status_response_v3 import PagedPayeeInvitationStatusResponseV3
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
    invitation_status = InvitationStatusV4("ACCEPTED") # InvitationStatusV4 | The invitation status of the payees. (optional)
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
 **invitation_status** | **InvitationStatusV4**| The invitation status of the payees. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] if omitted the server will use the default value of 25

### Return type

[**PagedPayeeInvitationStatusResponseV3**](PagedPayeeInvitationStatusResponseV3.md)

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
> PagedPayeeInvitationStatusResponseV4 get_payees_invitation_status_v4(payor_id)

Get Payee Invitation Status

Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.invitation_status_v4 import InvitationStatusV4
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.paged_payee_invitation_status_response_v4 import PagedPayeeInvitationStatusResponseV4
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
    invitation_status = InvitationStatusV4("ACCEPTED") # InvitationStatusV4 | The invitation status of the payees. (optional)
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
 **invitation_status** | **InvitationStatusV4**| The invitation status of the payees. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] if omitted the server will use the default value of 25

### Return type

[**PagedPayeeInvitationStatusResponseV4**](PagedPayeeInvitationStatusResponseV4.md)

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
> QueryBatchResponseV3 query_batch_status_v3(batch_id)

Query Batch Status

<p>Use v4 instead</p> Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.query_batch_response_v3 import QueryBatchResponseV3
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

[**QueryBatchResponseV3**](QueryBatchResponseV3.md)

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
> QueryBatchResponseV4 query_batch_status_v4(batch_id)

Query Batch Status

Fetch the status of a specific batch of payees. The batch is fully processed when status is ACCEPTED and pendingCount is 0 ( 200 - OK, 404 - batch not found ). 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.query_batch_response_v4 import QueryBatchResponseV4
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

[**QueryBatchResponseV4**](QueryBatchResponseV4.md)

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
> resend_payee_invite_v3(payee_id, invite_payee_request_v3)

Resend Payee Invite

<p>Use v4 instead</p> <p>Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined</p> <p>Any previous invites to the payee by this Payor will be invalidated</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payee_invitation_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.invite_payee_request_v3 import InvitePayeeRequestV3
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
    invite_payee_request_v3 = InvitePayeeRequestV3(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
    ) # InvitePayeeRequestV3 | Provide Payor Id in body of request

    # example passing only required values which don't have defaults set
    try:
        # Resend Payee Invite
        api_instance.resend_payee_invite_v3(payee_id, invite_payee_request_v3)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->resend_payee_invite_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **invite_payee_request_v3** | [**InvitePayeeRequestV3**](InvitePayeeRequestV3.md)| Provide Payor Id in body of request |

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
> resend_payee_invite_v4(payee_id, invite_payee_request_v4)

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
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.invite_payee_request_v4 import InvitePayeeRequestV4
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
    invite_payee_request_v4 = InvitePayeeRequestV4(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
    ) # InvitePayeeRequestV4 | Provide Payor Id in body of request

    # example passing only required values which don't have defaults set
    try:
        # Resend Payee Invite
        api_instance.resend_payee_invite_v4(payee_id, invite_payee_request_v4)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->resend_payee_invite_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **invite_payee_request_v4** | [**InvitePayeeRequestV4**](InvitePayeeRequestV4.md)| Provide Payor Id in body of request |

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

# **v4_create_payee**
> CreatePayeesCSVResponseV4 v4_create_payee()

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
from velo_payments.model.create_payees_request_v4 import CreatePayeesRequestV4
from velo_payments.model.create_payees_csv_response_v4 import CreatePayeesCSVResponseV4
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.v4_create_payee_request import V4CreatePayeeRequest
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
    create_payees_request_v4 = CreatePayeesRequestV4(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
        payees=[
            CreatePayeeV4(
                email="bob@example.com",
                remote_id="Remote ID",
                type=PayeeType2("Individual"),
                address=CreatePayeeAddressV4(
                    line1="500 Duval St",
                    line2="line2_example",
                    line3="line3_example",
                    line4="line4_example",
                    city="Key West",
                    county_or_province="FL",
                    zip_or_postcode="33945",
                    country="US",
                ),
                payment_channel=CreatePaymentChannelV4(
                    payment_channel_name="My Payment Channel",
                    iban="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX1234",
                    account_number="XXXXXX5678",
                    routing_number="XXXXX6789",
                    country_code="US",
                    currency="USD",
                    account_name="My account",
                ),
                challenge=ChallengeV4(
                    value="11984567",
                    description="challenge description",
                ),
                language="en-US",
                company=CompanyV4(
                    name="ABC Group Plc",
                    tax_id="123123123",
                    operating_name="ABC Co",
                ),
                individual=CreateIndividualV4(
                    name=CreateIndividualV3Name(None),
                    national_identification="SA211123K",
                    date_of_birth=dateutil_parser('Wed May 20 00:00:00 UTC 1970').date(),
                ),
            ),
        ],
    ) # CreatePayeesRequestV4 | Post payees to create. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initiate Payee Creation
        api_response = api_instance.v4_create_payee(create_payees_request_v4=create_payees_request_v4)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeeInvitationApi->v4_create_payee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payees_request_v4** | [**CreatePayeesRequestV4**](CreatePayeesRequestV4.md)| Post payees to create. | [optional]

### Return type

[**CreatePayeesCSVResponseV4**](CreatePayeesCSVResponseV4.md)

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

