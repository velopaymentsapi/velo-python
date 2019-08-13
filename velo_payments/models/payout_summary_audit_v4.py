# coding: utf-8

"""
    Velo Payments APIs

    ## Terms and Definitions  Throughout this document and the Velo platform the following terms are used:  * **Payor.** An entity (typically a corporation) which wishes to pay funds to one or more payees via a payout. * **Payee.** The recipient of funds paid out by a payor. * **Payment.** A single transfer of funds from a payor to a payee. * **Payout.** A batch of Payments, typically used by a payor to logically group payments (e.g. by business day). Technically there need be no relationship between the payments in a payout - a single payout can contain payments to multiple payees and/or multiple payments to a single payee. * **Sandbox.** An integration environment provided by Velo Payments which offers a similar API experience to the production environment, but all funding and payment events are simulated, along with many other services such as OFAC sanctions list checking.  ## Overview  The Velo Payments API allows a payor to perform a number of operations. The following is a list of the main capabilities in a natural order of execution:  * Authenticate with the Velo platform * Maintain a collection of payees * Query the payor’s current balance of funds within the platform and perform additional funding * Issue payments to payees * Query the platform for a history of those payments  This document describes the main concepts and APIs required to get up and running with the Velo Payments platform. It is not an exhaustive API reference. For that, please see the separate Velo Payments API Reference.  ## API Considerations  The Velo Payments API is REST based and uses the JSON format for requests and responses.  Most calls are secured using OAuth 2 security and require a valid authentication access token for successful operation. See the Authentication section for details.  Where a dynamic value is required in the examples below, the {token} format is used, suggesting that the caller needs to supply the appropriate value of the token in question (without including the { or } characters).  Where curl examples are given, the –d @filename.json approach is used, indicating that the request body should be placed into a file named filename.json in the current directory. Each of the curl examples in this document should be considered a single line on the command-line, regardless of how they appear in print.  ## Authenticating with the Velo Platform  Once Velo backoffice staff have added your organization as a payor within the Velo platform sandbox, they will create you a payor Id, an API key and an API secret and share these with you in a secure manner.  You will need to use these values to authenticate with the Velo platform in order to gain access to the APIs. The steps to take are explained in the following:  create a string comprising the API key (e.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8) and API secret (e.g. c396b26b-137a-44fd-87f5-34631f8fd529) with a colon between them. E.g. 44a9537d-d55d-4b47-8082-14061c2bcdd8:c396b26b-137a-44fd-87f5-34631f8fd529  base64 encode this string. E.g.: NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  create an HTTP **Authorization** header with the value set to e.g. Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==  perform the Velo authentication REST call using the HTTP header created above e.g. via curl:  ```   curl -X POST \\   -H \"Content-Type: application/json\" \\   -H \"Authorization: Basic NDRhOTUzN2QtZDU1ZC00YjQ3LTgwODItMTQwNjFjMmJjZGQ4OmMzOTZiMjZiLTEzN2EtNDRmZC04N2Y1LTM0NjMxZjhmZDUyOQ==\" \\   'https://api.sandbox.velopayments.com/v1/authenticate?grant_type=client_credentials' ```  If successful, this call will result in a **200** HTTP status code and a response body such as:  ```   {     \"access_token\":\"19f6bafd-93fd-4747-b229-00507bbc991f\",     \"token_type\":\"bearer\",     \"expires_in\":1799,     \"scope\":\"...\"   } ``` ## API access following authentication Following successful authentication, the value of the access_token field in the response (indicated in green above) should then be presented with all subsequent API calls to allow the Velo platform to validate that the caller is authenticated.  This is achieved by setting the HTTP Authorization header with the value set to e.g. Bearer 19f6bafd-93fd-4747-b229-00507bbc991f such as the curl example below:  ```   -H \"Authorization: Bearer 19f6bafd-93fd-4747-b229-00507bbc991f \" ```  If you make other Velo API calls which require authorization but the Authorization header is missing or invalid then you will get a **401** HTTP status response.   # noqa: E501

    The version of the OpenAPI document: 2.14.94
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PayoutSummaryAuditV4(object):
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
        'payor_id': 'str',
        'status': 'PayoutStatusV4',
        'date_time': 'datetime',
        'submitted_date_time': 'str',
        'instructed_date_time': 'str',
        'withdrawn_date_time': 'str',
        'total_payments': 'int',
        'total_incomplete_payments': 'int',
        'total_returned_payments': 'int',
        'source_account_summary': 'list[SourceAccountSummaryV4]',
        'fx_summaries': 'list[FxSummaryV4]',
        'payout_memo': 'str'
    }

    attribute_map = {
        'payout_id': 'payoutId',
        'payor_id': 'payorId',
        'status': 'status',
        'date_time': 'dateTime',
        'submitted_date_time': 'submittedDateTime',
        'instructed_date_time': 'instructedDateTime',
        'withdrawn_date_time': 'withdrawnDateTime',
        'total_payments': 'totalPayments',
        'total_incomplete_payments': 'totalIncompletePayments',
        'total_returned_payments': 'totalReturnedPayments',
        'source_account_summary': 'sourceAccountSummary',
        'fx_summaries': 'fxSummaries',
        'payout_memo': 'payoutMemo'
    }

    def __init__(self, payout_id=None, payor_id=None, status=None, date_time=None, submitted_date_time=None, instructed_date_time=None, withdrawn_date_time=None, total_payments=None, total_incomplete_payments=None, total_returned_payments=None, source_account_summary=None, fx_summaries=None, payout_memo=None):  # noqa: E501
        """PayoutSummaryAuditV4 - a model defined in OpenAPI"""  # noqa: E501

        self._payout_id = None
        self._payor_id = None
        self._status = None
        self._date_time = None
        self._submitted_date_time = None
        self._instructed_date_time = None
        self._withdrawn_date_time = None
        self._total_payments = None
        self._total_incomplete_payments = None
        self._total_returned_payments = None
        self._source_account_summary = None
        self._fx_summaries = None
        self._payout_memo = None
        self.discriminator = None

        self.payout_id = payout_id
        if payor_id is not None:
            self.payor_id = payor_id
        self.status = status
        if date_time is not None:
            self.date_time = date_time
        self.submitted_date_time = submitted_date_time
        if instructed_date_time is not None:
            self.instructed_date_time = instructed_date_time
        if withdrawn_date_time is not None:
            self.withdrawn_date_time = withdrawn_date_time
        if total_payments is not None:
            self.total_payments = total_payments
        if total_incomplete_payments is not None:
            self.total_incomplete_payments = total_incomplete_payments
        if total_returned_payments is not None:
            self.total_returned_payments = total_returned_payments
        if source_account_summary is not None:
            self.source_account_summary = source_account_summary
        if fx_summaries is not None:
            self.fx_summaries = fx_summaries
        if payout_memo is not None:
            self.payout_memo = payout_memo

    @property
    def payout_id(self):
        """Gets the payout_id of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The payout_id of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: str
        """
        return self._payout_id

    @payout_id.setter
    def payout_id(self, payout_id):
        """Sets the payout_id of this PayoutSummaryAuditV4.


        :param payout_id: The payout_id of this PayoutSummaryAuditV4.  # noqa: E501
        :type: str
        """
        if payout_id is None:
            raise ValueError("Invalid value for `payout_id`, must not be `None`")  # noqa: E501

        self._payout_id = payout_id

    @property
    def payor_id(self):
        """Gets the payor_id of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The payor_id of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this PayoutSummaryAuditV4.


        :param payor_id: The payor_id of this PayoutSummaryAuditV4.  # noqa: E501
        :type: str
        """

        self._payor_id = payor_id

    @property
    def status(self):
        """Gets the status of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The status of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: PayoutStatusV4
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PayoutSummaryAuditV4.


        :param status: The status of this PayoutSummaryAuditV4.  # noqa: E501
        :type: PayoutStatusV4
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def date_time(self):
        """Gets the date_time of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        """Sets the date_time of this PayoutSummaryAuditV4.


        :param date_time: The date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :type: datetime
        """

        self._date_time = date_time

    @property
    def submitted_date_time(self):
        """Gets the submitted_date_time of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The submitted_date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: str
        """
        return self._submitted_date_time

    @submitted_date_time.setter
    def submitted_date_time(self, submitted_date_time):
        """Sets the submitted_date_time of this PayoutSummaryAuditV4.


        :param submitted_date_time: The submitted_date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :type: str
        """
        if submitted_date_time is None:
            raise ValueError("Invalid value for `submitted_date_time`, must not be `None`")  # noqa: E501

        self._submitted_date_time = submitted_date_time

    @property
    def instructed_date_time(self):
        """Gets the instructed_date_time of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The instructed_date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: str
        """
        return self._instructed_date_time

    @instructed_date_time.setter
    def instructed_date_time(self, instructed_date_time):
        """Sets the instructed_date_time of this PayoutSummaryAuditV4.


        :param instructed_date_time: The instructed_date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :type: str
        """

        self._instructed_date_time = instructed_date_time

    @property
    def withdrawn_date_time(self):
        """Gets the withdrawn_date_time of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The withdrawn_date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: str
        """
        return self._withdrawn_date_time

    @withdrawn_date_time.setter
    def withdrawn_date_time(self, withdrawn_date_time):
        """Sets the withdrawn_date_time of this PayoutSummaryAuditV4.


        :param withdrawn_date_time: The withdrawn_date_time of this PayoutSummaryAuditV4.  # noqa: E501
        :type: str
        """

        self._withdrawn_date_time = withdrawn_date_time

    @property
    def total_payments(self):
        """Gets the total_payments of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The total_payments of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: int
        """
        return self._total_payments

    @total_payments.setter
    def total_payments(self, total_payments):
        """Sets the total_payments of this PayoutSummaryAuditV4.


        :param total_payments: The total_payments of this PayoutSummaryAuditV4.  # noqa: E501
        :type: int
        """

        self._total_payments = total_payments

    @property
    def total_incomplete_payments(self):
        """Gets the total_incomplete_payments of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The total_incomplete_payments of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: int
        """
        return self._total_incomplete_payments

    @total_incomplete_payments.setter
    def total_incomplete_payments(self, total_incomplete_payments):
        """Sets the total_incomplete_payments of this PayoutSummaryAuditV4.


        :param total_incomplete_payments: The total_incomplete_payments of this PayoutSummaryAuditV4.  # noqa: E501
        :type: int
        """

        self._total_incomplete_payments = total_incomplete_payments

    @property
    def total_returned_payments(self):
        """Gets the total_returned_payments of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The total_returned_payments of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: int
        """
        return self._total_returned_payments

    @total_returned_payments.setter
    def total_returned_payments(self, total_returned_payments):
        """Sets the total_returned_payments of this PayoutSummaryAuditV4.


        :param total_returned_payments: The total_returned_payments of this PayoutSummaryAuditV4.  # noqa: E501
        :type: int
        """

        self._total_returned_payments = total_returned_payments

    @property
    def source_account_summary(self):
        """Gets the source_account_summary of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The source_account_summary of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: list[SourceAccountSummaryV4]
        """
        return self._source_account_summary

    @source_account_summary.setter
    def source_account_summary(self, source_account_summary):
        """Sets the source_account_summary of this PayoutSummaryAuditV4.


        :param source_account_summary: The source_account_summary of this PayoutSummaryAuditV4.  # noqa: E501
        :type: list[SourceAccountSummaryV4]
        """

        self._source_account_summary = source_account_summary

    @property
    def fx_summaries(self):
        """Gets the fx_summaries of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The fx_summaries of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: list[FxSummaryV4]
        """
        return self._fx_summaries

    @fx_summaries.setter
    def fx_summaries(self, fx_summaries):
        """Sets the fx_summaries of this PayoutSummaryAuditV4.


        :param fx_summaries: The fx_summaries of this PayoutSummaryAuditV4.  # noqa: E501
        :type: list[FxSummaryV4]
        """

        self._fx_summaries = fx_summaries

    @property
    def payout_memo(self):
        """Gets the payout_memo of this PayoutSummaryAuditV4.  # noqa: E501


        :return: The payout_memo of this PayoutSummaryAuditV4.  # noqa: E501
        :rtype: str
        """
        return self._payout_memo

    @payout_memo.setter
    def payout_memo(self, payout_memo):
        """Sets the payout_memo of this PayoutSummaryAuditV4.


        :param payout_memo: The payout_memo of this PayoutSummaryAuditV4.  # noqa: E501
        :type: str
        """

        self._payout_memo = payout_memo

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
        if not isinstance(other, PayoutSummaryAuditV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
