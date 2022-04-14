# velo_payments.PayeesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payee_by_id_v3**](PayeesApi.md#delete_payee_by_id_v3) | **DELETE** /v3/payees/{payeeId} | Delete Payee by Id
[**delete_payee_by_id_v4**](PayeesApi.md#delete_payee_by_id_v4) | **DELETE** /v4/payees/{payeeId} | Delete Payee by Id
[**get_payee_by_id_v3**](PayeesApi.md#get_payee_by_id_v3) | **GET** /v3/payees/{payeeId} | Get Payee by Id
[**get_payee_by_id_v4**](PayeesApi.md#get_payee_by_id_v4) | **GET** /v4/payees/{payeeId} | Get Payee by Id
[**list_payee_changes_v3**](PayeesApi.md#list_payee_changes_v3) | **GET** /v3/payees/deltas | List Payee Changes
[**list_payee_changes_v4**](PayeesApi.md#list_payee_changes_v4) | **GET** /v4/payees/deltas | List Payee Changes
[**list_payees_v3**](PayeesApi.md#list_payees_v3) | **GET** /v3/payees | List Payees
[**list_payees_v4**](PayeesApi.md#list_payees_v4) | **GET** /v4/payees | List Payees
[**payee_details_update_v3**](PayeesApi.md#payee_details_update_v3) | **POST** /v3/payees/{payeeId}/payeeDetailsUpdate | Update Payee Details
[**payee_details_update_v4**](PayeesApi.md#payee_details_update_v4) | **POST** /v4/payees/{payeeId}/payeeDetailsUpdate | Update Payee Details
[**v3_payees_payee_id_remote_id_update_post**](PayeesApi.md#v3_payees_payee_id_remote_id_update_post) | **POST** /v3/payees/{payeeId}/remoteIdUpdate | Update Payee Remote Id
[**v4_payees_payee_id_remote_id_update_post**](PayeesApi.md#v4_payees_payee_id_remote_id_update_post) | **POST** /v4/payees/{payeeId}/remoteIdUpdate | Update Payee Remote Id


# **delete_payee_by_id_v3**
> delete_payee_by_id_v3(payee_id)

Delete Payee by Id

<p>Use v4 instead</p> <p>This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:</p> <p>* Payee ID is not found</p> <p>* If Payee has not been on-boarded</p> <p>* If Payee is in grace period</p> <p>* If Payee has existing payments</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.

    # example passing only required values which don't have defaults set
    try:
        # Delete Payee by Id
        api_instance.delete_payee_by_id_v3(payee_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->delete_payee_by_id_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. Payee Id accepted for deletion. |  -  |
**400** | Bad Request. Payee Id failed validation for deletion. |  -  |
**404** | Payee Id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payee_by_id_v4**
> delete_payee_by_id_v4(payee_id)

Delete Payee by Id

<p>This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:</p> <p>* Payee ID is not found</p> <p>* If Payee has not been on-boarded</p> <p>* If Payee is in grace period</p> <p>* If Payee has existing payments</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.

    # example passing only required values which don't have defaults set
    try:
        # Delete Payee by Id
        api_instance.delete_payee_by_id_v4(payee_id)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->delete_payee_by_id_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content. Payee Id accepted for deletion. |  -  |
**400** | Bad Request. Payee Id failed validation for deletion. |  -  |
**404** | Payee Id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payee_by_id_v3**
> PayeeDetailResponseV3 get_payee_by_id_v3(payee_id)

Get Payee by Id

<p>Use v4 instead</p> <p>Get Payee by Id</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.payee_detail_response_v3 import PayeeDetailResponseV3
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v3(payee_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v3(payee_id, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional]

### Return type

[**PayeeDetailResponseV3**](PayeeDetailResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response, request completed okay |  -  |
**404** | Payee Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payee_by_id_v4**
> PayeeDetailResponseV4 get_payee_by_id_v4(payee_id)

Get Payee by Id

Get Payee by Id

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.payee_detail_response_v4 import PayeeDetailResponseV4
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v4(payee_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v4(payee_id, sensitive=sensitive)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional]

### Return type

[**PayeeDetailResponseV4**](PayeeDetailResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response, request completed okay |  -  |
**404** | Payee Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payee_changes_v3**
> PayeeDeltaResponseV3 list_payee_changes_v3(payor_id, updated_since)

List Payee Changes

<p>Use v4 instead</p> <p>Get a paginated response listing payee changes.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.payee_delta_response_v3 import PayeeDeltaResponseV3
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
    api_instance = payees_api.PayeesApi(api_client)
    payor_id = "payorId_example" # str | The Payor ID to find associated Payees
    updated_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 100 # int | Page size. Default is 100. Max allowable is 1000. (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # List Payee Changes
        api_response = api_instance.list_payee_changes_v3(payor_id, updated_since)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payee_changes_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payee Changes
        api_response = api_instance.list_payee_changes_v3(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payee_changes_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor ID to find associated Payees |
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 100. Max allowable is 1000. | [optional] if omitted the server will use the default value of 100

### Return type

[**PayeeDeltaResponseV3**](PayeeDeltaResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee Changes |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payee_changes_v4**
> PayeeDeltaResponseV4 list_payee_changes_v4(payor_id, updated_since)

List Payee Changes

Get a paginated response listing payee changes (updated since a particular time) to a limited set of fields: - dbaName - displayName - email - onboardedStatus - payeeCountry - payeeId - remoteId 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.payee_delta_response_v4 import PayeeDeltaResponseV4
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
    api_instance = payees_api.PayeesApi(api_client)
    payor_id = "payorId_example" # str | The Payor ID to find associated Payees
    updated_since = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 100 # int | Page size. Default is 100. Max allowable is 1000. (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # List Payee Changes
        api_response = api_instance.list_payee_changes_v4(payor_id, updated_since)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payee_changes_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payee Changes
        api_response = api_instance.list_payee_changes_v4(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payee_changes_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The Payor ID to find associated Payees |
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm |
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 100. Max allowable is 1000. | [optional] if omitted the server will use the default value of 100

### Return type

[**PayeeDeltaResponseV4**](PayeeDeltaResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee Changes |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payees_v3**
> PagedPayeeResponseV3 list_payees_v3(payor_id)

List Payees

<p>Use v4 instead</p> Get a paginated response listing the payees for a payor. 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.onboarded_status_v4 import OnboardedStatusV4
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.paged_payee_response_v3 import PagedPayeeResponseV3
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.watchlist_status_v3 import WatchlistStatusV3
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.payee_type2 import PayeeType2
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
    api_instance = payees_api.PayeesApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID
    watchlist_status = WatchlistStatusV3("NONE") # WatchlistStatusV3 | The watchlistStatus of the payees. (optional)
    disabled = True # bool | Payee disabled (optional)
    onboarded_status = OnboardedStatusV4("CREATED") # OnboardedStatusV4 | The onboarded status of the payees. (optional)
    email = "bob@example.com" # str | Email address (optional)
    display_name = "Bob Smith" # str | The display name of the payees. (optional)
    remote_id = "remoteId123" # str | The remote id of the payees. (optional)
    payee_type = PayeeType2("Individual") # PayeeType2 | The onboarded status of the payees. (optional)
    payee_country = "US" # str | The country of the payee - 2 letter ISO 3166-1 country code (upper case) (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) if omitted the server will use the default value of 25
    sort = "displayName:asc" # str | List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  (optional) if omitted the server will use the default value of "displayName:asc"

    # example passing only required values which don't have defaults set
    try:
        # List Payees
        api_response = api_instance.list_payees_v3(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payees_v3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payees
        api_response = api_instance.list_payees_v3(payor_id, watchlist_status=watchlist_status, disabled=disabled, onboarded_status=onboarded_status, email=email, display_name=display_name, remote_id=remote_id, payee_type=payee_type, payee_country=payee_country, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payees_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID |
 **watchlist_status** | **WatchlistStatusV3**| The watchlistStatus of the payees. | [optional]
 **disabled** | **bool**| Payee disabled | [optional]
 **onboarded_status** | **OnboardedStatusV4**| The onboarded status of the payees. | [optional]
 **email** | **str**| Email address | [optional]
 **display_name** | **str**| The display name of the payees. | [optional]
 **remote_id** | **str**| The remote id of the payees. | [optional]
 **payee_type** | **PayeeType2**| The onboarded status of the payees. | [optional]
 **payee_country** | **str**| The country of the payee - 2 letter ISO 3166-1 country code (upper case) | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  | [optional] if omitted the server will use the default value of "displayName:asc"

### Return type

[**PagedPayeeResponseV3**](PagedPayeeResponseV3.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payees_v4**
> PagedPayeeResponseV4 list_payees_v4(payor_id)

List Payees

Get a paginated response listing the payees for a payor.

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.onboarded_status_v4 import OnboardedStatusV4
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.ofac_status_v4 import OfacStatusV4
from velo_payments.model.watchlist_status_v3 import WatchlistStatusV3
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.paged_payee_response_v4 import PagedPayeeResponseV4
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.payee_type2 import PayeeType2
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
    api_instance = payees_api.PayeesApi(api_client)
    payor_id = "payorId_example" # str | The account owner Payor ID
    watchlist_status = WatchlistStatusV3("NONE") # WatchlistStatusV3 | The watchlistStatus of the payees. (optional)
    disabled = True # bool | Payee disabled (optional)
    onboarded_status = OnboardedStatusV4("CREATED") # OnboardedStatusV4 | The onboarded status of the payees. (optional)
    email = "bob@example.com" # str | Email address (optional)
    display_name = "Bob Smith" # str | The display name of the payees. (optional)
    remote_id = "remoteId123" # str | The remote id of the payees. (optional)
    payee_type = PayeeType2("Individual") # PayeeType2 | The onboarded status of the payees. (optional)
    payee_country = "US" # str | The country of the payee - 2 letter ISO 3166-1 country code (upper case) (optional)
    ofac_status = OfacStatusV4("PENDING") # OfacStatusV4 | The ofacStatus of the payees. (optional)
    page = 1 # int | Page number. Default is 1. (optional) if omitted the server will use the default value of 1
    page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) if omitted the server will use the default value of 25
    sort = "displayName:asc" # str | List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  (optional) if omitted the server will use the default value of "displayName:asc"

    # example passing only required values which don't have defaults set
    try:
        # List Payees
        api_response = api_instance.list_payees_v4(payor_id)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payees_v4: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Payees
        api_response = api_instance.list_payees_v4(payor_id, watchlist_status=watchlist_status, disabled=disabled, onboarded_status=onboarded_status, email=email, display_name=display_name, remote_id=remote_id, payee_type=payee_type, payee_country=payee_country, ofac_status=ofac_status, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->list_payees_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | **str**| The account owner Payor ID |
 **watchlist_status** | **WatchlistStatusV3**| The watchlistStatus of the payees. | [optional]
 **disabled** | **bool**| Payee disabled | [optional]
 **onboarded_status** | **OnboardedStatusV4**| The onboarded status of the payees. | [optional]
 **email** | **str**| Email address | [optional]
 **display_name** | **str**| The display name of the payees. | [optional]
 **remote_id** | **str**| The remote id of the payees. | [optional]
 **payee_type** | **PayeeType2**| The onboarded status of the payees. | [optional]
 **payee_country** | **str**| The country of the payee - 2 letter ISO 3166-1 country code (upper case) | [optional]
 **ofac_status** | **OfacStatusV4**| The ofacStatus of the payees. | [optional]
 **page** | **int**| Page number. Default is 1. | [optional] if omitted the server will use the default value of 1
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] if omitted the server will use the default value of 25
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  | [optional] if omitted the server will use the default value of "displayName:asc"

### Return type

[**PagedPayeeResponseV4**](PagedPayeeResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payee_details_update_v3**
> payee_details_update_v3(payee_id, update_payee_details_request_v3)

Update Payee Details

<p>Use v4 instead</p> <p>Update payee details for the given Payee Id.<p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.update_payee_details_request_v3 import UpdatePayeeDetailsRequestV3
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    update_payee_details_request_v3 = UpdatePayeeDetailsRequestV3(
        address=PayeeAddressV3(
            line1="500 Duval St",
            line2="line2_example",
            line3="line3_example",
            line4="line4_example",
            city="Key West",
            county_or_province="FL",
            zip_or_postcode="33945",
            country="US",
        ),
        individual=IndividualV3(
            name=IndividualV3Name(None),
        ),
        company=CompanyV3(
            name="ABC Group Plc",
            tax_id="123123123",
            operating_name="ABC Co",
        ),
        language="en-US",
        payee_type=PayeeType2("Individual"),
        challenge=ChallengeV3(
            value="challenge test",
            description="challenge description",
        ),
        email="bob@example.com",
    ) # UpdatePayeeDetailsRequestV3 | Request to update payee details

    # example passing only required values which don't have defaults set
    try:
        # Update Payee Details
        api_instance.payee_details_update_v3(payee_id, update_payee_details_request_v3)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->payee_details_update_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **update_payee_details_request_v3** | [**UpdatePayeeDetailsRequestV3**](UpdatePayeeDetailsRequestV3.md)| Request to update payee details |

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
**204** | Request accepted |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **payee_details_update_v4**
> payee_details_update_v4(payee_id, update_payee_details_request_v4)

Update Payee Details

<p>Update payee details for the given Payee Id.</p> <p>Payors may only update the payee details if the payee has not yet onboarded</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.inline_response404 import InlineResponse404
from velo_payments.model.update_payee_details_request_v4 import UpdatePayeeDetailsRequestV4
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    update_payee_details_request_v4 = UpdatePayeeDetailsRequestV4(
        address=PayeeAddressV4(
            line1="500 Duval St",
            line2="line2_example",
            line3="line3_example",
            line4="line4_example",
            city="Key West",
            county_or_province="FL",
            zip_or_postcode="33945",
            country="US",
        ),
        individual=IndividualV4(
            name=IndividualV3Name(None),
        ),
        company=CompanyV4(
            name="ABC Group Plc",
            tax_id="123123123",
            operating_name="ABC Co",
        ),
        language="en-US",
        payee_type=PayeeType2("Individual"),
        challenge=ChallengeV4(
            value="11984567",
            description="challenge description",
        ),
        email="bob@example.com",
        contact_sms_number="11235555555",
    ) # UpdatePayeeDetailsRequestV4 | Request to update payee details

    # example passing only required values which don't have defaults set
    try:
        # Update Payee Details
        api_instance.payee_details_update_v4(payee_id, update_payee_details_request_v4)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->payee_details_update_v4: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **update_payee_details_request_v4** | [**UpdatePayeeDetailsRequestV4**](UpdatePayeeDetailsRequestV4.md)| Request to update payee details |

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
**204** | Request accepted |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_payees_payee_id_remote_id_update_post**
> v3_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request_v3)

Update Payee Remote Id

<p>Use v4 instead</p> <p>Update the remote Id for the given Payee Id.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.update_remote_id_request_v3 import UpdateRemoteIdRequestV3
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    update_remote_id_request_v3 = UpdateRemoteIdRequestV3(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
        remote_id="remoteId123",
    ) # UpdateRemoteIdRequestV3 | Request to update payee remote id v3

    # example passing only required values which don't have defaults set
    try:
        # Update Payee Remote Id
        api_instance.v3_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request_v3)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->v3_payees_payee_id_remote_id_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **update_remote_id_request_v3** | [**UpdateRemoteIdRequestV3**](UpdateRemoteIdRequestV3.md)| Request to update payee remote id v3 |

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
**204** | Accepted, No Content |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v4_payees_payee_id_remote_id_update_post**
> v4_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request_v4)

Update Payee Remote Id

<p>Update the remote Id for the given Payee Id.</p> 

### Example

* OAuth Authentication (OAuth2):

```python
import time
import velo_payments
from velo_payments.api import payees_api
from velo_payments.model.inline_response401 import InlineResponse401
from velo_payments.model.inline_response403 import InlineResponse403
from velo_payments.model.inline_response400 import InlineResponse400
from velo_payments.model.update_remote_id_request_v4 import UpdateRemoteIdRequestV4
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
    api_instance = payees_api.PayeesApi(api_client)
    payee_id = "2aa5d7e0-2ecb-403f-8494-1865ed0454e9" # str | The UUID of the payee.
    update_remote_id_request_v4 = UpdateRemoteIdRequestV4(
        payor_id="9ac75325-5dcd-42d5-b992-175d7e0a035e",
        remote_id="remoteId123",
    ) # UpdateRemoteIdRequestV4 | Request to update payee remote id v4

    # example passing only required values which don't have defaults set
    try:
        # Update Payee Remote Id
        api_instance.v4_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request_v4)
    except velo_payments.ApiException as e:
        print("Exception when calling PayeesApi->v4_payees_payee_id_remote_id_update_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | **str**| The UUID of the payee. |
 **update_remote_id_request_v4** | [**UpdateRemoteIdRequestV4**](UpdateRemoteIdRequestV4.md)| Request to update payee remote id v4 |

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
**204** | Accepted, No Content |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

