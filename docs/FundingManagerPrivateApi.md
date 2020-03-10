# velo_payments.FundingManagerPrivateApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_funding_account**](FundingManagerPrivateApi.md#create_funding_account) | **POST** /v1/fundingAccounts | Create Funding Account


# **create_funding_account**
> create_funding_account(create_funding_account_request=create_funding_account_request)

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
configuration = velo_payments.Configuration()
# Configure OAuth2 access token for authorization: OAuth2
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Defining host is optional and default to https://api.sandbox.velopayments.com
configuration.host = "https://api.sandbox.velopayments.com"

# Enter a context with an instance of the API client
with velo_payments.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = velo_payments.FundingManagerPrivateApi(api_client)
    create_funding_account_request = velo_payments.CreateFundingAccountRequest() # CreateFundingAccountRequest |  (optional)

    try:
        # Create Funding Account
        api_instance.create_funding_account(create_funding_account_request=create_funding_account_request)
    except ApiException as e:
        print("Exception when calling FundingManagerPrivateApi->create_funding_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_funding_account_request** | [**CreateFundingAccountRequest**](CreateFundingAccountRequest.md)|  | [optional] 

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
**202** | Funding Account Created |  * Location - Reference to created account <br>  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**401** | Invalid access token. May be expired or invalid |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

