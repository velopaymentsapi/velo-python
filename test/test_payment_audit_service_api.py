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
from velo_payments.api.payment_audit_service_api import PaymentAuditServiceApi  # noqa: E501
from velo_payments.rest import ApiException


class TestPaymentAuditServiceApi(unittest.TestCase):
    """PaymentAuditServiceApi unit test stubs"""

    def setUp(self):
        self.api = velo_payments.api.payment_audit_service_api.PaymentAuditServiceApi()  # noqa: E501

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

    def test_export_transactions_csvv3(self):
        """Test case for export_transactions_csvv3

        Export Transactions  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_export_transactions_csvv4(self):
        """Test case for export_transactions_csvv4

        Export Transactions  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_fundings_v4(self):
        """Test case for get_fundings_v4

        Get Fundings for Payor  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str | 
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'dateTime:desc' # str | List of sort fields. Example: ```?sort=destinationCurrency:asc,destinationAmount:asc``` Default is no sort. The supported sort fields are: dateTime and amount.  (optional)

        api_response = api_instance.get_fundings_v4(payor_id, page=page, page_size=page_size, sort=sort)

    def test_get_payment_details(self):
        """Test case for get_payment_details

        Get Payment  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_payment_details_v4(self):
        """Test case for get_payment_details_v4

        Get Payment  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_payments_for_payout(self):
        """Test case for get_payments_for_payout

        Get Payments for Payout  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_payments_for_payout_v4(self):
        """Test case for get_payments_for_payout_v4

        Get Payments for Payout  # noqa: E501
        """
        self.skipTest("skipping test")

    def test_get_payout_stats_v4(self):
        """Test case for get_payout_stats_v4

        Get Payout Statistics  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str | 

        api_response = api_instance.get_payout_stats_v4(payor_id=payor_id)

    def test_get_payouts_for_payor_v4(self):
        """Test case for get_payouts_for_payor_v4

        Get Payouts for Payor  # noqa: E501
        """
        configuration = velo_payments.Configuration()
        configuration.access_token = os.environ["APITOKEN"]
        configuration.host = os.environ.get('APIURL')
        api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))

        payor_id = os.environ["PAYOR"] # str | 
        page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        sort = 'submittedDateTime:desc' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,instructedDateTime:asc,status:asc) Default is submittedDateTime:asc The supported sort fields are: submittedDateTime, instructedDateTime, status, totalPayments, payoutId  (optional)

        api_response = api_instance.get_payouts_for_payor_v4(payor_id=payor_id, page=page, page_size=page_size, sort=sort)

    def test_list_payment_changes_v4(self):
        """Test case for list_payment_changes_v4

        List Payment Changes  # noqa: E501
        """
        self.skipTest("skipping broken test")
        # configuration = velo_payments.Configuration()
        # configuration.access_token = os.environ["APITOKEN"]
        # configuration.host = os.environ.get('APIURL')
        # api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))

        # payor_id = os.environ["PAYOR"] # str | 
        # updated_since = '2013-10-20T19:20:30+01:00' # datetime | The updatedSince filter in the format YYYY-MM-DDThh:mm:ss+hh:mm
        # page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        # page_size = 100 # int | The number of results to return in a page (optional) (default to 100)

        # api_response = api_instance.list_payment_changes_v4(payor_id, updated_since, page=page, page_size=page_size)

    def test_list_payments_audit(self):
        """Test case for list_payments_audit

        Get List of Payments  # noqa: E501
        """
        self.skipTest("skipping broken test")
        # configuration = velo_payments.Configuration()
        # configuration.access_token = os.environ["APITOKEN"]
        # configuration.host = os.environ.get('APIURL')
        # api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))

        # payee_id = None # str | The UUID of the payee. (optional)
        # payor_id = os.environ["PAYOR"] # str | 
        # payor_name = None # str | The payor’s name. This filters via a case insensitive substring match. (optional)
        # remote_id = None # str | The remote id of the payees. (optional)
        # status = None # str | Payment Status (optional)
        # source_account_name = None # str | The source account name filter. This filters via a case insensitive substring match. (optional)
        # source_amount_from = None # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
        # source_amount_to = None # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
        # source_currency = None # str | The source currency filter. Filters based on an exact match on the currency. (optional)
        # payment_amount_from = None # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
        # payment_amount_to = None # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
        # payment_currency = None # str | The payment currency filter. Filters based on an exact match on the currency. (optional)
        # submitted_date_from = None # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
        # submitted_date_to = None # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
        # payment_memo = None # str | The payment memo filter. This filters via a case insensitive substring match. (optional)
        # page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        # page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        # sort = 'submittedDateTime:desc' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
        # sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

        # api_response = api_instance.list_payments_audit(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)

    def test_list_payments_audit_v4(self):
        """Test case for list_payments_audit_v4

        Get List of Payments  # noqa: E501
        """
        self.skipTest("skipping broken test")
        # configuration = velo_payments.Configuration()
        # configuration.access_token = os.environ["APITOKEN"]
        # configuration.host = os.environ.get('APIURL')
        # api_instance = velo_payments.PaymentAuditServiceApi(velo_payments.ApiClient(configuration))

        # payee_id = None # str | The UUID of the payee. (optional)
        # payor_id = os.environ["PAYOR"] # str | 
        # payor_name = None # str | The payor’s name. This filters via a case insensitive substring match. (optional)
        # remote_id = None # str | The remote id of the payees. (optional)
        # status = None # str | Payment Status (optional)
        # source_account_name = None # str | The source account name filter. This filters via a case insensitive substring match. (optional)
        # source_amount_from = None # int | The source amount from range filter. Filters for sourceAmount >= sourceAmountFrom (optional)
        # source_amount_to = None # int | The source amount to range filter. Filters for sourceAmount ⇐ sourceAmountTo (optional)
        # source_currency = None # str | The source currency filter. Filters based on an exact match on the currency. (optional)
        # payment_amount_from = None # int | The payment amount from range filter. Filters for paymentAmount >= paymentAmountFrom (optional)
        # payment_amount_to = None # int | The payment amount to range filter. Filters for paymentAmount ⇐ paymentAmountTo (optional)
        # payment_currency = None # str | The payment currency filter. Filters based on an exact match on the currency. (optional)
        # submitted_date_from = None # date | The submitted date from range filter. Format is yyyy-MM-dd. (optional)
        # submitted_date_to = None # date | The submitted date to range filter. Format is yyyy-MM-dd. (optional)
        # payment_memo = None # str | The payment memo filter. This filters via a case insensitive substring match. (optional)
        # page = 1 # int | Page number. Default is 1. (optional) (default to 1)
        # page_size = 25 # int | The number of results to return in a page (optional) (default to 25)
        # sort = 'submittedDateTime:desc' # str | List of sort fields (e.g. ?sort=submittedDateTime:asc,status:asc). Default is sort by remoteId The supported sort fields are: sourceAmount, sourceCurrency, paymentAmount, paymentCurrency, routingNumber, accountNumber, remoteId, submittedDateTime and status  (optional)
        # sensitive = True # bool | Optional. If omitted or set to false, any Personal Identifiable Information (PII) values are returned masked. If set to true, and you have permission, the PII values will be returned as their original unmasked values.  (optional)

        # api_response = api_instance.list_payments_audit_v4(payee_id=payee_id, payor_id=payor_id, payor_name=payor_name, remote_id=remote_id, status=status, source_account_name=source_account_name, source_amount_from=source_amount_from, source_amount_to=source_amount_to, source_currency=source_currency, payment_amount_from=payment_amount_from, payment_amount_to=payment_amount_to, payment_currency=payment_currency, submitted_date_from=submitted_date_from, submitted_date_to=submitted_date_to, payment_memo=payment_memo, page=page, page_size=page_size, sort=sort, sensitive=sensitive)


if __name__ == '__main__':
    unittest.main()
