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


class GetPaymentsForPayoutResponseV3Summary(object):
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
        'payout_status': 'str',
        'submitted_date_time': 'datetime',
        'instructed_date_time': 'datetime',
        'withdrawn_date_time': 'datetime',
        'payout_memo': 'str',
        'total_payments': 'int',
        'confirmed_payments': 'int',
        'released_payments': 'int',
        'incomplete_payments': 'int',
        'failed_payments': 'int'
    }

    attribute_map = {
        'payout_status': 'payoutStatus',
        'submitted_date_time': 'submittedDateTime',
        'instructed_date_time': 'instructedDateTime',
        'withdrawn_date_time': 'withdrawnDateTime',
        'payout_memo': 'payoutMemo',
        'total_payments': 'totalPayments',
        'confirmed_payments': 'confirmedPayments',
        'released_payments': 'releasedPayments',
        'incomplete_payments': 'incompletePayments',
        'failed_payments': 'failedPayments'
    }

    def __init__(self, payout_status=None, submitted_date_time=None, instructed_date_time=None, withdrawn_date_time=None, payout_memo=None, total_payments=None, confirmed_payments=None, released_payments=None, incomplete_payments=None, failed_payments=None):  # noqa: E501
        """GetPaymentsForPayoutResponseV3Summary - a model defined in OpenAPI"""  # noqa: E501

        self._payout_status = None
        self._submitted_date_time = None
        self._instructed_date_time = None
        self._withdrawn_date_time = None
        self._payout_memo = None
        self._total_payments = None
        self._confirmed_payments = None
        self._released_payments = None
        self._incomplete_payments = None
        self._failed_payments = None
        self.discriminator = None

        if payout_status is not None:
            self.payout_status = payout_status
        if submitted_date_time is not None:
            self.submitted_date_time = submitted_date_time
        if instructed_date_time is not None:
            self.instructed_date_time = instructed_date_time
        if withdrawn_date_time is not None:
            self.withdrawn_date_time = withdrawn_date_time
        if payout_memo is not None:
            self.payout_memo = payout_memo
        if total_payments is not None:
            self.total_payments = total_payments
        if confirmed_payments is not None:
            self.confirmed_payments = confirmed_payments
        if released_payments is not None:
            self.released_payments = released_payments
        if incomplete_payments is not None:
            self.incomplete_payments = incomplete_payments
        if failed_payments is not None:
            self.failed_payments = failed_payments

    @property
    def payout_status(self):
        """Gets the payout_status of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The current status of the payout.  # noqa: E501

        :return: The payout_status of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: str
        """
        return self._payout_status

    @payout_status.setter
    def payout_status(self, payout_status):
        """Sets the payout_status of this GetPaymentsForPayoutResponseV3Summary.

        The current status of the payout.  # noqa: E501

        :param payout_status: The payout_status of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCEPTED", "REJECTED", "SUBMITTED", "QUOTED", "INSTRUCTED", "COMPLETED", "INCOMPLETE", "CONFIRMED", "WITHDRAWN"]  # noqa: E501
        if payout_status not in allowed_values:
            raise ValueError(
                "Invalid value for `payout_status` ({0}), must be one of {1}"  # noqa: E501
                .format(payout_status, allowed_values)
            )

        self._payout_status = payout_status

    @property
    def submitted_date_time(self):
        """Gets the submitted_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The date/time at which the payout was submitted.  # noqa: E501

        :return: The submitted_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: datetime
        """
        return self._submitted_date_time

    @submitted_date_time.setter
    def submitted_date_time(self, submitted_date_time):
        """Sets the submitted_date_time of this GetPaymentsForPayoutResponseV3Summary.

        The date/time at which the payout was submitted.  # noqa: E501

        :param submitted_date_time: The submitted_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: datetime
        """

        self._submitted_date_time = submitted_date_time

    @property
    def instructed_date_time(self):
        """Gets the instructed_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The date/time at which the payout was instructed.  # noqa: E501

        :return: The instructed_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: datetime
        """
        return self._instructed_date_time

    @instructed_date_time.setter
    def instructed_date_time(self, instructed_date_time):
        """Sets the instructed_date_time of this GetPaymentsForPayoutResponseV3Summary.

        The date/time at which the payout was instructed.  # noqa: E501

        :param instructed_date_time: The instructed_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: datetime
        """

        self._instructed_date_time = instructed_date_time

    @property
    def withdrawn_date_time(self):
        """Gets the withdrawn_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The date/time at which the payout was withdrawn.  # noqa: E501

        :return: The withdrawn_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: datetime
        """
        return self._withdrawn_date_time

    @withdrawn_date_time.setter
    def withdrawn_date_time(self, withdrawn_date_time):
        """Sets the withdrawn_date_time of this GetPaymentsForPayoutResponseV3Summary.

        The date/time at which the payout was withdrawn.  # noqa: E501

        :param withdrawn_date_time: The withdrawn_date_time of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: datetime
        """

        self._withdrawn_date_time = withdrawn_date_time

    @property
    def payout_memo(self):
        """Gets the payout_memo of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The memo attached to the payout.  # noqa: E501

        :return: The payout_memo of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: str
        """
        return self._payout_memo

    @payout_memo.setter
    def payout_memo(self, payout_memo):
        """Sets the payout_memo of this GetPaymentsForPayoutResponseV3Summary.

        The memo attached to the payout.  # noqa: E501

        :param payout_memo: The payout_memo of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: str
        """

        self._payout_memo = payout_memo

    @property
    def total_payments(self):
        """Gets the total_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The count of payments within the payout.  # noqa: E501

        :return: The total_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._total_payments

    @total_payments.setter
    def total_payments(self, total_payments):
        """Sets the total_payments of this GetPaymentsForPayoutResponseV3Summary.

        The count of payments within the payout.  # noqa: E501

        :param total_payments: The total_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._total_payments = total_payments

    @property
    def confirmed_payments(self):
        """Gets the confirmed_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The count of payments within the payout which have been confirmed.  # noqa: E501

        :return: The confirmed_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._confirmed_payments

    @confirmed_payments.setter
    def confirmed_payments(self, confirmed_payments):
        """Sets the confirmed_payments of this GetPaymentsForPayoutResponseV3Summary.

        The count of payments within the payout which have been confirmed.  # noqa: E501

        :param confirmed_payments: The confirmed_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._confirmed_payments = confirmed_payments

    @property
    def released_payments(self):
        """Gets the released_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The count of payments within the payout which have been released.  # noqa: E501

        :return: The released_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._released_payments

    @released_payments.setter
    def released_payments(self, released_payments):
        """Sets the released_payments of this GetPaymentsForPayoutResponseV3Summary.

        The count of payments within the payout which have been released.  # noqa: E501

        :param released_payments: The released_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._released_payments = released_payments

    @property
    def incomplete_payments(self):
        """Gets the incomplete_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The count of payments within the payout which are incomplete.  # noqa: E501

        :return: The incomplete_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._incomplete_payments

    @incomplete_payments.setter
    def incomplete_payments(self, incomplete_payments):
        """Sets the incomplete_payments of this GetPaymentsForPayoutResponseV3Summary.

        The count of payments within the payout which are incomplete.  # noqa: E501

        :param incomplete_payments: The incomplete_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._incomplete_payments = incomplete_payments

    @property
    def failed_payments(self):
        """Gets the failed_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501

        The count of payments within the payout which have failed or been returned.  # noqa: E501

        :return: The failed_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :rtype: int
        """
        return self._failed_payments

    @failed_payments.setter
    def failed_payments(self, failed_payments):
        """Sets the failed_payments of this GetPaymentsForPayoutResponseV3Summary.

        The count of payments within the payout which have failed or been returned.  # noqa: E501

        :param failed_payments: The failed_payments of this GetPaymentsForPayoutResponseV3Summary.  # noqa: E501
        :type: int
        """

        self._failed_payments = failed_payments

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
        if not isinstance(other, GetPaymentsForPayoutResponseV3Summary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
