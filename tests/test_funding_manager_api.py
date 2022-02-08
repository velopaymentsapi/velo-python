# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.22.122
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import os
import unittest

import velo_payments
from velo_payments.api.login_api import LoginApi
from velo_payments.api.funding_manager_api import FundingManagerApi  # noqa: E501
from velo_payments.rest import ApiException


class TestFundingManagerApi(unittest.TestCase):
    """FundingManagerApi unit test stubs"""

    def setUp(self):
        self.api = velo_payments.api.funding_manager_api.FundingManagerApi()  # noqa: E501

        if os.environ.get('APITOKEN') == "":
            configuration = velo_payments.Configuration()
            # Configure HTTP basic authorization: basicAuth
            configuration.username = os.environ.get('KEY')
            configuration.password = os.environ.get('SECRET')

            # Defining host is optional and default to https://api.sandbox.velopayments.com
            configuration.host = os.environ.get('APIURL')
            # Create an instance of the API class
            api_instance = LoginApi(velo_payments.ApiClient(configuration))
            grant_type = 'client_credentials' # str | OAuth grant type. Should use 'client_credentials' (optional) (default to 'client_credentials')

            try:
                # Authentication endpoint
                api_response = api_instance.velo_auth(grant_type=grant_type)
                os.environ["APITOKEN"] = api_response.access_token
                
            except ApiException as e:
                print("Exception when calling LoginApi->velo_auth: %s\n" % e)

    def tearDown(self):
        pass

    def test_create_ach_funding_request(self):
        """Test case for create_ach_funding_request

        Create Funding Request  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_create_funding_request(self):
        """Test case for create_funding_request

        Create Funding Request  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_create_funding_request_v3(self):
        """Test case for create_funding_request_v3

        Create Funding Request  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_funding_account(self):
        """Test case for get_funding_account

        Get Funding Account  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_funding_account_v2(self):
        """Test case for get_funding_account_v2

        Get Funding Account  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_funding_accounts(self):
        """Test case for get_funding_accounts

        Get Funding Accounts  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = FundingManagerApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str |  (optional)
        source_account_id = '' # str |  (optional)
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'accountName:asc' # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name and currency. (optional) (default to 'accountName:asc')
        sensitive = False # bool |  (optional) (default to False)

        api_response = api_instance.get_funding_accounts(payor_id=payor_id, source_account_id=source_account_id, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

    def test_get_funding_accounts_v2(self):
        """Test case for get_funding_accounts_v2

        Get Funding Accounts  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = FundingManagerApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str |  (optional)
        name = '' # str | The descriptive funding account name (optional)
        country = 'US' # str | The 2 letter ISO 3166-1 country code (upper case) (optional)
        currency = 'USD' # str | The ISO 4217 currency code (optional)
        type = 'FBO' # FundingAccountType | The type of funding account. (optional)
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'accountName:asc' # str | List of sort fields (e.g. ?sort=accountName:asc,name:asc) Default is accountName:asc The supported sort fields are - accountName, name. (optional) (default to 'accountName:asc')
        sensitive = False # bool |  (optional) (default to False)

        api_response = api_instance.get_funding_accounts_v2(payor_id=payor_id, name=name, country=country, currency=currency, type=type, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

    def test_get_source_account(self):
        """Test case for get_source_account

        Get details about given source account.  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_source_account_v2(self):
        """Test case for get_source_account_v2

        Get details about given source account.  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_source_account_v3(self):
        """Test case for get_source_account_v3

        Get details about given source account.  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_source_accounts(self):
        """Test case for get_source_accounts

        Get list of source accounts  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = FundingManagerApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str |  (optional)
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef  (optional) (default to 'fundingRef:asc')

        api_response = api_instance.get_source_accounts(payor_id=payor_id, page=page, page_size=page_size, sort=sort)

    def test_get_source_accounts_v2(self):
        """Test case for get_source_accounts_v2

        Get list of source accounts  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = FundingManagerApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str | The account owner Payor ID (optional)
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) (default to 'fundingRef:asc')

        api_response = api_instance.get_source_accounts_v2(payor_id=payor_id, page=page, page_size=page_size, sort=sort)

    def test_get_source_accounts_v3(self):
        """Test case for get_source_accounts_v3

        Get list of source accounts  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = FundingManagerApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str | The account owner Payor ID (optional)
        type = "FBO" # velo_payments.SourceAccountType() # SourceAccountType | The type of source account. (optional)
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'fundingRef:asc' # str | List of sort fields e.g. ?sort=name:asc Default is name:asc The supported sort fields are - fundingRef, name, balance  (optional) (default to 'fundingRef:asc')

        api_response = api_instance.get_source_accounts_v3(payor_id=payor_id, type=type, page=page, page_size=page_size, sort=sort)

    def test_list_funding_audit_deltas(self):
        """Test case for list_funding_audit_deltas

        Get Funding Audit Delta  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = FundingManagerApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str | 
        updated_since = '2013-10-20T19:20:30+01:00' # datetime | 
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)

        api_response = api_instance.list_funding_audit_deltas(payor_id, updated_since, page=page, page_size=page_size)

    def test_set_notifications_request(self):
        """Test case for set_notifications_request

        Set notifications  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_transfer_funds(self):
        """Test case for transfer_funds

        Transfer Funds between source accounts  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_transfer_funds_v3(self):
        """Test case for transfer_funds_v3

        Transfer Funds between source accounts  # noqa: E501
        """
        self.skipTest("skipping test")


if __name__ == '__main__':
    unittest.main()
