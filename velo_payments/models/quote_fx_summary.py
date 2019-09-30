# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.15.95
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class QuoteFxSummary(object):
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
        'rate': 'float',
        'inverted_rate': 'float',
        'creation_time': 'datetime',
        'expiry_time': 'datetime',
        'quote_id': 'str',
        'total_source_amount': 'int',
        'total_payment_amount': 'int',
        'source_currency': 'str',
        'payment_currency': 'str',
        'funding_status': 'str',
        'status': 'str'
    }

    attribute_map = {
        'rate': 'rate',
        'inverted_rate': 'invertedRate',
        'creation_time': 'creationTime',
        'expiry_time': 'expiryTime',
        'quote_id': 'quoteId',
        'total_source_amount': 'totalSourceAmount',
        'total_payment_amount': 'totalPaymentAmount',
        'source_currency': 'sourceCurrency',
        'payment_currency': 'paymentCurrency',
        'funding_status': 'fundingStatus',
        'status': 'status'
    }

    def __init__(self, rate=None, inverted_rate=None, creation_time=None, expiry_time=None, quote_id=None, total_source_amount=None, total_payment_amount=None, source_currency=None, payment_currency=None, funding_status=None, status=None):  # noqa: E501
        """QuoteFxSummary - a model defined in OpenAPI"""  # noqa: E501

        self._rate = None
        self._inverted_rate = None
        self._creation_time = None
        self._expiry_time = None
        self._quote_id = None
        self._total_source_amount = None
        self._total_payment_amount = None
        self._source_currency = None
        self._payment_currency = None
        self._funding_status = None
        self._status = None
        self.discriminator = None

        self.rate = rate
        if inverted_rate is not None:
            self.inverted_rate = inverted_rate
        self.creation_time = creation_time
        if expiry_time is not None:
            self.expiry_time = expiry_time
        self.quote_id = quote_id
        self.total_source_amount = total_source_amount
        self.total_payment_amount = total_payment_amount
        self.source_currency = source_currency
        self.payment_currency = payment_currency
        if funding_status is not None:
            self.funding_status = funding_status
        if status is not None:
            self.status = status

    @property
    def rate(self):
        """Gets the rate of this QuoteFxSummary.  # noqa: E501


        :return: The rate of this QuoteFxSummary.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this QuoteFxSummary.


        :param rate: The rate of this QuoteFxSummary.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def inverted_rate(self):
        """Gets the inverted_rate of this QuoteFxSummary.  # noqa: E501


        :return: The inverted_rate of this QuoteFxSummary.  # noqa: E501
        :rtype: float
        """
        return self._inverted_rate

    @inverted_rate.setter
    def inverted_rate(self, inverted_rate):
        """Sets the inverted_rate of this QuoteFxSummary.


        :param inverted_rate: The inverted_rate of this QuoteFxSummary.  # noqa: E501
        :type: float
        """

        self._inverted_rate = inverted_rate

    @property
    def creation_time(self):
        """Gets the creation_time of this QuoteFxSummary.  # noqa: E501


        :return: The creation_time of this QuoteFxSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this QuoteFxSummary.


        :param creation_time: The creation_time of this QuoteFxSummary.  # noqa: E501
        :type: datetime
        """
        if creation_time is None:
            raise ValueError("Invalid value for `creation_time`, must not be `None`")  # noqa: E501

        self._creation_time = creation_time

    @property
    def expiry_time(self):
        """Gets the expiry_time of this QuoteFxSummary.  # noqa: E501


        :return: The expiry_time of this QuoteFxSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry_time

    @expiry_time.setter
    def expiry_time(self, expiry_time):
        """Sets the expiry_time of this QuoteFxSummary.


        :param expiry_time: The expiry_time of this QuoteFxSummary.  # noqa: E501
        :type: datetime
        """

        self._expiry_time = expiry_time

    @property
    def quote_id(self):
        """Gets the quote_id of this QuoteFxSummary.  # noqa: E501


        :return: The quote_id of this QuoteFxSummary.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this QuoteFxSummary.


        :param quote_id: The quote_id of this QuoteFxSummary.  # noqa: E501
        :type: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def total_source_amount(self):
        """Gets the total_source_amount of this QuoteFxSummary.  # noqa: E501


        :return: The total_source_amount of this QuoteFxSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_source_amount

    @total_source_amount.setter
    def total_source_amount(self, total_source_amount):
        """Sets the total_source_amount of this QuoteFxSummary.


        :param total_source_amount: The total_source_amount of this QuoteFxSummary.  # noqa: E501
        :type: int
        """
        if total_source_amount is None:
            raise ValueError("Invalid value for `total_source_amount`, must not be `None`")  # noqa: E501

        self._total_source_amount = total_source_amount

    @property
    def total_payment_amount(self):
        """Gets the total_payment_amount of this QuoteFxSummary.  # noqa: E501


        :return: The total_payment_amount of this QuoteFxSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_payment_amount

    @total_payment_amount.setter
    def total_payment_amount(self, total_payment_amount):
        """Sets the total_payment_amount of this QuoteFxSummary.


        :param total_payment_amount: The total_payment_amount of this QuoteFxSummary.  # noqa: E501
        :type: int
        """
        if total_payment_amount is None:
            raise ValueError("Invalid value for `total_payment_amount`, must not be `None`")  # noqa: E501

        self._total_payment_amount = total_payment_amount

    @property
    def source_currency(self):
        """Gets the source_currency of this QuoteFxSummary.  # noqa: E501


        :return: The source_currency of this QuoteFxSummary.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this QuoteFxSummary.


        :param source_currency: The source_currency of this QuoteFxSummary.  # noqa: E501
        :type: str
        """
        if source_currency is None:
            raise ValueError("Invalid value for `source_currency`, must not be `None`")  # noqa: E501
        if source_currency is not None and len(source_currency) > 3:
            raise ValueError("Invalid value for `source_currency`, length must be less than or equal to `3`")  # noqa: E501
        if source_currency is not None and len(source_currency) < 3:
            raise ValueError("Invalid value for `source_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._source_currency = source_currency

    @property
    def payment_currency(self):
        """Gets the payment_currency of this QuoteFxSummary.  # noqa: E501


        :return: The payment_currency of this QuoteFxSummary.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this QuoteFxSummary.


        :param payment_currency: The payment_currency of this QuoteFxSummary.  # noqa: E501
        :type: str
        """
        if payment_currency is None:
            raise ValueError("Invalid value for `payment_currency`, must not be `None`")  # noqa: E501
        if payment_currency is not None and len(payment_currency) > 3:
            raise ValueError("Invalid value for `payment_currency`, length must be less than or equal to `3`")  # noqa: E501
        if payment_currency is not None and len(payment_currency) < 3:
            raise ValueError("Invalid value for `payment_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._payment_currency = payment_currency

    @property
    def funding_status(self):
        """Gets the funding_status of this QuoteFxSummary.  # noqa: E501


        :return: The funding_status of this QuoteFxSummary.  # noqa: E501
        :rtype: str
        """
        return self._funding_status

    @funding_status.setter
    def funding_status(self, funding_status):
        """Sets the funding_status of this QuoteFxSummary.


        :param funding_status: The funding_status of this QuoteFxSummary.  # noqa: E501
        :type: str
        """

        self._funding_status = funding_status

    @property
    def status(self):
        """Gets the status of this QuoteFxSummary.  # noqa: E501


        :return: The status of this QuoteFxSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this QuoteFxSummary.


        :param status: The status of this QuoteFxSummary.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if not isinstance(other, QuoteFxSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
