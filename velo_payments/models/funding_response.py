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


class FundingResponse(object):
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
        'funding_id': 'str',
        'payor_id': 'str',
        'created_at': 'datetime',
        'detected_funding_ref': 'str',
        'amount': 'int',
        'currency': 'str',
        'text': 'str',
        'physical_account_name': 'str',
        'source_account_id': 'str',
        'allocation_type': 'str',
        'allocated_at': 'datetime',
        'allocation_date': 'datetime',
        'reason': 'str',
        'hidden_date': 'datetime',
        'funding_account_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'funding_id': 'fundingId',
        'payor_id': 'payorId',
        'created_at': 'createdAt',
        'detected_funding_ref': 'detectedFundingRef',
        'amount': 'amount',
        'currency': 'currency',
        'text': 'text',
        'physical_account_name': 'physicalAccountName',
        'source_account_id': 'sourceAccountId',
        'allocation_type': 'allocationType',
        'allocated_at': 'allocatedAt',
        'allocation_date': 'allocationDate',
        'reason': 'reason',
        'hidden_date': 'hiddenDate',
        'funding_account_type': 'fundingAccountType',
        'status': 'status'
    }

    def __init__(self, funding_id=None, payor_id=None, created_at=None, detected_funding_ref=None, amount=None, currency=None, text=None, physical_account_name=None, source_account_id=None, allocation_type=None, allocated_at=None, allocation_date=None, reason=None, hidden_date=None, funding_account_type=None, status=None):  # noqa: E501
        """FundingResponse - a model defined in OpenAPI"""  # noqa: E501

        self._funding_id = None
        self._payor_id = None
        self._created_at = None
        self._detected_funding_ref = None
        self._amount = None
        self._currency = None
        self._text = None
        self._physical_account_name = None
        self._source_account_id = None
        self._allocation_type = None
        self._allocated_at = None
        self._allocation_date = None
        self._reason = None
        self._hidden_date = None
        self._funding_account_type = None
        self._status = None
        self.discriminator = None

        self.funding_id = funding_id
        self.payor_id = payor_id
        self.created_at = created_at
        if detected_funding_ref is not None:
            self.detected_funding_ref = detected_funding_ref
        self.amount = amount
        self.currency = currency
        if text is not None:
            self.text = text
        if physical_account_name is not None:
            self.physical_account_name = physical_account_name
        if source_account_id is not None:
            self.source_account_id = source_account_id
        if allocation_type is not None:
            self.allocation_type = allocation_type
        if allocated_at is not None:
            self.allocated_at = allocated_at
        if allocation_date is not None:
            self.allocation_date = allocation_date
        if reason is not None:
            self.reason = reason
        if hidden_date is not None:
            self.hidden_date = hidden_date
        self.funding_account_type = funding_account_type
        self.status = status

    @property
    def funding_id(self):
        """Gets the funding_id of this FundingResponse.  # noqa: E501


        :return: The funding_id of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._funding_id

    @funding_id.setter
    def funding_id(self, funding_id):
        """Sets the funding_id of this FundingResponse.


        :param funding_id: The funding_id of this FundingResponse.  # noqa: E501
        :type: str
        """
        if funding_id is None:
            raise ValueError("Invalid value for `funding_id`, must not be `None`")  # noqa: E501

        self._funding_id = funding_id

    @property
    def payor_id(self):
        """Gets the payor_id of this FundingResponse.  # noqa: E501


        :return: The payor_id of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this FundingResponse.


        :param payor_id: The payor_id of this FundingResponse.  # noqa: E501
        :type: str
        """
        if payor_id is None:
            raise ValueError("Invalid value for `payor_id`, must not be `None`")  # noqa: E501

        self._payor_id = payor_id

    @property
    def created_at(self):
        """Gets the created_at of this FundingResponse.  # noqa: E501

        The date and time the funding was created  # noqa: E501

        :return: The created_at of this FundingResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FundingResponse.

        The date and time the funding was created  # noqa: E501

        :param created_at: The created_at of this FundingResponse.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def detected_funding_ref(self):
        """Gets the detected_funding_ref of this FundingResponse.  # noqa: E501


        :return: The detected_funding_ref of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._detected_funding_ref

    @detected_funding_ref.setter
    def detected_funding_ref(self, detected_funding_ref):
        """Sets the detected_funding_ref of this FundingResponse.


        :param detected_funding_ref: The detected_funding_ref of this FundingResponse.  # noqa: E501
        :type: str
        """

        self._detected_funding_ref = detected_funding_ref

    @property
    def amount(self):
        """Gets the amount of this FundingResponse.  # noqa: E501


        :return: The amount of this FundingResponse.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this FundingResponse.


        :param amount: The amount of this FundingResponse.  # noqa: E501
        :type: int
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def currency(self):
        """Gets the currency of this FundingResponse.  # noqa: E501

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The currency of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this FundingResponse.

        Valid ISO 4217 3 letter currency code. See the <a href=\"https://www.iso.org/iso-4217-currency-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param currency: The currency of this FundingResponse.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if currency is not None and len(currency) > 3:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `3`")  # noqa: E501
        if currency is not None and len(currency) < 3:
            raise ValueError("Invalid value for `currency`, length must be greater than or equal to `3`")  # noqa: E501
        if currency is not None and not re.search(r'^[A-Z]{3}$', currency):  # noqa: E501
            raise ValueError(r"Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Z]{3}$/`")  # noqa: E501

        self._currency = currency

    @property
    def text(self):
        """Gets the text of this FundingResponse.  # noqa: E501


        :return: The text of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FundingResponse.


        :param text: The text of this FundingResponse.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def physical_account_name(self):
        """Gets the physical_account_name of this FundingResponse.  # noqa: E501


        :return: The physical_account_name of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._physical_account_name

    @physical_account_name.setter
    def physical_account_name(self, physical_account_name):
        """Sets the physical_account_name of this FundingResponse.


        :param physical_account_name: The physical_account_name of this FundingResponse.  # noqa: E501
        :type: str
        """

        self._physical_account_name = physical_account_name

    @property
    def source_account_id(self):
        """Gets the source_account_id of this FundingResponse.  # noqa: E501


        :return: The source_account_id of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._source_account_id

    @source_account_id.setter
    def source_account_id(self, source_account_id):
        """Sets the source_account_id of this FundingResponse.


        :param source_account_id: The source_account_id of this FundingResponse.  # noqa: E501
        :type: str
        """

        self._source_account_id = source_account_id

    @property
    def allocation_type(self):
        """Gets the allocation_type of this FundingResponse.  # noqa: E501

        Funding Allocation Type. One of the following values: AUTOMATIC, MANUAL  # noqa: E501

        :return: The allocation_type of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._allocation_type

    @allocation_type.setter
    def allocation_type(self, allocation_type):
        """Sets the allocation_type of this FundingResponse.

        Funding Allocation Type. One of the following values: AUTOMATIC, MANUAL  # noqa: E501

        :param allocation_type: The allocation_type of this FundingResponse.  # noqa: E501
        :type: str
        """

        self._allocation_type = allocation_type

    @property
    def allocated_at(self):
        """Gets the allocated_at of this FundingResponse.  # noqa: E501

        Populated only if the funding has been allocated. The date and time the funding was allocated.  # noqa: E501

        :return: The allocated_at of this FundingResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._allocated_at

    @allocated_at.setter
    def allocated_at(self, allocated_at):
        """Sets the allocated_at of this FundingResponse.

        Populated only if the funding has been allocated. The date and time the funding was allocated.  # noqa: E501

        :param allocated_at: The allocated_at of this FundingResponse.  # noqa: E501
        :type: datetime
        """

        self._allocated_at = allocated_at

    @property
    def allocation_date(self):
        """Gets the allocation_date of this FundingResponse.  # noqa: E501

        Populated with allocatedAt if allocated otherwise createdAt. Deprecated in v2.36 - will be removed in the future.  # noqa: E501

        :return: The allocation_date of this FundingResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._allocation_date

    @allocation_date.setter
    def allocation_date(self, allocation_date):
        """Sets the allocation_date of this FundingResponse.

        Populated with allocatedAt if allocated otherwise createdAt. Deprecated in v2.36 - will be removed in the future.  # noqa: E501

        :param allocation_date: The allocation_date of this FundingResponse.  # noqa: E501
        :type: datetime
        """

        self._allocation_date = allocation_date

    @property
    def reason(self):
        """Gets the reason of this FundingResponse.  # noqa: E501


        :return: The reason of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this FundingResponse.


        :param reason: The reason of this FundingResponse.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def hidden_date(self):
        """Gets the hidden_date of this FundingResponse.  # noqa: E501


        :return: The hidden_date of this FundingResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._hidden_date

    @hidden_date.setter
    def hidden_date(self, hidden_date):
        """Sets the hidden_date of this FundingResponse.


        :param hidden_date: The hidden_date of this FundingResponse.  # noqa: E501
        :type: datetime
        """

        self._hidden_date = hidden_date

    @property
    def funding_account_type(self):
        """Gets the funding_account_type of this FundingResponse.  # noqa: E501

        Funding Account Type. One of the following values: FBO, PRIVATE  # noqa: E501

        :return: The funding_account_type of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._funding_account_type

    @funding_account_type.setter
    def funding_account_type(self, funding_account_type):
        """Sets the funding_account_type of this FundingResponse.

        Funding Account Type. One of the following values: FBO, PRIVATE  # noqa: E501

        :param funding_account_type: The funding_account_type of this FundingResponse.  # noqa: E501
        :type: str
        """
        if funding_account_type is None:
            raise ValueError("Invalid value for `funding_account_type`, must not be `None`")  # noqa: E501

        self._funding_account_type = funding_account_type

    @property
    def status(self):
        """Gets the status of this FundingResponse.  # noqa: E501

        Current status of the funding. One of the follwing values: PENDING, UNALLOCATED, ALLOCATED, HIDDEN, RETURNED, RETURNING, BULK_RETURN, OTHER  # noqa: E501

        :return: The status of this FundingResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this FundingResponse.

        Current status of the funding. One of the follwing values: PENDING, UNALLOCATED, ALLOCATED, HIDDEN, RETURNED, RETURNING, BULK_RETURN, OTHER  # noqa: E501

        :param status: The status of this FundingResponse.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, FundingResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
