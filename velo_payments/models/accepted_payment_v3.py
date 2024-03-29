# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.26.124
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class AcceptedPaymentV3(object):
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
        'remote_id': 'str',
        'currency_type': 'str',
        'amount': 'int',
        'source_account_name': 'str',
        'payor_payment_id': 'str',
        'payment_memo': 'str',
        'remote_system_id': 'str',
        'payment_metadata': 'str'
    }

    attribute_map = {
        'remote_id': 'remoteId',
        'currency_type': 'currencyType',
        'amount': 'amount',
        'source_account_name': 'sourceAccountName',
        'payor_payment_id': 'payorPaymentId',
        'payment_memo': 'paymentMemo',
        'remote_system_id': 'remoteSystemId',
        'payment_metadata': 'paymentMetadata'
    }

    def __init__(self, remote_id=None, currency_type=None, amount=None, source_account_name=None, payor_payment_id=None, payment_memo=None, remote_system_id=None, payment_metadata=None):  # noqa: E501
        """AcceptedPaymentV3 - a model defined in OpenAPI"""  # noqa: E501

        self._remote_id = None
        self._currency_type = None
        self._amount = None
        self._source_account_name = None
        self._payor_payment_id = None
        self._payment_memo = None
        self._remote_system_id = None
        self._payment_metadata = None
        self.discriminator = None

        self.remote_id = remote_id
        self.currency_type = currency_type
        self.amount = amount
        self.source_account_name = source_account_name
        self.payor_payment_id = payor_payment_id
        if payment_memo is not None:
            self.payment_memo = payment_memo
        if remote_system_id is not None:
            self.remote_system_id = remote_system_id
        if payment_metadata is not None:
            self.payment_metadata = payment_metadata

    @property
    def remote_id(self):
        """Gets the remote_id of this AcceptedPaymentV3.  # noqa: E501


        :return: The remote_id of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this AcceptedPaymentV3.


        :param remote_id: The remote_id of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """
        if remote_id is None:
            raise ValueError("Invalid value for `remote_id`, must not be `None`")  # noqa: E501

        self._remote_id = remote_id

    @property
    def currency_type(self):
        """Gets the currency_type of this AcceptedPaymentV3.  # noqa: E501

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The currency_type of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._currency_type

    @currency_type.setter
    def currency_type(self, currency_type):
        """Sets the currency_type of this AcceptedPaymentV3.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param currency_type: The currency_type of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """
        if currency_type is None:
            raise ValueError("Invalid value for `currency_type`, must not be `None`")  # noqa: E501
        if currency_type is not None and len(currency_type) > 3:
            raise ValueError("Invalid value for `currency_type`, length must be less than or equal to `3`")  # noqa: E501
        if currency_type is not None and len(currency_type) < 3:
            raise ValueError("Invalid value for `currency_type`, length must be greater than or equal to `3`")  # noqa: E501
        if currency_type is not None and not re.search(r'^[A-Z]{3}$', currency_type):  # noqa: E501
            raise ValueError(r"Invalid value for `currency_type`, must be a follow pattern or equal to `/^[A-Z]{3}$/`")  # noqa: E501

        self._currency_type = currency_type

    @property
    def amount(self):
        """Gets the amount of this AcceptedPaymentV3.  # noqa: E501


        :return: The amount of this AcceptedPaymentV3.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this AcceptedPaymentV3.


        :param amount: The amount of this AcceptedPaymentV3.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def source_account_name(self):
        """Gets the source_account_name of this AcceptedPaymentV3.  # noqa: E501


        :return: The source_account_name of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._source_account_name

    @source_account_name.setter
    def source_account_name(self, source_account_name):
        """Sets the source_account_name of this AcceptedPaymentV3.


        :param source_account_name: The source_account_name of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """
        if source_account_name is None:
            raise ValueError("Invalid value for `source_account_name`, must not be `None`")  # noqa: E501

        self._source_account_name = source_account_name

    @property
    def payor_payment_id(self):
        """Gets the payor_payment_id of this AcceptedPaymentV3.  # noqa: E501


        :return: The payor_payment_id of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._payor_payment_id

    @payor_payment_id.setter
    def payor_payment_id(self, payor_payment_id):
        """Sets the payor_payment_id of this AcceptedPaymentV3.


        :param payor_payment_id: The payor_payment_id of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """
        if payor_payment_id is None:
            raise ValueError("Invalid value for `payor_payment_id`, must not be `None`")  # noqa: E501

        self._payor_payment_id = payor_payment_id

    @property
    def payment_memo(self):
        """Gets the payment_memo of this AcceptedPaymentV3.  # noqa: E501


        :return: The payment_memo of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_memo

    @payment_memo.setter
    def payment_memo(self, payment_memo):
        """Sets the payment_memo of this AcceptedPaymentV3.


        :param payment_memo: The payment_memo of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """

        self._payment_memo = payment_memo

    @property
    def remote_system_id(self):
        """Gets the remote_system_id of this AcceptedPaymentV3.  # noqa: E501


        :return: The remote_system_id of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._remote_system_id

    @remote_system_id.setter
    def remote_system_id(self, remote_system_id):
        """Sets the remote_system_id of this AcceptedPaymentV3.


        :param remote_system_id: The remote_system_id of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """

        self._remote_system_id = remote_system_id

    @property
    def payment_metadata(self):
        """Gets the payment_metadata of this AcceptedPaymentV3.  # noqa: E501


        :return: The payment_metadata of this AcceptedPaymentV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_metadata

    @payment_metadata.setter
    def payment_metadata(self, payment_metadata):
        """Sets the payment_metadata of this AcceptedPaymentV3.


        :param payment_metadata: The payment_metadata of this AcceptedPaymentV3.  # noqa: E501
        :type: str
        """

        self._payment_metadata = payment_metadata

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
        if not isinstance(other, AcceptedPaymentV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
