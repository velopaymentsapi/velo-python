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


class FundingAudit(object):
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
        'payor_id': 'str',
        'amount': 'float',
        'currency': 'str',
        'date_time': 'datetime',
        'status': 'str',
        'source_account_name': 'str',
        'funding_account_name': 'str',
        'funding_type': 'str',
        'events': 'list[FundingEvent2]',
        'topup_type': 'str',
        'transaction_id': 'str',
        'transaction_reference': 'str'
    }

    attribute_map = {
        'payor_id': 'payorId',
        'amount': 'amount',
        'currency': 'currency',
        'date_time': 'dateTime',
        'status': 'status',
        'source_account_name': 'sourceAccountName',
        'funding_account_name': 'fundingAccountName',
        'funding_type': 'fundingType',
        'events': 'events',
        'topup_type': 'topupType',
        'transaction_id': 'transactionId',
        'transaction_reference': 'transactionReference'
    }

    def __init__(self, payor_id=None, amount=None, currency=None, date_time=None, status=None, source_account_name=None, funding_account_name=None, funding_type=None, events=None, topup_type=None, transaction_id=None, transaction_reference=None):  # noqa: E501
        """FundingAudit - a model defined in OpenAPI"""  # noqa: E501

        self._payor_id = None
        self._amount = None
        self._currency = None
        self._date_time = None
        self._status = None
        self._source_account_name = None
        self._funding_account_name = None
        self._funding_type = None
        self._events = None
        self._topup_type = None
        self._transaction_id = None
        self._transaction_reference = None
        self.discriminator = None

        if payor_id is not None:
            self.payor_id = payor_id
        if amount is not None:
            self.amount = amount
        if currency is not None:
            self.currency = currency
        if date_time is not None:
            self.date_time = date_time
        if status is not None:
            self.status = status
        if source_account_name is not None:
            self.source_account_name = source_account_name
        if funding_account_name is not None:
            self.funding_account_name = funding_account_name
        if funding_type is not None:
            self.funding_type = funding_type
        if events is not None:
            self.events = events
        if topup_type is not None:
            self.topup_type = topup_type
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_reference is not None:
            self.transaction_reference = transaction_reference

    @property
    def payor_id(self):
        """Gets the payor_id of this FundingAudit.  # noqa: E501

        The id of the payor associated with the funding.  # noqa: E501

        :return: The payor_id of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this FundingAudit.

        The id of the payor associated with the funding.  # noqa: E501

        :param payor_id: The payor_id of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._payor_id = payor_id

    @property
    def amount(self):
        """Gets the amount of this FundingAudit.  # noqa: E501

        The amount funded  # noqa: E501

        :return: The amount of this FundingAudit.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FundingAudit.

        The amount funded  # noqa: E501

        :param amount: The amount of this FundingAudit.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this FundingAudit.  # noqa: E501

        The currency of the funding  # noqa: E501

        :return: The currency of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FundingAudit.

        The currency of the funding  # noqa: E501

        :param currency: The currency of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def date_time(self):
        """Gets the date_time of this FundingAudit.  # noqa: E501


        :return: The date_time of this FundingAudit.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this FundingAudit.


        :param date_time: The date_time of this FundingAudit.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def status(self):
        """Gets the status of this FundingAudit.  # noqa: E501

        Status of the funding. One of the following values: PENDING, FAILED, CREDIT, DEBIT  # noqa: E501

        :return: The status of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FundingAudit.

        Status of the funding. One of the following values: PENDING, FAILED, CREDIT, DEBIT  # noqa: E501

        :param status: The status of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def source_account_name(self):
        """Gets the source_account_name of this FundingAudit.  # noqa: E501


        :return: The source_account_name of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._source_account_name

    @source_account_name.setter
    def source_account_name(self, source_account_name):
        """Sets the source_account_name of this FundingAudit.


        :param source_account_name: The source_account_name of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._source_account_name = source_account_name

    @property
    def funding_account_name(self):
        """Gets the funding_account_name of this FundingAudit.  # noqa: E501


        :return: The funding_account_name of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._funding_account_name

    @funding_account_name.setter
    def funding_account_name(self, funding_account_name):
        """Sets the funding_account_name of this FundingAudit.


        :param funding_account_name: The funding_account_name of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._funding_account_name = funding_account_name

    @property
    def funding_type(self):
        """Gets the funding_type of this FundingAudit.  # noqa: E501

        Funding type. One of the following values: ACH, WIRE, EMBEDDED, BANK_TRANSFER  # noqa: E501

        :return: The funding_type of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._funding_type

    @funding_type.setter
    def funding_type(self, funding_type):
        """Sets the funding_type of this FundingAudit.

        Funding type. One of the following values: ACH, WIRE, EMBEDDED, BANK_TRANSFER  # noqa: E501

        :param funding_type: The funding_type of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._funding_type = funding_type

    @property
    def events(self):
        """Gets the events of this FundingAudit.  # noqa: E501


        :return: The events of this FundingAudit.  # noqa: E501
        :rtype: list[FundingEvent2]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this FundingAudit.


        :param events: The events of this FundingAudit.  # noqa: E501
        :type: list[FundingEvent2]
        """

        self._events = events

    @property
    def topup_type(self):
        """Gets the topup_type of this FundingAudit.  # noqa: E501

        Type of top up. One of the following values: AUTOMATIC, MANUAL  # noqa: E501

        :return: The topup_type of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._topup_type

    @topup_type.setter
    def topup_type(self, topup_type):
        """Sets the topup_type of this FundingAudit.

        Type of top up. One of the following values: AUTOMATIC, MANUAL  # noqa: E501

        :param topup_type: The topup_type of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._topup_type = topup_type

    @property
    def transaction_id(self):
        """Gets the transaction_id of this FundingAudit.  # noqa: E501

        The id of the transaction associated with the funding if there was one  # noqa: E501

        :return: The transaction_id of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this FundingAudit.

        The id of the transaction associated with the funding if there was one  # noqa: E501

        :param transaction_id: The transaction_id of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def transaction_reference(self):
        """Gets the transaction_reference of this FundingAudit.  # noqa: E501

        The payors reference for the transaction associated with the funding if there was one  # noqa: E501

        :return: The transaction_reference of this FundingAudit.  # noqa: E501
        :rtype: str
        """
        return self._transaction_reference

    @transaction_reference.setter
    def transaction_reference(self, transaction_reference):
        """Sets the transaction_reference of this FundingAudit.

        The payors reference for the transaction associated with the funding if there was one  # noqa: E501

        :param transaction_reference: The transaction_reference of this FundingAudit.  # noqa: E501
        :type: str
        """

        self._transaction_reference = transaction_reference

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
        if not isinstance(other, FundingAudit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
