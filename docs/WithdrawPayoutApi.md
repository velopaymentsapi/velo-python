# velo_payments.WithdrawPayoutApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v3_payouts_payout_id_delete**](WithdrawPayoutApi.md#v3_payouts_payout_id_delete) | **DELETE** /v3/payouts/{payoutId} | Withdraw Payout


# **v3_payouts_payout_id_delete**
> v3_payouts_payout_id_delete(payout_id)

Withdraw Payout

Withdraw Payout will delete payout details from payout service and rails services but will just move the status of the payout to WITHDRAWN in payment audit.

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
api_instance = velo_payments.WithdrawPayoutApi(velo_payments.ApiClient(configuration))
payout_id = 'payout_id_example' # str | Id of the payout

try:
    # Withdraw Payout
    api_instance.v3_payouts_payout_id_delete(payout_id)
except ApiException as e:
    print("Exception when calling WithdrawPayoutApi->v3_payouts_payout_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payout_id** | [**str**](.md)| Id of the payout | 

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
**202** | HTTP 202 Accepted |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

