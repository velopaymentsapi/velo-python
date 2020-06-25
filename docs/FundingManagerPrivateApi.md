# velo_payments.FundingManagerPrivateApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_funding_account_v2**](FundingManagerPrivateApi.md#create_funding_account_v2) | **POST** /v2/fundingAccounts | Create Funding Account


# **create_funding_account_v2**
> create_funding_account_v2(create_funding_account_request_v2=create_funding_account_request_v2)

Create Funding Account

Create Funding Account

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
    api_instance = velo_payments.FundingManagerPrivateApi(api_client)
    create_funding_account_request_v2 = {"type":"FBO","name":"My FBO Account","payorId":"ee53e01d-c078-43fd-abd4-47e92f4a06cf","accountName":"My Account Name","accountNumber":1231231234556,"routingNumber":123456789} # CreateFundingAccountRequestV2 |  (optional)

    try:
        # Create Funding Account
        api_instance.create_funding_account_v2(create_funding_account_request_v2=create_funding_account_request_v2)
    except ApiException as e:
        print("Exception when calling FundingManagerPrivateApi->create_funding_account_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_funding_account_request_v2** | [**CreateFundingAccountRequestV2**](CreateFundingAccountRequestV2.md)|  | [optional] 

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
**202** | Funding Account Creation Request Accepted |  * Location - Reference to status object <br>  * Retry-After - How long the user agent should wait before making a follow-up request (seconds) <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

