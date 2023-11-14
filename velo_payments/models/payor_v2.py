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


class PayorV2(object):
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
        'payor_id': 'str',
        'payor_name': 'str',
        'payor_xid': 'str',
        'provider': 'str',
        'address': 'PayorAddressV2',
        'primary_contact_name': 'str',
        'primary_contact_phone': 'str',
        'primary_contact_email': 'str',
        'kyc_state': 'str',
        'manual_lockout': 'bool',
        'open_banking_enabled': 'bool',
        'payee_grace_period_processing_enabled': 'bool',
        'payee_grace_period_days': 'int',
        'collective_alias': 'str',
        'support_contact': 'str',
        'dba_name': 'str',
        'allows_language_choice': 'bool',
        'reminder_emails_opt_out': 'bool',
        'language': 'str',
        'includes_reports': 'bool',
        'wu_customer_id': 'str',
        'max_master_payor_admins': 'int',
        'payment_rails': 'str',
        'remote_system_ids': 'list[str]',
        'usd_txn_value_reporting_threshold': 'int',
        'managing_payees': 'bool',
        'created_at': 'datetime'
    }

    attribute_map = {
        'payor_id': 'payorId',
        'payor_name': 'payorName',
        'payor_xid': 'payorXid',
        'provider': 'provider',
        'address': 'address',
        'primary_contact_name': 'primaryContactName',
        'primary_contact_phone': 'primaryContactPhone',
        'primary_contact_email': 'primaryContactEmail',
        'kyc_state': 'kycState',
        'manual_lockout': 'manualLockout',
        'open_banking_enabled': 'openBankingEnabled',
        'payee_grace_period_processing_enabled': 'payeeGracePeriodProcessingEnabled',
        'payee_grace_period_days': 'payeeGracePeriodDays',
        'collective_alias': 'collectiveAlias',
        'support_contact': 'supportContact',
        'dba_name': 'dbaName',
        'allows_language_choice': 'allowsLanguageChoice',
        'reminder_emails_opt_out': 'reminderEmailsOptOut',
        'language': 'language',
        'includes_reports': 'includesReports',
        'wu_customer_id': 'wuCustomerId',
        'max_master_payor_admins': 'maxMasterPayorAdmins',
        'payment_rails': 'paymentRails',
        'remote_system_ids': 'remoteSystemIds',
        'usd_txn_value_reporting_threshold': 'usdTxnValueReportingThreshold',
        'managing_payees': 'managingPayees',
        'created_at': 'createdAt'
    }

    def __init__(self, payor_id=None, payor_name=None, payor_xid=None, provider=None, address=None, primary_contact_name=None, primary_contact_phone=None, primary_contact_email=None, kyc_state=None, manual_lockout=None, open_banking_enabled=None, payee_grace_period_processing_enabled=None, payee_grace_period_days=None, collective_alias=None, support_contact=None, dba_name=None, allows_language_choice=None, reminder_emails_opt_out=None, language=None, includes_reports=None, wu_customer_id=None, max_master_payor_admins=None, payment_rails=None, remote_system_ids=None, usd_txn_value_reporting_threshold=None, managing_payees=None, created_at=None):  # noqa: E501
        """PayorV2 - a model defined in OpenAPI"""  # noqa: E501

        self._payor_id = None
        self._payor_name = None
        self._payor_xid = None
        self._provider = None
        self._address = None
        self._primary_contact_name = None
        self._primary_contact_phone = None
        self._primary_contact_email = None
        self._kyc_state = None
        self._manual_lockout = None
        self._open_banking_enabled = None
        self._payee_grace_period_processing_enabled = None
        self._payee_grace_period_days = None
        self._collective_alias = None
        self._support_contact = None
        self._dba_name = None
        self._allows_language_choice = None
        self._reminder_emails_opt_out = None
        self._language = None
        self._includes_reports = None
        self._wu_customer_id = None
        self._max_master_payor_admins = None
        self._payment_rails = None
        self._remote_system_ids = None
        self._usd_txn_value_reporting_threshold = None
        self._managing_payees = None
        self._created_at = None
        self.discriminator = None

        self.payor_id = payor_id
        self.payor_name = payor_name
        if payor_xid is not None:
            self.payor_xid = payor_xid
        if provider is not None:
            self.provider = provider
        if address is not None:
            self.address = address
        if primary_contact_name is not None:
            self.primary_contact_name = primary_contact_name
        if primary_contact_phone is not None:
            self.primary_contact_phone = primary_contact_phone
        if primary_contact_email is not None:
            self.primary_contact_email = primary_contact_email
        if kyc_state is not None:
            self.kyc_state = kyc_state
        if manual_lockout is not None:
            self.manual_lockout = manual_lockout
        if open_banking_enabled is not None:
            self.open_banking_enabled = open_banking_enabled
        if payee_grace_period_processing_enabled is not None:
            self.payee_grace_period_processing_enabled = payee_grace_period_processing_enabled
        if payee_grace_period_days is not None:
            self.payee_grace_period_days = payee_grace_period_days
        if collective_alias is not None:
            self.collective_alias = collective_alias
        if support_contact is not None:
            self.support_contact = support_contact
        if dba_name is not None:
            self.dba_name = dba_name
        if allows_language_choice is not None:
            self.allows_language_choice = allows_language_choice
        if reminder_emails_opt_out is not None:
            self.reminder_emails_opt_out = reminder_emails_opt_out
        if language is not None:
            self.language = language
        if includes_reports is not None:
            self.includes_reports = includes_reports
        if wu_customer_id is not None:
            self.wu_customer_id = wu_customer_id
        if max_master_payor_admins is not None:
            self.max_master_payor_admins = max_master_payor_admins
        if payment_rails is not None:
            self.payment_rails = payment_rails
        if remote_system_ids is not None:
            self.remote_system_ids = remote_system_ids
        if usd_txn_value_reporting_threshold is not None:
            self.usd_txn_value_reporting_threshold = usd_txn_value_reporting_threshold
        if managing_payees is not None:
            self.managing_payees = managing_payees
        if created_at is not None:
            self.created_at = created_at

    @property
    def payor_id(self):
        """Gets the payor_id of this PayorV2.  # noqa: E501

        The Payor Id  # noqa: E501

        :return: The payor_id of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._payor_id

    @payor_id.setter
    def payor_id(self, payor_id):
        """Sets the payor_id of this PayorV2.

        The Payor Id  # noqa: E501

        :param payor_id: The payor_id of this PayorV2.  # noqa: E501
        :type: str
        """
        if payor_id is None:
            raise ValueError("Invalid value for `payor_id`, must not be `None`")  # noqa: E501

        self._payor_id = payor_id

    @property
    def payor_name(self):
        """Gets the payor_name of this PayorV2.  # noqa: E501

        The name of the payor  # noqa: E501

        :return: The payor_name of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._payor_name

    @payor_name.setter
    def payor_name(self, payor_name):
        """Sets the payor_name of this PayorV2.

        The name of the payor  # noqa: E501

        :param payor_name: The payor_name of this PayorV2.  # noqa: E501
        :type: str
        """
        if payor_name is None:
            raise ValueError("Invalid value for `payor_name`, must not be `None`")  # noqa: E501

        self._payor_name = payor_name

    @property
    def payor_xid(self):
        """Gets the payor_xid of this PayorV2.  # noqa: E501

        A unique identifier that an external system uses to reference the payor in their system  # noqa: E501

        :return: The payor_xid of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._payor_xid

    @payor_xid.setter
    def payor_xid(self, payor_xid):
        """Sets the payor_xid of this PayorV2.

        A unique identifier that an external system uses to reference the payor in their system  # noqa: E501

        :param payor_xid: The payor_xid of this PayorV2.  # noqa: E501
        :type: str
        """

        self._payor_xid = payor_xid

    @property
    def provider(self):
        """Gets the provider of this PayorV2.  # noqa: E501

        The source of the payorXid, default is null which means Velo  # noqa: E501

        :return: The provider of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this PayorV2.

        The source of the payorXid, default is null which means Velo  # noqa: E501

        :param provider: The provider of this PayorV2.  # noqa: E501
        :type: str
        """

        self._provider = provider

    @property
    def address(self):
        """Gets the address of this PayorV2.  # noqa: E501


        :return: The address of this PayorV2.  # noqa: E501
        :rtype: PayorAddressV2
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PayorV2.


        :param address: The address of this PayorV2.  # noqa: E501
        :type: PayorAddressV2
        """

        self._address = address

    @property
    def primary_contact_name(self):
        """Gets the primary_contact_name of this PayorV2.  # noqa: E501

        Name of primary contact for the payor.  # noqa: E501

        :return: The primary_contact_name of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._primary_contact_name

    @primary_contact_name.setter
    def primary_contact_name(self, primary_contact_name):
        """Sets the primary_contact_name of this PayorV2.

        Name of primary contact for the payor.  # noqa: E501

        :param primary_contact_name: The primary_contact_name of this PayorV2.  # noqa: E501
        :type: str
        """

        self._primary_contact_name = primary_contact_name

    @property
    def primary_contact_phone(self):
        """Gets the primary_contact_phone of this PayorV2.  # noqa: E501

        Primary contact phone number for the payor.  # noqa: E501

        :return: The primary_contact_phone of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._primary_contact_phone

    @primary_contact_phone.setter
    def primary_contact_phone(self, primary_contact_phone):
        """Sets the primary_contact_phone of this PayorV2.

        Primary contact phone number for the payor.  # noqa: E501

        :param primary_contact_phone: The primary_contact_phone of this PayorV2.  # noqa: E501
        :type: str
        """

        self._primary_contact_phone = primary_contact_phone

    @property
    def primary_contact_email(self):
        """Gets the primary_contact_email of this PayorV2.  # noqa: E501

        Primary contact email for the payor.  # noqa: E501

        :return: The primary_contact_email of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._primary_contact_email

    @primary_contact_email.setter
    def primary_contact_email(self, primary_contact_email):
        """Sets the primary_contact_email of this PayorV2.

        Primary contact email for the payor.  # noqa: E501

        :param primary_contact_email: The primary_contact_email of this PayorV2.  # noqa: E501
        :type: str
        """

        self._primary_contact_email = primary_contact_email

    @property
    def kyc_state(self):
        """Gets the kyc_state of this PayorV2.  # noqa: E501

        The kyc state of the payor. One of the following values: FAILED_KYC, PASSED_KYC, REQUIRES_KYC  # noqa: E501

        :return: The kyc_state of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._kyc_state

    @kyc_state.setter
    def kyc_state(self, kyc_state):
        """Sets the kyc_state of this PayorV2.

        The kyc state of the payor. One of the following values: FAILED_KYC, PASSED_KYC, REQUIRES_KYC  # noqa: E501

        :param kyc_state: The kyc_state of this PayorV2.  # noqa: E501
        :type: str
        """

        self._kyc_state = kyc_state

    @property
    def manual_lockout(self):
        """Gets the manual_lockout of this PayorV2.  # noqa: E501

        Whether or not the payor has been manually locked by the backoffice.  # noqa: E501

        :return: The manual_lockout of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._manual_lockout

    @manual_lockout.setter
    def manual_lockout(self, manual_lockout):
        """Sets the manual_lockout of this PayorV2.

        Whether or not the payor has been manually locked by the backoffice.  # noqa: E501

        :param manual_lockout: The manual_lockout of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._manual_lockout = manual_lockout

    @property
    def open_banking_enabled(self):
        """Gets the open_banking_enabled of this PayorV2.  # noqa: E501

        Is Open Banking supported for this payor  # noqa: E501

        :return: The open_banking_enabled of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._open_banking_enabled

    @open_banking_enabled.setter
    def open_banking_enabled(self, open_banking_enabled):
        """Sets the open_banking_enabled of this PayorV2.

        Is Open Banking supported for this payor  # noqa: E501

        :param open_banking_enabled: The open_banking_enabled of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._open_banking_enabled = open_banking_enabled

    @property
    def payee_grace_period_processing_enabled(self):
        """Gets the payee_grace_period_processing_enabled of this PayorV2.  # noqa: E501

        Whether grace period processing is enabled.  # noqa: E501

        :return: The payee_grace_period_processing_enabled of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._payee_grace_period_processing_enabled

    @payee_grace_period_processing_enabled.setter
    def payee_grace_period_processing_enabled(self, payee_grace_period_processing_enabled):
        """Sets the payee_grace_period_processing_enabled of this PayorV2.

        Whether grace period processing is enabled.  # noqa: E501

        :param payee_grace_period_processing_enabled: The payee_grace_period_processing_enabled of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._payee_grace_period_processing_enabled = payee_grace_period_processing_enabled

    @property
    def payee_grace_period_days(self):
        """Gets the payee_grace_period_days of this PayorV2.  # noqa: E501

        The grace period for paying payees in days before the payee must be onboarded.  # noqa: E501

        :return: The payee_grace_period_days of this PayorV2.  # noqa: E501
        :rtype: int
        """
        return self._payee_grace_period_days

    @payee_grace_period_days.setter
    def payee_grace_period_days(self, payee_grace_period_days):
        """Sets the payee_grace_period_days of this PayorV2.

        The grace period for paying payees in days before the payee must be onboarded.  # noqa: E501

        :param payee_grace_period_days: The payee_grace_period_days of this PayorV2.  # noqa: E501
        :type: int
        """

        self._payee_grace_period_days = payee_grace_period_days

    @property
    def collective_alias(self):
        """Gets the collective_alias of this PayorV2.  # noqa: E501

        How the payor has chosen to refer to payees.  # noqa: E501

        :return: The collective_alias of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._collective_alias

    @collective_alias.setter
    def collective_alias(self, collective_alias):
        """Sets the collective_alias of this PayorV2.

        How the payor has chosen to refer to payees.  # noqa: E501

        :param collective_alias: The collective_alias of this PayorV2.  # noqa: E501
        :type: str
        """

        self._collective_alias = collective_alias

    @property
    def support_contact(self):
        """Gets the support_contact of this PayorV2.  # noqa: E501

        The payor’s support contact email address.  # noqa: E501

        :return: The support_contact of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._support_contact

    @support_contact.setter
    def support_contact(self, support_contact):
        """Sets the support_contact of this PayorV2.

        The payor’s support contact email address.  # noqa: E501

        :param support_contact: The support_contact of this PayorV2.  # noqa: E501
        :type: str
        """

        self._support_contact = support_contact

    @property
    def dba_name(self):
        """Gets the dba_name of this PayorV2.  # noqa: E501

        The payor’s 'Doing Business As' name.  # noqa: E501

        :return: The dba_name of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._dba_name

    @dba_name.setter
    def dba_name(self, dba_name):
        """Sets the dba_name of this PayorV2.

        The payor’s 'Doing Business As' name.  # noqa: E501

        :param dba_name: The dba_name of this PayorV2.  # noqa: E501
        :type: str
        """

        self._dba_name = dba_name

    @property
    def allows_language_choice(self):
        """Gets the allows_language_choice of this PayorV2.  # noqa: E501

        Whether or not the payor allows language choice in the UI.  # noqa: E501

        :return: The allows_language_choice of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._allows_language_choice

    @allows_language_choice.setter
    def allows_language_choice(self, allows_language_choice):
        """Sets the allows_language_choice of this PayorV2.

        Whether or not the payor allows language choice in the UI.  # noqa: E501

        :param allows_language_choice: The allows_language_choice of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._allows_language_choice = allows_language_choice

    @property
    def reminder_emails_opt_out(self):
        """Gets the reminder_emails_opt_out of this PayorV2.  # noqa: E501

        Whether or not the payor has opted-out of reminder emails being sent.  # noqa: E501

        :return: The reminder_emails_opt_out of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._reminder_emails_opt_out

    @reminder_emails_opt_out.setter
    def reminder_emails_opt_out(self, reminder_emails_opt_out):
        """Sets the reminder_emails_opt_out of this PayorV2.

        Whether or not the payor has opted-out of reminder emails being sent.  # noqa: E501

        :param reminder_emails_opt_out: The reminder_emails_opt_out of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._reminder_emails_opt_out = reminder_emails_opt_out

    @property
    def language(self):
        """Gets the language of this PayorV2.  # noqa: E501

        The payor’s language preference. Must be one of [EN, FR]  # noqa: E501

        :return: The language of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PayorV2.

        The payor’s language preference. Must be one of [EN, FR]  # noqa: E501

        :param language: The language of this PayorV2.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def includes_reports(self):
        """Gets the includes_reports of this PayorV2.  # noqa: E501

        For internal use only (will be removed in a later version)  # noqa: E501

        :return: The includes_reports of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._includes_reports

    @includes_reports.setter
    def includes_reports(self, includes_reports):
        """Sets the includes_reports of this PayorV2.

        For internal use only (will be removed in a later version)  # noqa: E501

        :param includes_reports: The includes_reports of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._includes_reports = includes_reports

    @property
    def wu_customer_id(self):
        """Gets the wu_customer_id of this PayorV2.  # noqa: E501

        For internal use only (will be removed in a later version)  # noqa: E501

        :return: The wu_customer_id of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._wu_customer_id

    @wu_customer_id.setter
    def wu_customer_id(self, wu_customer_id):
        """Sets the wu_customer_id of this PayorV2.

        For internal use only (will be removed in a later version)  # noqa: E501

        :param wu_customer_id: The wu_customer_id of this PayorV2.  # noqa: E501
        :type: str
        """

        self._wu_customer_id = wu_customer_id

    @property
    def max_master_payor_admins(self):
        """Gets the max_master_payor_admins of this PayorV2.  # noqa: E501

        The maximum number of payor users with the master admin role  # noqa: E501

        :return: The max_master_payor_admins of this PayorV2.  # noqa: E501
        :rtype: int
        """
        return self._max_master_payor_admins

    @max_master_payor_admins.setter
    def max_master_payor_admins(self, max_master_payor_admins):
        """Sets the max_master_payor_admins of this PayorV2.

        The maximum number of payor users with the master admin role  # noqa: E501

        :param max_master_payor_admins: The max_master_payor_admins of this PayorV2.  # noqa: E501
        :type: int
        """

        self._max_master_payor_admins = max_master_payor_admins

    @property
    def payment_rails(self):
        """Gets the payment_rails of this PayorV2.  # noqa: E501

        For internal use only (will be removed in a later version)  # noqa: E501

        :return: The payment_rails of this PayorV2.  # noqa: E501
        :rtype: str
        """
        return self._payment_rails

    @payment_rails.setter
    def payment_rails(self, payment_rails):
        """Sets the payment_rails of this PayorV2.

        For internal use only (will be removed in a later version)  # noqa: E501

        :param payment_rails: The payment_rails of this PayorV2.  # noqa: E501
        :type: str
        """

        self._payment_rails = payment_rails

    @property
    def remote_system_ids(self):
        """Gets the remote_system_ids of this PayorV2.  # noqa: E501

        For internal use only (will be removed in a later version)  # noqa: E501

        :return: The remote_system_ids of this PayorV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._remote_system_ids

    @remote_system_ids.setter
    def remote_system_ids(self, remote_system_ids):
        """Sets the remote_system_ids of this PayorV2.

        For internal use only (will be removed in a later version)  # noqa: E501

        :param remote_system_ids: The remote_system_ids of this PayorV2.  # noqa: E501
        :type: list[str]
        """

        self._remote_system_ids = remote_system_ids

    @property
    def usd_txn_value_reporting_threshold(self):
        """Gets the usd_txn_value_reporting_threshold of this PayorV2.  # noqa: E501

        USD in minor units. For internal use only (will be removed in a later version)  # noqa: E501

        :return: The usd_txn_value_reporting_threshold of this PayorV2.  # noqa: E501
        :rtype: int
        """
        return self._usd_txn_value_reporting_threshold

    @usd_txn_value_reporting_threshold.setter
    def usd_txn_value_reporting_threshold(self, usd_txn_value_reporting_threshold):
        """Sets the usd_txn_value_reporting_threshold of this PayorV2.

        USD in minor units. For internal use only (will be removed in a later version)  # noqa: E501

        :param usd_txn_value_reporting_threshold: The usd_txn_value_reporting_threshold of this PayorV2.  # noqa: E501
        :type: int
        """

        self._usd_txn_value_reporting_threshold = usd_txn_value_reporting_threshold

    @property
    def managing_payees(self):
        """Gets the managing_payees of this PayorV2.  # noqa: E501

        Does this payor manage their own payees (payees are not invited but managed by the payor)  # noqa: E501

        :return: The managing_payees of this PayorV2.  # noqa: E501
        :rtype: bool
        """
        return self._managing_payees

    @managing_payees.setter
    def managing_payees(self, managing_payees):
        """Sets the managing_payees of this PayorV2.

        Does this payor manage their own payees (payees are not invited but managed by the payor)  # noqa: E501

        :param managing_payees: The managing_payees of this PayorV2.  # noqa: E501
        :type: bool
        """

        self._managing_payees = managing_payees

    @property
    def created_at(self):
        """Gets the created_at of this PayorV2.  # noqa: E501

        The date of creation of the payor  # noqa: E501

        :return: The created_at of this PayorV2.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PayorV2.

        The date of creation of the payor  # noqa: E501

        :param created_at: The created_at of this PayorV2.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, PayorV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
