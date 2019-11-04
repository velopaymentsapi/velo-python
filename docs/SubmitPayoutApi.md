# velo_payments.SubmitPayoutApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**submit_payout**](SubmitPayoutApi.md#submit_payout) | **POST** /v3/payouts | Submit Payout


# **submit_payout**
> submit_payout(create_payout_request)

Submit Payout

Create a new payout and return a location header with a link to get the payout. Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously, the results of which can be obtained by issuing a HTTP GET to the URL returned in the location header. **NOTE:** amount values in payments must be in 'minor units' format. E.g. cents for USD, pence for GBP etc.  with no decimal places. 

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
api_instance = velo_payments.SubmitPayoutApi(velo_payments.ApiClient(configuration))
create_payout_request = velo_payments.CreatePayoutRequest() # CreatePayoutRequest | Post amount to transfer using stored funding account details.

try:
    # Submit Payout
    api_instance.submit_payout(create_payout_request)
except ApiException as e:
    print("Exception when calling SubmitPayoutApi->submit_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_payout_request** | [**CreatePayoutRequest**](CreatePayoutRequest.md)| Post amount to transfer using stored funding account details. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Detailed response of payout instructions |  * Location - Reference to created payout <br>  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

