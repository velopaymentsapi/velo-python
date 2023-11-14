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


class CreatePayeeAddressV4(object):
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
        'line1': 'str',
        'line2': 'str',
        'line3': 'str',
        'line4': 'str',
        'city': 'str',
        'county_or_province': 'str',
        'zip_or_postcode': 'str',
        'country': 'str'
    }

    attribute_map = {
        'line1': 'line1',
        'line2': 'line2',
        'line3': 'line3',
        'line4': 'line4',
        'city': 'city',
        'county_or_province': 'countyOrProvince',
        'zip_or_postcode': 'zipOrPostcode',
        'country': 'country'
    }

    def __init__(self, line1=None, line2=None, line3=None, line4=None, city=None, county_or_province=None, zip_or_postcode=None, country=None):  # noqa: E501
        """CreatePayeeAddressV4 - a model defined in OpenAPI"""  # noqa: E501

        self._line1 = None
        self._line2 = None
        self._line3 = None
        self._line4 = None
        self._city = None
        self._county_or_province = None
        self._zip_or_postcode = None
        self._country = None
        self.discriminator = None

        self.line1 = line1
        self.line2 = line2
        self.line3 = line3
        self.line4 = line4
        self.city = city
        self.county_or_province = county_or_province
        self.zip_or_postcode = zip_or_postcode
        self.country = country

    @property
    def line1(self):
        """Gets the line1 of this CreatePayeeAddressV4.  # noqa: E501


        :return: The line1 of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this CreatePayeeAddressV4.


        :param line1: The line1 of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if line1 is None:
            raise ValueError("Invalid value for `line1`, must not be `None`")  # noqa: E501
        if line1 is not None and len(line1) > 100:
            raise ValueError("Invalid value for `line1`, length must be less than or equal to `100`")  # noqa: E501
        if line1 is not None and len(line1) < 1:
            raise ValueError("Invalid value for `line1`, length must be greater than or equal to `1`")  # noqa: E501

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this CreatePayeeAddressV4.  # noqa: E501


        :return: The line2 of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this CreatePayeeAddressV4.


        :param line2: The line2 of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if line2 is not None and len(line2) > 100:
            raise ValueError("Invalid value for `line2`, length must be less than or equal to `100`")  # noqa: E501
        if line2 is not None and len(line2) < 0:
            raise ValueError("Invalid value for `line2`, length must be greater than or equal to `0`")  # noqa: E501

        self._line2 = line2

    @property
    def line3(self):
        """Gets the line3 of this CreatePayeeAddressV4.  # noqa: E501


        :return: The line3 of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """Sets the line3 of this CreatePayeeAddressV4.


        :param line3: The line3 of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if line3 is not None and len(line3) > 100:
            raise ValueError("Invalid value for `line3`, length must be less than or equal to `100`")  # noqa: E501
        if line3 is not None and len(line3) < 0:
            raise ValueError("Invalid value for `line3`, length must be greater than or equal to `0`")  # noqa: E501

        self._line3 = line3

    @property
    def line4(self):
        """Gets the line4 of this CreatePayeeAddressV4.  # noqa: E501


        :return: The line4 of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._line4

    @line4.setter
    def line4(self, line4):
        """Sets the line4 of this CreatePayeeAddressV4.


        :param line4: The line4 of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if line4 is not None and len(line4) > 100:
            raise ValueError("Invalid value for `line4`, length must be less than or equal to `100`")  # noqa: E501
        if line4 is not None and len(line4) < 0:
            raise ValueError("Invalid value for `line4`, length must be greater than or equal to `0`")  # noqa: E501

        self._line4 = line4

    @property
    def city(self):
        """Gets the city of this CreatePayeeAddressV4.  # noqa: E501


        :return: The city of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreatePayeeAddressV4.


        :param city: The city of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501
        if city is not None and len(city) > 50:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `50`")  # noqa: E501
        if city is not None and len(city) < 2:
            raise ValueError("Invalid value for `city`, length must be greater than or equal to `2`")  # noqa: E501

        self._city = city

    @property
    def county_or_province(self):
        """Gets the county_or_province of this CreatePayeeAddressV4.  # noqa: E501


        :return: The county_or_province of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._county_or_province

    @county_or_province.setter
    def county_or_province(self, county_or_province):
        """Sets the county_or_province of this CreatePayeeAddressV4.


        :param county_or_province: The county_or_province of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if county_or_province is not None and len(county_or_province) > 50:
            raise ValueError("Invalid value for `county_or_province`, length must be less than or equal to `50`")  # noqa: E501
        if county_or_province is not None and len(county_or_province) < 2:
            raise ValueError("Invalid value for `county_or_province`, length must be greater than or equal to `2`")  # noqa: E501

        self._county_or_province = county_or_province

    @property
    def zip_or_postcode(self):
        """Gets the zip_or_postcode of this CreatePayeeAddressV4.  # noqa: E501


        :return: The zip_or_postcode of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._zip_or_postcode

    @zip_or_postcode.setter
    def zip_or_postcode(self, zip_or_postcode):
        """Sets the zip_or_postcode of this CreatePayeeAddressV4.


        :param zip_or_postcode: The zip_or_postcode of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if zip_or_postcode is not None and len(zip_or_postcode) > 60:
            raise ValueError("Invalid value for `zip_or_postcode`, length must be less than or equal to `60`")  # noqa: E501
        if zip_or_postcode is not None and len(zip_or_postcode) < 2:
            raise ValueError("Invalid value for `zip_or_postcode`, length must be greater than or equal to `2`")  # noqa: E501

        self._zip_or_postcode = zip_or_postcode

    @property
    def country(self):
        """Gets the country of this CreatePayeeAddressV4.  # noqa: E501

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :return: The country of this CreatePayeeAddressV4.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreatePayeeAddressV4.

        Valid ISO 3166 2 character country code. See the <a href=\"https://www.iso.org/iso-3166-country-codes.html\" target=\"_blank\" a>ISO specification</a> for details.  # noqa: E501

        :param country: The country of this CreatePayeeAddressV4.  # noqa: E501
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")  # noqa: E501
        if country is not None and len(country) < 2:
            raise ValueError("Invalid value for `country`, length must be greater than or equal to `2`")  # noqa: E501
        if country is not None and not re.search(r'^[A-Z]{2}$', country):  # noqa: E501
            raise ValueError(r"Invalid value for `country`, must be a follow pattern or equal to `/^[A-Z]{2}$/`")  # noqa: E501

        self._country = country

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
        if not isinstance(other, CreatePayeeAddressV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
