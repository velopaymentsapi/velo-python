# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.16.18
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from velo_payments.configuration import Configuration


class GetPayoutsResponseV3Summary(object):
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
        'total_payees_count': 'int',
        'total_invited_count': 'int',
        'total_registered_count': 'int',
        'total_onboarded_count': 'int',
        'total_ofac_failed_count': 'int'
    }

    attribute_map = {
        'total_payees_count': 'totalPayeesCount',
        'total_invited_count': 'totalInvitedCount',
        'total_registered_count': 'totalRegisteredCount',
        'total_onboarded_count': 'totalOnboardedCount',
        'total_ofac_failed_count': 'totalOfacFailedCount'
    }

    def __init__(self, total_payees_count=None, total_invited_count=None, total_registered_count=None, total_onboarded_count=None, total_ofac_failed_count=None, local_vars_configuration=None):  # noqa: E501
        """GetPayoutsResponseV3Summary - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_payees_count = None
        self._total_invited_count = None
        self._total_registered_count = None
        self._total_onboarded_count = None
        self._total_ofac_failed_count = None
        self.discriminator = None

        if total_payees_count is not None:
            self.total_payees_count = total_payees_count
        if total_invited_count is not None:
            self.total_invited_count = total_invited_count
        if total_registered_count is not None:
            self.total_registered_count = total_registered_count
        if total_onboarded_count is not None:
            self.total_onboarded_count = total_onboarded_count
        if total_ofac_failed_count is not None:
            self.total_ofac_failed_count = total_ofac_failed_count

    @property
    def total_payees_count(self):
        """Gets the total_payees_count of this GetPayoutsResponseV3Summary.  # noqa: E501


        :return: The total_payees_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_payees_count

    @total_payees_count.setter
    def total_payees_count(self, total_payees_count):
        """Sets the total_payees_count of this GetPayoutsResponseV3Summary.


        :param total_payees_count: The total_payees_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._total_payees_count = total_payees_count

    @property
    def total_invited_count(self):
        """Gets the total_invited_count of this GetPayoutsResponseV3Summary.  # noqa: E501


        :return: The total_invited_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_invited_count

    @total_invited_count.setter
    def total_invited_count(self, total_invited_count):
        """Sets the total_invited_count of this GetPayoutsResponseV3Summary.


        :param total_invited_count: The total_invited_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._total_invited_count = total_invited_count

    @property
    def total_registered_count(self):
        """Gets the total_registered_count of this GetPayoutsResponseV3Summary.  # noqa: E501


        :return: The total_registered_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_registered_count

    @total_registered_count.setter
    def total_registered_count(self, total_registered_count):
        """Sets the total_registered_count of this GetPayoutsResponseV3Summary.


        :param total_registered_count: The total_registered_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._total_registered_count = total_registered_count

    @property
    def total_onboarded_count(self):
        """Gets the total_onboarded_count of this GetPayoutsResponseV3Summary.  # noqa: E501


        :return: The total_onboarded_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_onboarded_count

    @total_onboarded_count.setter
    def total_onboarded_count(self, total_onboarded_count):
        """Sets the total_onboarded_count of this GetPayoutsResponseV3Summary.


        :param total_onboarded_count: The total_onboarded_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._total_onboarded_count = total_onboarded_count

    @property
    def total_ofac_failed_count(self):
        """Gets the total_ofac_failed_count of this GetPayoutsResponseV3Summary.  # noqa: E501


        :return: The total_ofac_failed_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_ofac_failed_count

    @total_ofac_failed_count.setter
    def total_ofac_failed_count(self, total_ofac_failed_count):
        """Sets the total_ofac_failed_count of this GetPayoutsResponseV3Summary.


        :param total_ofac_failed_count: The total_ofac_failed_count of this GetPayoutsResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._total_ofac_failed_count = total_ofac_failed_count

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
        if not isinstance(other, GetPayoutsResponseV3Summary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetPayoutsResponseV3Summary):
            return True

        return self.to_dict() != other.to_dict()
