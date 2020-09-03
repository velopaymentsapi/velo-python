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
from velo_payments.api.users_api import UsersApi  # noqa: E501
from velo_payments.rest import ApiException


class TestUsersApi(unittest.TestCase):
    """UsersApi unit test stubs"""

    def setUp(self):
        self.api = velo_payments.api.users_api.UsersApi()  # noqa: E501

        if os.environ.get('APITOKEN') == "":
            configuration = velo_payments.Configuration()
            # Configure HTTP basic authorization: basicAuth
            configuration.username = os.environ.get('KEY')
            configuration.password = os.environ.get('SECRET')

            # Defining host is optional and default to https://api.sandbox.velopayments.com
            configuration.host = os.environ.get('APIURL')
            # Create an instance of the API class
            api_instance = velo_payments.LoginApi(velo_payments.ApiClient(configuration))
            grant_type = 'client_credentials' # str | OAuth grant type. Should use 'client_credentials' (optional) (default to 'client_credentials')

            try:
                # Authentication endpoint
                api_response = api_instance.velo_auth(grant_type=grant_type)
                os.environ["APITOKEN"] = api_response.access_token
                
            except ApiException as e:
                print("Exception when calling LoginApi->velo_auth: %s\n" % e)

    def tearDown(self):
        pass

    def test_delete_user_by_id_v2(self):
        """Test case for delete_user_by_id_v2

        Delete a User  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_disable_user_v2(self):
        """Test case for disable_user_v2

        Disable a User  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_enable_user_v2(self):
        """Test case for enable_user_v2

        Enable a User  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_self(self):
        """Test case for get_self

        Get Self  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_user_by_id_v2(self):
        """Test case for get_user_by_id_v2

        Get User  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_invite_user(self):
        """Test case for invite_user

        Invite a User  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_list_users(self):
        """Test case for list_users

        List Users  # noqa: E501
        """
        self.skipTest("skipping broken test")
        # configuration = velo_payments.Configuration()
        # configuration.access_token = os.environ["APITOKEN"]
        # configuration.host = os.environ.get('APIURL')
        # api_instance = velo_payments.UsersApi(velo_payments.ApiClient(configuration))

        # type = None # velo_payments.UserType() # UserType | The Type of the User. (optional)
        # status = None # velo_payments.UserStatus() # UserStatus | The status of the User. (optional)
        # entity_id = os.environ["PAYOR"] # str | The entityId of the User. (optional)
        # page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        # page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        # sort = 'email:asc' # str | List of sort fields (e.g. ?sort=email:asc,lastName:asc) Default is email:asc 'name' The supported sort fields are - email, lastNmae.  (optional) (default to 'email:asc')

        # api_response = api_instance.list_users(type=type, status=status, entity_id=entity_id, page=page, page_size=page_size, sort=sort)

    def test_register_sms(self):
        """Test case for register_sms

        Register SMS Number  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_resend_token(self):
        """Test case for resend_token

        Resend a token  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_role_update(self):
        """Test case for role_update

        Update User Role  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_unlock_user_v2(self):
        """Test case for unlock_user_v2

        Unlock a User  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_unregister_mfa(self):
        """Test case for unregister_mfa

        Unregister MFA for the user  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_unregister_mfa_for_self(self):
        """Test case for unregister_mfa_for_self

        Unregister MFA for Self  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_update_password_self(self):
        """Test case for update_password_self

        Update Password for self  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_user_details_update(self):
        """Test case for user_details_update

        Update User Details  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_user_details_update_for_self(self):
        """Test case for user_details_update_for_self

        Update User Details for self  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_validate_password_self(self):
        """Test case for validate_password_self

        Validate the proposed password  # noqa: E501
        """
        self.skipTest("skipping test")


if __name__ == '__main__':
    unittest.main()
