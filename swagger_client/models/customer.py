# coding: utf-8

"""
    Scubawhere API Documentation

    This is the documentation for scubawhere's RMS API. This API is only to be used by authorized parties with valid auth tokens.  [Learn about scubawhere](http://www.scubawhere.com) to become an authorized consumer of our API 

    OpenAPI spec version: 1.0.0
    Contact: bryan@scubawhere.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class Customer(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, email=None, firstname=None, lastname=None, verified=None, birthday=None, gender=None, address_1=None, address_2=None, city=None, county=None, postcode=None, country_id=None, phone=None, last_dive=None, number_of_dives=None, chest_size=None, shoe_size=None, height=None, cylinder_size=None, notes=None, unsubscribed=None, country=None):
        """
        Customer - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'email': 'str',
            'firstname': 'str',
            'lastname': 'str',
            'verified': 'int',
            'birthday': 'date',
            'gender': 'int',
            'address_1': 'str',
            'address_2': 'str',
            'city': 'str',
            'county': 'str',
            'postcode': 'str',
            'country_id': 'int',
            'phone': 'str',
            'last_dive': 'date',
            'number_of_dives': 'int',
            'chest_size': 'str',
            'shoe_size': 'str',
            'height': 'str',
            'cylinder_size': 'str',
            'notes': 'str',
            'unsubscribed': 'bool',
            'country': 'Country'
        }

        self.attribute_map = {
            'id': 'id',
            'email': 'email',
            'firstname': 'firstname',
            'lastname': 'lastname',
            'verified': 'verified',
            'birthday': 'birthday',
            'gender': 'gender',
            'address_1': 'address_1',
            'address_2': 'address_2',
            'city': 'city',
            'county': 'county',
            'postcode': 'postcode',
            'country_id': 'country_id',
            'phone': 'phone',
            'last_dive': 'last_dive',
            'number_of_dives': 'number_of_dives',
            'chest_size': 'chest_size',
            'shoe_size': 'shoe_size',
            'height': 'height',
            'cylinder_size': 'cylinder_size',
            'notes': 'notes',
            'unsubscribed': 'unsubscribed',
            'country': 'country'
        }

        self._id = id
        self._email = email
        self._firstname = firstname
        self._lastname = lastname
        self._verified = verified
        self._birthday = birthday
        self._gender = gender
        self._address_1 = address_1
        self._address_2 = address_2
        self._city = city
        self._county = county
        self._postcode = postcode
        self._country_id = country_id
        self._phone = phone
        self._last_dive = last_dive
        self._number_of_dives = number_of_dives
        self._chest_size = chest_size
        self._shoe_size = shoe_size
        self._height = height
        self._cylinder_size = cylinder_size
        self._notes = notes
        self._unsubscribed = unsubscribed
        self._country = country

    @property
    def id(self):
        """
        Gets the id of this Customer.


        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Customer.


        :param id: The id of this Customer.
        :type: int
        """

        self._id = id

    @property
    def email(self):
        """
        Gets the email of this Customer.


        :return: The email of this Customer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this Customer.


        :param email: The email of this Customer.
        :type: str
        """

        self._email = email

    @property
    def firstname(self):
        """
        Gets the firstname of this Customer.


        :return: The firstname of this Customer.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """
        Sets the firstname of this Customer.


        :param firstname: The firstname of this Customer.
        :type: str
        """

        self._firstname = firstname

    @property
    def lastname(self):
        """
        Gets the lastname of this Customer.


        :return: The lastname of this Customer.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """
        Sets the lastname of this Customer.


        :param lastname: The lastname of this Customer.
        :type: str
        """

        self._lastname = lastname

    @property
    def verified(self):
        """
        Gets the verified of this Customer.


        :return: The verified of this Customer.
        :rtype: int
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """
        Sets the verified of this Customer.


        :param verified: The verified of this Customer.
        :type: int
        """

        self._verified = verified

    @property
    def birthday(self):
        """
        Gets the birthday of this Customer.


        :return: The birthday of this Customer.
        :rtype: date
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """
        Sets the birthday of this Customer.


        :param birthday: The birthday of this Customer.
        :type: date
        """

        self._birthday = birthday

    @property
    def gender(self):
        """
        Gets the gender of this Customer.


        :return: The gender of this Customer.
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """
        Sets the gender of this Customer.


        :param gender: The gender of this Customer.
        :type: int
        """

        self._gender = gender

    @property
    def address_1(self):
        """
        Gets the address_1 of this Customer.


        :return: The address_1 of this Customer.
        :rtype: str
        """
        return self._address_1

    @address_1.setter
    def address_1(self, address_1):
        """
        Sets the address_1 of this Customer.


        :param address_1: The address_1 of this Customer.
        :type: str
        """

        self._address_1 = address_1

    @property
    def address_2(self):
        """
        Gets the address_2 of this Customer.


        :return: The address_2 of this Customer.
        :rtype: str
        """
        return self._address_2

    @address_2.setter
    def address_2(self, address_2):
        """
        Sets the address_2 of this Customer.


        :param address_2: The address_2 of this Customer.
        :type: str
        """

        self._address_2 = address_2

    @property
    def city(self):
        """
        Gets the city of this Customer.


        :return: The city of this Customer.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this Customer.


        :param city: The city of this Customer.
        :type: str
        """

        self._city = city

    @property
    def county(self):
        """
        Gets the county of this Customer.


        :return: The county of this Customer.
        :rtype: str
        """
        return self._county

    @county.setter
    def county(self, county):
        """
        Sets the county of this Customer.


        :param county: The county of this Customer.
        :type: str
        """

        self._county = county

    @property
    def postcode(self):
        """
        Gets the postcode of this Customer.


        :return: The postcode of this Customer.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """
        Sets the postcode of this Customer.


        :param postcode: The postcode of this Customer.
        :type: str
        """

        self._postcode = postcode

    @property
    def country_id(self):
        """
        Gets the country_id of this Customer.


        :return: The country_id of this Customer.
        :rtype: int
        """
        return self._country_id

    @country_id.setter
    def country_id(self, country_id):
        """
        Sets the country_id of this Customer.


        :param country_id: The country_id of this Customer.
        :type: int
        """

        self._country_id = country_id

    @property
    def phone(self):
        """
        Gets the phone of this Customer.


        :return: The phone of this Customer.
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """
        Sets the phone of this Customer.


        :param phone: The phone of this Customer.
        :type: str
        """

        self._phone = phone

    @property
    def last_dive(self):
        """
        Gets the last_dive of this Customer.


        :return: The last_dive of this Customer.
        :rtype: date
        """
        return self._last_dive

    @last_dive.setter
    def last_dive(self, last_dive):
        """
        Sets the last_dive of this Customer.


        :param last_dive: The last_dive of this Customer.
        :type: date
        """

        self._last_dive = last_dive

    @property
    def number_of_dives(self):
        """
        Gets the number_of_dives of this Customer.


        :return: The number_of_dives of this Customer.
        :rtype: int
        """
        return self._number_of_dives

    @number_of_dives.setter
    def number_of_dives(self, number_of_dives):
        """
        Sets the number_of_dives of this Customer.


        :param number_of_dives: The number_of_dives of this Customer.
        :type: int
        """

        self._number_of_dives = number_of_dives

    @property
    def chest_size(self):
        """
        Gets the chest_size of this Customer.


        :return: The chest_size of this Customer.
        :rtype: str
        """
        return self._chest_size

    @chest_size.setter
    def chest_size(self, chest_size):
        """
        Sets the chest_size of this Customer.


        :param chest_size: The chest_size of this Customer.
        :type: str
        """

        self._chest_size = chest_size

    @property
    def shoe_size(self):
        """
        Gets the shoe_size of this Customer.


        :return: The shoe_size of this Customer.
        :rtype: str
        """
        return self._shoe_size

    @shoe_size.setter
    def shoe_size(self, shoe_size):
        """
        Sets the shoe_size of this Customer.


        :param shoe_size: The shoe_size of this Customer.
        :type: str
        """

        self._shoe_size = shoe_size

    @property
    def height(self):
        """
        Gets the height of this Customer.


        :return: The height of this Customer.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this Customer.


        :param height: The height of this Customer.
        :type: str
        """

        self._height = height

    @property
    def cylinder_size(self):
        """
        Gets the cylinder_size of this Customer.


        :return: The cylinder_size of this Customer.
        :rtype: str
        """
        return self._cylinder_size

    @cylinder_size.setter
    def cylinder_size(self, cylinder_size):
        """
        Sets the cylinder_size of this Customer.


        :param cylinder_size: The cylinder_size of this Customer.
        :type: str
        """

        self._cylinder_size = cylinder_size

    @property
    def notes(self):
        """
        Gets the notes of this Customer.


        :return: The notes of this Customer.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """
        Sets the notes of this Customer.


        :param notes: The notes of this Customer.
        :type: str
        """

        self._notes = notes

    @property
    def unsubscribed(self):
        """
        Gets the unsubscribed of this Customer.


        :return: The unsubscribed of this Customer.
        :rtype: bool
        """
        return self._unsubscribed

    @unsubscribed.setter
    def unsubscribed(self, unsubscribed):
        """
        Sets the unsubscribed of this Customer.


        :param unsubscribed: The unsubscribed of this Customer.
        :type: bool
        """

        self._unsubscribed = unsubscribed

    @property
    def country(self):
        """
        Gets the country of this Customer.


        :return: The country of this Customer.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Customer.


        :param country: The country of this Customer.
        :type: Country
        """

        self._country = country

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
