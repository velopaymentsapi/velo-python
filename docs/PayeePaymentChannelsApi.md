# velo_payments.PayeePaymentChannelsApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payment_channel_v4**](PayeePaymentChannelsApi.md#create_payment_channel_v4) | **POST** /v4/payees/{payeeId}/paymentChannels/ | Create Payment Channel
[**delete_payment_channel_v4**](PayeePaymentChannelsApi.md#delete_payment_channel_v4) | **DELETE** /v4/payees/{payeeId}/paymentChannels/{paymentChannelId} | Delete Payment Channel
[**enable_payment_channel_v4**](PayeePaymentChannelsApi.md#enable_payment_channel_v4) | **POST** /v4/payees/{payeeId}/paymentChannels/{paymentChannelId}/enable | Enable Payment Channel
[**get_payment_channel_v4**](PayeePaymentChannelsApi.md#get_payment_channel_v4) | **GET** /v4/payees/{payeeId}/paymentChannels/{paymentChannelId} | Get Payment Channel Details
[**get_payment_channels_v4**](PayeePaymentChannelsApi.md#get_payment_channels_v4) | **GET** /v4/payees/{payeeId}/paymentChannels/ | Get All Payment Channels Details
[**update_payment_channel_order_v4**](PayeePaymentChannelsApi.md#update_payment_channel_order_v4) | **PUT** /v4/payees/{payeeId}/paymentChannels/order | Update Payees preferred Payment Channel order
[**update_payment_channel_v4**](PayeePaymentChannelsApi.md#update_payment_channel_v4) | **POST** /v4/payees/{payeeId}/paymentChannels/{paymentChannelId} | Update Payment Channel


# **create_payment_channel_v4**
> create_payment_channel_v4(payee_id, create_payment_channel_request_v4)

Create Payment Channel

<p>Create a payment channel</p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
create_payment_channel_request_v4 = velo_payments.CreatePaymentChannelRequestV4() # CreatePaymentChannelRequestV4 | Post payment channel to update

try:
    # Create Payment Channel
    api_instance.create_payment_channel_v4(payee_id, create_payment_channel_request_v4)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->create_payment_channel_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **create_payment_channel_request_v4** | [**CreatePaymentChannelRequestV4**](CreatePaymentChannelRequestV4.md)| Post payment channel to update | 

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
**201** | Payment channel is created. |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_payment_channel_v4**
> delete_payment_channel_v4(payee_id, payment_channel_id)

Delete Payment Channel

<p>Delete a payees payment channel</p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
payment_channel_id = '70faaff7-2c32-4b44-b27f-f0b6c484e6f3' # str | The UUID of the payment channel.

try:
    # Delete Payment Channel
    api_instance.delete_payment_channel_v4(payee_id, payment_channel_id)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->delete_payment_channel_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **payment_channel_id** | [**str**](.md)| The UUID of the payment channel. | 

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
**204** | Deleted. No content. |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_payment_channel_v4**
> enable_payment_channel_v4(payee_id, payment_channel_id)

Enable Payment Channel

<p>Enable a payment channel for a payee</p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
payment_channel_id = '70faaff7-2c32-4b44-b27f-f0b6c484e6f3' # str | The UUID of the payment channel.

try:
    # Enable Payment Channel
    api_instance.enable_payment_channel_v4(payee_id, payment_channel_id)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->enable_payment_channel_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **payment_channel_id** | [**str**](.md)| The UUID of the payment channel. | 

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
**204** | Enabled. No content. |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_channel_v4**
> PaymentChannelResponseV4 get_payment_channel_v4(payee_id, payment_channel_id, payable=payable, sensitive=sensitive)

Get Payment Channel Details

<p>Get the payment channel details for the payee</p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
payment_channel_id = '70faaff7-2c32-4b44-b27f-f0b6c484e6f3' # str | The UUID of the payment channel.
payable = True # bool | payable if true only return the payment channel if the payee is payable (optional)
sensitive = True # bool | <p>Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.</p> <p>If set to true, and you have permission, the PII values will be returned as their original unmasked values.</p>  (optional)

try:
    # Get Payment Channel Details
    api_response = api_instance.get_payment_channel_v4(payee_id, payment_channel_id, payable=payable, sensitive=sensitive)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->get_payment_channel_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **payment_channel_id** | [**str**](.md)| The UUID of the payment channel. | 
 **payable** | **bool**| payable if true only return the payment channel if the payee is payable | [optional] 
 **sensitive** | **bool**| &lt;p&gt;Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.&lt;/p&gt; &lt;p&gt;If set to true, and you have permission, the PII values will be returned as their original unmasked values.&lt;/p&gt;  | [optional] 

### Return type

[**PaymentChannelResponseV4**](PaymentChannelResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response, request completed okay |  -  |
**204** | payee not payable but the request is valid |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_channels_v4**
> PaymentChannelsResponseV4 get_payment_channels_v4(payee_id, payor_id=payor_id, payable=payable, sensitive=sensitive, ignore_payor_invite_status=ignore_payor_invite_status)

Get All Payment Channels Details

<p>Get all payment channels details for a payee</p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
payor_id = 'payor_id_example' # str | <p>(UUID) the id of the Payor.</p> <p>If specified the payment channels are filtered to those mapped to this payor.</p>  (optional)
payable = True # bool | payable if true only return the payment channel if the payee is payable (optional)
sensitive = True # bool | <p>Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.</p> <p>If set to true, and you have permission, the PII values will be returned as their original unmasked values.</p>  (optional)
ignore_payor_invite_status = True # bool | payable if true only return the payment channel if the payee is payable (optional)

try:
    # Get All Payment Channels Details
    api_response = api_instance.get_payment_channels_v4(payee_id, payor_id=payor_id, payable=payable, sensitive=sensitive, ignore_payor_invite_status=ignore_payor_invite_status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->get_payment_channels_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **payor_id** | [**str**](.md)| &lt;p&gt;(UUID) the id of the Payor.&lt;/p&gt; &lt;p&gt;If specified the payment channels are filtered to those mapped to this payor.&lt;/p&gt;  | [optional] 
 **payable** | **bool**| payable if true only return the payment channel if the payee is payable | [optional] 
 **sensitive** | **bool**| &lt;p&gt;Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked.&lt;/p&gt; &lt;p&gt;If set to true, and you have permission, the PII values will be returned as their original unmasked values.&lt;/p&gt;  | [optional] 
 **ignore_payor_invite_status** | **bool**| payable if true only return the payment channel if the payee is payable | [optional] 

### Return type

[**PaymentChannelsResponseV4**](PaymentChannelsResponseV4.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response, request completed okay |  -  |
**204** | payee not payable but the request is valid |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_channel_order_v4**
> update_payment_channel_order_v4(payee_id, payment_channel_order_request_v4)

Update Payees preferred Payment Channel order

<p>Update the Payee's preferred order of payment channels by passing in just the payment channel ids. When payments are made to the payee then in the absence of any other rules (e.g. matching on currency) the first payment channel in this list will be chosen. </p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
payment_channel_order_request_v4 = velo_payments.PaymentChannelOrderRequestV4() # PaymentChannelOrderRequestV4 | Put the payment channel ids in the preferred order

try:
    # Update Payees preferred Payment Channel order
    api_instance.update_payment_channel_order_v4(payee_id, payment_channel_order_request_v4)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->update_payment_channel_order_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **payment_channel_order_request_v4** | [**PaymentChannelOrderRequestV4**](PaymentChannelOrderRequestV4.md)| Put the payment channel ids in the preferred order | 

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
**204** | Request accepted. No content. |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_channel_v4**
> update_payment_channel_v4(payee_id, payment_channel_id, update_payment_channel_request_v4)

Update Payment Channel

<p>Update the details of the payment channel. Note payment channels are immutable. The current payment channel will be logically deleted as part of this call and replaced with new one with the correct details; this endpoint will return a Location header with a link to the new payment channel upon success. Updating a currently disabled payment channel will result in a new, fully enabled, payment channel.</p> 

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
api_instance = velo_payments.PayeePaymentChannelsApi(velo_payments.ApiClient(configuration))
payee_id = '2aa5d7e0-2ecb-403f-8494-1865ed0454e9' # str | The UUID of the payee.
payment_channel_id = '70faaff7-2c32-4b44-b27f-f0b6c484e6f3' # str | The UUID of the payment channel.
update_payment_channel_request_v4 = velo_payments.UpdatePaymentChannelRequestV4() # UpdatePaymentChannelRequestV4 | Post payment channel to update

try:
    # Update Payment Channel
    api_instance.update_payment_channel_v4(payee_id, payment_channel_id, update_payment_channel_request_v4)
except ApiException as e:
    print("Exception when calling PayeePaymentChannelsApi->update_payment_channel_v4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payee_id** | [**str**](.md)| The UUID of the payee. | 
 **payment_channel_id** | [**str**](.md)| The UUID of the payment channel. | 
 **update_payment_channel_request_v4** | [**UpdatePaymentChannelRequestV4**](UpdatePaymentChannelRequestV4.md)| Post payment channel to update | 

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
**204** | Request accepted. No content. |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**409** | The request contained data that would result in a duplicate value  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

