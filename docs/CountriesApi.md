# velo_payments.CountriesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_payment_channel_rules_v1**](CountriesApi.md#list_payment_channel_rules_v1) | **GET** /v1/paymentChannelRules | List Payment Channel Country Rules
[**list_supported_countries_v1**](CountriesApi.md#list_supported_countries_v1) | **GET** /v1/supportedCountries | List Supported Countries
[**list_supported_countries_v2**](CountriesApi.md#list_supported_countries_v2) | **GET** /v2/supportedCountries | List Supported Countries


# **list_payment_channel_rules_v1**
> PaymentChannelRulesResponse list_payment_channel_rules_v1()

List Payment Channel Country Rules

List the country specific payment channel rules.

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
api_instance = velo_payments.CountriesApi(velo_payments.ApiClient(configuration))

try:
    # List Payment Channel Country Rules
    api_response = api_instance.list_payment_channel_rules_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->list_payment_channel_rules_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PaymentChannelRulesResponse**](PaymentChannelRulesResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Payment Channel Country Rules |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_countries_v1**
> SupportedCountriesResponse list_supported_countries_v1()

List Supported Countries

<p>List the supported countries.</p> <p>This version will be retired in March 2020. Use /v2/supportedCountries</p> 

### Example

```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = velo_payments.CountriesApi()

try:
    # List Supported Countries
    api_response = api_instance.list_supported_countries_v1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->list_supported_countries_v1: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedCountriesResponse**](SupportedCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Supported Countries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_supported_countries_v2**
> SupportedCountriesResponseV2 list_supported_countries_v2()

List Supported Countries

List the supported countries.

### Example

```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = velo_payments.CountriesApi()

try:
    # List Supported Countries
    api_response = api_instance.list_supported_countries_v2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountriesApi->list_supported_countries_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedCountriesResponseV2**](SupportedCountriesResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Supported Countries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

