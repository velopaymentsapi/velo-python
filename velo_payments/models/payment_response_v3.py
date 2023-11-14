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


class PaymentResponseV3(object):
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
        'payment_id': 'str',
        'payee_id': 'str',
        'payor_id': 'str',
        'payor_name': 'str',
        'quote_id': 'str',
        'source_account_id': 'str',
        'source_account_name': 'str',
        'remote_id': 'str',
        'source_amount': 'int',
        'source_currency': 'str',
        'payment_amount': 'int',
        'payment_currency': 'str',
        'rate': 'float',
        'inverted_rate': 'float',
        'submitted_date_time': 'datetime',
        'status': 'str',
        'funding_status': 'str',
        'routing_number': 'str',
        'account_number': 'str',
        'iban': 'str',
        'payment_memo': 'str',
        'filename_reference': 'str',
        'individual_identification_number': 'str',
        'trace_number': 'str',
        'payor_payment_id': 'str',
        'payment_channel_id': 'str',
        'payment_channel_name': 'str',
        'account_name': 'str',
        'rails_id': 'str',
        'country_code': 'str',
        'events': 'list[PaymentEventResponseV3]',
        'return_cost': 'int',
        'return_reason': 'str',
        'rails_payment_id': 'str',
        'rails_batch_id': 'str',
        'payment_scheme': 'str',
        'rejection_reason': 'str'
    }

    attribute_map = {
        'payment_id': 'paymentId',
        'payee_id': 'payeeId',
        'payor_id': 'payorId',
        'payor_name': 'payorName',
        'quote_id': 'quoteId',
        'source_account_id': 'sourceAccountId',
        'source_account_name': 'sourceAccountName',
        'remote_id': 'remoteId',
        'source_amount': 'sourceAmount',
        'source_currency': 'sourceCurrency',
        'payment_amount': 'paymentAmount',
        'payment_currency': 'paymentCurrency',
        'rate': 'rate',
        'inverted_rate': 'invertedRate',
        'submitted_date_time': 'submittedDateTime',
        'status': 'status',
        'funding_status': 'fundingStatus',
        'routing_number': 'routingNumber',
        'account_number': 'accountNumber',
        'iban': 'iban',
        'payment_memo': 'paymentMemo',
        'filename_reference': 'filenameReference',
        'individual_identification_number': 'individualIdentificationNumber',
        'trace_number': 'traceNumber',
        'payor_payment_id': 'payorPaymentId',
        'payment_channel_id': 'paymentChannelId',
        'payment_channel_name': 'paymentChannelName',
        'account_name': 'accountName',
        'rails_id': 'railsId',
        'country_code': 'countryCode',
        'events': 'events',
        'return_cost': 'returnCost',
        'return_reason': 'returnReason',
        'rails_payment_id': 'railsPaymentId',
        'rails_batch_id': 'railsBatchId',
        'payment_scheme': 'paymentScheme',
        'rejection_reason': 'rejectionReason'
    }

    def __init__(self, payment_id=None, payee_id=None, payor_id=None, payor_name=None, quote_id=None, source_account_id=None, source_account_name=None, remote_id=None, source_amount=None, source_currency=None, payment_amount=None, payment_currency=None, rate=None, inverted_rate=None, submitted_date_time=None, status=None, funding_status=None, routing_number=None, account_number=None, iban=None, payment_memo=None, filename_reference=None, individual_identification_number=None, trace_number=None, payor_payment_id=None, payment_channel_id=None, payment_channel_name=None, account_name=None, rails_id='RAILS ID UNAVAILABLE', country_code=None, events=None, return_cost=None, return_reason=None, rails_payment_id=None, rails_batch_id=None, payment_scheme=None, rejection_reason=None):  # noqa: E501
        """PaymentResponseV3 - a model defined in OpenAPI"""  # noqa: E501

        self._payment_id = None
        self._payee_id = None
        self._payor_id = None
        self._payor_name = None
        self._quote_id = None
        self._source_account_id = None
        self._source_account_name = None
        self._remote_id = None
        self._source_amount = None
        self._source_currency = None
        self._payment_amount = None
        self._payment_currency = None
        self._rate = None
        self._inverted_rate = None
        self._submitted_date_time = None
        self._status = None
        self._funding_status = None
        self._routing_number = None
        self._account_number = None
        self._iban = None
        self._payment_memo = None
        self._filename_reference = None
        self._individual_identification_number = None
        self._trace_number = None
        self._payor_payment_id = None
        self._payment_channel_id = None
        self._payment_channel_name = None
        self._account_name = None
        self._rails_id = None
        self._country_code = None
        self._events = None
        self._return_cost = None
        self._return_reason = None
        self._rails_payment_id = None
        self._rails_batch_id = None
        self._payment_scheme = None
        self._rejection_reason = None
        self.discriminator = None

        self.payment_id = payment_id
        self.payee_id = payee_id
        self.payor_id = payor_id
        if payor_name is not None:
            self.payor_name = payor_name
        self.quote_id = quote_id
        self.source_account_id = source_account_id
        if source_account_name is not None:
            self.source_account_name = source_account_name
        if remote_id is not None:
            self.remote_id = remote_id
        if source_amount is not None:
            self.source_amount = source_amount
        if source_currency is not None:
            self.source_currency = source_currency
        self.payment_amount = payment_amount
        if payment_currency is not None:
            self.payment_currency = payment_currency
        if rate is not None:
            self.rate = rate
        if inverted_rate is not None:
            self.inverted_rate = inverted_rate
        self.submitted_date_time = submitted_date_time
        self.status = status
        self.funding_status = funding_status
        if routing_number is not None:
            self.routing_number = routing_number
        if account_number is not None:
            self.account_number = account_number
        if iban is not None:
            self.iban = iban
        if payment_memo is not None:
            self.payment_memo = payment_memo
        if filename_reference is not None:
            self.filename_reference = filename_reference
        if individual_identification_number is not None:
            self.individual_identification_number = individual_identification_number
        if trace_number is not None:
            self.trace_number = trace_number
        if payor_payment_id is not None:
            self.payor_payment_id = payor_payment_id
        if payment_channel_id is not None:
            self.payment_channel_id = payment_channel_id
        if payment_channel_name is not None:
            self.payment_channel_name = payment_channel_name
        if account_name is not None:
            self.account_name = account_name
        self.rails_id = rails_id
        if country_code is not None:
            self.country_code = country_code
        self.events = events
        if return_cost is not None:
            self.return_cost = return_cost
        if return_reason is not None:
            self.return_reason = return_reason
        if rails_payment_id is not None:
            self.rails_payment_id = rails_payment_id
        if rails_batch_id is not None:
            self.rails_batch_id = rails_batch_id
        if payment_scheme is not None:
            self.payment_scheme = payment_scheme
        if rejection_reason is not None:
            self.rejection_reason = rejection_reason

    @property
    def payment_id(self):
        """Gets the payment_id of this PaymentResponseV3.  # noqa: E501

        The id of the payment  # noqa: E501

        :return: The payment_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this PaymentResponseV3.

        The id of the payment  # noqa: E501

        :param payment_id: The payment_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if payment_id is None:
            raise ValueError("Invalid value for `payment_id`, must not be `None`")  # noqa: E501

        self._payment_id = payment_id

    @property
    def payee_id(self):
        """Gets the payee_id of this PaymentResponseV3.  # noqa: E501

        The id of the paymeee  # noqa: E501

        :return: The payee_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PaymentResponseV3.

        The id of the paymeee  # noqa: E501

        :param payee_id: The payee_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if payee_id is None:
            raise ValueError("Invalid value for `payee_id`, must not be `None`")  # noqa: E501

        self._payee_id = payee_id

    @property
    def payor_id(self):
        """Gets the payor_id of this PaymentResponseV3.  # noqa: E501

        The id of the payor  # noqa: E501

        :return: The payor_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this PaymentResponseV3.

        The id of the payor  # noqa: E501

        :param payor_id: The payor_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if payor_id is None:
            raise ValueError("Invalid value for `payor_id`, must not be `None`")  # noqa: E501

        self._payor_id = payor_id

    @property
    def payor_name(self):
        """Gets the payor_name of this PaymentResponseV3.  # noqa: E501

        The name of the payor  # noqa: E501

        :return: The payor_name of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payor_name

    @payor_name.setter
    def payor_name(self, payor_name):
        """Sets the payor_name of this PaymentResponseV3.

        The name of the payor  # noqa: E501

        :param payor_name: The payor_name of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._payor_name = payor_name

    @property
    def quote_id(self):
        """Gets the quote_id of this PaymentResponseV3.  # noqa: E501

        The quote Id used for the FX  # noqa: E501

        :return: The quote_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this PaymentResponseV3.

        The quote Id used for the FX  # noqa: E501

        :param quote_id: The quote_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def source_account_id(self):
        """Gets the source_account_id of this PaymentResponseV3.  # noqa: E501

        The id of the source account from which the payment was taken  # noqa: E501

        :return: The source_account_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._source_account_id

    @source_account_id.setter
    def source_account_id(self, source_account_id):
        """Sets the source_account_id of this PaymentResponseV3.

        The id of the source account from which the payment was taken  # noqa: E501

        :param source_account_id: The source_account_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if source_account_id is None:
            raise ValueError("Invalid value for `source_account_id`, must not be `None`")  # noqa: E501

        self._source_account_id = source_account_id

    @property
    def source_account_name(self):
        """Gets the source_account_name of this PaymentResponseV3.  # noqa: E501

        The name of the source account from which the payment was taken  # noqa: E501

        :return: The source_account_name of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._source_account_name

    @source_account_name.setter
    def source_account_name(self, source_account_name):
        """Sets the source_account_name of this PaymentResponseV3.

        The name of the source account from which the payment was taken  # noqa: E501

        :param source_account_name: The source_account_name of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._source_account_name = source_account_name

    @property
    def remote_id(self):
        """Gets the remote_id of this PaymentResponseV3.  # noqa: E501

        The remote id by which the payor refers to the payee. Only populated once payment is confirmed  # noqa: E501

        :return: The remote_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this PaymentResponseV3.

        The remote id by which the payor refers to the payee. Only populated once payment is confirmed  # noqa: E501

        :param remote_id: The remote_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._remote_id = remote_id

    @property
    def source_amount(self):
        """Gets the source_amount of this PaymentResponseV3.  # noqa: E501

        The source amount for the payment (amount debited to make the payment)  # noqa: E501

        :return: The source_amount of this PaymentResponseV3.  # noqa: E501
        :rtype: int
        """
        return self._source_amount

    @source_amount.setter
    def source_amount(self, source_amount):
        """Sets the source_amount of this PaymentResponseV3.

        The source amount for the payment (amount debited to make the payment)  # noqa: E501

        :param source_amount: The source_amount of this PaymentResponseV3.  # noqa: E501
        :type: int
        """

        self._source_amount = source_amount

    @property
    def source_currency(self):
        """Gets the source_currency of this PaymentResponseV3.  # noqa: E501

        ISO 3 character currency code  # noqa: E501

        :return: The source_currency of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this PaymentResponseV3.

        ISO 3 character currency code  # noqa: E501

        :param source_currency: The source_currency of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if source_currency is not None and len(source_currency) > 3:
            raise ValueError("Invalid value for `source_currency`, length must be less than or equal to `3`")  # noqa: E501
        if source_currency is not None and len(source_currency) < 3:
            raise ValueError("Invalid value for `source_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._source_currency = source_currency

    @property
    def payment_amount(self):
        """Gets the payment_amount of this PaymentResponseV3.  # noqa: E501

        The amount which the payee will receive  # noqa: E501

        :return: The payment_amount of this PaymentResponseV3.  # noqa: E501
        :rtype: int
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this PaymentResponseV3.

        The amount which the payee will receive  # noqa: E501

        :param payment_amount: The payment_amount of this PaymentResponseV3.  # noqa: E501
        :type: int
        """
        if payment_amount is None:
            raise ValueError("Invalid value for `payment_amount`, must not be `None`")  # noqa: E501

        self._payment_amount = payment_amount

    @property
    def payment_currency(self):
        """Gets the payment_currency of this PaymentResponseV3.  # noqa: E501

        ISO 3 character currency code  # noqa: E501

        :return: The payment_currency of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this PaymentResponseV3.

        ISO 3 character currency code  # noqa: E501

        :param payment_currency: The payment_currency of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if payment_currency is not None and len(payment_currency) > 3:
            raise ValueError("Invalid value for `payment_currency`, length must be less than or equal to `3`")  # noqa: E501
        if payment_currency is not None and len(payment_currency) < 3:
            raise ValueError("Invalid value for `payment_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._payment_currency = payment_currency

    @property
    def rate(self):
        """Gets the rate of this PaymentResponseV3.  # noqa: E501

        The FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed  # noqa: E501

        :return: The rate of this PaymentResponseV3.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this PaymentResponseV3.

        The FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed  # noqa: E501

        :param rate: The rate of this PaymentResponseV3.  # noqa: E501
        :type: float
        """

        self._rate = rate

    @property
    def inverted_rate(self):
        """Gets the inverted_rate of this PaymentResponseV3.  # noqa: E501

        The inverted FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed  # noqa: E501

        :return: The inverted_rate of this PaymentResponseV3.  # noqa: E501
        :rtype: float
        """
        return self._inverted_rate

    @inverted_rate.setter
    def inverted_rate(self, inverted_rate):
        """Sets the inverted_rate of this PaymentResponseV3.

        The inverted FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed  # noqa: E501

        :param inverted_rate: The inverted_rate of this PaymentResponseV3.  # noqa: E501
        :type: float
        """

        self._inverted_rate = inverted_rate

    @property
    def submitted_date_time(self):
        """Gets the submitted_date_time of this PaymentResponseV3.  # noqa: E501


        :return: The submitted_date_time of this PaymentResponseV3.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_date_time

    @submitted_date_time.setter
    def submitted_date_time(self, submitted_date_time):
        """Sets the submitted_date_time of this PaymentResponseV3.


        :param submitted_date_time: The submitted_date_time of this PaymentResponseV3.  # noqa: E501
        :type: datetime
        """
        if submitted_date_time is None:
            raise ValueError("Invalid value for `submitted_date_time`, must not be `None`")  # noqa: E501

        self._submitted_date_time = submitted_date_time

    @property
    def status(self):
        """Gets the status of this PaymentResponseV3.  # noqa: E501

        Current status of the payment. One of the following values: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, WITHDRAWN  # noqa: E501

        :return: The status of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PaymentResponseV3.

        Current status of the payment. One of the following values: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, WITHDRAWN  # noqa: E501

        :param status: The status of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def funding_status(self):
        """Gets the funding_status of this PaymentResponseV3.  # noqa: E501

        The funding status of the payment. One of the following values: [FUNDED, INSTRUCTED, UNFUNDED  # noqa: E501

        :return: The funding_status of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._funding_status

    @funding_status.setter
    def funding_status(self, funding_status):
        """Sets the funding_status of this PaymentResponseV3.

        The funding status of the payment. One of the following values: [FUNDED, INSTRUCTED, UNFUNDED  # noqa: E501

        :param funding_status: The funding_status of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if funding_status is None:
            raise ValueError("Invalid value for `funding_status`, must not be `None`")  # noqa: E501

        self._funding_status = funding_status

    @property
    def routing_number(self):
        """Gets the routing_number of this PaymentResponseV3.  # noqa: E501

        The routing number for the payment.  # noqa: E501

        :return: The routing_number of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this PaymentResponseV3.

        The routing number for the payment.  # noqa: E501

        :param routing_number: The routing_number of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._routing_number = routing_number

    @property
    def account_number(self):
        """Gets the account_number of this PaymentResponseV3.  # noqa: E501

        The account number for the account which will receive the payment.  # noqa: E501

        :return: The account_number of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PaymentResponseV3.

        The account number for the account which will receive the payment.  # noqa: E501

        :param account_number: The account_number of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def iban(self):
        """Gets the iban of this PaymentResponseV3.  # noqa: E501

        The iban for the payment.  # noqa: E501

        :return: The iban of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PaymentResponseV3.

        The iban for the payment.  # noqa: E501

        :param iban: The iban of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def payment_memo(self):
        """Gets the payment_memo of this PaymentResponseV3.  # noqa: E501

        The payment memo set by the payor  # noqa: E501

        :return: The payment_memo of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_memo

    @payment_memo.setter
    def payment_memo(self, payment_memo):
        """Sets the payment_memo of this PaymentResponseV3.

        The payment memo set by the payor  # noqa: E501

        :param payment_memo: The payment_memo of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._payment_memo = payment_memo

    @property
    def filename_reference(self):
        """Gets the filename_reference of this PaymentResponseV3.  # noqa: E501

        ACH file payment was submitted in, if applicable  # noqa: E501

        :return: The filename_reference of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._filename_reference

    @filename_reference.setter
    def filename_reference(self, filename_reference):
        """Sets the filename_reference of this PaymentResponseV3.

        ACH file payment was submitted in, if applicable  # noqa: E501

        :param filename_reference: The filename_reference of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._filename_reference = filename_reference

    @property
    def individual_identification_number(self):
        """Gets the individual_identification_number of this PaymentResponseV3.  # noqa: E501

        Individual Identification Number assigned to the payment in the ACH file, if applicable  # noqa: E501

        :return: The individual_identification_number of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._individual_identification_number

    @individual_identification_number.setter
    def individual_identification_number(self, individual_identification_number):
        """Sets the individual_identification_number of this PaymentResponseV3.

        Individual Identification Number assigned to the payment in the ACH file, if applicable  # noqa: E501

        :param individual_identification_number: The individual_identification_number of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._individual_identification_number = individual_identification_number

    @property
    def trace_number(self):
        """Gets the trace_number of this PaymentResponseV3.  # noqa: E501

        Trace Number assigned to the payment in the ACH file, if applicable  # noqa: E501

        :return: The trace_number of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._trace_number

    @trace_number.setter
    def trace_number(self, trace_number):
        """Sets the trace_number of this PaymentResponseV3.

        Trace Number assigned to the payment in the ACH file, if applicable  # noqa: E501

        :param trace_number: The trace_number of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._trace_number = trace_number

    @property
    def payor_payment_id(self):
        """Gets the payor_payment_id of this PaymentResponseV3.  # noqa: E501


        :return: The payor_payment_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payor_payment_id

    @payor_payment_id.setter
    def payor_payment_id(self, payor_payment_id):
        """Sets the payor_payment_id of this PaymentResponseV3.


        :param payor_payment_id: The payor_payment_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._payor_payment_id = payor_payment_id

    @property
    def payment_channel_id(self):
        """Gets the payment_channel_id of this PaymentResponseV3.  # noqa: E501


        :return: The payment_channel_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_id

    @payment_channel_id.setter
    def payment_channel_id(self, payment_channel_id):
        """Sets the payment_channel_id of this PaymentResponseV3.


        :param payment_channel_id: The payment_channel_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._payment_channel_id = payment_channel_id

    @property
    def payment_channel_name(self):
        """Gets the payment_channel_name of this PaymentResponseV3.  # noqa: E501


        :return: The payment_channel_name of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_name

    @payment_channel_name.setter
    def payment_channel_name(self, payment_channel_name):
        """Sets the payment_channel_name of this PaymentResponseV3.


        :param payment_channel_name: The payment_channel_name of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._payment_channel_name = payment_channel_name

    @property
    def account_name(self):
        """Gets the account_name of this PaymentResponseV3.  # noqa: E501


        :return: The account_name of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this PaymentResponseV3.


        :param account_name: The account_name of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def rails_id(self):
        """Gets the rails_id of this PaymentResponseV3.  # noqa: E501

        The rails ID. Default value is RAILS ID UNAVAILABLE when not populated.  # noqa: E501

        :return: The rails_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._rails_id

    @rails_id.setter
    def rails_id(self, rails_id):
        """Sets the rails_id of this PaymentResponseV3.

        The rails ID. Default value is RAILS ID UNAVAILABLE when not populated.  # noqa: E501

        :param rails_id: The rails_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """
        if rails_id is None:
            raise ValueError("Invalid value for `rails_id`, must not be `None`")  # noqa: E501

        self._rails_id = rails_id

    @property
    def country_code(self):
        """Gets the country_code of this PaymentResponseV3.  # noqa: E501

        The country code of the payment channel.  # noqa: E501

        :return: The country_code of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PaymentResponseV3.

        The country code of the payment channel.  # noqa: E501

        :param country_code: The country_code of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def events(self):
        """Gets the events of this PaymentResponseV3.  # noqa: E501


        :return: The events of this PaymentResponseV3.  # noqa: E501
        :rtype: list[PaymentEventResponseV3]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this PaymentResponseV3.


        :param events: The events of this PaymentResponseV3.  # noqa: E501
        :type: list[PaymentEventResponseV3]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")  # noqa: E501

        self._events = events

    @property
    def return_cost(self):
        """Gets the return_cost of this PaymentResponseV3.  # noqa: E501

        The return cost if a returned payment.  # noqa: E501

        :return: The return_cost of this PaymentResponseV3.  # noqa: E501
        :rtype: int
        """
        return self._return_cost

    @return_cost.setter
    def return_cost(self, return_cost):
        """Sets the return_cost of this PaymentResponseV3.

        The return cost if a returned payment.  # noqa: E501

        :param return_cost: The return_cost of this PaymentResponseV3.  # noqa: E501
        :type: int
        """

        self._return_cost = return_cost

    @property
    def return_reason(self):
        """Gets the return_reason of this PaymentResponseV3.  # noqa: E501


        :return: The return_reason of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._return_reason

    @return_reason.setter
    def return_reason(self, return_reason):
        """Sets the return_reason of this PaymentResponseV3.


        :param return_reason: The return_reason of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._return_reason = return_reason

    @property
    def rails_payment_id(self):
        """Gets the rails_payment_id of this PaymentResponseV3.  # noqa: E501


        :return: The rails_payment_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._rails_payment_id

    @rails_payment_id.setter
    def rails_payment_id(self, rails_payment_id):
        """Sets the rails_payment_id of this PaymentResponseV3.


        :param rails_payment_id: The rails_payment_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._rails_payment_id = rails_payment_id

    @property
    def rails_batch_id(self):
        """Gets the rails_batch_id of this PaymentResponseV3.  # noqa: E501


        :return: The rails_batch_id of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._rails_batch_id

    @rails_batch_id.setter
    def rails_batch_id(self, rails_batch_id):
        """Sets the rails_batch_id of this PaymentResponseV3.


        :param rails_batch_id: The rails_batch_id of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._rails_batch_id = rails_batch_id

    @property
    def payment_scheme(self):
        """Gets the payment_scheme of this PaymentResponseV3.  # noqa: E501


        :return: The payment_scheme of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_scheme

    @payment_scheme.setter
    def payment_scheme(self, payment_scheme):
        """Sets the payment_scheme of this PaymentResponseV3.


        :param payment_scheme: The payment_scheme of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._payment_scheme = payment_scheme

    @property
    def rejection_reason(self):
        """Gets the rejection_reason of this PaymentResponseV3.  # noqa: E501


        :return: The rejection_reason of this PaymentResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._rejection_reason

    @rejection_reason.setter
    def rejection_reason(self, rejection_reason):
        """Sets the rejection_reason of this PaymentResponseV3.


        :param rejection_reason: The rejection_reason of this PaymentResponseV3.  # noqa: E501
        :type: str
        """

        self._rejection_reason = rejection_reason

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
        if not isinstance(other, PaymentResponseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
