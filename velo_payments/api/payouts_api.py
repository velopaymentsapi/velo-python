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


class PayoutsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_quote_for_payout_v3(self, payout_id, **kwargs):  # noqa: E501
        """Create a quote for the payout  # noqa: E501

        Create quote for a payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_quote_for_payout_v3(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: QuoteResponseV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_quote_for_payout_v3_with_http_info(payout_id, **kwargs)  # noqa: E501

    def create_quote_for_payout_v3_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Create a quote for the payout  # noqa: E501

        Create quote for a payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_quote_for_payout_v3_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(QuoteResponseV3, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_quote_for_payout_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `create_quote_for_payout_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []

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
            '/v3/payouts/{payoutId}/quote', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='QuoteResponseV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deschedule_payout(self, payout_id, **kwargs):  # noqa: E501
        """Deschedule a payout  # noqa: E501

        Remove the schedule for a scheduled payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deschedule_payout(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.deschedule_payout_with_http_info(payout_id, **kwargs)  # noqa: E501

    def deschedule_payout_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Deschedule a payout  # noqa: E501

        Remove the schedule for a scheduled payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deschedule_payout_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deschedule_payout" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `deschedule_payout`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []

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
            '/v3/payouts/{payoutId}/schedule', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payments_for_payout_v3(self, payout_id, **kwargs):  # noqa: E501
        """Retrieve payments for a payout  # noqa: E501

        Retrieve payments for a payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_for_payout_v3(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param str status: Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal 
        :param str remote_id: The remote id of the payees.
        :param str payor_payment_id: Payor's Id of the Payment
        :param str source_account_name: Physical Account Name
        :param str transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE 
        :param str payment_memo: Payment Memo of the Payment
        :param int page_size: The number of results to return in a page
        :param int page: Page number. Default is 1.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PagedPaymentsResponseV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payments_for_payout_v3_with_http_info(payout_id, **kwargs)  # noqa: E501

    def get_payments_for_payout_v3_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Retrieve payments for a payout  # noqa: E501

        Retrieve payments for a payout  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payments_for_payout_v3_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param str status: Payment Status * ACCEPTED: any payment which was accepted at submission time (status may have changed since) * REJECTED: any payment rejected by initial submission processing * WITHDRAWN: any payment which has been withdrawn * WITHDRAWABLE: any payment eligible for withdrawal 
        :param str remote_id: The remote id of the payees.
        :param str payor_payment_id: Payor's Id of the Payment
        :param str source_account_name: Physical Account Name
        :param str transmission_type: Transmission Type * ACH * SAME_DAY_ACH * WIRE 
        :param str payment_memo: Payment Memo of the Payment
        :param int page_size: The number of results to return in a page
        :param int page: Page number. Default is 1.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PagedPaymentsResponseV3, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id', 'status', 'remote_id', 'payor_payment_id', 'source_account_name', 'transmission_type', 'payment_memo', 'page_size', 'page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payments_for_payout_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `get_payments_for_payout_v3`")  # noqa: E501

        if 'page_size' in local_var_params and local_var_params['page_size'] > 100:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_payments_for_payout_v3`, must be a value less than or equal to `100`")  # noqa: E501
        if 'page_size' in local_var_params and local_var_params['page_size'] < 1:  # noqa: E501
            raise ApiValueError("Invalid value for parameter `page_size` when calling `get_payments_for_payout_v3`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []
        if 'status' in local_var_params:
            query_params.append(('status', local_var_params['status']))  # noqa: E501
        if 'remote_id' in local_var_params:
            query_params.append(('remoteId', local_var_params['remote_id']))  # noqa: E501
        if 'payor_payment_id' in local_var_params:
            query_params.append(('payorPaymentId', local_var_params['payor_payment_id']))  # noqa: E501
        if 'source_account_name' in local_var_params:
            query_params.append(('sourceAccountName', local_var_params['source_account_name']))  # noqa: E501
        if 'transmission_type' in local_var_params:
            query_params.append(('transmissionType', local_var_params['transmission_type']))  # noqa: E501
        if 'payment_memo' in local_var_params:
            query_params.append(('paymentMemo', local_var_params['payment_memo']))  # noqa: E501
        if 'page_size' in local_var_params:
            query_params.append(('pageSize', local_var_params['page_size']))  # noqa: E501
        if 'page' in local_var_params:
            query_params.append(('page', local_var_params['page']))  # noqa: E501

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
            '/v3/payouts/{payoutId}/payments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedPaymentsResponseV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_payout_summary_v3(self, payout_id, **kwargs):  # noqa: E501
        """Get Payout Summary  # noqa: E501

        Get payout summary - returns the current state of the payout.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payout_summary_v3(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PayoutSummaryResponseV3
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payout_summary_v3_with_http_info(payout_id, **kwargs)  # noqa: E501

    def get_payout_summary_v3_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Get Payout Summary  # noqa: E501

        Get payout summary - returns the current state of the payout.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payout_summary_v3_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PayoutSummaryResponseV3, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payout_summary_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `get_payout_summary_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []

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
            '/v3/payouts/{payoutId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayoutSummaryResponseV3',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def instruct_payout_v3(self, payout_id, **kwargs):  # noqa: E501
        """Instruct Payout  # noqa: E501

        Instruct a payout to be made for the specified payoutId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.instruct_payout_v3(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param InstructPayoutRequestV3 instruct_payout_request_v3: Additional instruct payout parameters
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.instruct_payout_v3_with_http_info(payout_id, **kwargs)  # noqa: E501

    def instruct_payout_v3_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Instruct Payout  # noqa: E501

        Instruct a payout to be made for the specified payoutId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.instruct_payout_v3_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param InstructPayoutRequestV3 instruct_payout_request_v3: Additional instruct payout parameters
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id', 'instruct_payout_request_v3']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method instruct_payout_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `instruct_payout_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'instruct_payout_request_v3' in local_var_params:
            body_params = local_var_params['instruct_payout_request_v3']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v3/payouts/{payoutId}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def schedule_for_payout(self, payout_id, **kwargs):  # noqa: E501
        """Schedule a payout  # noqa: E501

        <p>Schedule a payout for auto-instruction in the future or update existing payout schedule if the payout has been scheduled before.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_for_payout(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param SchedulePayoutRequestV3 schedule_payout_request_v3: schedule payout parameters
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.schedule_for_payout_with_http_info(payout_id, **kwargs)  # noqa: E501

    def schedule_for_payout_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Schedule a payout  # noqa: E501

        <p>Schedule a payout for auto-instruction in the future or update existing payout schedule if the payout has been scheduled before.</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schedule_for_payout_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param SchedulePayoutRequestV3 schedule_payout_request_v3: schedule payout parameters
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id', 'schedule_payout_request_v3']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method schedule_for_payout" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `schedule_for_payout`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'schedule_payout_request_v3' in local_var_params:
            body_params = local_var_params['schedule_payout_request_v3']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v3/payouts/{payoutId}/schedule', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_payout_v3(self, create_payout_request_v3, **kwargs):  # noqa: E501
        """Submit Payout  # noqa: E501

        <p>Create a new payout and return a location header with a link to the payout</p> <p>Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously</p> <p>The results can be obtained by issuing a HTTP GET to the URL returned in the location header</p> <p>**NOTE:** amount values in payments must be in 'minor units' format. E.g. cents for USD, pence for GBP etc with no decimal places</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_payout_v3(create_payout_request_v3, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePayoutRequestV3 create_payout_request_v3: Post amount to transfer using stored funding account details. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.submit_payout_v3_with_http_info(create_payout_request_v3, **kwargs)  # noqa: E501

    def submit_payout_v3_with_http_info(self, create_payout_request_v3, **kwargs):  # noqa: E501
        """Submit Payout  # noqa: E501

        <p>Create a new payout and return a location header with a link to the payout</p> <p>Basic validation of the payout is performed before returning but more comprehensive validation is done asynchronously</p> <p>The results can be obtained by issuing a HTTP GET to the URL returned in the location header</p> <p>**NOTE:** amount values in payments must be in 'minor units' format. E.g. cents for USD, pence for GBP etc with no decimal places</p>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_payout_v3_with_http_info(create_payout_request_v3, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePayoutRequestV3 create_payout_request_v3: Post amount to transfer using stored funding account details. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['create_payout_request_v3']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_payout_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'create_payout_request_v3' is set
        if ('create_payout_request_v3' not in local_var_params or
                local_var_params['create_payout_request_v3'] is None):
            raise ApiValueError("Missing the required parameter `create_payout_request_v3` when calling `submit_payout_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'create_payout_request_v3' in local_var_params:
            body_params = local_var_params['create_payout_request_v3']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v3/payouts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def withdraw_payment(self, payment_id, withdraw_payment_request, **kwargs):  # noqa: E501
        """Withdraw a Payment  # noqa: E501

        <p>withdraw a payment </p> <p>There are a variety of reasons why this can fail</p> <ul>     <li>the payment must be in a state of 'accepted' or 'unfunded'</li>     <li>the payout must not be in a state of 'instructed'</li> </ul>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.withdraw_payment(payment_id, withdraw_payment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_id: Id of the Payment (required)
        :param WithdrawPaymentRequest withdraw_payment_request: details for withdrawal (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.withdraw_payment_with_http_info(payment_id, withdraw_payment_request, **kwargs)  # noqa: E501

    def withdraw_payment_with_http_info(self, payment_id, withdraw_payment_request, **kwargs):  # noqa: E501
        """Withdraw a Payment  # noqa: E501

        <p>withdraw a payment </p> <p>There are a variety of reasons why this can fail</p> <ul>     <li>the payment must be in a state of 'accepted' or 'unfunded'</li>     <li>the payout must not be in a state of 'instructed'</li> </ul>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.withdraw_payment_with_http_info(payment_id, withdraw_payment_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payment_id: Id of the Payment (required)
        :param WithdrawPaymentRequest withdraw_payment_request: details for withdrawal (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payment_id', 'withdraw_payment_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method withdraw_payment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in local_var_params or
                local_var_params['payment_id'] is None):
            raise ApiValueError("Missing the required parameter `payment_id` when calling `withdraw_payment`")  # noqa: E501
        # verify the required parameter 'withdraw_payment_request' is set
        if ('withdraw_payment_request' not in local_var_params or
                local_var_params['withdraw_payment_request'] is None):
            raise ApiValueError("Missing the required parameter `withdraw_payment_request` when calling `withdraw_payment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payment_id' in local_var_params:
            path_params['paymentId'] = local_var_params['payment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'withdraw_payment_request' in local_var_params:
            body_params = local_var_params['withdraw_payment_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/payments/{paymentId}/withdraw', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def withdraw_payout_v3(self, payout_id, **kwargs):  # noqa: E501
        """Withdraw Payout  # noqa: E501

        Withdraw Payout will remove the payout details from the rails but the payout will still be accessible in payout service in WITHDRAWN status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.withdraw_payout_v3(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.withdraw_payout_v3_with_http_info(payout_id, **kwargs)  # noqa: E501

    def withdraw_payout_v3_with_http_info(self, payout_id, **kwargs):  # noqa: E501
        """Withdraw Payout  # noqa: E501

        Withdraw Payout will remove the payout details from the rails but the payout will still be accessible in payout service in WITHDRAWN status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.withdraw_payout_v3_with_http_info(payout_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payout_id: Id of the payout (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payout_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method withdraw_payout_v3" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payout_id' is set
        if ('payout_id' not in local_var_params or
                local_var_params['payout_id'] is None):
            raise ApiValueError("Missing the required parameter `payout_id` when calling `withdraw_payout_v3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payout_id' in local_var_params:
            path_params['payoutId'] = local_var_params['payout_id']  # noqa: E501

        query_params = []

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
            '/v3/payouts/{payoutId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
