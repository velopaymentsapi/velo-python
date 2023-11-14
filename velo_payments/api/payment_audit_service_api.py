# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   ## Http Status Codes Following is a list of Http Status codes that could be returned by the platform      | Status Code            | Description                                                                          |     | -----------------------| -------------------------------------------------------------------------------------|     | 200 OK                 | The request was successfully processed and usually returns a json response           |     | 201 Created            | A resource was created and a Location header is returned linking to the new resource |     | 202 Accepted           | The request has been accepted for processing                                         |     | 204 No Content         | The request has been processed and there is no response (usually deletes and updates)|     | 400 Bad Request        | The request is invalid and should be fixed before retrying                           |     | 401 Unauthorized       | Authentication has failed, usually means the token has expired                       |     | 403 Forbidden          | The user does not have permissions for the request                                   |     | 404 Not Found          | The resource was not found                                                           |     | 409 Conflict           | The resource already exists and there is a conflict                                  |     | 429 Too Many Requests  | The user has submitted too many requests in a given amount of time                   |     | 5xx Server Error       | Platform internal error (should rarely happen)                                       |   # noqa: E501

    The version of the OpenAPI document: 2.37.148
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from velo_payments.api_client import ApiClient
from velo_payments.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PaymentAuditServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def export_transactions_csvv4(self, **kwargs):  # noqa: E501
        """Export Transactions  # noqa: E501

        Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export_transactions_csvv4(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: <p>The Payor ID for whom you wish to run the report.</p> <p>For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.</p> 
        :param date start_date: Start date, inclusive. Format is YYYY-MM-DD
        :param date end_date: End date, inclusive. Format is YYYY-MM-DD
        :param str include: <p>Mode to determine whether to include other Payor's data in the results.</p> <p>May only be used if payorId is specified.</p> <p>Can be omitted or set to 'payorOnly' or 'payorAndDescendants'.</p> <p>payorOnly: Only include results for the specified Payor. This is the default if 'include' is omitted.</p> <p>payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.</p> <p>Note when a Payor requests the report and include=payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id</p> 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PayorAmlTransaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.export_transactions_csvv4_with_http_info(**kwargs)  # noqa: E501

    def export_transactions_csvv4_with_http_info(self, **kwargs):  # noqa: E501
        """Export Transactions  # noqa: E501

        Download a CSV file containing payments in a date range. Uses Transfer-Encoding - chunked to stream to the client. Date range is inclusive of both the start and end dates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.export_transactions_csvv4_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: <p>The Payor ID for whom you wish to run the report.</p> <p>For a Payor requesting the report, this could be their exact Payor, or it could be a child/descendant Payor.</p> 
        :param date start_date: Start date, inclusive. Format is YYYY-MM-DD
        :param date end_date: End date, inclusive. Format is YYYY-MM-DD
        :param str include: <p>Mode to determine whether to include other Payor's data in the results.</p> <p>May only be used if payorId is specified.</p> <p>Can be omitted or set to 'payorOnly' or 'payorAndDescendants'.</p> <p>payorOnly: Only include results for the specified Payor. This is the default if 'include' is omitted.</p> <p>payorAndDescendants: Aggregate results for all descendant Payors of the specified Payor. Should only be used if the Payor with the specified payorId has at least one child Payor.</p> <p>Note when a Payor requests the report and include=payorAndDescendants is used, the following additional columns are included in the CSV: Payor Name, Payor Id</p> 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PayorAmlTransaction, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payor_id', 'start_date', 'end_date', 'include']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method export_transactions_csvv4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'start_date' in local_var_params:
            query_params.append(('startDate', local_var_params['start_date']))  # noqa: E501
        if 'end_date' in local_var_params:
            query_params.append(('endDate', local_var_params['end_date']))  # noqa: E501
        if 'include' in local_var_params:
            query_params.append(('include', local_var_params['include']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/csv', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/transactions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayorAmlTransaction',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_fundings_v4(self, payor_id, **kwargs):  # noqa: E501
        """Get Fundings for Payor  # noqa: E501

        <p>Get a list of Fundings for a payor.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fundings_v4(payor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The account owner Payor ID (required)
        :param str source_account_name: The source account name
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetFundingsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_fundings_v4_with_http_info(payor_id, **kwargs)  # noqa: E501

    def get_fundings_v4_with_http_info(self, payor_id, **kwargs):  # noqa: E501
        """Get Fundings for Payor  # noqa: E501

        <p>Get a list of Fundings for a payor.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fundings_v4_with_http_info(payor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The account owner Payor ID (required)
        :param str source_account_name: The source account name
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetFundingsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payor_id', 'source_account_name', 'page', 'page_size', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_fundings_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payor_id' is set
        if ('payor_id' not in local_var_params or
                local_var_params['payor_id'] is None):
            raise ApiValueError("Missing the required parameter `payor_id` when calling `get_fundings_v4`")  # noqa: E501

        if 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_fundings_v4`, must be a value less than or equal to `100`")  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_fundings_v4`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'source_account_name' in local_var_params:
            query_params.append(('sourceAccountName', local_var_params['source_account_name']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/fundings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetFundingsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payment_details_v4(self, payment_id, **kwargs):  # noqa: E501
        """Get Payment  # noqa: E501

        Get the payment with the given id. This contains the payment history.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_details_v4(payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_id: Payment Id (required)
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaymentResponseV4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payment_details_v4_with_http_info(payment_id, **kwargs)  # noqa: E501

    def get_payment_details_v4_with_http_info(self, payment_id, **kwargs):  # noqa: E501
        """Get Payment  # noqa: E501

        Get the payment with the given id. This contains the payment history.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payment_details_v4_with_http_info(payment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_id: Payment Id (required)
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaymentResponseV4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payment_id', 'sensitive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payment_details_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in local_var_params or
                local_var_params['payment_id'] is None):
            raise ApiValueError("Missing the required parameter `payment_id` when calling `get_payment_details_v4`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in local_var_params:
            path_params['paymentId'] = local_var_params['payment_id']  # noqa: E501

        query_params = []
        if 'sensitive' in local_var_params:
            query_params.append(('sensitive', local_var_params['sensitive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/payments/{paymentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentResponseV4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payments_for_payout_v4(self, payout_id, **kwargs):  # noqa: E501
        """Get Payments for Payout  # noqa: E501

        Get List of payments for Payout, allowing for RETURNED status   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_for_payout_v4(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: The id (UUID) of the payout. (required)
        :param str rails_id: Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the 'Get Supported Rails' endpoint. 
        :param str remote_id: The remote id of the payees.
        :param str remote_system_id: The id of the remote system that is orchestrating payments
        :param str status: Payment Status
        :param int source_amount_from: The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
        :param int source_amount_to: The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
        :param int payment_amount_from: The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
        :param int payment_amount_to: The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
        :param date submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
        :param date submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
        :param str transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status 
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetPaymentsForPayoutResponseV4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payments_for_payout_v4_with_http_info(payout_id, **kwargs)  # noqa: E501

    def get_payments_for_payout_v4_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Get Payments for Payout  # noqa: E501

        Get List of payments for Payout, allowing for RETURNED status   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_for_payout_v4_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: The id (UUID) of the payout. (required)
        :param str rails_id: Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the 'Get Supported Rails' endpoint. 
        :param str remote_id: The remote id of the payees.
        :param str remote_system_id: The id of the remote system that is orchestrating payments
        :param str status: Payment Status
        :param int source_amount_from: The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
        :param int source_amount_to: The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
        :param int payment_amount_from: The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
        :param int payment_amount_to: The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
        :param date submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
        :param date submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
        :param str transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status 
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetPaymentsForPayoutResponseV4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id', 'rails_id', 'remote_id', 'remote_system_id', 'status', 'source_amount_from', 'source_amount_to', 'payment_amount_from', 'payment_amount_to', 'submitted_date_from', 'submitted_date_to', 'transmission_type', 'page', 'page_size', 'sort', 'sensitive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments_for_payout_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `get_payments_for_payout_v4`")  # noqa: E501

        if 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_payments_for_payout_v4`, must be a value less than or equal to `100`")  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_payments_for_payout_v4`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []
        if 'rails_id' in local_var_params:
            query_params.append(('railsId', local_var_params['rails_id']))  # noqa: E501
        if 'remote_id' in local_var_params:
            query_params.append(('remoteId', local_var_params['remote_id']))  # noqa: E501
        if 'remote_system_id' in local_var_params:
            query_params.append(('remoteSystemId', local_var_params['remote_system_id']))  # noqa: E501
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'source_amount_from' in local_var_params:
            query_params.append(('sourceAmountFrom', local_var_params['source_amount_from']))  # noqa: E501
        if 'source_amount_to' in local_var_params:
            query_params.append(('sourceAmountTo', local_var_params['source_amount_to']))  # noqa: E501
        if 'payment_amount_from' in local_var_params:
            query_params.append(('paymentAmountFrom', local_var_params['payment_amount_from']))  # noqa: E501
        if 'payment_amount_to' in local_var_params:
            query_params.append(('paymentAmountTo', local_var_params['payment_amount_to']))  # noqa: E501
        if 'submitted_date_from' in local_var_params:
            query_params.append(('submittedDateFrom', local_var_params['submitted_date_from']))  # noqa: E501
        if 'submitted_date_to' in local_var_params:
            query_params.append(('submittedDateTo', local_var_params['submitted_date_to']))  # noqa: E501
        if 'transmission_type' in local_var_params:
            query_params.append(('transmissionType', local_var_params['transmission_type']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'sensitive' in local_var_params:
            query_params.append(('sensitive', local_var_params['sensitive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/payouts/{payoutId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPaymentsForPayoutResponseV4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payout_stats_v4(self, **kwargs):  # noqa: E501
        """Get Payout Statistics  # noqa: E501

        <p>Get payout statistics for a payor.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payout_stats_v4(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The account owner Payor ID. Required for external users.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetPayoutStatistics
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payout_stats_v4_with_http_info(**kwargs)  # noqa: E501

    def get_payout_stats_v4_with_http_info(self, **kwargs):  # noqa: E501
        """Get Payout Statistics  # noqa: E501

        <p>Get payout statistics for a payor.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payout_stats_v4_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The account owner Payor ID. Required for external users.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetPayoutStatistics, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payor_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payout_stats_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/payoutStatistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPayoutStatistics',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payouts_for_payor_v4(self, **kwargs):  # noqa: E501
        """Get Payouts for Payor  # noqa: E501

        Get List of payouts for payor   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payouts_for_payor_v4(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The id (UUID) of the payor funding the payout or the payor whose payees are being paid.
        :param str payout_memo: Payout Memo filter - case insensitive sub-string match
        :param str status: Payout Status
        :param date submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
        :param date submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
        :param str from_payor_name: The name of the payor whose payees are being paid. This filters via a case insensitive substring match.
        :param date scheduled_for_date_from: Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
        :param date scheduled_for_date_to: Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
        :param str schedule_status: Payout Schedule Status
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetPayoutsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payouts_for_payor_v4_with_http_info(**kwargs)  # noqa: E501

    def get_payouts_for_payor_v4_with_http_info(self, **kwargs):  # noqa: E501
        """Get Payouts for Payor  # noqa: E501

        Get List of payouts for payor   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payouts_for_payor_v4_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The id (UUID) of the payor funding the payout or the payor whose payees are being paid.
        :param str payout_memo: Payout Memo filter - case insensitive sub-string match
        :param str status: Payout Status
        :param date submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
        :param date submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
        :param str from_payor_name: The name of the payor whose payees are being paid. This filters via a case insensitive substring match.
        :param date scheduled_for_date_from: Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
        :param date scheduled_for_date_to: Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
        :param str schedule_status: Payout Schedule Status
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId, scheduledFor 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetPayoutsResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payor_id', 'payout_memo', 'status', 'submitted_date_from', 'submitted_date_to', 'from_payor_name', 'scheduled_for_date_from', 'scheduled_for_date_to', 'schedule_status', 'page', 'page_size', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payouts_for_payor_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_payouts_for_payor_v4`, must be a value less than or equal to `100`")  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_payouts_for_payor_v4`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'payout_memo' in local_var_params:
            query_params.append(('payoutMemo', local_var_params['payout_memo']))  # noqa: E501
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'submitted_date_from' in local_var_params:
            query_params.append(('submittedDateFrom', local_var_params['submitted_date_from']))  # noqa: E501
        if 'submitted_date_to' in local_var_params:
            query_params.append(('submittedDateTo', local_var_params['submitted_date_to']))  # noqa: E501
        if 'from_payor_name' in local_var_params:
            query_params.append(('fromPayorName', local_var_params['from_payor_name']))  # noqa: E501
        if 'scheduled_for_date_from' in local_var_params:
            query_params.append(('scheduledForDateFrom', local_var_params['scheduled_for_date_from']))  # noqa: E501
        if 'scheduled_for_date_to' in local_var_params:
            query_params.append(('scheduledForDateTo', local_var_params['scheduled_for_date_to']))  # noqa: E501
        if 'schedule_status' in local_var_params:
            query_params.append(('scheduleStatus', local_var_params['schedule_status']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/payouts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPayoutsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_payment_changes_v4(self, payor_id, updated_since, **kwargs):  # noqa: E501
        """List Payment Changes  # noqa: E501

        Get a paginated response listing payment changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payment_changes_v4(payor_id, updated_since, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The Payor ID to find associated Payments (required)
        :param datetime updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm (required)
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaymentDeltaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_payment_changes_v4_with_http_info(payor_id, updated_since, **kwargs)  # noqa: E501

    def list_payment_changes_v4_with_http_info(self, payor_id, updated_since, **kwargs):  # noqa: E501
        """List Payment Changes  # noqa: E501

        Get a paginated response listing payment changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payment_changes_v4_with_http_info(payor_id, updated_since, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The Payor ID to find associated Payments (required)
        :param datetime updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm (required)
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaymentDeltaResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payor_id', 'updated_since', 'page', 'page_size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_payment_changes_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payor_id' is set
        if ('payor_id' not in local_var_params or
                local_var_params['payor_id'] is None):
            raise ApiValueError("Missing the required parameter `payor_id` when calling `list_payment_changes_v4`")  # noqa: E501
        # verify the required parameter 'updated_since' is set
        if ('updated_since' not in local_var_params or
                local_var_params['updated_since'] is None):
            raise ApiValueError("Missing the required parameter `updated_since` when calling `list_payment_changes_v4`")  # noqa: E501

        if 'page_size' in local_var_params and local_var_params['page_size'] > 1000:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_payment_changes_v4`, must be a value less than or equal to `1000`")  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_payment_changes_v4`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'updated_since' in local_var_params:
            query_params.append(('updatedSince', local_var_params['updated_since']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/payments/deltas', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentDeltaResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_payments_audit_v4(self, **kwargs):  # noqa: E501
        """Get List of Payments  # noqa: E501

        Get payments for the given payor Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payments_audit_v4(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee.
        :param str payor_id: The account owner Payor Id. Required for external users.
        :param str payor_name: The payor’s name. This filters via a case insensitive substring match.
        :param str remote_id: The remote id of the payees.
        :param str remote_system_id: The id of the remote system that is orchestrating payments
        :param str status: Payment Status
        :param str transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
        :param str source_account_name: The source account name filter. This filters via a case insensitive substring match.
        :param int source_amount_from: The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
        :param int source_amount_to: The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
        :param str source_currency: The source currency filter. Filters based on an exact match on the currency.
        :param int payment_amount_from: The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
        :param int payment_amount_to: The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
        :param str payment_currency: The payment currency filter. Filters based on an exact match on the currency.
        :param date submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
        :param date submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
        :param str payment_memo: The payment memo filter. This filters via a case insensitive substring match.
        :param str payor_payment_id: Payor's Id of the Payment
        :param str rails_id: Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the 'Get Supported Rails' endpoint. 
        :param date scheduled_for_date_from: Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
        :param date scheduled_for_date_to: Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
        :param str schedule_status: Payout Schedule Status
        :param str post_instruct_fx_status: The status of the post instruct FX step if one was required for the payment
        :param str transaction_reference: Query for all payments associated with a specific transaction reference
        :param str transaction_id: Query for all payments associated with a specific transaction id
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId 
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ListPaymentsResponseV4
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_payments_audit_v4_with_http_info(**kwargs)  # noqa: E501

    def list_payments_audit_v4_with_http_info(self, **kwargs):  # noqa: E501
        """Get List of Payments  # noqa: E501

        Get payments for the given payor Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payments_audit_v4_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee.
        :param str payor_id: The account owner Payor Id. Required for external users.
        :param str payor_name: The payor’s name. This filters via a case insensitive substring match.
        :param str remote_id: The remote id of the payees.
        :param str remote_system_id: The id of the remote system that is orchestrating payments
        :param str status: Payment Status
        :param str transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE * GACHO 
        :param str source_account_name: The source account name filter. This filters via a case insensitive substring match.
        :param int source_amount_from: The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom
        :param int source_amount_to: The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo
        :param str source_currency: The source currency filter. Filters based on an exact match on the currency.
        :param int payment_amount_from: The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom
        :param int payment_amount_to: The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo
        :param str payment_currency: The payment currency filter. Filters based on an exact match on the currency.
        :param date submitted_date_from: The submitted date from range filter. Format is yyyy-MM-dd.
        :param date submitted_date_to: The submitted date to range filter. Format is yyyy-MM-dd.
        :param str payment_memo: The payment memo filter. This filters via a case insensitive substring match.
        :param str payor_payment_id: Payor's Id of the Payment
        :param str rails_id: Payout Rails ID filter - case insensitive match. Any value is allowed, but you should use one of the supported railsId values. To get this list of values, you should call the 'Get Supported Rails' endpoint. 
        :param date scheduled_for_date_from: Filter payouts scheduled to run on or after the given date. Format is yyyy-MM-dd.
        :param date scheduled_for_date_to: Filter payouts scheduled to run on or before the given date. Format is yyyy-MM-dd.
        :param str schedule_status: Payout Schedule Status
        :param str post_instruct_fx_status: The status of the post instruct FX step if one was required for the payment
        :param str transaction_reference: Query for all payments associated with a specific transaction reference
        :param str transaction_id: Query for all payments associated with a specific transaction id
        :param int page: Page number. Default is 1.
        :param int page_size: The number of results to return in a page
        :param str sort: List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by submittedDateTime:desc,paymentId:asc The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime, status and paymentId 
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ListPaymentsResponseV4, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'payor_id', 'payor_name', 'remote_id', 'remote_system_id', 'status', 'transmission_type', 'source_account_name', 'source_amount_from', 'source_amount_to', 'source_currency', 'payment_amount_from', 'payment_amount_to', 'payment_currency', 'submitted_date_from', 'submitted_date_to', 'payment_memo', 'payor_payment_id', 'rails_id', 'scheduled_for_date_from', 'scheduled_for_date_to', 'schedule_status', 'post_instruct_fx_status', 'transaction_reference', 'transaction_id', 'page', 'page_size', 'sort', 'sensitive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_payments_audit_v4" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        if 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_payments_audit_v4`, must be a value less than or equal to `100`")  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `list_payments_audit_v4`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payee_id' in local_var_params:
            query_params.append(('payeeId', local_var_params['payee_id']))  # noqa: E501
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'payor_name' in local_var_params:
            query_params.append(('payorName', local_var_params['payor_name']))  # noqa: E501
        if 'remote_id' in local_var_params:
            query_params.append(('remoteId', local_var_params['remote_id']))  # noqa: E501
        if 'remote_system_id' in local_var_params:
            query_params.append(('remoteSystemId', local_var_params['remote_system_id']))  # noqa: E501
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'transmission_type' in local_var_params:
            query_params.append(('transmissionType', local_var_params['transmission_type']))  # noqa: E501
        if 'source_account_name' in local_var_params:
            query_params.append(('sourceAccountName', local_var_params['source_account_name']))  # noqa: E501
        if 'source_amount_from' in local_var_params:
            query_params.append(('sourceAmountFrom', local_var_params['source_amount_from']))  # noqa: E501
        if 'source_amount_to' in local_var_params:
            query_params.append(('sourceAmountTo', local_var_params['source_amount_to']))  # noqa: E501
        if 'source_currency' in local_var_params:
            query_params.append(('sourceCurrency', local_var_params['source_currency']))  # noqa: E501
        if 'payment_amount_from' in local_var_params:
            query_params.append(('paymentAmountFrom', local_var_params['payment_amount_from']))  # noqa: E501
        if 'payment_amount_to' in local_var_params:
            query_params.append(('paymentAmountTo', local_var_params['payment_amount_to']))  # noqa: E501
        if 'payment_currency' in local_var_params:
            query_params.append(('paymentCurrency', local_var_params['payment_currency']))  # noqa: E501
        if 'submitted_date_from' in local_var_params:
            query_params.append(('submittedDateFrom', local_var_params['submitted_date_from']))  # noqa: E501
        if 'submitted_date_to' in local_var_params:
            query_params.append(('submittedDateTo', local_var_params['submitted_date_to']))  # noqa: E501
        if 'payment_memo' in local_var_params:
            query_params.append(('paymentMemo', local_var_params['payment_memo']))  # noqa: E501
        if 'payor_payment_id' in local_var_params:
            query_params.append(('payorPaymentId', local_var_params['payor_payment_id']))  # noqa: E501
        if 'rails_id' in local_var_params:
            query_params.append(('railsId', local_var_params['rails_id']))  # noqa: E501
        if 'scheduled_for_date_from' in local_var_params:
            query_params.append(('scheduledForDateFrom', local_var_params['scheduled_for_date_from']))  # noqa: E501
        if 'scheduled_for_date_to' in local_var_params:
            query_params.append(('scheduledForDateTo', local_var_params['scheduled_for_date_to']))  # noqa: E501
        if 'schedule_status' in local_var_params:
            query_params.append(('scheduleStatus', local_var_params['schedule_status']))  # noqa: E501
        if 'post_instruct_fx_status' in local_var_params:
            query_params.append(('postInstructFxStatus', local_var_params['post_instruct_fx_status']))  # noqa: E501
        if 'transaction_reference' in local_var_params:
            query_params.append(('transactionReference', local_var_params['transaction_reference']))  # noqa: E501
        if 'transaction_id' in local_var_params:
            query_params.append(('transactionId', local_var_params['transaction_id']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'sort' in local_var_params:
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'sensitive' in local_var_params:
            query_params.append(('sensitive', local_var_params['sensitive']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v4/paymentaudit/payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ListPaymentsResponseV4',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
