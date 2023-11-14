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


class PayeeDetailResponseV4(object):
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
        'payment_channels': 'list[PaymentChannelSummaryV4]',
        'email': 'str',
        'onboarded_status': 'str',
        'watchlist_status': 'str',
        'watchlist_override_expires_at_timestamp': 'datetime',
        'watchlist_override_comment': 'str',
        'language': 'str',
        'created': 'datetime',
        'country': 'str',
        'display_name': 'str',
        'payee_type': 'str',
        'disabled': 'bool',
        'disabled_comment': 'str',
        'disabled_updated_timestamp': 'datetime',
        'address': 'PayeeAddressV4',
        'individual': 'IndividualV4',
        'company': 'CompanyV4',
        'cellphone_number': 'str',
        'managed_by_payor_id': 'str',
        'watchlist_status_updated_timestamp': 'str',
        'grace_period_end_date': 'date',
        'enhanced_kyc_completed': 'bool',
        'kyc_completed_timestamp': 'str',
        'pause_payment': 'bool',
        'pause_payment_timestamp': 'str',
        'marketing_opt_in_decision': 'bool',
        'marketing_opt_in_timestamp': 'str',
        'accept_terms_and_conditions_timestamp': 'datetime',
        'challenge': 'ChallengeV4'
    }

    attribute_map = {
        'payee_id': 'payeeId',
        'payor_refs': 'payorRefs',
        'payment_channels': 'paymentChannels',
        'email': 'email',
        'onboarded_status': 'onboardedStatus',
        'watchlist_status': 'watchlistStatus',
        'watchlist_override_expires_at_timestamp': 'watchlistOverrideExpiresAtTimestamp',
        'watchlist_override_comment': 'watchlistOverrideComment',
        'language': 'language',
        'created': 'created',
        'country': 'country',
        'display_name': 'displayName',
        'payee_type': 'payeeType',
        'disabled': 'disabled',
        'disabled_comment': 'disabledComment',
        'disabled_updated_timestamp': 'disabledUpdatedTimestamp',
        'address': 'address',
        'individual': 'individual',
        'company': 'company',
        'cellphone_number': 'cellphoneNumber',
        'managed_by_payor_id': 'managedByPayorId',
        'watchlist_status_updated_timestamp': 'watchlistStatusUpdatedTimestamp',
        'grace_period_end_date': 'gracePeriodEndDate',
        'enhanced_kyc_completed': 'enhancedKycCompleted',
        'kyc_completed_timestamp': 'kycCompletedTimestamp',
        'pause_payment': 'pausePayment',
        'pause_payment_timestamp': 'pausePaymentTimestamp',
        'marketing_opt_in_decision': 'marketingOptInDecision',
        'marketing_opt_in_timestamp': 'marketingOptInTimestamp',
        'accept_terms_and_conditions_timestamp': 'acceptTermsAndConditionsTimestamp',
        'challenge': 'challenge'
    }

    def __init__(self, payee_id=None, payor_refs=None, payment_channels=None, email=None, onboarded_status=None, watchlist_status=None, watchlist_override_expires_at_timestamp=None, watchlist_override_comment=None, language=None, created=None, country=None, display_name=None, payee_type=None, disabled=None, disabled_comment=None, disabled_updated_timestamp=None, address=None, individual=None, company=None, cellphone_number=None, managed_by_payor_id=None, watchlist_status_updated_timestamp=None, grace_period_end_date=None, enhanced_kyc_completed=None, kyc_completed_timestamp=None, pause_payment=None, pause_payment_timestamp=None, marketing_opt_in_decision=None, marketing_opt_in_timestamp=None, accept_terms_and_conditions_timestamp=None, challenge=None):  # noqa: E501
        """PayeeDetailResponseV4 - a model defined in OpenAPI"""  # noqa: E501

        self._payee_id = None
        self._payor_refs = None
        self._payment_channels = None
        self._email = None
        self._onboarded_status = None
        self._watchlist_status = None
        self._watchlist_override_expires_at_timestamp = None
        self._watchlist_override_comment = None
        self._language = None
        self._created = None
        self._country = None
        self._display_name = None
        self._payee_type = None
        self._disabled = None
        self._disabled_comment = None
        self._disabled_updated_timestamp = None
        self._address = None
        self._individual = None
        self._company = None
        self._cellphone_number = None
        self._managed_by_payor_id = None
        self._watchlist_status_updated_timestamp = None
        self._grace_period_end_date = None
        self._enhanced_kyc_completed = None
        self._kyc_completed_timestamp = None
        self._pause_payment = None
        self._pause_payment_timestamp = None
        self._marketing_opt_in_decision = None
        self._marketing_opt_in_timestamp = None
        self._accept_terms_and_conditions_timestamp = None
        self._challenge = None
        self.discriminator = None

        if payee_id is not None:
            self.payee_id = payee_id
        self.payor_refs = payor_refs
        self.payment_channels = payment_channels
        self.email = email
        if onboarded_status is not None:
            self.onboarded_status = onboarded_status
        if watchlist_status is not None:
            self.watchlist_status = watchlist_status
        self.watchlist_override_expires_at_timestamp = watchlist_override_expires_at_timestamp
        if watchlist_override_comment is not None:
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
        if address is not None:
            self.address = address
        if individual is not None:
            self.individual = individual
        self.company = company
        if cellphone_number is not None:
            self.cellphone_number = cellphone_number
        if managed_by_payor_id is not None:
            self.managed_by_payor_id = managed_by_payor_id
        self.watchlist_status_updated_timestamp = watchlist_status_updated_timestamp
        self.grace_period_end_date = grace_period_end_date
        if enhanced_kyc_completed is not None:
            self.enhanced_kyc_completed = enhanced_kyc_completed
        self.kyc_completed_timestamp = kyc_completed_timestamp
        if pause_payment is not None:
            self.pause_payment = pause_payment
        self.pause_payment_timestamp = pause_payment_timestamp
        if marketing_opt_in_decision is not None:
            self.marketing_opt_in_decision = marketing_opt_in_decision
        self.marketing_opt_in_timestamp = marketing_opt_in_timestamp
        self.accept_terms_and_conditions_timestamp = accept_terms_and_conditions_timestamp
        if challenge is not None:
            self.challenge = challenge

    @property
    def payee_id(self):
        """Gets the payee_id of this PayeeDetailResponseV4.  # noqa: E501


        :return: The payee_id of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this PayeeDetailResponseV4.


        :param payee_id: The payee_id of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._payee_id = payee_id

    @property
    def payor_refs(self):
        """Gets the payor_refs of this PayeeDetailResponseV4.  # noqa: E501


        :return: The payor_refs of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: list[PayeePayorRefV4]
        """
        return self._payor_refs

    @payor_refs.setter
    def payor_refs(self, payor_refs):
        """Sets the payor_refs of this PayeeDetailResponseV4.


        :param payor_refs: The payor_refs of this PayeeDetailResponseV4.  # noqa: E501
        :type: list[PayeePayorRefV4]
        """

        self._payor_refs = payor_refs

    @property
    def payment_channels(self):
        """Gets the payment_channels of this PayeeDetailResponseV4.  # noqa: E501

        A list of the Payee's payment channels in their preferred order  # noqa: E501

        :return: The payment_channels of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: list[PaymentChannelSummaryV4]
        """
        return self._payment_channels

    @payment_channels.setter
    def payment_channels(self, payment_channels):
        """Sets the payment_channels of this PayeeDetailResponseV4.

        A list of the Payee's payment channels in their preferred order  # noqa: E501

        :param payment_channels: The payment_channels of this PayeeDetailResponseV4.  # noqa: E501
        :type: list[PaymentChannelSummaryV4]
        """

        self._payment_channels = payment_channels

    @property
    def email(self):
        """Gets the email of this PayeeDetailResponseV4.  # noqa: E501


        :return: The email of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PayeeDetailResponseV4.


        :param email: The email of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def onboarded_status(self):
        """Gets the onboarded_status of this PayeeDetailResponseV4.  # noqa: E501

        Payee onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED  # noqa: E501

        :return: The onboarded_status of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._onboarded_status

    @onboarded_status.setter
    def onboarded_status(self, onboarded_status):
        """Sets the onboarded_status of this PayeeDetailResponseV4.

        Payee onboarded status. One of the following values: CREATED, INVITED, REGISTERED, ONBOARDED  # noqa: E501

        :param onboarded_status: The onboarded_status of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._onboarded_status = onboarded_status

    @property
    def watchlist_status(self):
        """Gets the watchlist_status of this PayeeDetailResponseV4.  # noqa: E501

        Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED  # noqa: E501

        :return: The watchlist_status of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_status

    @watchlist_status.setter
    def watchlist_status(self, watchlist_status):
        """Sets the watchlist_status of this PayeeDetailResponseV4.

        Current watchlist status. One of the following values: NONE, PENDING, REVIEW, PASSED, FAILED  # noqa: E501

        :param watchlist_status: The watchlist_status of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._watchlist_status = watchlist_status

    @property
    def watchlist_override_expires_at_timestamp(self):
        """Gets the watchlist_override_expires_at_timestamp of this PayeeDetailResponseV4.  # noqa: E501


        :return: The watchlist_override_expires_at_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: datetime
        """
        return self._watchlist_override_expires_at_timestamp

    @watchlist_override_expires_at_timestamp.setter
    def watchlist_override_expires_at_timestamp(self, watchlist_override_expires_at_timestamp):
        """Sets the watchlist_override_expires_at_timestamp of this PayeeDetailResponseV4.


        :param watchlist_override_expires_at_timestamp: The watchlist_override_expires_at_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: datetime
        """

        self._watchlist_override_expires_at_timestamp = watchlist_override_expires_at_timestamp

    @property
    def watchlist_override_comment(self):
        """Gets the watchlist_override_comment of this PayeeDetailResponseV4.  # noqa: E501


        :return: The watchlist_override_comment of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_override_comment

    @watchlist_override_comment.setter
    def watchlist_override_comment(self, watchlist_override_comment):
        """Sets the watchlist_override_comment of this PayeeDetailResponseV4.


        :param watchlist_override_comment: The watchlist_override_comment of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._watchlist_override_comment = watchlist_override_comment

    @property
    def language(self):
        """Gets the language of this PayeeDetailResponseV4.  # noqa: E501

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :return: The language of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PayeeDetailResponseV4.

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :param language: The language of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def created(self):
        """Gets the created of this PayeeDetailResponseV4.  # noqa: E501


        :return: The created of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this PayeeDetailResponseV4.


        :param created: The created of this PayeeDetailResponseV4.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def country(self):
        """Gets the country of this PayeeDetailResponseV4.  # noqa: E501


        :return: The country of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this PayeeDetailResponseV4.


        :param country: The country of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def display_name(self):
        """Gets the display_name of this PayeeDetailResponseV4.  # noqa: E501


        :return: The display_name of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PayeeDetailResponseV4.


        :param display_name: The display_name of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def payee_type(self):
        """Gets the payee_type of this PayeeDetailResponseV4.  # noqa: E501

        Type of Payee. One of the following values: Individual, Company  # noqa: E501

        :return: The payee_type of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._payee_type

    @payee_type.setter
    def payee_type(self, payee_type):
        """Sets the payee_type of this PayeeDetailResponseV4.

        Type of Payee. One of the following values: Individual, Company  # noqa: E501

        :param payee_type: The payee_type of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._payee_type = payee_type

    @property
    def disabled(self):
        """Gets the disabled of this PayeeDetailResponseV4.  # noqa: E501


        :return: The disabled of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        """Sets the disabled of this PayeeDetailResponseV4.


        :param disabled: The disabled of this PayeeDetailResponseV4.  # noqa: E501
        :type: bool
        """

        self._disabled = disabled

    @property
    def disabled_comment(self):
        """Gets the disabled_comment of this PayeeDetailResponseV4.  # noqa: E501


        :return: The disabled_comment of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._disabled_comment

    @disabled_comment.setter
    def disabled_comment(self, disabled_comment):
        """Sets the disabled_comment of this PayeeDetailResponseV4.


        :param disabled_comment: The disabled_comment of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._disabled_comment = disabled_comment

    @property
    def disabled_updated_timestamp(self):
        """Gets the disabled_updated_timestamp of this PayeeDetailResponseV4.  # noqa: E501


        :return: The disabled_updated_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: datetime
        """
        return self._disabled_updated_timestamp

    @disabled_updated_timestamp.setter
    def disabled_updated_timestamp(self, disabled_updated_timestamp):
        """Sets the disabled_updated_timestamp of this PayeeDetailResponseV4.


        :param disabled_updated_timestamp: The disabled_updated_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: datetime
        """

        self._disabled_updated_timestamp = disabled_updated_timestamp

    @property
    def address(self):
        """Gets the address of this PayeeDetailResponseV4.  # noqa: E501


        :return: The address of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: PayeeAddressV4
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PayeeDetailResponseV4.


        :param address: The address of this PayeeDetailResponseV4.  # noqa: E501
        :type: PayeeAddressV4
        """

        self._address = address

    @property
    def individual(self):
        """Gets the individual of this PayeeDetailResponseV4.  # noqa: E501


        :return: The individual of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: IndividualV4
        """
        return self._individual

    @individual.setter
    def individual(self, individual):
        """Sets the individual of this PayeeDetailResponseV4.


        :param individual: The individual of this PayeeDetailResponseV4.  # noqa: E501
        :type: IndividualV4
        """

        self._individual = individual

    @property
    def company(self):
        """Gets the company of this PayeeDetailResponseV4.  # noqa: E501


        :return: The company of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: CompanyV4
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this PayeeDetailResponseV4.


        :param company: The company of this PayeeDetailResponseV4.  # noqa: E501
        :type: CompanyV4
        """

        self._company = company

    @property
    def cellphone_number(self):
        """Gets the cellphone_number of this PayeeDetailResponseV4.  # noqa: E501


        :return: The cellphone_number of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._cellphone_number

    @cellphone_number.setter
    def cellphone_number(self, cellphone_number):
        """Sets the cellphone_number of this PayeeDetailResponseV4.


        :param cellphone_number: The cellphone_number of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._cellphone_number = cellphone_number

    @property
    def managed_by_payor_id(self):
        """Gets the managed_by_payor_id of this PayeeDetailResponseV4.  # noqa: E501

        The id of the payor if the payee is managed  # noqa: E501

        :return: The managed_by_payor_id of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._managed_by_payor_id

    @managed_by_payor_id.setter
    def managed_by_payor_id(self, managed_by_payor_id):
        """Sets the managed_by_payor_id of this PayeeDetailResponseV4.

        The id of the payor if the payee is managed  # noqa: E501

        :param managed_by_payor_id: The managed_by_payor_id of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._managed_by_payor_id = managed_by_payor_id

    @property
    def watchlist_status_updated_timestamp(self):
        """Gets the watchlist_status_updated_timestamp of this PayeeDetailResponseV4.  # noqa: E501


        :return: The watchlist_status_updated_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._watchlist_status_updated_timestamp

    @watchlist_status_updated_timestamp.setter
    def watchlist_status_updated_timestamp(self, watchlist_status_updated_timestamp):
        """Sets the watchlist_status_updated_timestamp of this PayeeDetailResponseV4.


        :param watchlist_status_updated_timestamp: The watchlist_status_updated_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._watchlist_status_updated_timestamp = watchlist_status_updated_timestamp

    @property
    def grace_period_end_date(self):
        """Gets the grace_period_end_date of this PayeeDetailResponseV4.  # noqa: E501


        :return: The grace_period_end_date of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: date
        """
        return self._grace_period_end_date

    @grace_period_end_date.setter
    def grace_period_end_date(self, grace_period_end_date):
        """Sets the grace_period_end_date of this PayeeDetailResponseV4.


        :param grace_period_end_date: The grace_period_end_date of this PayeeDetailResponseV4.  # noqa: E501
        :type: date
        """

        self._grace_period_end_date = grace_period_end_date

    @property
    def enhanced_kyc_completed(self):
        """Gets the enhanced_kyc_completed of this PayeeDetailResponseV4.  # noqa: E501


        :return: The enhanced_kyc_completed of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._enhanced_kyc_completed

    @enhanced_kyc_completed.setter
    def enhanced_kyc_completed(self, enhanced_kyc_completed):
        """Sets the enhanced_kyc_completed of this PayeeDetailResponseV4.


        :param enhanced_kyc_completed: The enhanced_kyc_completed of this PayeeDetailResponseV4.  # noqa: E501
        :type: bool
        """

        self._enhanced_kyc_completed = enhanced_kyc_completed

    @property
    def kyc_completed_timestamp(self):
        """Gets the kyc_completed_timestamp of this PayeeDetailResponseV4.  # noqa: E501


        :return: The kyc_completed_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._kyc_completed_timestamp

    @kyc_completed_timestamp.setter
    def kyc_completed_timestamp(self, kyc_completed_timestamp):
        """Sets the kyc_completed_timestamp of this PayeeDetailResponseV4.


        :param kyc_completed_timestamp: The kyc_completed_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._kyc_completed_timestamp = kyc_completed_timestamp

    @property
    def pause_payment(self):
        """Gets the pause_payment of this PayeeDetailResponseV4.  # noqa: E501


        :return: The pause_payment of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._pause_payment

    @pause_payment.setter
    def pause_payment(self, pause_payment):
        """Sets the pause_payment of this PayeeDetailResponseV4.


        :param pause_payment: The pause_payment of this PayeeDetailResponseV4.  # noqa: E501
        :type: bool
        """

        self._pause_payment = pause_payment

    @property
    def pause_payment_timestamp(self):
        """Gets the pause_payment_timestamp of this PayeeDetailResponseV4.  # noqa: E501


        :return: The pause_payment_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._pause_payment_timestamp

    @pause_payment_timestamp.setter
    def pause_payment_timestamp(self, pause_payment_timestamp):
        """Sets the pause_payment_timestamp of this PayeeDetailResponseV4.


        :param pause_payment_timestamp: The pause_payment_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._pause_payment_timestamp = pause_payment_timestamp

    @property
    def marketing_opt_in_decision(self):
        """Gets the marketing_opt_in_decision of this PayeeDetailResponseV4.  # noqa: E501


        :return: The marketing_opt_in_decision of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: bool
        """
        return self._marketing_opt_in_decision

    @marketing_opt_in_decision.setter
    def marketing_opt_in_decision(self, marketing_opt_in_decision):
        """Sets the marketing_opt_in_decision of this PayeeDetailResponseV4.


        :param marketing_opt_in_decision: The marketing_opt_in_decision of this PayeeDetailResponseV4.  # noqa: E501
        :type: bool
        """

        self._marketing_opt_in_decision = marketing_opt_in_decision

    @property
    def marketing_opt_in_timestamp(self):
        """Gets the marketing_opt_in_timestamp of this PayeeDetailResponseV4.  # noqa: E501


        :return: The marketing_opt_in_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: str
        """
        return self._marketing_opt_in_timestamp

    @marketing_opt_in_timestamp.setter
    def marketing_opt_in_timestamp(self, marketing_opt_in_timestamp):
        """Sets the marketing_opt_in_timestamp of this PayeeDetailResponseV4.


        :param marketing_opt_in_timestamp: The marketing_opt_in_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: str
        """

        self._marketing_opt_in_timestamp = marketing_opt_in_timestamp

    @property
    def accept_terms_and_conditions_timestamp(self):
        """Gets the accept_terms_and_conditions_timestamp of this PayeeDetailResponseV4.  # noqa: E501

        The timestamp when the payee last accepted T&Cs  # noqa: E501

        :return: The accept_terms_and_conditions_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: datetime
        """
        return self._accept_terms_and_conditions_timestamp

    @accept_terms_and_conditions_timestamp.setter
    def accept_terms_and_conditions_timestamp(self, accept_terms_and_conditions_timestamp):
        """Sets the accept_terms_and_conditions_timestamp of this PayeeDetailResponseV4.

        The timestamp when the payee last accepted T&Cs  # noqa: E501

        :param accept_terms_and_conditions_timestamp: The accept_terms_and_conditions_timestamp of this PayeeDetailResponseV4.  # noqa: E501
        :type: datetime
        """

        self._accept_terms_and_conditions_timestamp = accept_terms_and_conditions_timestamp

    @property
    def challenge(self):
        """Gets the challenge of this PayeeDetailResponseV4.  # noqa: E501


        :return: The challenge of this PayeeDetailResponseV4.  # noqa: E501
        :rtype: ChallengeV4
        """
        return self._challenge

    @challenge.setter
    def challenge(self, challenge):
        """Sets the challenge of this PayeeDetailResponseV4.


        :param challenge: The challenge of this PayeeDetailResponseV4.  # noqa: E501
        :type: ChallengeV4
        """

        self._challenge = challenge

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
        if not isinstance(other, PayeeDetailResponseV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
