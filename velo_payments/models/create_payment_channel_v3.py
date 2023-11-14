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


class CreatePaymentChannelV3(object):
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
        'payment_channel_name': 'str',
        'iban': 'str',
        'account_number': 'str',
        'routing_number': 'str',
        'country_code': 'str',
        'currency': 'str',
        'account_name': 'str'
    }

    attribute_map = {
        'payment_channel_name': 'paymentChannelName',
        'iban': 'iban',
        'account_number': 'accountNumber',
        'routing_number': 'routingNumber',
        'country_code': 'countryCode',
        'currency': 'currency',
        'account_name': 'accountName'
    }

    def __init__(self, payment_channel_name=None, iban=None, account_number=None, routing_number=None, country_code=None, currency=None, account_name=None):  # noqa: E501
        """CreatePaymentChannelV3 - a model defined in OpenAPI"""  # noqa: E501

        self._payment_channel_name = None
        self._iban = None
        self._account_number = None
        self._routing_number = None
        self._country_code = None
        self._currency = None
        self._account_name = None
        self.discriminator = None

        if payment_channel_name is not None:
            self.payment_channel_name = payment_channel_name
        if iban is not None:
            self.iban = iban
        if account_number is not None:
            self.account_number = account_number
        if routing_number is not None:
            self.routing_number = routing_number
        self.country_code = country_code
        self.currency = currency
        self.account_name = account_name

    @property
    def payment_channel_name(self):
        """Gets the payment_channel_name of this CreatePaymentChannelV3.  # noqa: E501


        :return: The payment_channel_name of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_name

    @payment_channel_name.setter
    def payment_channel_name(self, payment_channel_name):
        """Sets the payment_channel_name of this CreatePaymentChannelV3.


        :param payment_channel_name: The payment_channel_name of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """

        self._payment_channel_name = payment_channel_name

    @property
    def iban(self):
        """Gets the iban of this CreatePaymentChannelV3.  # noqa: E501

        Must match the regular expression ```^[A-Za-z0-9]+$```.  # noqa: E501

        :return: The iban of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this CreatePaymentChannelV3.

        Must match the regular expression ```^[A-Za-z0-9]+$```.  # noqa: E501

        :param iban: The iban of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """
        if iban is not None and len(iban) > 34:
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `34`")  # noqa: E501
        if iban is not None and len(iban) < 15:
            raise ValueError("Invalid value for `iban`, length must be greater than or equal to `15`")  # noqa: E501
        if iban is not None and not re.search(r'^[A-Za-z0-9]+$', iban):  # noqa: E501
            raise ValueError(r"Invalid value for `iban`, must be a follow pattern or equal to `/^[A-Za-z0-9]+$/`")  # noqa: E501

        self._iban = iban

    @property
    def account_number(self):
        """Gets the account_number of this CreatePaymentChannelV3.  # noqa: E501

        Either routing number and account number or only iban must be set  # noqa: E501

        :return: The account_number of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this CreatePaymentChannelV3.

        Either routing number and account number or only iban must be set  # noqa: E501

        :param account_number: The account_number of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """
        if account_number is not None and len(account_number) > 17:
            raise ValueError("Invalid value for `account_number`, length must be less than or equal to `17`")  # noqa: E501
        if account_number is not None and len(account_number) < 6:
            raise ValueError("Invalid value for `account_number`, length must be greater than or equal to `6`")  # noqa: E501

        self._account_number = account_number

    @property
    def routing_number(self):
        """Gets the routing_number of this CreatePaymentChannelV3.  # noqa: E501

        Either routing number and account number or only iban must be set  # noqa: E501

        :return: The routing_number of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._routing_number

    @routing_number.setter
    def routing_number(self, routing_number):
        """Sets the routing_number of this CreatePaymentChannelV3.

        Either routing number and account number or only iban must be set  # noqa: E501

        :param routing_number: The routing_number of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """
        if routing_number is not None and len(routing_number) > 9:
            raise ValueError("Invalid value for `routing_number`, length must be less than or equal to `9`")  # noqa: E501
        if routing_number is not None and len(routing_number) < 9:
            raise ValueError("Invalid value for `routing_number`, length must be greater than or equal to `9`")  # noqa: E501

        self._routing_number = routing_number

    @property
    def country_code(self):
        """Gets the country_code of this CreatePaymentChannelV3.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The country_code of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this CreatePaymentChannelV3.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param country_code: The country_code of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")  # noqa: E501
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")  # noqa: E501
        if country_code is not None and len(country_code) < 2:
            raise ValueError("Invalid value for `country_code`, length must be greater than or equal to `2`")  # noqa: E501
        if country_code is not None and not re.search(r'^[A-Z]{2}$', country_code):  # noqa: E501
            raise ValueError(r"Invalid value for `country_code`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._country_code = country_code

    @property
    def currency(self):
        """Gets the currency of this CreatePaymentChannelV3.  # noqa: E501

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The currency of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreatePaymentChannelV3.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param currency: The currency of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501
        if currency is not None and not re.search(r'^[A-Z]{3}$', currency):  # noqa: E501
            raise ValueError(r"Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Z]{3}$/`")  # noqa: E501

        self._currency = currency

    @property
    def account_name(self):
        """Gets the account_name of this CreatePaymentChannelV3.  # noqa: E501


        :return: The account_name of this CreatePaymentChannelV3.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CreatePaymentChannelV3.


        :param account_name: The account_name of this CreatePaymentChannelV3.  # noqa: E501
        :type: str
        """
        if account_name is None:
            raise ValueError("Invalid value for `account_name`, must not be `None`")  # noqa: E501

        self._account_name = account_name

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
        if not isinstance(other, CreatePaymentChannelV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
