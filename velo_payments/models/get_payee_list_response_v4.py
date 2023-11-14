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


class GetPayeeListResponseV4(object):
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
        'payor_refs': 'list[PayeePayorRefV4]',
        'email': 'str',
        'onboarded_status': 'str',
        'watchlist_status': 'str',
        'watchlist_status_updated_timestamp': 'str',
        'watchlist_override_comment': 'str',
        'language': 'str',
        'created': 'datetime',
        'country': 'str',
        'display_name': 'str',
        'payee_type': 'str',
        'disabled': 'bool',
        'disabled_comment': 'str',
        'disabled_updated_timestamp': 'datetime',
        'managed_by_payor_id': 'str',
        'individual': 'GetPayeeListResponseIndividualV4',
        'company': 'GetPayeeListResponseCompanyV4'
    }

    attribute_map = {
        'payee_id': 'payeeId',
        'payor_refs': 'payorRefs',
        'email': 'email',
        'onboarded_status': 'onboardedStatus',
        'watchlist_status': 'watchlistStatus',
        'watchlist_status_updated_timestamp': 'watchlistStatusUpdatedTimestamp',
        'watchlist_override_comment': 'watchlistOverrideComment',
        'language': 'language',
        'created': 'created',
        'country': 'country',
        'display_name': 'displayName',
        'payee_type': 'payeeType',
        'disabled': 'disabled',
        'disabled_comment': 'disabledComment',
        'disabled_updated_timestamp': 'disabledUpdatedTimestamp',
        'managed_by_payor_id': 'managedByPayorId',
        'individual': 'individual',
        'company': 'company'
    }

    def __init__(self, payee_id=None, payor_refs=None, email=None, onboarded_status=None, watchlist_status=None, watchlist_status_updated_timestamp=None, watchlist_override_comment=None, language=None, created=None, country=None, display_name=None, payee_type=None, disabled=None, disabled_comment=None, disabled_updated_timestamp=None, managed_by_payor_id=None, individual=None, company=None):  # noqa: E501
        """GetPayeeListResponseV4 - a model defined in OpenAPI"""  # noqa: E501

        self._payee_id = None
        self._payor_refs = None
        self._email = None
        self._onboarded_status = None
        self._watchlist_status = None
        self._watchlist_status_updated_timestamp = None
        self._watchlist_override_comment = None
        self._language = None
        self._created = None
        self._country = None
        self._display_name = None
        self._payee_type = None
        self._disabled = None
        self._disabled_comment = None
        self._disabled_updated_timestamp = None
        self._managed_by_payor_id = None
        self._individual = None
        self._company = None
        self.discriminator = None

        if payee_id is not None:
            self.payee_id = payee_id
        self.payor_refs = payor_refs
        self.email = email
        if onboarded_status is not None:
            self.onboarded_status = onboarded_status
        if watchlist_status is not None:
            self.watchlist_status = watchlist_status
        self.watchlist_status_updated_timestamp = watchlist_status_updated_timestamp
        self.watchlist_override_comment = watchlist_override_comment
        if language is not None:
            self.language = language
        if created is not None:
            self.created = created
        if country is not None:
            self.country = country
        if display_name is not None:
            self.display_name = display_name
        if payee_type is not None:
            self.payee_type = payee_type
        if disabled is not None:
            self.disabled = disabled
        if disabled_comment is not None:
            self.disabled_comment = disabled_comment
        if disabled_updated_timestamp is not None:
            self.disabled_updated_timestamp = disabled_updated_timestamp
        if managed_by_payor_id is not None:
            self.managed_by_payor_id = managed_by_payor_id
        if individual is not None:
            self.individual = individual
        if company is not None:
            self.company = company

    @property
    def payee_id(self):
        """Gets the payee_id of this GetPayeeListResponseV4.  # noqa: E501


        :return: The payee_id of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this GetPayeeListResponseV4.


        :param payee_id: The payee_id of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def payor_refs(self):
        """Gets the payor_refs of this GetPayeeListResponseV4.  # noqa: E501


        :return: The payor_refs of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: list[PayeePayorRefV4]
        """
        return self._payor_refs

    @payor_refs.setter
    def payor_refs(self, payor_refs):
        """Sets the payor_refs of this GetPayeeListResponseV4.


        :param payor_refs: The payor_refs of this GetPayeeListResponseV4.  # noqa: E501
        :type: list[PayeePayorRefV4]
        """

        self._payor_refs = payor_refs

    @property
    def email(self):
        """Gets the email of this GetPayeeListResponseV4.  # noqa: E501


        :return: The email of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this GetPayeeListResponseV4.


        :param email: The email of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def onboarded_status(self):
        """Gets the onboarded_status of this GetPayeeListResponseV4.  # noqa: E501

        Payee onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED  # noqa: E501

        :return: The onboarded_status of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._onboarded_status

    @onboarded_status.setter
    def onboarded_status(self, onboarded_status):
        """Sets the onboarded_status of this GetPayeeListResponseV4.

        Payee onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED  # noqa: E501

        :param onboarded_status: The onboarded_status of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._onboarded_status = onboarded_status

    @property
    def watchlist_status(self):
        """Gets the watchlist_status of this GetPayeeListResponseV4.  # noqa: E501

        Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED  # noqa: E501

        :return: The watchlist_status of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_status

    @watchlist_status.setter
    def watchlist_status(self, watchlist_status):
        """Sets the watchlist_status of this GetPayeeListResponseV4.

        Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED  # noqa: E501

        :param watchlist_status: The watchlist_status of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._watchlist_status = watchlist_status

    @property
    def watchlist_status_updated_timestamp(self):
        """Gets the watchlist_status_updated_timestamp of this GetPayeeListResponseV4.  # noqa: E501


        :return: The watchlist_status_updated_timestamp of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_status_updated_timestamp

    @watchlist_status_updated_timestamp.setter
    def watchlist_status_updated_timestamp(self, watchlist_status_updated_timestamp):
        """Sets the watchlist_status_updated_timestamp of this GetPayeeListResponseV4.


        :param watchlist_status_updated_timestamp: The watchlist_status_updated_timestamp of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._watchlist_status_updated_timestamp = watchlist_status_updated_timestamp

    @property
    def watchlist_override_comment(self):
        """Gets the watchlist_override_comment of this GetPayeeListResponseV4.  # noqa: E501


        :return: The watchlist_override_comment of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_override_comment

    @watchlist_override_comment.setter
    def watchlist_override_comment(self, watchlist_override_comment):
        """Sets the watchlist_override_comment of this GetPayeeListResponseV4.


        :param watchlist_override_comment: The watchlist_override_comment of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._watchlist_override_comment = watchlist_override_comment

    @property
    def language(self):
        """Gets the language of this GetPayeeListResponseV4.  # noqa: E501

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :return: The language of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this GetPayeeListResponseV4.

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :param language: The language of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def created(self):
        """Gets the created of this GetPayeeListResponseV4.  # noqa: E501


        :return: The created of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this GetPayeeListResponseV4.


        :param created: The created of this GetPayeeListResponseV4.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def country(self):
        """Gets the country of this GetPayeeListResponseV4.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The country of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this GetPayeeListResponseV4.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param country: The country of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")  # noqa: E501
        if country is not None and len(country) < 2:
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")  # noqa: E501
        if country is not None and not re.search(r'^[A-Z]{2}$', country):  # noqa: E501
            raise ValueError(r"Invalid value for `country`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._country = country

    @property
    def display_name(self):
        """Gets the display_name of this GetPayeeListResponseV4.  # noqa: E501


        :return: The display_name of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetPayeeListResponseV4.


        :param display_name: The display_name of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def payee_type(self):
        """Gets the payee_type of this GetPayeeListResponseV4.  # noqa: E501

        Type of Payee. One of the following values: Individual, Company  # noqa: E501

        :return: The payee_type of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payee_type

    @payee_type.setter
    def payee_type(self, payee_type):
        """Sets the payee_type of this GetPayeeListResponseV4.

        Type of Payee. One of the following values: Individual, Company  # noqa: E501

        :param payee_type: The payee_type of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._payee_type = payee_type

    @property
    def disabled(self):
        """Gets the disabled of this GetPayeeListResponseV4.  # noqa: E501


        :return: The disabled of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this GetPayeeListResponseV4.


        :param disabled: The disabled of this GetPayeeListResponseV4.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def disabled_comment(self):
        """Gets the disabled_comment of this GetPayeeListResponseV4.  # noqa: E501


        :return: The disabled_comment of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._disabled_comment

    @disabled_comment.setter
    def disabled_comment(self, disabled_comment):
        """Sets the disabled_comment of this GetPayeeListResponseV4.


        :param disabled_comment: The disabled_comment of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._disabled_comment = disabled_comment

    @property
    def disabled_updated_timestamp(self):
        """Gets the disabled_updated_timestamp of this GetPayeeListResponseV4.  # noqa: E501


        :return: The disabled_updated_timestamp of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: datetime
        """
        return self._disabled_updated_timestamp

    @disabled_updated_timestamp.setter
    def disabled_updated_timestamp(self, disabled_updated_timestamp):
        """Sets the disabled_updated_timestamp of this GetPayeeListResponseV4.


        :param disabled_updated_timestamp: The disabled_updated_timestamp of this GetPayeeListResponseV4.  # noqa: E501
        :type: datetime
        """

        self._disabled_updated_timestamp = disabled_updated_timestamp

    @property
    def managed_by_payor_id(self):
        """Gets the managed_by_payor_id of this GetPayeeListResponseV4.  # noqa: E501

        The id of the payor if the payee is managed  # noqa: E501

        :return: The managed_by_payor_id of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_payor_id

    @managed_by_payor_id.setter
    def managed_by_payor_id(self, managed_by_payor_id):
        """Sets the managed_by_payor_id of this GetPayeeListResponseV4.

        The id of the payor if the payee is managed  # noqa: E501

        :param managed_by_payor_id: The managed_by_payor_id of this GetPayeeListResponseV4.  # noqa: E501
        :type: str
        """

        self._managed_by_payor_id = managed_by_payor_id

    @property
    def individual(self):
        """Gets the individual of this GetPayeeListResponseV4.  # noqa: E501


        :return: The individual of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: GetPayeeListResponseIndividualV4
        """
        return self._individual

    @individual.setter
    def individual(self, individual):
        """Sets the individual of this GetPayeeListResponseV4.


        :param individual: The individual of this GetPayeeListResponseV4.  # noqa: E501
        :type: GetPayeeListResponseIndividualV4
        """

        self._individual = individual

    @property
    def company(self):
        """Gets the company of this GetPayeeListResponseV4.  # noqa: E501


        :return: The company of this GetPayeeListResponseV4.  # noqa: E501
        :rtype: GetPayeeListResponseCompanyV4
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this GetPayeeListResponseV4.


        :param company: The company of this GetPayeeListResponseV4.  # noqa: E501
        :type: GetPayeeListResponseCompanyV4
        """

        self._company = company

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
        if not isinstance(other, GetPayeeListResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
