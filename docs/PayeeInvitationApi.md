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
> CreatePayeesCSVResponseV3 create_payee_v3(create_payees_request_v3=create_payees_request_v3)

Initiate Payee Creation

<p>Use v4 instead</p> Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body. In addition to standard semantic validations, a 400 will also result if there is a duplicate remote id within the batch / if there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch). The validation at this stage is intra-batch only. Validation against payees who have already been invited occurs subsequently during processing of the batch. 

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
create_payees_request_v3 = velo_payments.CreatePayeesRequestV3() # CreatePayeesRequestV3 | Post payees to create. (optional)

try:
    # Initiate Payee Creation
    api_response = api_instance.create_payee_v3(create_payees_request_v3=create_payees_request_v3)
    pprint(api_response)
except ApiException as e:
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
> PagedPayeeInvitationStatusResponseV3 get_payees_invitation_status_v3(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)

Get Payee Invitation Status

<p>Use v4 instead</p> <p>Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date.</p> 

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
payor_id = '9ac75325-5dcd-42d5-b992-175d7e0a035e' # str | The account owner Payor ID
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee. (optional)
invitation_status = 'invitation_status_example' # str | The invitation status of the payees. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)

try:
    # Get Payee Invitation Status
    api_response = api_instance.get_payees_invitation_status_v3(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **payee_id** | [**str**](.md)| The UUID of the payee. | [optional] 
 **invitation_status** | **str**| The invitation status of the payees. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]

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
> PagedPayeeInvitationStatusResponseV4 get_payees_invitation_status_v4(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)

Get Payee Invitation Status

Returns a filtered, paginated list of payees associated with a payor, along with invitation status and grace period end date. 

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
payor_id = '9ac75325-5dcd-42d5-b992-175d7e0a035e' # str | The account owner Payor ID
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee. (optional)
invitation_status = 'invitation_status_example' # str | The invitation status of the payees. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)

try:
    # Get Payee Invitation Status
    api_response = api_instance.get_payees_invitation_status_v4(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **payee_id** | [**str**](.md)| The UUID of the payee. | [optional] 
 **invitation_status** | **str**| The invitation status of the payees. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
batch_id = 'batch_id_example' # str | Batch Id

try:
    # Query Batch Status
    api_response = api_instance.query_batch_status_v3(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->query_batch_status_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | [**str**](.md)| Batch Id | 

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
batch_id = 'batch_id_example' # str | Batch Id

try:
    # Query Batch Status
    api_response = api_instance.query_batch_status_v4(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->query_batch_status_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | [**str**](.md)| Batch Id | 

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
invite_payee_request_v3 = velo_payments.InvitePayeeRequestV3() # InvitePayeeRequestV3 | Provide Payor Id in body of request

try:
    # Resend Payee Invite
    api_instance.resend_payee_invite_v3(payee_id, invite_payee_request_v3)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->resend_payee_invite_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
invite_payee_request_v4 = velo_payments.InvitePayeeRequestV4() # InvitePayeeRequestV4 | Provide Payor Id in body of request

try:
    # Resend Payee Invite
    api_instance.resend_payee_invite_v4(payee_id, invite_payee_request_v4)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->resend_payee_invite_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
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
> CreatePayeesCSVResponseV4 v4_create_payee(create_payees_request_v4=create_payees_request_v4)

Initiate Payee Creation

<p>Initiate the process of creating 1 to 2000 payees in a batch</p> <p>Use the batchId in the response to query for status.</p> <p>In addition to standard semantic validations, a 400 will also result if: </p> <ul> <li>there is a duplicate remote id within the batch</li> <li>there is a duplicate email within the batch, i.e. if there is a conflict between the data provided for one payee within the batch and that provided for another payee within the same batch).</li> </ul> <p>The validation at this stage is intra-batch only.</p> <p>Validation against payees who have already been invited occurs subsequently during processing of the batch.</p> 

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
api_instance = velo_payments.PayeeInvitationApi(velo_payments.ApiClient(configuration))
create_payees_request_v4 = velo_payments.CreatePayeesRequestV4() # CreatePayeesRequestV4 | Post payees to create. (optional)

try:
    # Initiate Payee Creation
    api_response = api_instance.v4_create_payee(create_payees_request_v4=create_payees_request_v4)
    pprint(api_response)
except ApiException as e:
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
**201** | HTTP Created. Body created only on CSV requests |  * Location -  <br>  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

