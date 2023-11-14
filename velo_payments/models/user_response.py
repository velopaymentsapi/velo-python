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


class UserResponse(object):
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
        'status': 'str',
        'email': 'str',
        'sms_number': 'str',
        'primary_contact_number': 'str',
        'secondary_contact_number': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'entity_id': 'str',
        'company_name': 'str',
        'roles': 'list[Role]',
        'user_type': 'str',
        'mfa_type': 'str',
        'mfa_status': 'str',
        'locked_out': 'bool',
        'locked_out_timestamp': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'email': 'email',
        'sms_number': 'smsNumber',
        'primary_contact_number': 'primaryContactNumber',
        'secondary_contact_number': 'secondaryContactNumber',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'entity_id': 'entityId',
        'company_name': 'companyName',
        'roles': 'roles',
        'user_type': 'userType',
        'mfa_type': 'mfaType',
        'mfa_status': 'mfaStatus',
        'locked_out': 'lockedOut',
        'locked_out_timestamp': 'lockedOutTimestamp'
    }

    def __init__(self, id=None, status=None, email=None, sms_number=None, primary_contact_number=None, secondary_contact_number=None, first_name=None, last_name=None, entity_id=None, company_name=None, roles=None, user_type=None, mfa_type=None, mfa_status=None, locked_out=None, locked_out_timestamp=None):  # noqa: E501
        """UserResponse - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._status = None
        self._email = None
        self._sms_number = None
        self._primary_contact_number = None
        self._secondary_contact_number = None
        self._first_name = None
        self._last_name = None
        self._entity_id = None
        self._company_name = None
        self._roles = None
        self._user_type = None
        self._mfa_type = None
        self._mfa_status = None
        self._locked_out = None
        self._locked_out_timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if email is not None:
            self.email = email
        if sms_number is not None:
            self.sms_number = sms_number
        if primary_contact_number is not None:
            self.primary_contact_number = primary_contact_number
        if secondary_contact_number is not None:
            self.secondary_contact_number = secondary_contact_number
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if entity_id is not None:
            self.entity_id = entity_id
        if company_name is not None:
            self.company_name = company_name
        if roles is not None:
            self.roles = roles
        if user_type is not None:
            self.user_type = user_type
        if mfa_type is not None:
            self.mfa_type = mfa_type
        if mfa_status is not None:
            self.mfa_status = mfa_status
        if locked_out is not None:
            self.locked_out = locked_out
        self.locked_out_timestamp = locked_out_timestamp

    @property
    def id(self):
        """Gets the id of this UserResponse.  # noqa: E501

        The id of the user  # noqa: E501

        :return: The id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserResponse.

        The id of the user  # noqa: E501

        :param id: The id of this UserResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this UserResponse.  # noqa: E501

        The status of the user when the user has been invited but not yet enrolled they will have a PENDING status   # noqa: E501

        :return: The status of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UserResponse.

        The status of the user when the user has been invited but not yet enrolled they will have a PENDING status   # noqa: E501

        :param status: The status of this UserResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED", "PENDING"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def email(self):
        """Gets the email of this UserResponse.  # noqa: E501

        the email address of the user  # noqa: E501

        :return: The email of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserResponse.

        the email address of the user  # noqa: E501

        :param email: The email of this UserResponse.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def sms_number(self):
        """Gets the sms_number of this UserResponse.  # noqa: E501

        The phone number of a device that the user can receive sms messages on   # noqa: E501

        :return: The sms_number of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._sms_number

    @sms_number.setter
    def sms_number(self, sms_number):
        """Sets the sms_number of this UserResponse.

        The phone number of a device that the user can receive sms messages on   # noqa: E501

        :param sms_number: The sms_number of this UserResponse.  # noqa: E501
        :type: str
        """
        if sms_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', sms_number):  # noqa: E501
            raise ValueError(r"Invalid value for `sms_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")  # noqa: E501

        self._sms_number = sms_number

    @property
    def primary_contact_number(self):
        """Gets the primary_contact_number of this UserResponse.  # noqa: E501

        The main contact number for the user   # noqa: E501

        :return: The primary_contact_number of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._primary_contact_number

    @primary_contact_number.setter
    def primary_contact_number(self, primary_contact_number):
        """Sets the primary_contact_number of this UserResponse.

        The main contact number for the user   # noqa: E501

        :param primary_contact_number: The primary_contact_number of this UserResponse.  # noqa: E501
        :type: str
        """
        if primary_contact_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', primary_contact_number):  # noqa: E501
            raise ValueError(r"Invalid value for `primary_contact_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")  # noqa: E501

        self._primary_contact_number = primary_contact_number

    @property
    def secondary_contact_number(self):
        """Gets the secondary_contact_number of this UserResponse.  # noqa: E501

        The secondary contact number for the user   # noqa: E501

        :return: The secondary_contact_number of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._secondary_contact_number

    @secondary_contact_number.setter
    def secondary_contact_number(self, secondary_contact_number):
        """Sets the secondary_contact_number of this UserResponse.

        The secondary contact number for the user   # noqa: E501

        :param secondary_contact_number: The secondary_contact_number of this UserResponse.  # noqa: E501
        :type: str
        """
        if secondary_contact_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', secondary_contact_number):  # noqa: E501
            raise ValueError(r"Invalid value for `secondary_contact_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")  # noqa: E501

        self._secondary_contact_number = secondary_contact_number

    @property
    def first_name(self):
        """Gets the first_name of this UserResponse.  # noqa: E501


        :return: The first_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserResponse.


        :param first_name: The first_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if first_name is not None and len(first_name) > 128:
            raise ValueError("Invalid value for `first_name`, length must be less than or equal to `128`")  # noqa: E501
        if first_name is not None and len(first_name) < 1:
            raise ValueError("Invalid value for `first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserResponse.  # noqa: E501


        :return: The last_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserResponse.


        :param last_name: The last_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if last_name is not None and len(last_name) > 128:
            raise ValueError("Invalid value for `last_name`, length must be less than or equal to `128`")  # noqa: E501
        if last_name is not None and len(last_name) < 1:
            raise ValueError("Invalid value for `last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._last_name = last_name

    @property
    def entity_id(self):
        """Gets the entity_id of this UserResponse.  # noqa: E501

        The payorId or payeeId or null if the user is not a payor or payee user   # noqa: E501

        :return: The entity_id of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this UserResponse.

        The payorId or payeeId or null if the user is not a payor or payee user   # noqa: E501

        :param entity_id: The entity_id of this UserResponse.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def company_name(self):
        """Gets the company_name of this UserResponse.  # noqa: E501

        The payor or payee company name or null if the user is not a payor or payee user   # noqa: E501

        :return: The company_name of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this UserResponse.

        The payor or payee company name or null if the user is not a payor or payee user   # noqa: E501

        :param company_name: The company_name of this UserResponse.  # noqa: E501
        :type: str
        """
        if company_name is not None and len(company_name) > 128:
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `128`")  # noqa: E501
        if company_name is not None and len(company_name) < 1:
            raise ValueError("Invalid value for `company_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._company_name = company_name

    @property
    def roles(self):
        """Gets the roles of this UserResponse.  # noqa: E501

        The role(s) for the user   # noqa: E501

        :return: The roles of this UserResponse.  # noqa: E501
        :rtype: list[Role]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this UserResponse.

        The role(s) for the user   # noqa: E501

        :param roles: The roles of this UserResponse.  # noqa: E501
        :type: list[Role]
        """

        self._roles = roles

    @property
    def user_type(self):
        """Gets the user_type of this UserResponse.  # noqa: E501

        Indicates the type of user. Could be BACKOFFICE, PAYOR or PAYEE.  # noqa: E501

        :return: The user_type of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this UserResponse.

        Indicates the type of user. Could be BACKOFFICE, PAYOR or PAYEE.  # noqa: E501

        :param user_type: The user_type of this UserResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["BACKOFFICE", "PAYOR", "PAYEE"]  # noqa: E501
        if user_type not in allowed_values:
            raise ValueError(
                "Invalid value for `user_type` ({0}), must be one of {1}"  # noqa: E501
                .format(user_type, allowed_values)
            )

        self._user_type = user_type

    @property
    def mfa_type(self):
        """Gets the mfa_type of this UserResponse.  # noqa: E501

        The type of the MFA device  # noqa: E501

        :return: The mfa_type of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._mfa_type

    @mfa_type.setter
    def mfa_type(self, mfa_type):
        """Sets the mfa_type of this UserResponse.

        The type of the MFA device  # noqa: E501

        :param mfa_type: The mfa_type of this UserResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["SMS", "YUBIKEY", "TOTP"]  # noqa: E501
        if mfa_type not in allowed_values:
            raise ValueError(
                "Invalid value for `mfa_type` ({0}), must be one of {1}"  # noqa: E501
                .format(mfa_type, allowed_values)
            )

        self._mfa_type = mfa_type

    @property
    def mfa_status(self):
        """Gets the mfa_status of this UserResponse.  # noqa: E501

        The status of the MFA device  # noqa: E501

        :return: The mfa_status of this UserResponse.  # noqa: E501
        :rtype: str
        """
        return self._mfa_status

    @mfa_status.setter
    def mfa_status(self, mfa_status):
        """Sets the mfa_status of this UserResponse.

        The status of the MFA device  # noqa: E501

        :param mfa_status: The mfa_status of this UserResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["REGISTERED", "UNREGISTERED", "VERIFIED"]  # noqa: E501
        if mfa_status not in allowed_values:
            raise ValueError(
                "Invalid value for `mfa_status` ({0}), must be one of {1}"  # noqa: E501
                .format(mfa_status, allowed_values)
            )

        self._mfa_status = mfa_status

    @property
    def locked_out(self):
        """Gets the locked_out of this UserResponse.  # noqa: E501

        If true the user is currently locked out and unable to log in  # noqa: E501

        :return: The locked_out of this UserResponse.  # noqa: E501
        :rtype: bool
        """
        return self._locked_out

    @locked_out.setter
    def locked_out(self, locked_out):
        """Sets the locked_out of this UserResponse.

        If true the user is currently locked out and unable to log in  # noqa: E501

        :param locked_out: The locked_out of this UserResponse.  # noqa: E501
        :type: bool
        """

        self._locked_out = locked_out

    @property
    def locked_out_timestamp(self):
        """Gets the locked_out_timestamp of this UserResponse.  # noqa: E501

        A timestamp showing when the user was locked out If null then the user is not currently locked out   # noqa: E501

        :return: The locked_out_timestamp of this UserResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._locked_out_timestamp

    @locked_out_timestamp.setter
    def locked_out_timestamp(self, locked_out_timestamp):
        """Sets the locked_out_timestamp of this UserResponse.

        A timestamp showing when the user was locked out If null then the user is not currently locked out   # noqa: E501

        :param locked_out_timestamp: The locked_out_timestamp of this UserResponse.  # noqa: E501
        :type: datetime
        """

        self._locked_out_timestamp = locked_out_timestamp

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
        if not isinstance(other, UserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
