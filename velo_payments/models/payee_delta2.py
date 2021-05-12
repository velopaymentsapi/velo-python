# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.26.127
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PayeeDelta2(object):
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
        'payee_id': 'str',
        'display_name': 'str',
        'dba_name': 'str',
        'email': 'str',
        'payee_country': 'str',
        'onboarded_status': 'OnboardedStatus2'
    }

    attribute_map = {
        'remote_id': 'remoteId',
        'payee_id': 'payeeId',
        'display_name': 'displayName',
        'dba_name': 'dbaName',
        'email': 'email',
        'payee_country': 'payeeCountry',
        'onboarded_status': 'onboardedStatus'
    }

    def __init__(self, remote_id=None, payee_id=None, display_name=None, dba_name=None, email=None, payee_country=None, onboarded_status=None):  # noqa: E501
        """PayeeDelta2 - a model defined in OpenAPI"""  # noqa: E501

        self._remote_id = None
        self._payee_id = None
        self._display_name = None
        self._dba_name = None
        self._email = None
        self._payee_country = None
        self._onboarded_status = None
        self.discriminator = None

        self.remote_id = remote_id
        self.payee_id = payee_id
        if display_name is not None:
            self.display_name = display_name
        if dba_name is not None:
            self.dba_name = dba_name
        self.email = email
        if payee_country is not None:
            self.payee_country = payee_country
        if onboarded_status is not None:
            self.onboarded_status = onboarded_status

    @property
    def remote_id(self):
        """Gets the remote_id of this PayeeDelta2.  # noqa: E501


        :return: The remote_id of this PayeeDelta2.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this PayeeDelta2.


        :param remote_id: The remote_id of this PayeeDelta2.  # noqa: E501
        :type: str
        """
        if remote_id is None:
            raise ValueError("Invalid value for `remote_id`, must not be `None`")  # noqa: E501
        if remote_id is not None and len(remote_id) > 100:
            raise ValueError("Invalid value for `remote_id`, length must be less than or equal to `100`")  # noqa: E501
        if remote_id is not None and len(remote_id) < 1:
            raise ValueError("Invalid value for `remote_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._remote_id = remote_id

    @property
    def payee_id(self):
        """Gets the payee_id of this PayeeDelta2.  # noqa: E501


        :return: The payee_id of this PayeeDelta2.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PayeeDelta2.


        :param payee_id: The payee_id of this PayeeDelta2.  # noqa: E501
        :type: str
        """
        if payee_id is None:
            raise ValueError("Invalid value for `payee_id`, must not be `None`")  # noqa: E501

        self._payee_id = payee_id

    @property
    def display_name(self):
        """Gets the display_name of this PayeeDelta2.  # noqa: E501


        :return: The display_name of this PayeeDelta2.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PayeeDelta2.


        :param display_name: The display_name of this PayeeDelta2.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def dba_name(self):
        """Gets the dba_name of this PayeeDelta2.  # noqa: E501


        :return: The dba_name of this PayeeDelta2.  # noqa: E501
        :rtype: str
        """
        return self._dba_name

    @dba_name.setter
    def dba_name(self, dba_name):
        """Sets the dba_name of this PayeeDelta2.


        :param dba_name: The dba_name of this PayeeDelta2.  # noqa: E501
        :type: str
        """

        self._dba_name = dba_name

    @property
    def email(self):
        """Gets the email of this PayeeDelta2.  # noqa: E501


        :return: The email of this PayeeDelta2.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayeeDelta2.


        :param email: The email of this PayeeDelta2.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def payee_country(self):
        """Gets the payee_country of this PayeeDelta2.  # noqa: E501


        :return: The payee_country of this PayeeDelta2.  # noqa: E501
        :rtype: str
        """
        return self._payee_country

    @payee_country.setter
    def payee_country(self, payee_country):
        """Sets the payee_country of this PayeeDelta2.


        :param payee_country: The payee_country of this PayeeDelta2.  # noqa: E501
        :type: str
        """

        self._payee_country = payee_country

    @property
    def onboarded_status(self):
        """Gets the onboarded_status of this PayeeDelta2.  # noqa: E501


        :return: The onboarded_status of this PayeeDelta2.  # noqa: E501
        :rtype: OnboardedStatus2
        """
        return self._onboarded_status

    @onboarded_status.setter
    def onboarded_status(self, onboarded_status):
        """Sets the onboarded_status of this PayeeDelta2.


        :param onboarded_status: The onboarded_status of this PayeeDelta2.  # noqa: E501
        :type: OnboardedStatus2
        """

        self._onboarded_status = onboarded_status

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
        if not isinstance(other, PayeeDelta2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
