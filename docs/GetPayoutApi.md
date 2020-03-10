# velo_payments.GetPayoutApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_payouts_payout_id_get**](GetPayoutApi.md#v3_payouts_payout_id_get) | **GET** /v3/payouts/{payoutId} | Get Payout Summary


# **v3_payouts_payout_id_get**
> PayoutSummaryResponse v3_payouts_payout_id_get(payout_id)

Get Payout Summary

Get payout summary - returns the current state of the payout.

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

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.GetPayoutApi(api_client)
    payout_id = 'payout_id_example' # str | Id of the payout

    try:
        # Get Payout Summary
        api_response = api_instance.v3_payouts_payout_id_get(payout_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GetPayoutApi->v3_payouts_payout_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 

### Return type

[**PayoutSummaryResponse**](PayoutSummaryResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payout |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

