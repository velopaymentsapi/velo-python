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


class SourceAccountResponseV2(object):
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
        'id': 'str',
        'balance': 'int',
        'currency': 'str',
        'funding_ref': 'str',
        'physical_account_name': 'str',
        'rails_id': 'str',
        'payor_id': 'str',
        'name': 'str',
        'pooled': 'bool',
        'balance_visible': 'bool',
        'customer_id': 'str',
        'physical_account_id': 'str',
        'notifications': 'Notifications',
        'funding_account_id': 'str',
        'auto_top_up_config': 'AutoTopUpConfig',
        'account_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'balance': 'balance',
        'currency': 'currency',
        'funding_ref': 'fundingRef',
        'physical_account_name': 'physicalAccountName',
        'rails_id': 'railsId',
        'payor_id': 'payorId',
        'name': 'name',
        'pooled': 'pooled',
        'balance_visible': 'balanceVisible',
        'customer_id': 'customerId',
        'physical_account_id': 'physicalAccountId',
        'notifications': 'notifications',
        'funding_account_id': 'fundingAccountId',
        'auto_top_up_config': 'autoTopUpConfig',
        'account_type': 'accountType'
    }

    def __init__(self, id=None, balance=None, currency=None, funding_ref=None, physical_account_name=None, rails_id=None, payor_id=None, name=None, pooled=None, balance_visible=None, customer_id=None, physical_account_id=None, notifications=None, funding_account_id=None, auto_top_up_config=None, account_type=None):  # noqa: E501
        """SourceAccountResponseV2 - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._balance = None
        self._currency = None
        self._funding_ref = None
        self._physical_account_name = None
        self._rails_id = None
        self._payor_id = None
        self._name = None
        self._pooled = None
        self._balance_visible = None
        self._customer_id = None
        self._physical_account_id = None
        self._notifications = None
        self._funding_account_id = None
        self._auto_top_up_config = None
        self._account_type = None
        self.discriminator = None

        self.id = id
        if balance is not None:
            self.balance = balance
        if currency is not None:
            self.currency = currency
        self.funding_ref = funding_ref
        self.physical_account_name = physical_account_name
        self.rails_id = rails_id
        if payor_id is not None:
            self.payor_id = payor_id
        if name is not None:
            self.name = name
        self.pooled = pooled
        self.balance_visible = balance_visible
        self.customer_id = customer_id
        if physical_account_id is not None:
            self.physical_account_id = physical_account_id
        if notifications is not None:
            self.notifications = notifications
        self.funding_account_id = funding_account_id
        if auto_top_up_config is not None:
            self.auto_top_up_config = auto_top_up_config
        self.account_type = account_type

    @property
    def id(self):
        """Gets the id of this SourceAccountResponseV2.  # noqa: E501

        Source Account Id  # noqa: E501

        :return: The id of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceAccountResponseV2.

        Source Account Id  # noqa: E501

        :param id: The id of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def balance(self):
        """Gets the balance of this SourceAccountResponseV2.  # noqa: E501

        Decimal implied  # noqa: E501

        :return: The balance of this SourceAccountResponseV2.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SourceAccountResponseV2.

        Decimal implied  # noqa: E501

        :param balance: The balance of this SourceAccountResponseV2.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def currency(self):
        """Gets the currency of this SourceAccountResponseV2.  # noqa: E501


        :return: The currency of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SourceAccountResponseV2.


        :param currency: The currency of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """
        allowed_values = ["USD"]  # noqa: E501
        if currency not in allowed_values:
            raise ValueError(
                "Invalid value for `currency` ({0}), must be one of {1}"  # noqa: E501
                .format(currency, allowed_values)
            )

        self._currency = currency

    @property
    def funding_ref(self):
        """Gets the funding_ref of this SourceAccountResponseV2.  # noqa: E501


        :return: The funding_ref of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._funding_ref

    @funding_ref.setter
    def funding_ref(self, funding_ref):
        """Sets the funding_ref of this SourceAccountResponseV2.


        :param funding_ref: The funding_ref of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """
        if funding_ref is None:
            raise ValueError("Invalid value for `funding_ref`, must not be `None`")  # noqa: E501

        self._funding_ref = funding_ref

    @property
    def physical_account_name(self):
        """Gets the physical_account_name of this SourceAccountResponseV2.  # noqa: E501


        :return: The physical_account_name of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._physical_account_name

    @physical_account_name.setter
    def physical_account_name(self, physical_account_name):
        """Sets the physical_account_name of this SourceAccountResponseV2.


        :param physical_account_name: The physical_account_name of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """
        if physical_account_name is None:
            raise ValueError("Invalid value for `physical_account_name`, must not be `None`")  # noqa: E501

        self._physical_account_name = physical_account_name

    @property
    def rails_id(self):
        """Gets the rails_id of this SourceAccountResponseV2.  # noqa: E501


        :return: The rails_id of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._rails_id

    @rails_id.setter
    def rails_id(self, rails_id):
        """Sets the rails_id of this SourceAccountResponseV2.


        :param rails_id: The rails_id of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """
        if rails_id is None:
            raise ValueError("Invalid value for `rails_id`, must not be `None`")  # noqa: E501

        self._rails_id = rails_id

    @property
    def payor_id(self):
        """Gets the payor_id of this SourceAccountResponseV2.  # noqa: E501


        :return: The payor_id of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this SourceAccountResponseV2.


        :param payor_id: The payor_id of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """

        self._payor_id = payor_id

    @property
    def name(self):
        """Gets the name of this SourceAccountResponseV2.  # noqa: E501


        :return: The name of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceAccountResponseV2.


        :param name: The name of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pooled(self):
        """Gets the pooled of this SourceAccountResponseV2.  # noqa: E501


        :return: The pooled of this SourceAccountResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._pooled

    @pooled.setter
    def pooled(self, pooled):
        """Sets the pooled of this SourceAccountResponseV2.


        :param pooled: The pooled of this SourceAccountResponseV2.  # noqa: E501
        :type: bool
        """
        if pooled is None:
            raise ValueError("Invalid value for `pooled`, must not be `None`")  # noqa: E501

        self._pooled = pooled

    @property
    def balance_visible(self):
        """Gets the balance_visible of this SourceAccountResponseV2.  # noqa: E501


        :return: The balance_visible of this SourceAccountResponseV2.  # noqa: E501
        :rtype: bool
        """
        return self._balance_visible

    @balance_visible.setter
    def balance_visible(self, balance_visible):
        """Sets the balance_visible of this SourceAccountResponseV2.


        :param balance_visible: The balance_visible of this SourceAccountResponseV2.  # noqa: E501
        :type: bool
        """
        if balance_visible is None:
            raise ValueError("Invalid value for `balance_visible`, must not be `None`")  # noqa: E501

        self._balance_visible = balance_visible

    @property
    def customer_id(self):
        """Gets the customer_id of this SourceAccountResponseV2.  # noqa: E501


        :return: The customer_id of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SourceAccountResponseV2.


        :param customer_id: The customer_id of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def physical_account_id(self):
        """Gets the physical_account_id of this SourceAccountResponseV2.  # noqa: E501


        :return: The physical_account_id of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._physical_account_id

    @physical_account_id.setter
    def physical_account_id(self, physical_account_id):
        """Sets the physical_account_id of this SourceAccountResponseV2.


        :param physical_account_id: The physical_account_id of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """

        self._physical_account_id = physical_account_id

    @property
    def notifications(self):
        """Gets the notifications of this SourceAccountResponseV2.  # noqa: E501


        :return: The notifications of this SourceAccountResponseV2.  # noqa: E501
        :rtype: Notifications
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this SourceAccountResponseV2.


        :param notifications: The notifications of this SourceAccountResponseV2.  # noqa: E501
        :type: Notifications
        """

        self._notifications = notifications

    @property
    def funding_account_id(self):
        """Gets the funding_account_id of this SourceAccountResponseV2.  # noqa: E501


        :return: The funding_account_id of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._funding_account_id

    @funding_account_id.setter
    def funding_account_id(self, funding_account_id):
        """Sets the funding_account_id of this SourceAccountResponseV2.


        :param funding_account_id: The funding_account_id of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """

        self._funding_account_id = funding_account_id

    @property
    def auto_top_up_config(self):
        """Gets the auto_top_up_config of this SourceAccountResponseV2.  # noqa: E501


        :return: The auto_top_up_config of this SourceAccountResponseV2.  # noqa: E501
        :rtype: AutoTopUpConfig
        """
        return self._auto_top_up_config

    @auto_top_up_config.setter
    def auto_top_up_config(self, auto_top_up_config):
        """Sets the auto_top_up_config of this SourceAccountResponseV2.


        :param auto_top_up_config: The auto_top_up_config of this SourceAccountResponseV2.  # noqa: E501
        :type: AutoTopUpConfig
        """

        self._auto_top_up_config = auto_top_up_config

    @property
    def account_type(self):
        """Gets the account_type of this SourceAccountResponseV2.  # noqa: E501


        :return: The account_type of this SourceAccountResponseV2.  # noqa: E501
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """Sets the account_type of this SourceAccountResponseV2.


        :param account_type: The account_type of this SourceAccountResponseV2.  # noqa: E501
        :type: str
        """
        if account_type is None:
            raise ValueError("Invalid value for `account_type`, must not be `None`")  # noqa: E501

        self._account_type = account_type

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
        if not isinstance(other, SourceAccountResponseV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
