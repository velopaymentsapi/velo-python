# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   ## Http Status Codes Following is a list of Http Status codes that could be returned by the platform      | Status Code            | Description                                                                          |     | -----------------------| -------------------------------------------------------------------------------------|     | 200 OK                 | The request was successfully processed and usually returns a json response           |     | 201 Created            | A resource was created and a Location header is returned linking to the new resource |     | 202 Accepted           | The request has been accepted for processing                                         |     | 204 No Content         | The request has been processed and there is no response (usually deletes and updates)|     | 400 Bad Request        | The request is invalid and should be fixed before retrying                           |     | 401 Unauthorized       | Authentication has failed, usually means the token has expired                       |     | 403 Forbidden          | The user does not have permissions for the request                                   |     | 404 Not Found          | The resource was not found                                                           |     | 409 Conflict           | The resource already exists and there is a conflict                                  |     | 429 Too Many Requests  | The user has submitted too many requests in a given amount of time                   |     | 5xx Server Error       | Platform internal error (should rarely happen)                                       |   # noqa: E501

    The version of the OpenAPI document: 2.37.148
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PayorAmlTransactionV3(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'transaction_date': 'date',
        'transaction_time': 'str',
        'report_transaction_type': 'str',
        'debit': 'int',
        'debit_currency': 'str',
        'credit': 'int',
        'credit_currency': 'str',
        'return_fee': 'str',
        'return_fee_currency': 'str',
        'return_fee_description': 'str',
        'return_code': 'str',
        'return_description': 'str',
        'funding_type': 'str',
        'date_funding_requested': 'str',
        'remote_id': 'str',
        'payee_type': 'str',
        'source_account': 'str',
        'payment_amount': 'int',
        'payment_currency': 'str',
        'payment_memo': 'str',
        'payment_rails': 'str',
        'payor_payment_id': 'str',
        'payment_status': 'str',
        'reject_reason': 'str',
        'fx_applied': 'float'
    }

    attribute_map = {
        'transaction_date': 'transactionDate',
        'transaction_time': 'transactionTime',
        'report_transaction_type': 'reportTransactionType',
        'debit': 'debit',
        'debit_currency': 'debitCurrency',
        'credit': 'credit',
        'credit_currency': 'creditCurrency',
        'return_fee': 'returnFee',
        'return_fee_currency': 'returnFeeCurrency',
        'return_fee_description': 'returnFeeDescription',
        'return_code': 'returnCode',
        'return_description': 'returnDescription',
        'funding_type': 'fundingType',
        'date_funding_requested': 'dateFundingRequested',
        'remote_id': 'remoteId',
        'payee_type': 'payeeType',
        'source_account': 'sourceAccount',
        'payment_amount': 'paymentAmount',
        'payment_currency': 'paymentCurrency',
        'payment_memo': 'paymentMemo',
        'payment_rails': 'paymentRails',
        'payor_payment_id': 'payorPaymentId',
        'payment_status': 'paymentStatus',
        'reject_reason': 'rejectReason',
        'fx_applied': 'fxApplied'
    }

    def __init__(self, transaction_date=None, transaction_time=None, report_transaction_type=None, debit=None, debit_currency=None, credit=None, credit_currency=None, return_fee=None, return_fee_currency=None, return_fee_description=None, return_code=None, return_description=None, funding_type=None, date_funding_requested=None, remote_id=None, payee_type=None, source_account=None, payment_amount=None, payment_currency=None, payment_memo=None, payment_rails=None, payor_payment_id=None, payment_status=None, reject_reason=None, fx_applied=None):  # noqa: E501
        """PayorAmlTransactionV3 - a model defined in OpenAPI"""  # noqa: E501

        self._transaction_date = None
        self._transaction_time = None
        self._report_transaction_type = None
        self._debit = None
        self._debit_currency = None
        self._credit = None
        self._credit_currency = None
        self._return_fee = None
        self._return_fee_currency = None
        self._return_fee_description = None
        self._return_code = None
        self._return_description = None
        self._funding_type = None
        self._date_funding_requested = None
        self._remote_id = None
        self._payee_type = None
        self._source_account = None
        self._payment_amount = None
        self._payment_currency = None
        self._payment_memo = None
        self._payment_rails = None
        self._payor_payment_id = None
        self._payment_status = None
        self._reject_reason = None
        self._fx_applied = None
        self.discriminator = None

        if transaction_date is not None:
            self.transaction_date = transaction_date
        if transaction_time is not None:
            self.transaction_time = transaction_time
        if report_transaction_type is not None:
            self.report_transaction_type = report_transaction_type
        if debit is not None:
            self.debit = debit
        if debit_currency is not None:
            self.debit_currency = debit_currency
        if credit is not None:
            self.credit = credit
        if credit_currency is not None:
            self.credit_currency = credit_currency
        if return_fee is not None:
            self.return_fee = return_fee
        if return_fee_currency is not None:
            self.return_fee_currency = return_fee_currency
        if return_fee_description is not None:
            self.return_fee_description = return_fee_description
        if return_code is not None:
            self.return_code = return_code
        if return_description is not None:
            self.return_description = return_description
        if funding_type is not None:
            self.funding_type = funding_type
        if date_funding_requested is not None:
            self.date_funding_requested = date_funding_requested
        if remote_id is not None:
            self.remote_id = remote_id
        if payee_type is not None:
            self.payee_type = payee_type
        if source_account is not None:
            self.source_account = source_account
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if payment_currency is not None:
            self.payment_currency = payment_currency
        if payment_memo is not None:
            self.payment_memo = payment_memo
        if payment_rails is not None:
            self.payment_rails = payment_rails
        if payor_payment_id is not None:
            self.payor_payment_id = payor_payment_id
        if payment_status is not None:
            self.payment_status = payment_status
        if reject_reason is not None:
            self.reject_reason = reject_reason
        if fx_applied is not None:
            self.fx_applied = fx_applied

    @property
    def transaction_date(self):
        """Gets the transaction_date of this PayorAmlTransactionV3.  # noqa: E501


        :return: The transaction_date of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: date
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this PayorAmlTransactionV3.


        :param transaction_date: The transaction_date of this PayorAmlTransactionV3.  # noqa: E501
        :type: date
        """

        self._transaction_date = transaction_date

    @property
    def transaction_time(self):
        """Gets the transaction_time of this PayorAmlTransactionV3.  # noqa: E501


        :return: The transaction_time of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._transaction_time

    @transaction_time.setter
    def transaction_time(self, transaction_time):
        """Sets the transaction_time of this PayorAmlTransactionV3.


        :param transaction_time: The transaction_time of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._transaction_time = transaction_time

    @property
    def report_transaction_type(self):
        """Gets the report_transaction_type of this PayorAmlTransactionV3.  # noqa: E501


        :return: The report_transaction_type of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._report_transaction_type

    @report_transaction_type.setter
    def report_transaction_type(self, report_transaction_type):
        """Sets the report_transaction_type of this PayorAmlTransactionV3.


        :param report_transaction_type: The report_transaction_type of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._report_transaction_type = report_transaction_type

    @property
    def debit(self):
        """Gets the debit of this PayorAmlTransactionV3.  # noqa: E501


        :return: The debit of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: int
        """
        return self._debit

    @debit.setter
    def debit(self, debit):
        """Sets the debit of this PayorAmlTransactionV3.


        :param debit: The debit of this PayorAmlTransactionV3.  # noqa: E501
        :type: int
        """

        self._debit = debit

    @property
    def debit_currency(self):
        """Gets the debit_currency of this PayorAmlTransactionV3.  # noqa: E501

        ISO 4217 3 character currency code  # noqa: E501

        :return: The debit_currency of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._debit_currency

    @debit_currency.setter
    def debit_currency(self, debit_currency):
        """Sets the debit_currency of this PayorAmlTransactionV3.

        ISO 4217 3 character currency code  # noqa: E501

        :param debit_currency: The debit_currency of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._debit_currency = debit_currency

    @property
    def credit(self):
        """Gets the credit of this PayorAmlTransactionV3.  # noqa: E501


        :return: The credit of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: int
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        """Sets the credit of this PayorAmlTransactionV3.


        :param credit: The credit of this PayorAmlTransactionV3.  # noqa: E501
        :type: int
        """

        self._credit = credit

    @property
    def credit_currency(self):
        """Gets the credit_currency of this PayorAmlTransactionV3.  # noqa: E501

        ISO 4217 3 character currency code  # noqa: E501

        :return: The credit_currency of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._credit_currency

    @credit_currency.setter
    def credit_currency(self, credit_currency):
        """Sets the credit_currency of this PayorAmlTransactionV3.

        ISO 4217 3 character currency code  # noqa: E501

        :param credit_currency: The credit_currency of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._credit_currency = credit_currency

    @property
    def return_fee(self):
        """Gets the return_fee of this PayorAmlTransactionV3.  # noqa: E501


        :return: The return_fee of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._return_fee

    @return_fee.setter
    def return_fee(self, return_fee):
        """Sets the return_fee of this PayorAmlTransactionV3.


        :param return_fee: The return_fee of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._return_fee = return_fee

    @property
    def return_fee_currency(self):
        """Gets the return_fee_currency of this PayorAmlTransactionV3.  # noqa: E501

        ISO 4217 3 character currency code  # noqa: E501

        :return: The return_fee_currency of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._return_fee_currency

    @return_fee_currency.setter
    def return_fee_currency(self, return_fee_currency):
        """Sets the return_fee_currency of this PayorAmlTransactionV3.

        ISO 4217 3 character currency code  # noqa: E501

        :param return_fee_currency: The return_fee_currency of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._return_fee_currency = return_fee_currency

    @property
    def return_fee_description(self):
        """Gets the return_fee_description of this PayorAmlTransactionV3.  # noqa: E501


        :return: The return_fee_description of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._return_fee_description

    @return_fee_description.setter
    def return_fee_description(self, return_fee_description):
        """Sets the return_fee_description of this PayorAmlTransactionV3.


        :param return_fee_description: The return_fee_description of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._return_fee_description = return_fee_description

    @property
    def return_code(self):
        """Gets the return_code of this PayorAmlTransactionV3.  # noqa: E501


        :return: The return_code of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._return_code

    @return_code.setter
    def return_code(self, return_code):
        """Sets the return_code of this PayorAmlTransactionV3.


        :param return_code: The return_code of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._return_code = return_code

    @property
    def return_description(self):
        """Gets the return_description of this PayorAmlTransactionV3.  # noqa: E501


        :return: The return_description of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._return_description

    @return_description.setter
    def return_description(self, return_description):
        """Sets the return_description of this PayorAmlTransactionV3.


        :param return_description: The return_description of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._return_description = return_description

    @property
    def funding_type(self):
        """Gets the funding_type of this PayorAmlTransactionV3.  # noqa: E501


        :return: The funding_type of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._funding_type

    @funding_type.setter
    def funding_type(self, funding_type):
        """Sets the funding_type of this PayorAmlTransactionV3.


        :param funding_type: The funding_type of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._funding_type = funding_type

    @property
    def date_funding_requested(self):
        """Gets the date_funding_requested of this PayorAmlTransactionV3.  # noqa: E501


        :return: The date_funding_requested of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._date_funding_requested

    @date_funding_requested.setter
    def date_funding_requested(self, date_funding_requested):
        """Sets the date_funding_requested of this PayorAmlTransactionV3.


        :param date_funding_requested: The date_funding_requested of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._date_funding_requested = date_funding_requested

    @property
    def remote_id(self):
        """Gets the remote_id of this PayorAmlTransactionV3.  # noqa: E501

        Remote ID of the Payee, set by Payor  # noqa: E501

        :return: The remote_id of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this PayorAmlTransactionV3.

        Remote ID of the Payee, set by Payor  # noqa: E501

        :param remote_id: The remote_id of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def payee_type(self):
        """Gets the payee_type of this PayorAmlTransactionV3.  # noqa: E501


        :return: The payee_type of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._payee_type

    @payee_type.setter
    def payee_type(self, payee_type):
        """Sets the payee_type of this PayorAmlTransactionV3.


        :param payee_type: The payee_type of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._payee_type = payee_type

    @property
    def source_account(self):
        """Gets the source_account of this PayorAmlTransactionV3.  # noqa: E501


        :return: The source_account of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._source_account

    @source_account.setter
    def source_account(self, source_account):
        """Sets the source_account of this PayorAmlTransactionV3.


        :param source_account: The source_account of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._source_account = source_account

    @property
    def payment_amount(self):
        """Gets the payment_amount of this PayorAmlTransactionV3.  # noqa: E501


        :return: The payment_amount of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: int
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this PayorAmlTransactionV3.


        :param payment_amount: The payment_amount of this PayorAmlTransactionV3.  # noqa: E501
        :type: int
        """

        self._payment_amount = payment_amount

    @property
    def payment_currency(self):
        """Gets the payment_currency of this PayorAmlTransactionV3.  # noqa: E501

        ISO 4217 3 character currency code  # noqa: E501

        :return: The payment_currency of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this PayorAmlTransactionV3.

        ISO 4217 3 character currency code  # noqa: E501

        :param payment_currency: The payment_currency of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._payment_currency = payment_currency

    @property
    def payment_memo(self):
        """Gets the payment_memo of this PayorAmlTransactionV3.  # noqa: E501


        :return: The payment_memo of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_memo

    @payment_memo.setter
    def payment_memo(self, payment_memo):
        """Sets the payment_memo of this PayorAmlTransactionV3.


        :param payment_memo: The payment_memo of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._payment_memo = payment_memo

    @property
    def payment_rails(self):
        """Gets the payment_rails of this PayorAmlTransactionV3.  # noqa: E501


        :return: The payment_rails of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_rails

    @payment_rails.setter
    def payment_rails(self, payment_rails):
        """Sets the payment_rails of this PayorAmlTransactionV3.


        :param payment_rails: The payment_rails of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._payment_rails = payment_rails

    @property
    def payor_payment_id(self):
        """Gets the payor_payment_id of this PayorAmlTransactionV3.  # noqa: E501


        :return: The payor_payment_id of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._payor_payment_id

    @payor_payment_id.setter
    def payor_payment_id(self, payor_payment_id):
        """Sets the payor_payment_id of this PayorAmlTransactionV3.


        :param payor_payment_id: The payor_payment_id of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._payor_payment_id = payor_payment_id

    @property
    def payment_status(self):
        """Gets the payment_status of this PayorAmlTransactionV3.  # noqa: E501


        :return: The payment_status of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_status

    @payment_status.setter
    def payment_status(self, payment_status):
        """Sets the payment_status of this PayorAmlTransactionV3.


        :param payment_status: The payment_status of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._payment_status = payment_status

    @property
    def reject_reason(self):
        """Gets the reject_reason of this PayorAmlTransactionV3.  # noqa: E501


        :return: The reject_reason of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: str
        """
        return self._reject_reason

    @reject_reason.setter
    def reject_reason(self, reject_reason):
        """Sets the reject_reason of this PayorAmlTransactionV3.


        :param reject_reason: The reject_reason of this PayorAmlTransactionV3.  # noqa: E501
        :type: str
        """

        self._reject_reason = reject_reason

    @property
    def fx_applied(self):
        """Gets the fx_applied of this PayorAmlTransactionV3.  # noqa: E501


        :return: The fx_applied of this PayorAmlTransactionV3.  # noqa: E501
        :rtype: float
        """
        return self._fx_applied

    @fx_applied.setter
    def fx_applied(self, fx_applied):
        """Sets the fx_applied of this PayorAmlTransactionV3.


        :param fx_applied: The fx_applied of this PayorAmlTransactionV3.  # noqa: E501
        :type: float
        """

        self._fx_applied = fx_applied

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayorAmlTransactionV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
