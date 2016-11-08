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


class Location(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, name=None, description=None, latitude=None, longitude=None):
        """
        Location - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'description': 'str',
            'latitude': 'float',
            'longitude': 'float'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'latitude': 'latitude',
            'longitude': 'longitude'
        }

        self._id = id
        self._name = name
        self._description = description
        self._latitude = latitude
        self._longitude = longitude

    @property
    def id(self):
        """
        Gets the id of this Location.


        :return: The id of this Location.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Location.


        :param id: The id of this Location.
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """
        Gets the name of this Location.


        :return: The name of this Location.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Location.


        :param name: The name of this Location.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Location.


        :return: The description of this Location.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Location.


        :param description: The description of this Location.
        :type: str
        """

        self._description = description

    @property
    def latitude(self):
        """
        Gets the latitude of this Location.


        :return: The latitude of this Location.
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """
        Sets the latitude of this Location.


        :param latitude: The latitude of this Location.
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """
        Gets the longitude of this Location.


        :return: The longitude of this Location.
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """
        Sets the longitude of this Location.


        :param longitude: The longitude of this Location.
        :type: float
        """

        self._longitude = longitude

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