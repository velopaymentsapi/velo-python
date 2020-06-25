# velo_payments.PayeesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payee_by_id_v1**](PayeesApi.md#delete_payee_by_id_v1) | **DELETE** /v1/payees/{payeeId} | Delete Payee by Id
[**delete_payee_by_id_v3**](PayeesApi.md#delete_payee_by_id_v3) | **DELETE** /v3/payees/{payeeId} | Delete Payee by Id
[**get_payee_by_id_v1**](PayeesApi.md#get_payee_by_id_v1) | **GET** /v1/payees/{payeeId} | Get Payee by Id
[**get_payee_by_id_v2**](PayeesApi.md#get_payee_by_id_v2) | **GET** /v2/payees/{payeeId} | Get Payee by Id
[**get_payee_by_id_v3**](PayeesApi.md#get_payee_by_id_v3) | **GET** /v3/payees/{payeeId} | Get Payee by Id
[**list_payee_changes**](PayeesApi.md#list_payee_changes) | **GET** /v1/deltas/payees | List Payee Changes
[**list_payee_changes_v3**](PayeesApi.md#list_payee_changes_v3) | **GET** /v3/payees/deltas | List Payee Changes
[**list_payees_v1**](PayeesApi.md#list_payees_v1) | **GET** /v1/payees | List Payees V1
[**list_payees_v3**](PayeesApi.md#list_payees_v3) | **GET** /v3/payees | List Payees
[**payee_details_update_v3**](PayeesApi.md#payee_details_update_v3) | **POST** /v3/payees/{payeeId}/payeeDetailsUpdate | Update Payee Details
[**v1_payees_payee_id_remote_id_update_post**](PayeesApi.md#v1_payees_payee_id_remote_id_update_post) | **POST** /v1/payees/{payeeId}/remoteIdUpdate | Update Payee Remote Id
[**v3_payees_payee_id_remote_id_update_post**](PayeesApi.md#v3_payees_payee_id_remote_id_update_post) | **POST** /v3/payees/{payeeId}/remoteIdUpdate | Update Payee Remote Id


# **delete_payee_by_id_v1**
> delete_payee_by_id_v1(payee_id)

Delete Payee by Id

<p>This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:</p> <p>* Payee ID is not found</p> <p>* If Payee has not been on-boarded</p> <p>* If Payee is in grace period</p> <p>* If Payee has existing payments</p> <p>Please use V3 instead.</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.

    try:
        # Delete Payee by Id
        api_instance.delete_payee_by_id_v1(payee_id)
    except ApiException as e:
        print("Exception when calling PayeesApi->delete_payee_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 

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

# **delete_payee_by_id_v3**
> delete_payee_by_id_v3(payee_id)

Delete Payee by Id

<p>This API will delete Payee by Id (UUID). Deletion by ID is not allowed if:</p> <p>* Payee ID is not found</p> <p>* If Payee has not been on-boarded</p> <p>* If Payee is in grace period</p> <p>* If Payee has existing payments</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.

    try:
        # Delete Payee by Id
        api_instance.delete_payee_by_id_v3(payee_id)
    except ApiException as e:
        print("Exception when calling PayeesApi->delete_payee_by_id_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 

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

# **get_payee_by_id_v1**
> Payee get_payee_by_id_v1(payee_id, sensitive=sensitive)

Get Payee by Id

<p>Get Payee by Id</p> <p>Please use V3 instead.</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v1(payee_id, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**Payee**](Payee.md)

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

# **get_payee_by_id_v2**
> PayeeResponseV2 get_payee_by_id_v2(payee_id, sensitive=sensitive)

Get Payee by Id

<p>Get Payee by Id</p> <p>Please use V3 instead.</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v2(payee_id, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**PayeeResponseV2**](PayeeResponseV2.md)

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

# **get_payee_by_id_v3**
> PayeeDetailResponse get_payee_by_id_v3(payee_id, sensitive=sensitive)

Get Payee by Id

Get Payee by Id

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

    try:
        # Get Payee by Id
        api_response = api_instance.get_payee_by_id_v3(payee_id, sensitive=sensitive)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->get_payee_by_id_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **sensitive** | **bool**| Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  | [optional] 

### Return type

[**PayeeDetailResponse**](PayeeDetailResponse.md)

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

# **list_payee_changes**
> PayeeDeltaResponse list_payee_changes(payor_id, updated_since, page=page, page_size=page_size)

List Payee Changes

<p>Get a paginated response listing payee changes.</p> <p>Please use V3 instead.</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payor_id = 'payor_id_example' # str | The Payor ID to find associated Payees
updated_since = '2013-10-20T19:20:30+01:00' # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 100 # int | Page size. Default is 100. Max allowable is 1000. (optional) (default to 100)

    try:
        # List Payee Changes
        api_response = api_instance.list_payee_changes(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->list_payee_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID to find associated Payees | 
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 100. Max allowable is 1000. | [optional] [default to 100]

### Return type

[**PayeeDeltaResponse**](PayeeDeltaResponse.md)

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

# **list_payee_changes_v3**
> PayeeDeltaResponse2 list_payee_changes_v3(payor_id, updated_since, page=page, page_size=page_size)

List Payee Changes

Get a paginated response listing payee changes.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payor_id = 'payor_id_example' # str | The Payor ID to find associated Payees
updated_since = '2013-10-20T19:20:30+01:00' # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 100 # int | Page size. Default is 100. Max allowable is 1000. (optional) (default to 100)

    try:
        # List Payee Changes
        api_response = api_instance.list_payee_changes_v3(payor_id, updated_since, page=page, page_size=page_size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->list_payee_changes_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The Payor ID to find associated Payees | 
 **updated_since** | **datetime**| The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm | 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 100. Max allowable is 1000. | [optional] [default to 100]

### Return type

[**PayeeDeltaResponse2**](PayeeDeltaResponse2.md)

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

# **list_payees_v1**
> PagedPayeeResponse list_payees_v1(payor_id, ofac_status=ofac_status, onboarded_status=onboarded_status, email=email, display_name=display_name, remote_id=remote_id, payee_type=payee_type, payee_country=payee_country, page=page, page_size=page_size, sort=sort)

List Payees V1

<p>Get a paginated response listing the payees for a payor.</p> <p>Please use V3 instead.</> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payor_id = 'payor_id_example' # str | The account owner Payor ID
ofac_status = velo_payments.OfacStatus() # OfacStatus | The ofacStatus of the payees. (optional)
onboarded_status = velo_payments.OnboardedStatus() # OnboardedStatus | The onboarded status of the payees. (optional)
email = 'bob@example.com' # str | Email address (optional)
display_name = 'Bob Smith' # str | The display name of the payees. (optional)
remote_id = 'remoteId123' # str | The remote id of the payees. (optional)
payee_type = velo_payments.PayeeType() # PayeeType | The onboarded status of the payees. (optional)
payee_country = 'US' # str | The country of the payee - 2 letter ISO 3166-1 country code (upper case) (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'displayName:asc' # str | List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  (optional) (default to 'displayName:asc')

    try:
        # List Payees V1
        api_response = api_instance.list_payees_v1(payor_id, ofac_status=ofac_status, onboarded_status=onboarded_status, email=email, display_name=display_name, remote_id=remote_id, payee_type=payee_type, payee_country=payee_country, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->list_payees_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **ofac_status** | [**OfacStatus**](.md)| The ofacStatus of the payees. | [optional] 
 **onboarded_status** | [**OnboardedStatus**](.md)| The onboarded status of the payees. | [optional] 
 **email** | [**str**](.md)| Email address | [optional] 
 **display_name** | **str**| The display name of the payees. | [optional] 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **payee_type** | [**PayeeType**](.md)| The onboarded status of the payees. | [optional] 
 **payee_country** | **str**| The country of the payee - 2 letter ISO 3166-1 country code (upper case) | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  | [optional] [default to &#39;displayName:asc&#39;]

### Return type

[**PagedPayeeResponse**](PagedPayeeResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payee |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payees_v3**
> PagedPayeeResponse2 list_payees_v3(payor_id, watchlist_status=watchlist_status, disabled=disabled, onboarded_status=onboarded_status, email=email, display_name=display_name, remote_id=remote_id, payee_type=payee_type, payee_country=payee_country, page=page, page_size=page_size, sort=sort)

List Payees

Get a paginated response listing the payees for a payor.

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payor_id = 'payor_id_example' # str | The account owner Payor ID
watchlist_status = velo_payments.WatchlistStatus() # WatchlistStatus | The watchlistStatus of the payees. (optional)
disabled = True # bool | Payee disabled (optional)
onboarded_status = velo_payments.OnboardedStatus() # OnboardedStatus | The onboarded status of the payees. (optional)
email = 'bob@example.com' # str | Email address (optional)
display_name = 'Bob Smith' # str | The display name of the payees. (optional)
remote_id = 'remoteId123' # str | The remote id of the payees. (optional)
payee_type = velo_payments.PayeeType() # PayeeType | The onboarded status of the payees. (optional)
payee_country = 'US' # str | The country of the payee - 2 letter ISO 3166-1 country code (upper case) (optional)
page = 1 # int | Page number. Default is 1. (optional) (default to 1)
page_size = 25 # int | Page size. Default is 25. Max allowable is 100. (optional) (default to 25)
sort = 'displayName:asc' # str | List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  (optional) (default to 'displayName:asc')

    try:
        # List Payees
        api_response = api_instance.list_payees_v3(payor_id, watchlist_status=watchlist_status, disabled=disabled, onboarded_status=onboarded_status, email=email, display_name=display_name, remote_id=remote_id, payee_type=payee_type, payee_country=payee_country, page=page, page_size=page_size, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PayeesApi->list_payees_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payor_id** | [**str**](.md)| The account owner Payor ID | 
 **watchlist_status** | [**WatchlistStatus**](.md)| The watchlistStatus of the payees. | [optional] 
 **disabled** | **bool**| Payee disabled | [optional] 
 **onboarded_status** | [**OnboardedStatus**](.md)| The onboarded status of the payees. | [optional] 
 **email** | [**str**](.md)| Email address | [optional] 
 **display_name** | **str**| The display name of the payees. | [optional] 
 **remote_id** | **str**| The remote id of the payees. | [optional] 
 **payee_type** | [**PayeeType**](.md)| The onboarded status of the payees. | [optional] 
 **payee_country** | **str**| The country of the payee - 2 letter ISO 3166-1 country code (upper case) | [optional] 
 **page** | **int**| Page number. Default is 1. | [optional] [default to 1]
 **page_size** | **int**| Page size. Default is 25. Max allowable is 100. | [optional] [default to 25]
 **sort** | **str**| List of sort fields (e.g. ?sort&#x3D;onboardedStatus:asc,name:asc) Default is name:asc &#39;name&#39; is treated as company name for companies - last name + &#39;,&#39; + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus.  | [optional] [default to &#39;displayName:asc&#39;]

### Return type

[**PagedPayeeResponse2**](PagedPayeeResponse2.md)

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
> payee_details_update_v3(payee_id, update_payee_details_request)

Update Payee Details

<p>Update payee details for the given Payee Id.<p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
update_payee_details_request = velo_payments.UpdatePayeeDetailsRequest() # UpdatePayeeDetailsRequest | Request to update payee details

    try:
        # Update Payee Details
        api_instance.payee_details_update_v3(payee_id, update_payee_details_request)
    except ApiException as e:
        print("Exception when calling PayeesApi->payee_details_update_v3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **update_payee_details_request** | [**UpdatePayeeDetailsRequest**](UpdatePayeeDetailsRequest.md)| Request to update payee details | 

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

# **v1_payees_payee_id_remote_id_update_post**
> v1_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request)

Update Payee Remote Id

<p>Update the remote Id for the given Payee Id.</p> <p>Please use V3 instead</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
update_remote_id_request = velo_payments.UpdateRemoteIdRequest() # UpdateRemoteIdRequest | Request to update payee remote id v1

    try:
        # Update Payee Remote Id
        api_instance.v1_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request)
    except ApiException as e:
        print("Exception when calling PayeesApi->v1_payees_payee_id_remote_id_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **update_remote_id_request** | [**UpdateRemoteIdRequest**](UpdateRemoteIdRequest.md)| Request to update payee remote id v1 | 

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
**202** | Accepted, No Content |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v3_payees_payee_id_remote_id_update_post**
> v3_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request)

Update Payee Remote Id

<p>Update the remote Id for the given Payee Id.</p> 

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
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
    api_instance = velo_payments.PayeesApi(api_client)
    payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
update_remote_id_request = velo_payments.UpdateRemoteIdRequest() # UpdateRemoteIdRequest | Request to update payee remote id v3

    try:
        # Update Payee Remote Id
        api_instance.v3_payees_payee_id_remote_id_update_post(payee_id, update_remote_id_request)
    except ApiException as e:
        print("Exception when calling PayeesApi->v3_payees_payee_id_remote_id_update_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **update_remote_id_request** | [**UpdateRemoteIdRequest**](UpdateRemoteIdRequest.md)| Request to update payee remote id v3 | 

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

