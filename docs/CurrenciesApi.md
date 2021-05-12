# velo_payments.CurrenciesApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_supported_currencies_v2**](CurrenciesApi.md#list_supported_currencies_v2) | **GET** /v2/currencies | List Supported Currencies


# **list_supported_currencies_v2**
> SupportedCurrencyResponseV2 list_supported_currencies_v2()

List Supported Currencies

List the supported currencies.

### Example

```python
from __future__ import print_function
import time
import velo_payments
from velo_payments.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = velo_payments.CurrenciesApi()

try:
    # List Supported Currencies
    api_response = api_instance.list_supported_currencies_v2()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->list_supported_currencies_v2: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SupportedCurrencyResponseV2**](SupportedCurrencyResponseV2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List Supported Currencies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

