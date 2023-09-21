# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.35.58
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PaymentEventResponseV3(object):
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
        'event_id': 'str',
        'event_date_time': 'datetime',
        'event_type': 'str',
        'source_currency': 'str',
        'source_amount': 'int',
        'payment_currency': 'str',
        'payment_amount': 'int',
        'account_number': 'str',
        'routing_number': 'str',
        'iban': 'str',
        'account_name': 'str',
        'principal': 'str'
    }

    attribute_map = {
        'event_id': 'eventId',
        'event_date_time': 'eventDateTime',
        'event_type': 'eventType',
        'source_currency': 'sourceCurrency',
        'source_amount': 'sourceAmount',
        'payment_currency': 'paymentCurrency',
        'payment_amount': 'paymentAmount',
        'account_number': 'accountNumber',
        'routing_number': 'routingNumber',
        'iban': 'iban',
        'account_name': 'accountName',
        'principal': 'principal'
    }

    def __init__(self, event_id=None, event_date_time=None, event_type=None, source_currency=None, source_amount=None, payment_currency=None, payment_amount=None, account_number=None, routing_number=None, iban=None, account_name=None, principal=None):  # noqa: E501
        """PaymentEventResponseV3 - a model defined in OpenAPI"""  # noqa: E501

        self._event_id = None
        self._event_date_time = None
        self._event_type = None
        self._source_currency = None
        self._source_amount = None
        self._payment_currency = None
        self._payment_amount = None
        self._account_number = None
        self._routing_number = None
        self._iban = None
        self._account_name = None
        self._principal = None
        self.discriminator = None

        self.event_id = event_id
        self.event_date_time = event_date_time
        self.event_type = event_type
        if source_currency is not None:
            self.source_currency = source_currency
        if source_amount is not None:
            self.source_amount = source_amount
        if payment_currency is not None:
            self.payment_currency = payment_currency
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if account_number is not None:
            self.account_number = account_number
        if routing_number is not None:
            self.routing_number = routing_number
        if iban is not None:
            self.iban = iban
        if account_name is not None:
            self.account_name = account_name
        if principal is not None:
            self.principal = principal

    @property
    def event_id(self):
        """Gets the event_id of this PaymentEventResponseV3.  # noqa: E501

        The id of the event.  # noqa: E501

        :return: The event_id of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this PaymentEventResponseV3.

        The id of the event.  # noqa: E501

        :param event_id: The event_id of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """
        if event_id is None:
            raise ValueError("Invalid value for `event_id`, must not be `None`")  # noqa: E501

        self._event_id = event_id

    @property
    def event_date_time(self):
        """Gets the event_date_time of this PaymentEventResponseV3.  # noqa: E501

        The date/time at which the event occurred.  # noqa: E501

        :return: The event_date_time of this PaymentEventResponseV3.  # noqa: E501
        :rtype: datetime
        """
        return self._event_date_time

    @event_date_time.setter
    def event_date_time(self, event_date_time):
        """Sets the event_date_time of this PaymentEventResponseV3.

        The date/time at which the event occurred.  # noqa: E501

        :param event_date_time: The event_date_time of this PaymentEventResponseV3.  # noqa: E501
        :type: datetime
        """
        if event_date_time is None:
            raise ValueError("Invalid value for `event_date_time`, must not be `None`")  # noqa: E501

        self._event_date_time = event_date_time

    @property
    def event_type(self):
        """Gets the event_type of this PaymentEventResponseV3.  # noqa: E501

        The type of the event. One of the following values: PAYOUT_SUBMITTED, PAYOUT_COMPLETED, PAYOUT_INSTRUCTED_V3, BANK_PAYMENT_REQUESTED, SOURCE_AMOUNT_CONFIRMED, PAYMENT_SUBMITTED, PAYMENT_SUBMITTED_ACCEPTED, PAYMENT_SUBMITTED_REJECTED, PAYMENT_CONFIRMED, PAYMENT_AWAITING_FUNDS, PAYMENT_FUNDED, PAYMENT_UNFUNDED, PAYMENT_FAILED, ACH_SUBMITTED_TO_ODFI, PAYMENT_ACCEPTED_BY_RAILS, ACH_RETURN_RECEIVED, RETURN_PAYMENT_FUNDING_REQUESTED, PAYOUT_BATCH_EXECUTED, PAYOUT_BATCH_QUOTE_EXPIRED, PAYOUT_BATCH_FUNDED, PAYOUT_BATCH_FUNDS_RETURN_REQUEST, PAYOUT_BATCH_FUNDS_RETURNED, PAYOUT_FUNDS_REQUEST, PAYOUT_FUNDS_GRANTED, PAYOUT_FUNDS_DENIED, PAYOUT_BATCH_QUOTED, PAYOUT_QUOTED, ACH_PAYMENT_RETURN_CANCELLED, RETURN_PAYMENT_CANCELLATION_REQUESTED, PAYOUT_WITHDRAWN  # noqa: E501

        :return: The event_type of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this PaymentEventResponseV3.

        The type of the event. One of the following values: PAYOUT_SUBMITTED, PAYOUT_COMPLETED, PAYOUT_INSTRUCTED_V3, BANK_PAYMENT_REQUESTED, SOURCE_AMOUNT_CONFIRMED, PAYMENT_SUBMITTED, PAYMENT_SUBMITTED_ACCEPTED, PAYMENT_SUBMITTED_REJECTED, PAYMENT_CONFIRMED, PAYMENT_AWAITING_FUNDS, PAYMENT_FUNDED, PAYMENT_UNFUNDED, PAYMENT_FAILED, ACH_SUBMITTED_TO_ODFI, PAYMENT_ACCEPTED_BY_RAILS, ACH_RETURN_RECEIVED, RETURN_PAYMENT_FUNDING_REQUESTED, PAYOUT_BATCH_EXECUTED, PAYOUT_BATCH_QUOTE_EXPIRED, PAYOUT_BATCH_FUNDED, PAYOUT_BATCH_FUNDS_RETURN_REQUEST, PAYOUT_BATCH_FUNDS_RETURNED, PAYOUT_FUNDS_REQUEST, PAYOUT_FUNDS_GRANTED, PAYOUT_FUNDS_DENIED, PAYOUT_BATCH_QUOTED, PAYOUT_QUOTED, ACH_PAYMENT_RETURN_CANCELLED, RETURN_PAYMENT_CANCELLATION_REQUESTED, PAYOUT_WITHDRAWN  # noqa: E501

        :param event_type: The event_type of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """
        if event_type is None:
            raise ValueError("Invalid value for `event_type`, must not be `None`")  # noqa: E501

        self._event_type = event_type

    @property
    def source_currency(self):
        """Gets the source_currency of this PaymentEventResponseV3.  # noqa: E501

        ISO 3 character currency code  # noqa: E501

        :return: The source_currency of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this PaymentEventResponseV3.

        ISO 3 character currency code  # noqa: E501

        :param source_currency: The source_currency of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """
        if source_currency is not None and len(source_currency) > 3:
            raise ValueError("Invalid value for `source_currency`, length must be less than or equal to `3`")  # noqa: E501
        if source_currency is not None and len(source_currency) < 3:
            raise ValueError("Invalid value for `source_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._source_currency = source_currency

    @property
    def source_amount(self):
        """Gets the source_amount of this PaymentEventResponseV3.  # noqa: E501

        The source amount exposed by the event.  # noqa: E501

        :return: The source_amount of this PaymentEventResponseV3.  # noqa: E501
        :rtype: int
        """
        return self._source_amount

    @source_amount.setter
    def source_amount(self, source_amount):
        """Sets the source_amount of this PaymentEventResponseV3.

        The source amount exposed by the event.  # noqa: E501

        :param source_amount: The source_amount of this PaymentEventResponseV3.  # noqa: E501
        :type: int
        """

        self._source_amount = source_amount

    @property
    def payment_currency(self):
        """Gets the payment_currency of this PaymentEventResponseV3.  # noqa: E501

        ISO 3 character currency code  # noqa: E501

        :return: The payment_currency of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this PaymentEventResponseV3.

        ISO 3 character currency code  # noqa: E501

        :param payment_currency: The payment_currency of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """
        if payment_currency is not None and len(payment_currency) > 3:
            raise ValueError("Invalid value for `payment_currency`, length must be less than or equal to `3`")  # noqa: E501
        if payment_currency is not None and len(payment_currency) < 3:
            raise ValueError("Invalid value for `payment_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._payment_currency = payment_currency

    @property
    def payment_amount(self):
        """Gets the payment_amount of this PaymentEventResponseV3.  # noqa: E501

        The destination amount exposed by the event.  # noqa: E501

        :return: The payment_amount of this PaymentEventResponseV3.  # noqa: E501
        :rtype: int
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this PaymentEventResponseV3.

        The destination amount exposed by the event.  # noqa: E501

        :param payment_amount: The payment_amount of this PaymentEventResponseV3.  # noqa: E501
        :type: int
        """

        self._payment_amount = payment_amount

    @property
    def account_number(self):
        """Gets the account_number of this PaymentEventResponseV3.  # noqa: E501

        The account number attached to the event.  # noqa: E501

        :return: The account_number of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this PaymentEventResponseV3.

        The account number attached to the event.  # noqa: E501

        :param account_number: The account_number of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def routing_number(self):
        """Gets the routing_number of this PaymentEventResponseV3.  # noqa: E501

        The routing number attached to the event.  # noqa: E501

        :return: The routing_number of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this PaymentEventResponseV3.

        The routing number attached to the event.  # noqa: E501

        :param routing_number: The routing_number of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """

        self._routing_number = routing_number

    @property
    def iban(self):
        """Gets the iban of this PaymentEventResponseV3.  # noqa: E501


        :return: The iban of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this PaymentEventResponseV3.


        :param iban: The iban of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def account_name(self):
        """Gets the account_name of this PaymentEventResponseV3.  # noqa: E501


        :return: The account_name of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this PaymentEventResponseV3.


        :param account_name: The account_name of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def principal(self):
        """Gets the principal of this PaymentEventResponseV3.  # noqa: E501


        :return: The principal of this PaymentEventResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        """Sets the principal of this PaymentEventResponseV3.


        :param principal: The principal of this PaymentEventResponseV3.  # noqa: E501
        :type: str
        """

        self._principal = principal

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
        if not isinstance(other, PaymentEventResponseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
