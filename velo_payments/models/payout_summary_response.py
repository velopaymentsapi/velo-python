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


class PayoutSummaryResponse(object):
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
        'payout_id': 'str',
        'status': 'str',
        'payments_submitted': 'int',
        'payments_accepted': 'int',
        'payments_rejected': 'int',
        'fx_summaries': 'list[QuoteFxSummary]',
        'accounts': 'list[SourceAccount]',
        'rejected_payments': 'list[RejectedPayment]'
    }

    attribute_map = {
        'payout_id': 'payoutId',
        'status': 'status',
        'payments_submitted': 'paymentsSubmitted',
        'payments_accepted': 'paymentsAccepted',
        'payments_rejected': 'paymentsRejected',
        'fx_summaries': 'fxSummaries',
        'accounts': 'accounts',
        'rejected_payments': 'rejectedPayments'
    }

    def __init__(self, payout_id=None, status=None, payments_submitted=None, payments_accepted=None, payments_rejected=None, fx_summaries=None, accounts=None, rejected_payments=None, local_vars_configuration=None):  # noqa: E501
        """PayoutSummaryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payout_id = None
        self._status = None
        self._payments_submitted = None
        self._payments_accepted = None
        self._payments_rejected = None
        self._fx_summaries = None
        self._accounts = None
        self._rejected_payments = None
        self.discriminator = None

        if payout_id is not None:
            self.payout_id = payout_id
        if status is not None:
            self.status = status
        if payments_submitted is not None:
            self.payments_submitted = payments_submitted
        if payments_accepted is not None:
            self.payments_accepted = payments_accepted
        if payments_rejected is not None:
            self.payments_rejected = payments_rejected
        self.fx_summaries = fx_summaries
        self.accounts = accounts
        self.rejected_payments = rejected_payments

    @property
    def payout_id(self):
        """Gets the payout_id of this PayoutSummaryResponse.  # noqa: E501


        :return: The payout_id of this PayoutSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._payout_id

    @payout_id.setter
    def payout_id(self, payout_id):
        """Sets the payout_id of this PayoutSummaryResponse.


        :param payout_id: The payout_id of this PayoutSummaryResponse.  # noqa: E501
        :type: str
        """

        self._payout_id = payout_id

    @property
    def status(self):
        """Gets the status of this PayoutSummaryResponse.  # noqa: E501


        :return: The status of this PayoutSummaryResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PayoutSummaryResponse.


        :param status: The status of this PayoutSummaryResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def payments_submitted(self):
        """Gets the payments_submitted of this PayoutSummaryResponse.  # noqa: E501


        :return: The payments_submitted of this PayoutSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._payments_submitted

    @payments_submitted.setter
    def payments_submitted(self, payments_submitted):
        """Sets the payments_submitted of this PayoutSummaryResponse.


        :param payments_submitted: The payments_submitted of this PayoutSummaryResponse.  # noqa: E501
        :type: int
        """

        self._payments_submitted = payments_submitted

    @property
    def payments_accepted(self):
        """Gets the payments_accepted of this PayoutSummaryResponse.  # noqa: E501


        :return: The payments_accepted of this PayoutSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._payments_accepted

    @payments_accepted.setter
    def payments_accepted(self, payments_accepted):
        """Sets the payments_accepted of this PayoutSummaryResponse.


        :param payments_accepted: The payments_accepted of this PayoutSummaryResponse.  # noqa: E501
        :type: int
        """

        self._payments_accepted = payments_accepted

    @property
    def payments_rejected(self):
        """Gets the payments_rejected of this PayoutSummaryResponse.  # noqa: E501


        :return: The payments_rejected of this PayoutSummaryResponse.  # noqa: E501
        :rtype: int
        """
        return self._payments_rejected

    @payments_rejected.setter
    def payments_rejected(self, payments_rejected):
        """Sets the payments_rejected of this PayoutSummaryResponse.


        :param payments_rejected: The payments_rejected of this PayoutSummaryResponse.  # noqa: E501
        :type: int
        """

        self._payments_rejected = payments_rejected

    @property
    def fx_summaries(self):
        """Gets the fx_summaries of this PayoutSummaryResponse.  # noqa: E501


        :return: The fx_summaries of this PayoutSummaryResponse.  # noqa: E501
        :rtype: list[QuoteFxSummary]
        """
        return self._fx_summaries

    @fx_summaries.setter
    def fx_summaries(self, fx_summaries):
        """Sets the fx_summaries of this PayoutSummaryResponse.


        :param fx_summaries: The fx_summaries of this PayoutSummaryResponse.  # noqa: E501
        :type: list[QuoteFxSummary]
        """
        if self.local_vars_configuration.client_side_validation and fx_summaries is None:  # noqa: E501
            raise ValueError("Invalid value for `fx_summaries`, must not be `None`")  # noqa: E501

        self._fx_summaries = fx_summaries

    @property
    def accounts(self):
        """Gets the accounts of this PayoutSummaryResponse.  # noqa: E501


        :return: The accounts of this PayoutSummaryResponse.  # noqa: E501
        :rtype: list[SourceAccount]
        """
        return self._accounts

    @accounts.setter
    def accounts(self, accounts):
        """Sets the accounts of this PayoutSummaryResponse.


        :param accounts: The accounts of this PayoutSummaryResponse.  # noqa: E501
        :type: list[SourceAccount]
        """
        if self.local_vars_configuration.client_side_validation and accounts is None:  # noqa: E501
            raise ValueError("Invalid value for `accounts`, must not be `None`")  # noqa: E501

        self._accounts = accounts

    @property
    def rejected_payments(self):
        """Gets the rejected_payments of this PayoutSummaryResponse.  # noqa: E501


        :return: The rejected_payments of this PayoutSummaryResponse.  # noqa: E501
        :rtype: list[RejectedPayment]
        """
        return self._rejected_payments

    @rejected_payments.setter
    def rejected_payments(self, rejected_payments):
        """Sets the rejected_payments of this PayoutSummaryResponse.


        :param rejected_payments: The rejected_payments of this PayoutSummaryResponse.  # noqa: E501
        :type: list[RejectedPayment]
        """
        if self.local_vars_configuration.client_side_validation and rejected_payments is None:  # noqa: E501
            raise ValueError("Invalid value for `rejected_payments`, must not be `None`")  # noqa: E501

        self._rejected_payments = rejected_payments

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
        if not isinstance(other, PayoutSummaryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PayoutSummaryResponse):
            return True

        return self.to_dict() != other.to_dict()
