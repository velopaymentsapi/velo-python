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


class CreatePayeesCSVRequestV3(object):
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
        'type': 'PayeeTypeEnum',
        'remote_id': 'str',
        'email': 'str',
        'address_line1': 'str',
        'address_line2': 'str',
        'address_line3': 'str',
        'address_line4': 'str',
        'address_city': 'str',
        'address_county_or_province': 'str',
        'address_zip_or_postcode': 'str',
        'address_country': 'str',
        'individual_national_identification': 'str',
        'individual_date_of_birth': 'date',
        'individual_title': 'str',
        'individual_first_name': 'str',
        'individual_other_names': 'str',
        'individual_last_name': 'str',
        'company_name': 'str',
        'company_ein': 'str',
        'company_operating_name': 'str',
        'payment_channel_account_number': 'str',
        'payment_channel_routing_number': 'str',
        'payment_channel_account_name': 'str',
        'payment_channel_iban': 'str',
        'payment_channel_country_code': 'str',
        'payment_channel_currency': 'str',
        'challenge_description': 'str',
        'challenge_value': 'str',
        'payee_language': 'str'
    }

    attribute_map = {
        'type': 'type',
        'remote_id': 'remoteId',
        'email': 'email',
        'address_line1': 'addressLine1',
        'address_line2': 'addressLine2',
        'address_line3': 'addressLine3',
        'address_line4': 'addressLine4',
        'address_city': 'addressCity',
        'address_county_or_province': 'addressCountyOrProvince',
        'address_zip_or_postcode': 'addressZipOrPostcode',
        'address_country': 'addressCountry',
        'individual_national_identification': 'individualNationalIdentification',
        'individual_date_of_birth': 'individualDateOfBirth',
        'individual_title': 'individualTitle',
        'individual_first_name': 'individualFirstName',
        'individual_other_names': 'individualOtherNames',
        'individual_last_name': 'individualLastName',
        'company_name': 'companyName',
        'company_ein': 'companyEIN',
        'company_operating_name': 'companyOperatingName',
        'payment_channel_account_number': 'paymentChannelAccountNumber',
        'payment_channel_routing_number': 'paymentChannelRoutingNumber',
        'payment_channel_account_name': 'paymentChannelAccountName',
        'payment_channel_iban': 'paymentChannelIban',
        'payment_channel_country_code': 'paymentChannelCountryCode',
        'payment_channel_currency': 'paymentChannelCurrency',
        'challenge_description': 'challengeDescription',
        'challenge_value': 'challengeValue',
        'payee_language': 'payeeLanguage'
    }

    def __init__(self, type=None, remote_id=None, email=None, address_line1=None, address_line2=None, address_line3=None, address_line4=None, address_city=None, address_county_or_province=None, address_zip_or_postcode=None, address_country=None, individual_national_identification=None, individual_date_of_birth=None, individual_title=None, individual_first_name=None, individual_other_names=None, individual_last_name=None, company_name=None, company_ein=None, company_operating_name=None, payment_channel_account_number=None, payment_channel_routing_number=None, payment_channel_account_name=None, payment_channel_iban=None, payment_channel_country_code=None, payment_channel_currency=None, challenge_description=None, challenge_value=None, payee_language=None):  # noqa: E501
        """CreatePayeesCSVRequestV3 - a model defined in OpenAPI"""  # noqa: E501

        self._type = None
        self._remote_id = None
        self._email = None
        self._address_line1 = None
        self._address_line2 = None
        self._address_line3 = None
        self._address_line4 = None
        self._address_city = None
        self._address_county_or_province = None
        self._address_zip_or_postcode = None
        self._address_country = None
        self._individual_national_identification = None
        self._individual_date_of_birth = None
        self._individual_title = None
        self._individual_first_name = None
        self._individual_other_names = None
        self._individual_last_name = None
        self._company_name = None
        self._company_ein = None
        self._company_operating_name = None
        self._payment_channel_account_number = None
        self._payment_channel_routing_number = None
        self._payment_channel_account_name = None
        self._payment_channel_iban = None
        self._payment_channel_country_code = None
        self._payment_channel_currency = None
        self._challenge_description = None
        self._challenge_value = None
        self._payee_language = None
        self.discriminator = None

        self.type = type
        self.remote_id = remote_id
        self.email = email
        self.address_line1 = address_line1
        if address_line2 is not None:
            self.address_line2 = address_line2
        if address_line3 is not None:
            self.address_line3 = address_line3
        if address_line4 is not None:
            self.address_line4 = address_line4
        self.address_city = address_city
        if address_county_or_province is not None:
            self.address_county_or_province = address_county_or_province
        self.address_zip_or_postcode = address_zip_or_postcode
        self.address_country = address_country
        if individual_national_identification is not None:
            self.individual_national_identification = individual_national_identification
        if individual_date_of_birth is not None:
            self.individual_date_of_birth = individual_date_of_birth
        if individual_title is not None:
            self.individual_title = individual_title
        if individual_first_name is not None:
            self.individual_first_name = individual_first_name
        if individual_other_names is not None:
            self.individual_other_names = individual_other_names
        if individual_last_name is not None:
            self.individual_last_name = individual_last_name
        if company_name is not None:
            self.company_name = company_name
        if company_ein is not None:
            self.company_ein = company_ein
        if company_operating_name is not None:
            self.company_operating_name = company_operating_name
        if payment_channel_account_number is not None:
            self.payment_channel_account_number = payment_channel_account_number
        if payment_channel_routing_number is not None:
            self.payment_channel_routing_number = payment_channel_routing_number
        if payment_channel_account_name is not None:
            self.payment_channel_account_name = payment_channel_account_name
        if payment_channel_iban is not None:
            self.payment_channel_iban = payment_channel_iban
        if payment_channel_country_code is not None:
            self.payment_channel_country_code = payment_channel_country_code
        if payment_channel_currency is not None:
            self.payment_channel_currency = payment_channel_currency
        if challenge_description is not None:
            self.challenge_description = challenge_description
        if challenge_value is not None:
            self.challenge_value = challenge_value
        if payee_language is not None:
            self.payee_language = payee_language

    @property
    def type(self):
        """Gets the type of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The type of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: PayeeTypeEnum
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreatePayeesCSVRequestV3.


        :param type: The type of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: PayeeTypeEnum
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def remote_id(self):
        """Gets the remote_id of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The remote_id of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._remote_id

    @remote_id.setter
    def remote_id(self, remote_id):
        """Sets the remote_id of this CreatePayeesCSVRequestV3.


        :param remote_id: The remote_id of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if remote_id is None:
            raise ValueError("Invalid value for `remote_id`, must not be `None`")  # noqa: E501
        if remote_id is not None and len(remote_id) > 100:
            raise ValueError("Invalid value for `remote_id`, length must be less than or equal to `100`")  # noqa: E501
        if remote_id is not None and len(remote_id) < 1:
            raise ValueError("Invalid value for `remote_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._remote_id = remote_id

    @property
    def email(self):
        """Gets the email of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The email of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this CreatePayeesCSVRequestV3.


        :param email: The email of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if email is not None and len(email) < 3:
            raise ValueError("Invalid value for `email`, length must be greater than or equal to `3`")  # noqa: E501

        self._email = email

    @property
    def address_line1(self):
        """Gets the address_line1 of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_line1 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_line1

    @address_line1.setter
    def address_line1(self, address_line1):
        """Sets the address_line1 of this CreatePayeesCSVRequestV3.


        :param address_line1: The address_line1 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_line1 is None:
            raise ValueError("Invalid value for `address_line1`, must not be `None`")  # noqa: E501
        if address_line1 is not None and len(address_line1) > 100:
            raise ValueError("Invalid value for `address_line1`, length must be less than or equal to `100`")  # noqa: E501
        if address_line1 is not None and len(address_line1) < 2:
            raise ValueError("Invalid value for `address_line1`, length must be greater than or equal to `2`")  # noqa: E501

        self._address_line1 = address_line1

    @property
    def address_line2(self):
        """Gets the address_line2 of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_line2 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_line2

    @address_line2.setter
    def address_line2(self, address_line2):
        """Sets the address_line2 of this CreatePayeesCSVRequestV3.


        :param address_line2: The address_line2 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_line2 is not None and len(address_line2) > 100:
            raise ValueError("Invalid value for `address_line2`, length must be less than or equal to `100`")  # noqa: E501
        if address_line2 is not None and len(address_line2) < 0:
            raise ValueError("Invalid value for `address_line2`, length must be greater than or equal to `0`")  # noqa: E501

        self._address_line2 = address_line2

    @property
    def address_line3(self):
        """Gets the address_line3 of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_line3 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_line3

    @address_line3.setter
    def address_line3(self, address_line3):
        """Sets the address_line3 of this CreatePayeesCSVRequestV3.


        :param address_line3: The address_line3 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_line3 is not None and len(address_line3) > 100:
            raise ValueError("Invalid value for `address_line3`, length must be less than or equal to `100`")  # noqa: E501
        if address_line3 is not None and len(address_line3) < 0:
            raise ValueError("Invalid value for `address_line3`, length must be greater than or equal to `0`")  # noqa: E501

        self._address_line3 = address_line3

    @property
    def address_line4(self):
        """Gets the address_line4 of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_line4 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_line4

    @address_line4.setter
    def address_line4(self, address_line4):
        """Sets the address_line4 of this CreatePayeesCSVRequestV3.


        :param address_line4: The address_line4 of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_line4 is not None and len(address_line4) > 100:
            raise ValueError("Invalid value for `address_line4`, length must be less than or equal to `100`")  # noqa: E501
        if address_line4 is not None and len(address_line4) < 0:
            raise ValueError("Invalid value for `address_line4`, length must be greater than or equal to `0`")  # noqa: E501

        self._address_line4 = address_line4

    @property
    def address_city(self):
        """Gets the address_city of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_city of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this CreatePayeesCSVRequestV3.


        :param address_city: The address_city of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_city is None:
            raise ValueError("Invalid value for `address_city`, must not be `None`")  # noqa: E501
        if address_city is not None and len(address_city) > 50:
            raise ValueError("Invalid value for `address_city`, length must be less than or equal to `50`")  # noqa: E501
        if address_city is not None and len(address_city) < 2:
            raise ValueError("Invalid value for `address_city`, length must be greater than or equal to `2`")  # noqa: E501

        self._address_city = address_city

    @property
    def address_county_or_province(self):
        """Gets the address_county_or_province of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_county_or_province of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_county_or_province

    @address_county_or_province.setter
    def address_county_or_province(self, address_county_or_province):
        """Sets the address_county_or_province of this CreatePayeesCSVRequestV3.


        :param address_county_or_province: The address_county_or_province of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_county_or_province is not None and len(address_county_or_province) > 50:
            raise ValueError("Invalid value for `address_county_or_province`, length must be less than or equal to `50`")  # noqa: E501
        if address_county_or_province is not None and len(address_county_or_province) < 1:
            raise ValueError("Invalid value for `address_county_or_province`, length must be greater than or equal to `1`")  # noqa: E501

        self._address_county_or_province = address_county_or_province

    @property
    def address_zip_or_postcode(self):
        """Gets the address_zip_or_postcode of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The address_zip_or_postcode of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_zip_or_postcode

    @address_zip_or_postcode.setter
    def address_zip_or_postcode(self, address_zip_or_postcode):
        """Sets the address_zip_or_postcode of this CreatePayeesCSVRequestV3.


        :param address_zip_or_postcode: The address_zip_or_postcode of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_zip_or_postcode is None:
            raise ValueError("Invalid value for `address_zip_or_postcode`, must not be `None`")  # noqa: E501
        if address_zip_or_postcode is not None and len(address_zip_or_postcode) > 60:
            raise ValueError("Invalid value for `address_zip_or_postcode`, length must be less than or equal to `60`")  # noqa: E501
        if address_zip_or_postcode is not None and len(address_zip_or_postcode) < 1:
            raise ValueError("Invalid value for `address_zip_or_postcode`, length must be greater than or equal to `1`")  # noqa: E501

        self._address_zip_or_postcode = address_zip_or_postcode

    @property
    def address_country(self):
        """Gets the address_country of this CreatePayeesCSVRequestV3.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The address_country of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._address_country

    @address_country.setter
    def address_country(self, address_country):
        """Sets the address_country of this CreatePayeesCSVRequestV3.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param address_country: The address_country of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if address_country is None:
            raise ValueError("Invalid value for `address_country`, must not be `None`")  # noqa: E501
        if address_country is not None and len(address_country) > 2:
            raise ValueError("Invalid value for `address_country`, length must be less than or equal to `2`")  # noqa: E501
        if address_country is not None and len(address_country) < 2:
            raise ValueError("Invalid value for `address_country`, length must be greater than or equal to `2`")  # noqa: E501
        if address_country is not None and not re.search(r'^[A-Z]{2}$', address_country):  # noqa: E501
            raise ValueError(r"Invalid value for `address_country`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._address_country = address_country

    @property
    def individual_national_identification(self):
        """Gets the individual_national_identification of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The individual_national_identification of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._individual_national_identification

    @individual_national_identification.setter
    def individual_national_identification(self, individual_national_identification):
        """Sets the individual_national_identification of this CreatePayeesCSVRequestV3.


        :param individual_national_identification: The individual_national_identification of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if individual_national_identification is not None and len(individual_national_identification) > 30:
            raise ValueError("Invalid value for `individual_national_identification`, length must be less than or equal to `30`")  # noqa: E501
        if individual_national_identification is not None and len(individual_national_identification) < 6:
            raise ValueError("Invalid value for `individual_national_identification`, length must be greater than or equal to `6`")  # noqa: E501

        self._individual_national_identification = individual_national_identification

    @property
    def individual_date_of_birth(self):
        """Gets the individual_date_of_birth of this CreatePayeesCSVRequestV3.  # noqa: E501

        Must not be date in future. Example - 1970-05-20  # noqa: E501

        :return: The individual_date_of_birth of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: date
        """
        return self._individual_date_of_birth

    @individual_date_of_birth.setter
    def individual_date_of_birth(self, individual_date_of_birth):
        """Sets the individual_date_of_birth of this CreatePayeesCSVRequestV3.

        Must not be date in future. Example - 1970-05-20  # noqa: E501

        :param individual_date_of_birth: The individual_date_of_birth of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: date
        """

        self._individual_date_of_birth = individual_date_of_birth

    @property
    def individual_title(self):
        """Gets the individual_title of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The individual_title of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._individual_title

    @individual_title.setter
    def individual_title(self, individual_title):
        """Sets the individual_title of this CreatePayeesCSVRequestV3.


        :param individual_title: The individual_title of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if individual_title is not None and len(individual_title) > 40:
            raise ValueError("Invalid value for `individual_title`, length must be less than or equal to `40`")  # noqa: E501
        if individual_title is not None and len(individual_title) < 1:
            raise ValueError("Invalid value for `individual_title`, length must be greater than or equal to `1`")  # noqa: E501

        self._individual_title = individual_title

    @property
    def individual_first_name(self):
        """Gets the individual_first_name of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The individual_first_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._individual_first_name

    @individual_first_name.setter
    def individual_first_name(self, individual_first_name):
        """Sets the individual_first_name of this CreatePayeesCSVRequestV3.


        :param individual_first_name: The individual_first_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if individual_first_name is not None and len(individual_first_name) > 40:
            raise ValueError("Invalid value for `individual_first_name`, length must be less than or equal to `40`")  # noqa: E501
        if individual_first_name is not None and len(individual_first_name) < 1:
            raise ValueError("Invalid value for `individual_first_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._individual_first_name = individual_first_name

    @property
    def individual_other_names(self):
        """Gets the individual_other_names of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The individual_other_names of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._individual_other_names

    @individual_other_names.setter
    def individual_other_names(self, individual_other_names):
        """Sets the individual_other_names of this CreatePayeesCSVRequestV3.


        :param individual_other_names: The individual_other_names of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if individual_other_names is not None and len(individual_other_names) > 40:
            raise ValueError("Invalid value for `individual_other_names`, length must be less than or equal to `40`")  # noqa: E501
        if individual_other_names is not None and len(individual_other_names) < 1:
            raise ValueError("Invalid value for `individual_other_names`, length must be greater than or equal to `1`")  # noqa: E501

        self._individual_other_names = individual_other_names

    @property
    def individual_last_name(self):
        """Gets the individual_last_name of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The individual_last_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._individual_last_name

    @individual_last_name.setter
    def individual_last_name(self, individual_last_name):
        """Sets the individual_last_name of this CreatePayeesCSVRequestV3.


        :param individual_last_name: The individual_last_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if individual_last_name is not None and len(individual_last_name) > 40:
            raise ValueError("Invalid value for `individual_last_name`, length must be less than or equal to `40`")  # noqa: E501
        if individual_last_name is not None and len(individual_last_name) < 1:
            raise ValueError("Invalid value for `individual_last_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._individual_last_name = individual_last_name

    @property
    def company_name(self):
        """Gets the company_name of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The company_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreatePayeesCSVRequestV3.


        :param company_name: The company_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if company_name is not None and len(company_name) > 40:
            raise ValueError("Invalid value for `company_name`, length must be less than or equal to `40`")  # noqa: E501
        if company_name is not None and len(company_name) < 1:
            raise ValueError("Invalid value for `company_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._company_name = company_name

    @property
    def company_ein(self):
        """Gets the company_ein of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The company_ein of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._company_ein

    @company_ein.setter
    def company_ein(self, company_ein):
        """Sets the company_ein of this CreatePayeesCSVRequestV3.


        :param company_ein: The company_ein of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if company_ein is not None and len(company_ein) > 30:
            raise ValueError("Invalid value for `company_ein`, length must be less than or equal to `30`")  # noqa: E501
        if company_ein is not None and len(company_ein) < 6:
            raise ValueError("Invalid value for `company_ein`, length must be greater than or equal to `6`")  # noqa: E501

        self._company_ein = company_ein

    @property
    def company_operating_name(self):
        """Gets the company_operating_name of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The company_operating_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._company_operating_name

    @company_operating_name.setter
    def company_operating_name(self, company_operating_name):
        """Sets the company_operating_name of this CreatePayeesCSVRequestV3.


        :param company_operating_name: The company_operating_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if company_operating_name is not None and len(company_operating_name) > 100:
            raise ValueError("Invalid value for `company_operating_name`, length must be less than or equal to `100`")  # noqa: E501
        if company_operating_name is not None and len(company_operating_name) < 1:
            raise ValueError("Invalid value for `company_operating_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._company_operating_name = company_operating_name

    @property
    def payment_channel_account_number(self):
        """Gets the payment_channel_account_number of this CreatePayeesCSVRequestV3.  # noqa: E501

        Either routing number and account number or only iban must be set  # noqa: E501

        :return: The payment_channel_account_number of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_account_number

    @payment_channel_account_number.setter
    def payment_channel_account_number(self, payment_channel_account_number):
        """Sets the payment_channel_account_number of this CreatePayeesCSVRequestV3.

        Either routing number and account number or only iban must be set  # noqa: E501

        :param payment_channel_account_number: The payment_channel_account_number of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if payment_channel_account_number is not None and len(payment_channel_account_number) > 17:
            raise ValueError("Invalid value for `payment_channel_account_number`, length must be less than or equal to `17`")  # noqa: E501
        if payment_channel_account_number is not None and len(payment_channel_account_number) < 6:
            raise ValueError("Invalid value for `payment_channel_account_number`, length must be greater than or equal to `6`")  # noqa: E501

        self._payment_channel_account_number = payment_channel_account_number

    @property
    def payment_channel_routing_number(self):
        """Gets the payment_channel_routing_number of this CreatePayeesCSVRequestV3.  # noqa: E501

        Either routing number and account number or only iban must be set  # noqa: E501

        :return: The payment_channel_routing_number of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_routing_number

    @payment_channel_routing_number.setter
    def payment_channel_routing_number(self, payment_channel_routing_number):
        """Sets the payment_channel_routing_number of this CreatePayeesCSVRequestV3.

        Either routing number and account number or only iban must be set  # noqa: E501

        :param payment_channel_routing_number: The payment_channel_routing_number of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if payment_channel_routing_number is not None and len(payment_channel_routing_number) > 9:
            raise ValueError("Invalid value for `payment_channel_routing_number`, length must be less than or equal to `9`")  # noqa: E501
        if payment_channel_routing_number is not None and len(payment_channel_routing_number) < 9:
            raise ValueError("Invalid value for `payment_channel_routing_number`, length must be greater than or equal to `9`")  # noqa: E501

        self._payment_channel_routing_number = payment_channel_routing_number

    @property
    def payment_channel_account_name(self):
        """Gets the payment_channel_account_name of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The payment_channel_account_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_account_name

    @payment_channel_account_name.setter
    def payment_channel_account_name(self, payment_channel_account_name):
        """Sets the payment_channel_account_name of this CreatePayeesCSVRequestV3.


        :param payment_channel_account_name: The payment_channel_account_name of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """

        self._payment_channel_account_name = payment_channel_account_name

    @property
    def payment_channel_iban(self):
        """Gets the payment_channel_iban of this CreatePayeesCSVRequestV3.  # noqa: E501

        Must match the regular expression ```^[A-Za-z0-9]+$```.  # noqa: E501

        :return: The payment_channel_iban of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_iban

    @payment_channel_iban.setter
    def payment_channel_iban(self, payment_channel_iban):
        """Sets the payment_channel_iban of this CreatePayeesCSVRequestV3.

        Must match the regular expression ```^[A-Za-z0-9]+$```.  # noqa: E501

        :param payment_channel_iban: The payment_channel_iban of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if payment_channel_iban is not None and len(payment_channel_iban) > 34:
            raise ValueError("Invalid value for `payment_channel_iban`, length must be less than or equal to `34`")  # noqa: E501
        if payment_channel_iban is not None and len(payment_channel_iban) < 15:
            raise ValueError("Invalid value for `payment_channel_iban`, length must be greater than or equal to `15`")  # noqa: E501
        if payment_channel_iban is not None and not re.search(r'^[A-Za-z0-9]+$', payment_channel_iban):  # noqa: E501
            raise ValueError(r"Invalid value for `payment_channel_iban`, must be a follow pattern or equal to `/^[A-Za-z0-9]+$/`")  # noqa: E501

        self._payment_channel_iban = payment_channel_iban

    @property
    def payment_channel_country_code(self):
        """Gets the payment_channel_country_code of this CreatePayeesCSVRequestV3.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The payment_channel_country_code of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_country_code

    @payment_channel_country_code.setter
    def payment_channel_country_code(self, payment_channel_country_code):
        """Sets the payment_channel_country_code of this CreatePayeesCSVRequestV3.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param payment_channel_country_code: The payment_channel_country_code of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if payment_channel_country_code is not None and len(payment_channel_country_code) > 2:
            raise ValueError("Invalid value for `payment_channel_country_code`, length must be less than or equal to `2`")  # noqa: E501
        if payment_channel_country_code is not None and len(payment_channel_country_code) < 2:
            raise ValueError("Invalid value for `payment_channel_country_code`, length must be greater than or equal to `2`")  # noqa: E501
        if payment_channel_country_code is not None and not re.search(r'^[A-Z]{2}$', payment_channel_country_code):  # noqa: E501
            raise ValueError(r"Invalid value for `payment_channel_country_code`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._payment_channel_country_code = payment_channel_country_code

    @property
    def payment_channel_currency(self):
        """Gets the payment_channel_currency of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The payment_channel_currency of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payment_channel_currency

    @payment_channel_currency.setter
    def payment_channel_currency(self, payment_channel_currency):
        """Sets the payment_channel_currency of this CreatePayeesCSVRequestV3.


        :param payment_channel_currency: The payment_channel_currency of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if payment_channel_currency is not None and len(payment_channel_currency) > 3:
            raise ValueError("Invalid value for `payment_channel_currency`, length must be less than or equal to `3`")  # noqa: E501
        if payment_channel_currency is not None and len(payment_channel_currency) < 3:
            raise ValueError("Invalid value for `payment_channel_currency`, length must be greater than or equal to `3`")  # noqa: E501

        self._payment_channel_currency = payment_channel_currency

    @property
    def challenge_description(self):
        """Gets the challenge_description of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The challenge_description of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._challenge_description

    @challenge_description.setter
    def challenge_description(self, challenge_description):
        """Sets the challenge_description of this CreatePayeesCSVRequestV3.


        :param challenge_description: The challenge_description of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if challenge_description is not None and len(challenge_description) > 255:
            raise ValueError("Invalid value for `challenge_description`, length must be less than or equal to `255`")  # noqa: E501
        if challenge_description is not None and len(challenge_description) < 1:
            raise ValueError("Invalid value for `challenge_description`, length must be greater than or equal to `1`")  # noqa: E501

        self._challenge_description = challenge_description

    @property
    def challenge_value(self):
        """Gets the challenge_value of this CreatePayeesCSVRequestV3.  # noqa: E501


        :return: The challenge_value of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._challenge_value

    @challenge_value.setter
    def challenge_value(self, challenge_value):
        """Sets the challenge_value of this CreatePayeesCSVRequestV3.


        :param challenge_value: The challenge_value of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """
        if challenge_value is not None and len(challenge_value) > 20:
            raise ValueError("Invalid value for `challenge_value`, length must be less than or equal to `20`")  # noqa: E501
        if challenge_value is not None and len(challenge_value) < 3:
            raise ValueError("Invalid value for `challenge_value`, length must be greater than or equal to `3`")  # noqa: E501

        self._challenge_value = challenge_value

    @property
    def payee_language(self):
        """Gets the payee_language of this CreatePayeesCSVRequestV3.  # noqa: E501

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :return: The payee_language of this CreatePayeesCSVRequestV3.  # noqa: E501
        :rtype: str
        """
        return self._payee_language

    @payee_language.setter
    def payee_language(self, payee_language):
        """Sets the payee_language of this CreatePayeesCSVRequestV3.

        An IETF BCP 47 language code which has been configured for use within this Velo environment.<BR> See the /v1/supportedLanguages endpoint to list the available codes for an environment.   # noqa: E501

        :param payee_language: The payee_language of this CreatePayeesCSVRequestV3.  # noqa: E501
        :type: str
        """

        self._payee_language = payee_language

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
        if not isinstance(other, CreatePayeesCSVRequestV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
