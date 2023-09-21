# velo_payments.PayorHierarchyApi

All URIs are relative to *https://api.sandbox.velopayments.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**payor_links_v1**](PayorHierarchyApi.md#payor_links_v1) | **GET** /v1/payorLinks | List Payor Links


# **payor_links_v1**
> PayorLinksResponse payor_links_v1(descendants_of_payor=descendants_of_payor, parent_of_payor=parent_of_payor, fields=fields)

List Payor Links

<p>If the payor is set up as part of a hierarchy you can use this API to traverse the hierarchy</p> 

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
api_instance = velo_payments.PayorHierarchyApi(velo_payments.ApiClient(configuration))
descendants_of_payor = 'descendants_of_payor_example' # str | The Payor ID from which to start the query to show all descendants (optional)
parent_of_payor = 'parent_of_payor_example' # str | Query for the parent payor details for this payor id (optional)
fields = 'fields_example' # str | <p>List of additional Payor fields to include in the response for each Payor</p> <p>The values of payorId and payorName are always included for each Payor by default</p> <p>You can add fields to the response for each payor by including them in the fields parameter separated by commas</p> <p>The supported fields are any combination of: primaryContactEmail,kycState</p>  (optional)

try:
    # List Payor Links
    api_response = api_instance.payor_links_v1(descendants_of_payor=descendants_of_payor, parent_of_payor=parent_of_payor, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayorHierarchyApi->payor_links_v1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descendants_of_payor** | [**str**](.md)| The Payor ID from which to start the query to show all descendants | [optional] 
 **parent_of_payor** | [**str**](.md)| Query for the parent payor details for this payor id | [optional] 
 **fields** | **str**| &lt;p&gt;List of additional Payor fields to include in the response for each Payor&lt;/p&gt; &lt;p&gt;The values of payorId and payorName are always included for each Payor by default&lt;/p&gt; &lt;p&gt;You can add fields to the response for each payor by including them in the fields parameter separated by commas&lt;/p&gt; &lt;p&gt;The supported fields are any combination of: primaryContactEmail,kycState&lt;/p&gt;  | [optional] 

### Return type

[**PayorLinksResponse**](PayorLinksResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Details of Payor Links |  -  |
**400** | Invalid request. See Error message payload for details of failure |  -  |
**404** | The resource was not found or is no longer available  |  -  |
**403** | The authentication does not have permissions to access the resource This usually occurs when there is a valid authentication instance (client or user) but they do not have the required permissions  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

