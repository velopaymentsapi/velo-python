# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.15.95
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


class PayeesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_payee_by_id(self, payee_id, **kwargs):  # noqa: E501
        """Delete Payee by Id  # noqa: E501

        This API will delete Payee by Id (UUID). Deletion by ID is not allowed if: * Payee ID is not found * If Payee has not been on-boarded * If Payee is in grace period * If Payee has existing payments   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_payee_by_id(payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
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
        return self.delete_payee_by_id_with_http_info(payee_id, **kwargs)  # noqa: E501

    def delete_payee_by_id_with_http_info(self, payee_id, **kwargs):  # noqa: E501
        """Delete Payee by Id  # noqa: E501

        This API will delete Payee by Id (UUID). Deletion by ID is not allowed if: * Payee ID is not found * If Payee has not been on-boarded * If Payee is in grace period * If Payee has existing payments   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_payee_by_id_with_http_info(payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
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

        all_params = ['payee_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_payee_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `delete_payee_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/v1/payees/{payeeId}', 'DELETE',
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

    def get_payee_by_id(self, payee_id, **kwargs):  # noqa: E501
        """Get Payee by Id  # noqa: E501

        Get Payee by Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_by_id(payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
        :param bool sensitive: Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Payee
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_payee_by_id_with_http_info(payee_id, **kwargs)  # noqa: E501

    def get_payee_by_id_with_http_info(self, payee_id, **kwargs):  # noqa: E501
        """Get Payee by Id  # noqa: E501

        Get Payee by Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_payee_by_id_with_http_info(payee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payee_id: The UUID of the payee. (required)
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
        :return: tuple(Payee, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payee_id', 'sensitive']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_payee_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payee_id' is set
        if ('payee_id' not in local_var_params or
                local_var_params['payee_id'] is None):
            raise ApiValueError("Missing the required parameter `payee_id` when calling `get_payee_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'payee_id' in local_var_params:
            path_params['payeeId'] = local_var_params['payee_id']  # noqa: E501

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
            '/v1/payees/{payeeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Payee',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_payee_changes(self, payor_id, updated_since, **kwargs):  # noqa: E501
        """List Payee Changes  # noqa: E501

        Get a paginated response listing payee changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payee_changes(payor_id, updated_since, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The Payor ID to find associated Payees (required)
        :param datetime updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm (required)
        :param int page: Page number. Default is 1.
        :param int page_size: Page size. Default is 100. Max allowable is 1000.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PayeeDeltaResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_payee_changes_with_http_info(payor_id, updated_since, **kwargs)  # noqa: E501

    def list_payee_changes_with_http_info(self, payor_id, updated_since, **kwargs):  # noqa: E501
        """List Payee Changes  # noqa: E501

        Get a paginated response listing payee changes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payee_changes_with_http_info(payor_id, updated_since, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The Payor ID to find associated Payees (required)
        :param datetime updated_since: The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm (required)
        :param int page: Page number. Default is 1.
        :param int page_size: Page size. Default is 100. Max allowable is 1000.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PayeeDeltaResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method list_payee_changes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payor_id' is set
        if ('payor_id' not in local_var_params or
                local_var_params['payor_id'] is None):
            raise ApiValueError("Missing the required parameter `payor_id` when calling `list_payee_changes`")  # noqa: E501
        # verify the required parameter 'updated_since' is set
        if ('updated_since' not in local_var_params or
                local_var_params['updated_since'] is None):
            raise ApiValueError("Missing the required parameter `updated_since` when calling `list_payee_changes`")  # noqa: E501

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
            '/v1/deltas/payees', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeeDeltaResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_payees(self, payor_id, **kwargs):  # noqa: E501
        """List Payees  # noqa: E501

        Get a paginated response listing the payees for a payor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payees(payor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The account owner Payor ID (required)
        :param OfacStatus ofac_status: The ofacStatus of the payees.
        :param OnboardedStatus onboarded_status: The onboarded status of the payees.
        :param str email: Email address
        :param str display_name: The display name of the payees.
        :param str remote_id: The remote id of the payees.
        :param PayeeType payee_type: The onboarded status of the payees.
        :param str payee_country: The country of the payees.
        :param int page: Page number. Default is 1.
        :param int page_size: Page size. Default is 25. Max allowable is 100.
        :param str sort: List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus. 
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PayeeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_payees_with_http_info(payor_id, **kwargs)  # noqa: E501

    def list_payees_with_http_info(self, payor_id, **kwargs):  # noqa: E501
        """List Payees  # noqa: E501

        Get a paginated response listing the payees for a payor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_payees_with_http_info(payor_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str payor_id: The account owner Payor ID (required)
        :param OfacStatus ofac_status: The ofacStatus of the payees.
        :param OnboardedStatus onboarded_status: The onboarded status of the payees.
        :param str email: Email address
        :param str display_name: The display name of the payees.
        :param str remote_id: The remote id of the payees.
        :param PayeeType payee_type: The onboarded status of the payees.
        :param str payee_country: The country of the payees.
        :param int page: Page number. Default is 1.
        :param int page_size: Page size. Default is 25. Max allowable is 100.
        :param str sort: List of sort fields (e.g. ?sort=onboardedStatus:asc,name:asc) Default is name:asc 'name' is treated as company name for companies - last name + ',' + firstName for individuals The supported sort fields are - payeeId, displayName, payoutStatus, onboardedStatus. 
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PayeeResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['payor_id', 'ofac_status', 'onboarded_status', 'email', 'display_name', 'remote_id', 'payee_type', 'payee_country', 'page', 'page_size', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_payees" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'payor_id' is set
        if ('payor_id' not in local_var_params or
                local_var_params['payor_id'] is None):
            raise ApiValueError("Missing the required parameter `payor_id` when calling `list_payees`")  # noqa: E501

        if 'sort' in local_var_params and not re.search(r'[a-zA-Z]+[:desc|:asc]', local_var_params['sort']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `sort` when calling `list_payees`, must conform to the pattern `/[a-zA-Z]+[:desc|:asc]/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'payor_id' in local_var_params:
            query_params.append(('payorId', local_var_params['payor_id']))  # noqa: E501
        if 'ofac_status' in local_var_params:
            query_params.append(('ofacStatus', local_var_params['ofac_status']))  # noqa: E501
        if 'onboarded_status' in local_var_params:
            query_params.append(('onboardedStatus', local_var_params['onboarded_status']))  # noqa: E501
        if 'email' in local_var_params:
            query_params.append(('Email', local_var_params['email']))  # noqa: E501
        if 'display_name' in local_var_params:
            query_params.append(('displayName', local_var_params['display_name']))  # noqa: E501
        if 'remote_id' in local_var_params:
            query_params.append(('remoteId', local_var_params['remote_id']))  # noqa: E501
        if 'payee_type' in local_var_params:
            query_params.append(('payeeType', local_var_params['payee_type']))  # noqa: E501
        if 'payee_country' in local_var_params:
            query_params.append(('payeeCountry', local_var_params['payee_country']))  # noqa: E501
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
            '/v1/payees', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PayeeResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
