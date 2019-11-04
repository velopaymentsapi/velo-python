# velo_payments.CurrenciesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_supported_currencies**](CurrenciesApi.md#list_supported_currencies) | **GET** /v2/currencies | List Supported Currencies


# **list_supported_currencies**
> SupportedCurrencyResponse list_supported_currencies()

List Supported Currencies

List the supported currencies.

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
api_instance = velo_payments.CurrenciesApi(velo_payments.ApiClient(configuration))

try:
    # List Supported Currencies
    api_response = api_instance.list_supported_currencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_supported_currencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedCurrencyResponse**](SupportedCurrencyResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Supported Currencies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

