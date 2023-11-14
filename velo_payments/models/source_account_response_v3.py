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


class SourceAccountResponseV3(object):
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
        'customer_id': 'str',
        'physical_account_id': 'str',
        'notifications': 'NotificationsV3',
        'auto_top_up_config': 'AutoTopUpConfigV3',
        'type': 'str',
        'country': 'str',
        'deleted': 'bool',
        'user_deleted': 'bool',
        'deleted_at': 'datetime',
        'transmission_types': 'list[str]'
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
        'customer_id': 'customerId',
        'physical_account_id': 'physicalAccountId',
        'notifications': 'notifications',
        'auto_top_up_config': 'autoTopUpConfig',
        'type': 'type',
        'country': 'country',
        'deleted': 'deleted',
        'user_deleted': 'userDeleted',
        'deleted_at': 'deletedAt',
        'transmission_types': 'transmissionTypes'
    }

    def __init__(self, id=None, balance=None, currency=None, funding_ref=None, physical_account_name=None, rails_id=None, payor_id=None, name=None, pooled=None, customer_id=None, physical_account_id=None, notifications=None, auto_top_up_config=None, type=None, country=None, deleted=None, user_deleted=None, deleted_at=None, transmission_types=None):  # noqa: E501
        """SourceAccountResponseV3 - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._balance = None
        self._currency = None
        self._funding_ref = None
        self._physical_account_name = None
        self._rails_id = None
        self._payor_id = None
        self._name = None
        self._pooled = None
        self._customer_id = None
        self._physical_account_id = None
        self._notifications = None
        self._auto_top_up_config = None
        self._type = None
        self._country = None
        self._deleted = None
        self._user_deleted = None
        self._deleted_at = None
        self._transmission_types = None
        self.discriminator = None

        self.id = id
        if balance is not None:
            self.balance = balance
        if currency is not None:
            self.currency = currency
        if funding_ref is not None:
            self.funding_ref = funding_ref
        if physical_account_name is not None:
            self.physical_account_name = physical_account_name
        self.rails_id = rails_id
        if payor_id is not None:
            self.payor_id = payor_id
        if name is not None:
            self.name = name
        if pooled is not None:
            self.pooled = pooled
        self.customer_id = customer_id
        if physical_account_id is not None:
            self.physical_account_id = physical_account_id
        if notifications is not None:
            self.notifications = notifications
        if auto_top_up_config is not None:
            self.auto_top_up_config = auto_top_up_config
        self.type = type
        if country is not None:
            self.country = country
        if deleted is not None:
            self.deleted = deleted
        if user_deleted is not None:
            self.user_deleted = user_deleted
        if deleted_at is not None:
            self.deleted_at = deleted_at
        if transmission_types is not None:
            self.transmission_types = transmission_types

    @property
    def id(self):
        """Gets the id of this SourceAccountResponseV3.  # noqa: E501

        Source Account Id  # noqa: E501

        :return: The id of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SourceAccountResponseV3.

        Source Account Id  # noqa: E501

        :param id: The id of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def balance(self):
        """Gets the balance of this SourceAccountResponseV3.  # noqa: E501

        Decimal implied  # noqa: E501

        :return: The balance of this SourceAccountResponseV3.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this SourceAccountResponseV3.

        Decimal implied  # noqa: E501

        :param balance: The balance of this SourceAccountResponseV3.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def currency(self):
        """Gets the currency of this SourceAccountResponseV3.  # noqa: E501

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The currency of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SourceAccountResponseV3.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param currency: The currency of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501
        if currency is not None and not re.search(r'^[A-Z]{3}$', currency):  # noqa: E501
            raise ValueError(r"Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Z]{3}$/`")  # noqa: E501

        self._currency = currency

    @property
    def funding_ref(self):
        """Gets the funding_ref of this SourceAccountResponseV3.  # noqa: E501

        The funding reference (will not be set for DECOUPLED accounts).  # noqa: E501

        :return: The funding_ref of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._funding_ref

    @funding_ref.setter
    def funding_ref(self, funding_ref):
        """Sets the funding_ref of this SourceAccountResponseV3.

        The funding reference (will not be set for DECOUPLED accounts).  # noqa: E501

        :param funding_ref: The funding_ref of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """

        self._funding_ref = funding_ref

    @property
    def physical_account_name(self):
        """Gets the physical_account_name of this SourceAccountResponseV3.  # noqa: E501

        The physical account name (will not be set for DECOUPLED accounts).  # noqa: E501

        :return: The physical_account_name of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._physical_account_name

    @physical_account_name.setter
    def physical_account_name(self, physical_account_name):
        """Sets the physical_account_name of this SourceAccountResponseV3.

        The physical account name (will not be set for DECOUPLED accounts).  # noqa: E501

        :param physical_account_name: The physical_account_name of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """

        self._physical_account_name = physical_account_name

    @property
    def rails_id(self):
        """Gets the rails_id of this SourceAccountResponseV3.  # noqa: E501


        :return: The rails_id of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._rails_id

    @rails_id.setter
    def rails_id(self, rails_id):
        """Sets the rails_id of this SourceAccountResponseV3.


        :param rails_id: The rails_id of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """
        if rails_id is None:
            raise ValueError("Invalid value for `rails_id`, must not be `None`")  # noqa: E501

        self._rails_id = rails_id

    @property
    def payor_id(self):
        """Gets the payor_id of this SourceAccountResponseV3.  # noqa: E501


        :return: The payor_id of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this SourceAccountResponseV3.


        :param payor_id: The payor_id of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """

        self._payor_id = payor_id

    @property
    def name(self):
        """Gets the name of this SourceAccountResponseV3.  # noqa: E501


        :return: The name of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SourceAccountResponseV3.


        :param name: The name of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def pooled(self):
        """Gets the pooled of this SourceAccountResponseV3.  # noqa: E501

        The pooled account flag (will not be set for DECOUPLED accounts).  # noqa: E501

        :return: The pooled of this SourceAccountResponseV3.  # noqa: E501
        :rtype: bool
        """
        return self._pooled

    @pooled.setter
    def pooled(self, pooled):
        """Sets the pooled of this SourceAccountResponseV3.

        The pooled account flag (will not be set for DECOUPLED accounts).  # noqa: E501

        :param pooled: The pooled of this SourceAccountResponseV3.  # noqa: E501
        :type: bool
        """

        self._pooled = pooled

    @property
    def customer_id(self):
        """Gets the customer_id of this SourceAccountResponseV3.  # noqa: E501


        :return: The customer_id of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this SourceAccountResponseV3.


        :param customer_id: The customer_id of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def physical_account_id(self):
        """Gets the physical_account_id of this SourceAccountResponseV3.  # noqa: E501

        The physical account id (will not be set for DECOUPLED accounts).  # noqa: E501

        :return: The physical_account_id of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._physical_account_id

    @physical_account_id.setter
    def physical_account_id(self, physical_account_id):
        """Sets the physical_account_id of this SourceAccountResponseV3.

        The physical account id (will not be set for DECOUPLED accounts).  # noqa: E501

        :param physical_account_id: The physical_account_id of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """

        self._physical_account_id = physical_account_id

    @property
    def notifications(self):
        """Gets the notifications of this SourceAccountResponseV3.  # noqa: E501


        :return: The notifications of this SourceAccountResponseV3.  # noqa: E501
        :rtype: NotificationsV3
        """
        return self._notifications

    @notifications.setter
    def notifications(self, notifications):
        """Sets the notifications of this SourceAccountResponseV3.


        :param notifications: The notifications of this SourceAccountResponseV3.  # noqa: E501
        :type: NotificationsV3
        """

        self._notifications = notifications

    @property
    def auto_top_up_config(self):
        """Gets the auto_top_up_config of this SourceAccountResponseV3.  # noqa: E501


        :return: The auto_top_up_config of this SourceAccountResponseV3.  # noqa: E501
        :rtype: AutoTopUpConfigV3
        """
        return self._auto_top_up_config

    @auto_top_up_config.setter
    def auto_top_up_config(self, auto_top_up_config):
        """Sets the auto_top_up_config of this SourceAccountResponseV3.


        :param auto_top_up_config: The auto_top_up_config of this SourceAccountResponseV3.  # noqa: E501
        :type: AutoTopUpConfigV3
        """

        self._auto_top_up_config = auto_top_up_config

    @property
    def type(self):
        """Gets the type of this SourceAccountResponseV3.  # noqa: E501


        :return: The type of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SourceAccountResponseV3.


        :param type: The type of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def country(self):
        """Gets the country of this SourceAccountResponseV3.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The country of this SourceAccountResponseV3.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SourceAccountResponseV3.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param country: The country of this SourceAccountResponseV3.  # noqa: E501
        :type: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")  # noqa: E501
        if country is not None and len(country) < 2:
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")  # noqa: E501
        if country is not None and not re.search(r'^[A-Z]{2}$', country):  # noqa: E501
            raise ValueError(r"Invalid value for `country`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._country = country

    @property
    def deleted(self):
        """Gets the deleted of this SourceAccountResponseV3.  # noqa: E501

        An optional flag for whether the source account has been deleted. Only present in the response if true.  # noqa: E501

        :return: The deleted of this SourceAccountResponseV3.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this SourceAccountResponseV3.

        An optional flag for whether the source account has been deleted. Only present in the response if true.  # noqa: E501

        :param deleted: The deleted of this SourceAccountResponseV3.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def user_deleted(self):
        """Gets the user_deleted of this SourceAccountResponseV3.  # noqa: E501

        An optional flag for whether the source account has been deleted by a user. Only present in the response if true.  # noqa: E501

        :return: The user_deleted of this SourceAccountResponseV3.  # noqa: E501
        :rtype: bool
        """
        return self._user_deleted

    @user_deleted.setter
    def user_deleted(self, user_deleted):
        """Sets the user_deleted of this SourceAccountResponseV3.

        An optional flag for whether the source account has been deleted by a user. Only present in the response if true.  # noqa: E501

        :param user_deleted: The user_deleted of this SourceAccountResponseV3.  # noqa: E501
        :type: bool
        """

        self._user_deleted = user_deleted

    @property
    def deleted_at(self):
        """Gets the deleted_at of this SourceAccountResponseV3.  # noqa: E501

        An optional timestamp when the source account has been deleted. Only present in the response if deleted.  # noqa: E501

        :return: The deleted_at of this SourceAccountResponseV3.  # noqa: E501
        :rtype: datetime
        """
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, deleted_at):
        """Sets the deleted_at of this SourceAccountResponseV3.

        An optional timestamp when the source account has been deleted. Only present in the response if deleted.  # noqa: E501

        :param deleted_at: The deleted_at of this SourceAccountResponseV3.  # noqa: E501
        :type: datetime
        """

        self._deleted_at = deleted_at

    @property
    def transmission_types(self):
        """Gets the transmission_types of this SourceAccountResponseV3.  # noqa: E501

        List of supported transmission types.  # noqa: E501

        :return: The transmission_types of this SourceAccountResponseV3.  # noqa: E501
        :rtype: list[str]
        """
        return self._transmission_types

    @transmission_types.setter
    def transmission_types(self, transmission_types):
        """Sets the transmission_types of this SourceAccountResponseV3.

        List of supported transmission types.  # noqa: E501

        :param transmission_types: The transmission_types of this SourceAccountResponseV3.  # noqa: E501
        :type: list[str]
        """

        self._transmission_types = transmission_types

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
        if not isinstance(other, SourceAccountResponseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
