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


class FxSummary(object):
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
        'quote_id': 'str',
        'creation_date_time': 'datetime',
        'rate': 'float',
        'inverted_rate': 'float',
        'total_cost': 'int',
        'total_payment_amount': 'int',
        'source_currency': 'str',
        'payment_currency': 'str',
        'status': 'str',
        'funding_status': 'str'
    }

    attribute_map = {
        'quote_id': 'quoteId',
        'creation_date_time': 'creationDateTime',
        'rate': 'rate',
        'inverted_rate': 'invertedRate',
        'total_cost': 'totalCost',
        'total_payment_amount': 'totalPaymentAmount',
        'source_currency': 'sourceCurrency',
        'payment_currency': 'paymentCurrency',
        'status': 'status',
        'funding_status': 'fundingStatus'
    }

    def __init__(self, quote_id=None, creation_date_time=None, rate=None, inverted_rate=None, total_cost=None, total_payment_amount=None, source_currency=None, payment_currency=None, status=None, funding_status=None):  # noqa: E501
        """FxSummary - a model defined in OpenAPI"""  # noqa: E501

        self._quote_id = None
        self._creation_date_time = None
        self._rate = None
        self._inverted_rate = None
        self._total_cost = None
        self._total_payment_amount = None
        self._source_currency = None
        self._payment_currency = None
        self._status = None
        self._funding_status = None
        self.discriminator = None

        self.quote_id = quote_id
        self.creation_date_time = creation_date_time
        self.rate = rate
        self.inverted_rate = inverted_rate
        self.total_cost = total_cost
        self.total_payment_amount = total_payment_amount
        if source_currency is not None:
            self.source_currency = source_currency
        if payment_currency is not None:
            self.payment_currency = payment_currency
        self.status = status
        self.funding_status = funding_status

    @property
    def quote_id(self):
        """Gets the quote_id of this FxSummary.  # noqa: E501


        :return: The quote_id of this FxSummary.  # noqa: E501
        :rtype: str
        """
        return self._quote_id

    @quote_id.setter
    def quote_id(self, quote_id):
        """Sets the quote_id of this FxSummary.


        :param quote_id: The quote_id of this FxSummary.  # noqa: E501
        :type: str
        """
        if quote_id is None:
            raise ValueError("Invalid value for `quote_id`, must not be `None`")  # noqa: E501

        self._quote_id = quote_id

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this FxSummary.  # noqa: E501


        :return: The creation_date_time of this FxSummary.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this FxSummary.


        :param creation_date_time: The creation_date_time of this FxSummary.  # noqa: E501
        :type: datetime
        """
        if creation_date_time is None:
            raise ValueError("Invalid value for `creation_date_time`, must not be `None`")  # noqa: E501

        self._creation_date_time = creation_date_time

    @property
    def rate(self):
        """Gets the rate of this FxSummary.  # noqa: E501


        :return: The rate of this FxSummary.  # noqa: E501
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this FxSummary.


        :param rate: The rate of this FxSummary.  # noqa: E501
        :type: float
        """
        if rate is None:
            raise ValueError("Invalid value for `rate`, must not be `None`")  # noqa: E501

        self._rate = rate

    @property
    def inverted_rate(self):
        """Gets the inverted_rate of this FxSummary.  # noqa: E501


        :return: The inverted_rate of this FxSummary.  # noqa: E501
        :rtype: float
        """
        return self._inverted_rate

    @inverted_rate.setter
    def inverted_rate(self, inverted_rate):
        """Sets the inverted_rate of this FxSummary.


        :param inverted_rate: The inverted_rate of this FxSummary.  # noqa: E501
        :type: float
        """
        if inverted_rate is None:
            raise ValueError("Invalid value for `inverted_rate`, must not be `None`")  # noqa: E501

        self._inverted_rate = inverted_rate

    @property
    def total_cost(self):
        """Gets the total_cost of this FxSummary.  # noqa: E501


        :return: The total_cost of this FxSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_cost

    @total_cost.setter
    def total_cost(self, total_cost):
        """Sets the total_cost of this FxSummary.


        :param total_cost: The total_cost of this FxSummary.  # noqa: E501
        :type: int
        """
        if total_cost is None:
            raise ValueError("Invalid value for `total_cost`, must not be `None`")  # noqa: E501

        self._total_cost = total_cost

    @property
    def total_payment_amount(self):
        """Gets the total_payment_amount of this FxSummary.  # noqa: E501


        :return: The total_payment_amount of this FxSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_payment_amount

    @total_payment_amount.setter
    def total_payment_amount(self, total_payment_amount):
        """Sets the total_payment_amount of this FxSummary.


        :param total_payment_amount: The total_payment_amount of this FxSummary.  # noqa: E501
        :type: int
        """
        if total_payment_amount is None:
            raise ValueError("Invalid value for `total_payment_amount`, must not be `None`")  # noqa: E501

        self._total_payment_amount = total_payment_amount

    @property
    def source_currency(self):
        """Gets the source_currency of this FxSummary.  # noqa: E501

        ISO-4217 3 character currency code  # noqa: E501

        :return: The source_currency of this FxSummary.  # noqa: E501
        :rtype: str
        """
        return self._source_currency

    @source_currency.setter
    def source_currency(self, source_currency):
        """Sets the source_currency of this FxSummary.

        ISO-4217 3 character currency code  # noqa: E501

        :param source_currency: The source_currency of this FxSummary.  # noqa: E501
        :type: str
        """
        if source_currency is not None and len(source_currency) > 3:
            raise ValueError("Invalid value for `source_currency`, length must be less than or equal to `3`")  # noqa: E501
        if source_currency is not None and len(source_currency) < 3:
            raise ValueError("Invalid value for `source_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._source_currency = source_currency

    @property
    def payment_currency(self):
        """Gets the payment_currency of this FxSummary.  # noqa: E501

        ISO-4217 3 character currency code  # noqa: E501

        :return: The payment_currency of this FxSummary.  # noqa: E501
        :rtype: str
        """
        return self._payment_currency

    @payment_currency.setter
    def payment_currency(self, payment_currency):
        """Sets the payment_currency of this FxSummary.

        ISO-4217 3 character currency code  # noqa: E501

        :param payment_currency: The payment_currency of this FxSummary.  # noqa: E501
        :type: str
        """
        if payment_currency is not None and len(payment_currency) > 3:
            raise ValueError("Invalid value for `payment_currency`, length must be less than or equal to `3`")  # noqa: E501
        if payment_currency is not None and len(payment_currency) < 3:
            raise ValueError("Invalid value for `payment_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._payment_currency = payment_currency

    @property
    def status(self):
        """Gets the status of this FxSummary.  # noqa: E501

        Current status of the FX Summary. One of the following values: UNQUOTED, QUOTED, EXPIRED, EXECUTED  # noqa: E501

        :return: The status of this FxSummary.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FxSummary.

        Current status of the FX Summary. One of the following values: UNQUOTED, QUOTED, EXPIRED, EXECUTED  # noqa: E501

        :param status: The status of this FxSummary.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def funding_status(self):
        """Gets the funding_status of this FxSummary.  # noqa: E501

        Current status of the funding. One of the following values: FUNDED, INSTRUCTED, UNFUNDED  # noqa: E501

        :return: The funding_status of this FxSummary.  # noqa: E501
        :rtype: str
        """
        return self._funding_status

    @funding_status.setter
    def funding_status(self, funding_status):
        """Sets the funding_status of this FxSummary.

        Current status of the funding. One of the following values: FUNDED, INSTRUCTED, UNFUNDED  # noqa: E501

        :param funding_status: The funding_status of this FxSummary.  # noqa: E501
        :type: str
        """
        if funding_status is None:
            raise ValueError("Invalid value for `funding_status`, must not be `None`")  # noqa: E501

        self._funding_status = funding_status

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
        if not isinstance(other, FxSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
