# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.22.122
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from velo_payments.configuration import Configuration


class CreatePayee(object):
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
        'payee_id': 'str',
        'payor_refs': 'list[PayeePayorRefV2]',
        'email': 'str',
        'remote_id': 'str',
        'type': 'PayeeType',
        'address': 'CreatePayeeAddress',
        'payment_channel': 'CreatePaymentChannel',
        'challenge': 'Challenge',
        'language': 'Language',
        'company': 'CompanyV1',
        'individual': 'CreateIndividual'
    }

    attribute_map = {
        'payee_id': 'payeeId',
        'payor_refs': 'payorRefs',
        'email': 'email',
        'remote_id': 'remoteId',
        'type': 'type',
        'address': 'address',
        'payment_channel': 'paymentChannel',
        'challenge': 'challenge',
        'language': 'language',
        'company': 'company',
        'individual': 'individual'
    }

    def __init__(self, payee_id=None, payor_refs=None, email=None, remote_id=None, type=None, address=None, payment_channel=None, challenge=None, language=None, company=None, individual=None, local_vars_configuration=None):  # noqa: E501
        """CreatePayee - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payee_id = None
        self._payor_refs = None
        self._email = None
        self._remote_id = None
        self._type = None
        self._address = None
        self._payment_channel = None
        self._challenge = None
        self._language = None
        self._company = None
        self._individual = None
        self.discriminator = None

        if payee_id is not None:
            self.payee_id = payee_id
        self.payor_refs = payor_refs
        self.email = email
        self.remote_id = remote_id
        self.type = type
        self.address = address
        if payment_channel is not None:
            self.payment_channel = payment_channel
        if challenge is not None:
            self.challenge = challenge
        if language is not None:
            self.language = language
        self.company = company
        if individual is not None:
            self.individual = individual

    @property
    def payee_id(self):
        """Gets the payee_id of this CreatePayee.  # noqa: E501


        :return: The payee_id of this CreatePayee.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this CreatePayee.


        :param payee_id: The payee_id of this CreatePayee.  # noqa: E501
        :type payee_id: str
        """

        self._payee_id = payee_id

    @property
    def payor_refs(self):
        """Gets the payor_refs of this CreatePayee.  # noqa: E501


        :return: The payor_refs of this CreatePayee.  # noqa: E501
        :rtype: list[PayeePayorRefV2]
        """
        return self._payor_refs

    @payor_refs.setter
    def payor_refs(self, payor_refs):
        """Sets the payor_refs of this CreatePayee.


        :param payor_refs: The payor_refs of this CreatePayee.  # noqa: E501
        :type payor_refs: list[PayeePayorRefV2]
        """

        self._payor_refs = payor_refs

    @property
    def email(self):
        """Gets the email of this CreatePayee.  # noqa: E501


        :return: The email of this CreatePayee.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreatePayee.


        :param email: The email of this CreatePayee.  # noqa: E501
        :type email: str
        """
        if self.local_vars_configuration.client_side_validation and email is None:  # noqa: E501
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) > 255):
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                email is not None and len(email) < 3):
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `3`")  # noqa: E501

        self._email = email

    @property
    def remote_id(self):
        """Gets the remote_id of this CreatePayee.  # noqa: E501


        :return: The remote_id of this CreatePayee.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this CreatePayee.


        :param remote_id: The remote_id of this CreatePayee.  # noqa: E501
        :type remote_id: str
        """
        if self.local_vars_configuration.client_side_validation and remote_id is None:  # noqa: E501
            raise ValueError("Invalid value for `remote_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                remote_id is not None and len(remote_id) > 100):
            raise ValueError("Invalid value for `remote_id`, length must be less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                remote_id is not None and len(remote_id) < 1):
            raise ValueError("Invalid value for `remote_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._remote_id = remote_id

    @property
    def type(self):
        """Gets the type of this CreatePayee.  # noqa: E501


        :return: The type of this CreatePayee.  # noqa: E501
        :rtype: PayeeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePayee.


        :param type: The type of this CreatePayee.  # noqa: E501
        :type type: PayeeType
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def address(self):
        """Gets the address of this CreatePayee.  # noqa: E501


        :return: The address of this CreatePayee.  # noqa: E501
        :rtype: CreatePayeeAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreatePayee.


        :param address: The address of this CreatePayee.  # noqa: E501
        :type address: CreatePayeeAddress
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def payment_channel(self):
        """Gets the payment_channel of this CreatePayee.  # noqa: E501


        :return: The payment_channel of this CreatePayee.  # noqa: E501
        :rtype: CreatePaymentChannel
        """
        return self._payment_channel

    @payment_channel.setter
    def payment_channel(self, payment_channel):
        """Sets the payment_channel of this CreatePayee.


        :param payment_channel: The payment_channel of this CreatePayee.  # noqa: E501
        :type payment_channel: CreatePaymentChannel
        """

        self._payment_channel = payment_channel

    @property
    def challenge(self):
        """Gets the challenge of this CreatePayee.  # noqa: E501


        :return: The challenge of this CreatePayee.  # noqa: E501
        :rtype: Challenge
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this CreatePayee.


        :param challenge: The challenge of this CreatePayee.  # noqa: E501
        :type challenge: Challenge
        """

        self._challenge = challenge

    @property
    def language(self):
        """Gets the language of this CreatePayee.  # noqa: E501


        :return: The language of this CreatePayee.  # noqa: E501
        :rtype: Language
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreatePayee.


        :param language: The language of this CreatePayee.  # noqa: E501
        :type language: Language
        """

        self._language = language

    @property
    def company(self):
        """Gets the company of this CreatePayee.  # noqa: E501


        :return: The company of this CreatePayee.  # noqa: E501
        :rtype: CompanyV1
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CreatePayee.


        :param company: The company of this CreatePayee.  # noqa: E501
        :type company: CompanyV1
        """

        self._company = company

    @property
    def individual(self):
        """Gets the individual of this CreatePayee.  # noqa: E501


        :return: The individual of this CreatePayee.  # noqa: E501
        :rtype: CreateIndividual
        """
        return self._individual

    @individual.setter
    def individual(self, individual):
        """Sets the individual of this CreatePayee.


        :param individual: The individual of this CreatePayee.  # noqa: E501
        :type individual: CreateIndividual
        """

        self._individual = individual

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
        if not isinstance(other, CreatePayee):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatePayee):
            return True

        return self.to_dict() != other.to_dict()
