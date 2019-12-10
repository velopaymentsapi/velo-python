# velo_payments.PayeeInvitationApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_payees_invitation_status**](PayeeInvitationApi.md#get_payees_invitation_status) | **GET** /v1/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
[**get_payees_invitation_status_v2**](PayeeInvitationApi.md#get_payees_invitation_status_v2) | **GET** /v2/payees/payors/{payorId}/invitationStatus | Get Payee Invitation Status
[**resend_payee_invite**](PayeeInvitationApi.md#resend_payee_invite) | **POST** /v1/payees/{payeeId}/invite | Resend Payee Invite
[**v2_create_payee**](PayeeInvitationApi.md#v2_create_payee) | **POST** /v2/payees | Intiate Payee Creation V2
[**v2_query_batch_status**](PayeeInvitationApi.md#v2_query_batch_status) | **GET** /v2/payees/batch/{batchId} | Query Batch Status
[**v3_create_payee**](PayeeInvitationApi.md#v3_create_payee) | **POST** /v3/payees | Intiate Payee Creation V3
[**v3_query_batch_status**](PayeeInvitationApi.md#v3_query_batch_status) | **GET** /v3/payees/batch/{batchId} | Query Batch Status


# **get_payees_invitation_status**
> InvitationStatusResponse get_payees_invitation_status(payor_id)

Get Payee Invitation Status

Returns a list of payees associated with a payor, along with invitation status and grace period end date. 

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
payor_id = 'payor_id_example' # str | The account owner Payor ID

try:
    # Get Payee Invitation Status
    api_response = api_instance.get_payees_invitation_status(payor_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->get_payees_invitation_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 

### Return type

[**InvitationStatusResponse**](InvitationStatusResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get Payees with Invitaion status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payees_invitation_status_v2**
> PagedPayeeInvitationStatusResponse get_payees_invitation_status_v2(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)

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
payor_id = 'payor_id_example' # str | The account owner Payor ID
payee_id = 'payee_id_example' # str | The UUID of the payee. (optional)
invitation_status = velo_payments.InvitationStatus() # InvitationStatus | The invitation status of the payees. (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)

try:
    # Get Payee Invitation Status
    api_response = api_instance.get_payees_invitation_status_v2(payor_id, payee_id=payee_id, invitation_status=invitation_status, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->get_payees_invitation_status_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **payee_id** | [**str**](.md)| The UUID of the payee. | [optional] 
 **invitation_status** | [**InvitationStatus**](.md)| The invitation status of the payees. | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]

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
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_payee_invite**
> InvitationStatusResponse resend_payee_invite(payee_id, invite_payee_request)

Resend Payee Invite

Resend an invite to the Payee The payee must have already been invited by the payor and not yet accepted or declined Any previous invites to the payee by this Payor will be invalidated

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
payee_id = 'payee_id_example' # str | The UUID of the payee.
invite_payee_request = velo_payments.InvitePayeeRequest() # InvitePayeeRequest | 

try:
    # Resend Payee Invite
    api_response = api_instance.resend_payee_invite(payee_id, invite_payee_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->resend_payee_invite: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **invite_payee_request** | [**InvitePayeeRequest**](InvitePayeeRequest.md)|  | 

### Return type

[**InvitationStatusResponse**](InvitationStatusResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 200 response, request completed okay |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_create_payee**
> CreatePayeesCSVResponse v2_create_payee(create_payees_request)

Intiate Payee Creation V2

Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body, 409 - if there is a duplicate remote id within the batch / if there is a duplicate email within the batch). 

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
create_payees_request = velo_payments.CreatePayeesRequest() # CreatePayeesRequest | Post payees to create.

try:
    # Intiate Payee Creation V2
    api_response = api_instance.v2_create_payee(create_payees_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->v2_create_payee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payees_request** | [**CreatePayeesRequest**](CreatePayeesRequest.md)| Post payees to create. | 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_query_batch_status**
> QueryBatchResponse v2_query_batch_status(batch_id)

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
    api_response = api_instance.v2_query_batch_status(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->v2_query_batch_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | [**str**](.md)| Batch Id | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_create_payee**
> CreatePayeesCSVResponse2 v3_create_payee(create_payees_request2)

Intiate Payee Creation V3

Initiate the process of creating 1 to 2000 payees in a batch Use the response location header to query for status (201 - Created, 400 - invalid request body, 409 - if there is a duplicate remote id within the batch / if there is a duplicate email within the batch). 

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
create_payees_request2 = velo_payments.CreatePayeesRequest2() # CreatePayeesRequest2 | Post payees to create.

try:
    # Intiate Payee Creation V3
    api_response = api_instance.v3_create_payee(create_payees_request2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->v3_create_payee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payees_request2** | [**CreatePayeesRequest2**](CreatePayeesRequest2.md)| Post payees to create. | 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_query_batch_status**
> QueryBatchResponse v3_query_batch_status(batch_id)

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
    api_response = api_instance.v3_query_batch_status(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeeInvitationApi->v3_query_batch_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | [**str**](.md)| Batch Id | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

