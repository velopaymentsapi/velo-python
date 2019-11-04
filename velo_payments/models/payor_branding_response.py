# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.15.16
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from velo_payments.configuration import Configuration


class PayorBrandingResponse(object):
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
        'payor_name': 'str',
        'logo_url': 'str',
        'collective_alias': 'str',
        'support_contact': 'str',
        'dba_name': 'str'
    }

    attribute_map = {
        'payor_name': 'payorName',
        'logo_url': 'logoUrl',
        'collective_alias': 'collectiveAlias',
        'support_contact': 'supportContact',
        'dba_name': 'dbaName'
    }

    def __init__(self, payor_name=None, logo_url=None, collective_alias=None, support_contact=None, dba_name=None, local_vars_configuration=None):  # noqa: E501
        """PayorBrandingResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payor_name = None
        self._logo_url = None
        self._collective_alias = None
        self._support_contact = None
        self._dba_name = None
        self.discriminator = None

        self.payor_name = payor_name
        self.logo_url = logo_url
        self.collective_alias = collective_alias
        self.support_contact = support_contact
        self.dba_name = dba_name

    @property
    def payor_name(self):
        """Gets the payor_name of this PayorBrandingResponse.  # noqa: E501

        The name of the payor  # noqa: E501

        :return: The payor_name of this PayorBrandingResponse.  # noqa: E501
        :rtype: str
        """
        return self._payor_name

    @payor_name.setter
    def payor_name(self, payor_name):
        """Sets the payor_name of this PayorBrandingResponse.

        The name of the payor  # noqa: E501

        :param payor_name: The payor_name of this PayorBrandingResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and payor_name is None:  # noqa: E501
            raise ValueError("Invalid value for `payor_name`, must not be `None`")  # noqa: E501

        self._payor_name = payor_name

    @property
    def logo_url(self):
        """Gets the logo_url of this PayorBrandingResponse.  # noqa: E501

        The URL to use for this payor’s logo  # noqa: E501

        :return: The logo_url of this PayorBrandingResponse.  # noqa: E501
        :rtype: str
        """
        return self._logo_url

    @logo_url.setter
    def logo_url(self, logo_url):
        """Sets the logo_url of this PayorBrandingResponse.

        The URL to use for this payor’s logo  # noqa: E501

        :param logo_url: The logo_url of this PayorBrandingResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and logo_url is None:  # noqa: E501
            raise ValueError("Invalid value for `logo_url`, must not be `None`")  # noqa: E501

        self._logo_url = logo_url

    @property
    def collective_alias(self):
        """Gets the collective_alias of this PayorBrandingResponse.  # noqa: E501

        How the payor has chosen to refer to payees  # noqa: E501

        :return: The collective_alias of this PayorBrandingResponse.  # noqa: E501
        :rtype: str
        """
        return self._collective_alias

    @collective_alias.setter
    def collective_alias(self, collective_alias):
        """Sets the collective_alias of this PayorBrandingResponse.

        How the payor has chosen to refer to payees  # noqa: E501

        :param collective_alias: The collective_alias of this PayorBrandingResponse.  # noqa: E501
        :type: str
        """

        self._collective_alias = collective_alias

    @property
    def support_contact(self):
        """Gets the support_contact of this PayorBrandingResponse.  # noqa: E501

        The payor’s support contact address  # noqa: E501

        :return: The support_contact of this PayorBrandingResponse.  # noqa: E501
        :rtype: str
        """
        return self._support_contact

    @support_contact.setter
    def support_contact(self, support_contact):
        """Sets the support_contact of this PayorBrandingResponse.

        The payor’s support contact address  # noqa: E501

        :param support_contact: The support_contact of this PayorBrandingResponse.  # noqa: E501
        :type: str
        """

        self._support_contact = support_contact

    @property
    def dba_name(self):
        """Gets the dba_name of this PayorBrandingResponse.  # noqa: E501

        The payor’s 'Doing Business As' name  # noqa: E501

        :return: The dba_name of this PayorBrandingResponse.  # noqa: E501
        :rtype: str
        """
        return self._dba_name

    @dba_name.setter
    def dba_name(self, dba_name):
        """Sets the dba_name of this PayorBrandingResponse.

        The payor’s 'Doing Business As' name  # noqa: E501

        :param dba_name: The dba_name of this PayorBrandingResponse.  # noqa: E501
        :type: str
        """

        self._dba_name = dba_name

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
        if not isinstance(other, PayorBrandingResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PayorBrandingResponse):
            return True

        return self.to_dict() != other.to_dict()
