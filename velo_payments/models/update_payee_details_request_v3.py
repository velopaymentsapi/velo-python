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


class UpdatePayeeDetailsRequestV3(object):
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
        'address': 'PayeeAddressV3',
        'individual': 'IndividualV3',
        'company': 'CompanyV3',
        'language': 'str',
        'payee_type': 'PayeeTypeEnum',
        'challenge': 'ChallengeV3',
        'email': 'str',
        'contact_sms_number': 'str'
    }

    attribute_map = {
        'address': 'address',
        'individual': 'individual',
        'company': 'company',
        'language': 'language',
        'payee_type': 'payeeType',
        'challenge': 'challenge',
        'email': 'email',
        'contact_sms_number': 'contactSmsNumber'
    }

    def __init__(self, address=None, individual=None, company=None, language=None, payee_type=None, challenge=None, email=None, contact_sms_number=None):  # noqa: E501
        """UpdatePayeeDetailsRequestV3 - a model defined in OpenAPI"""  # noqa: E501

        self._address = None
        self._individual = None
        self._company = None
        self._language = None
        self._payee_type = None
        self._challenge = None
        self._email = None
        self._contact_sms_number = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if individual is not None:
            self.individual = individual
        self.company = company
        if language is not None:
            self.language = language
        if payee_type is not None:
            self.payee_type = payee_type
        if challenge is not None:
            self.challenge = challenge
        self.email = email
        if contact_sms_number is not None:
            self.contact_sms_number = contact_sms_number

    @property
    def address(self):
        """Gets the address of this UpdatePayeeDetailsRequestV3.  # noqa: E501


        :return: The address of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: PayeeAddressV3
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this UpdatePayeeDetailsRequestV3.


        :param address: The address of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: PayeeAddressV3
        """

        self._address = address

    @property
    def individual(self):
        """Gets the individual of this UpdatePayeeDetailsRequestV3.  # noqa: E501


        :return: The individual of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: IndividualV3
        """
        return self._individual

    @individual.setter
    def individual(self, individual):
        """Sets the individual of this UpdatePayeeDetailsRequestV3.


        :param individual: The individual of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: IndividualV3
        """

        self._individual = individual

    @property
    def company(self):
        """Gets the company of this UpdatePayeeDetailsRequestV3.  # noqa: E501


        :return: The company of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: CompanyV3
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this UpdatePayeeDetailsRequestV3.


        :param company: The company of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: CompanyV3
        """

        self._company = company

    @property
    def language(self):
        """Gets the language of this UpdatePayeeDetailsRequestV3.  # noqa: E501

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :return: The language of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this UpdatePayeeDetailsRequestV3.

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :param language: The language of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def payee_type(self):
        """Gets the payee_type of this UpdatePayeeDetailsRequestV3.  # noqa: E501


        :return: The payee_type of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: PayeeTypeEnum
        """
        return self._payee_type

    @payee_type.setter
    def payee_type(self, payee_type):
        """Sets the payee_type of this UpdatePayeeDetailsRequestV3.


        :param payee_type: The payee_type of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: PayeeTypeEnum
        """

        self._payee_type = payee_type

    @property
    def challenge(self):
        """Gets the challenge of this UpdatePayeeDetailsRequestV3.  # noqa: E501


        :return: The challenge of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: ChallengeV3
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this UpdatePayeeDetailsRequestV3.


        :param challenge: The challenge of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: ChallengeV3
        """

        self._challenge = challenge

    @property
    def email(self):
        """Gets the email of this UpdatePayeeDetailsRequestV3.  # noqa: E501


        :return: The email of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UpdatePayeeDetailsRequestV3.


        :param email: The email of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def contact_sms_number(self):
        """Gets the contact_sms_number of this UpdatePayeeDetailsRequestV3.  # noqa: E501

        The phone number of a device that the payee wishes to receive sms messages on   # noqa: E501

        :return: The contact_sms_number of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._contact_sms_number

    @contact_sms_number.setter
    def contact_sms_number(self, contact_sms_number):
        """Sets the contact_sms_number of this UpdatePayeeDetailsRequestV3.

        The phone number of a device that the payee wishes to receive sms messages on   # noqa: E501

        :param contact_sms_number: The contact_sms_number of this UpdatePayeeDetailsRequestV3.  # noqa: E501
        :type: str
        """
        if contact_sms_number is not None and not re.search(r'^\+[1-9]\d{1,14}$', contact_sms_number):  # noqa: E501
            raise ValueError(r"Invalid value for `contact_sms_number`, must be a follow pattern or equal to `/^\+[1-9]\d{1,14}$/`")  # noqa: E501

        self._contact_sms_number = contact_sms_number

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
        if not isinstance(other, UpdatePayeeDetailsRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
