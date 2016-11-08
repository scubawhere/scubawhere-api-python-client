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


class Session(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, trip=None, start=None, boat=None, timetable_id=None):
        """
        Session - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'trip': 'Trip',
            'start': 'date',
            'boat': 'Boat',
            'timetable_id': 'int'
        }

        self.attribute_map = {
            'id': 'id',
            'trip': 'trip',
            'start': 'start',
            'boat': 'boat',
            'timetable_id': 'timetable_id'
        }

        self._id = id
        self._trip = trip
        self._start = start
        self._boat = boat
        self._timetable_id = timetable_id

    @property
    def id(self):
        """
        Gets the id of this Session.


        :return: The id of this Session.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Session.


        :param id: The id of this Session.
        :type: int
        """

        self._id = id

    @property
    def trip(self):
        """
        Gets the trip of this Session.


        :return: The trip of this Session.
        :rtype: Trip
        """
        return self._trip

    @trip.setter
    def trip(self, trip):
        """
        Sets the trip of this Session.


        :param trip: The trip of this Session.
        :type: Trip
        """

        self._trip = trip

    @property
    def start(self):
        """
        Gets the start of this Session.


        :return: The start of this Session.
        :rtype: date
        """
        return self._start

    @start.setter
    def start(self, start):
        """
        Sets the start of this Session.


        :param start: The start of this Session.
        :type: date
        """

        self._start = start

    @property
    def boat(self):
        """
        Gets the boat of this Session.


        :return: The boat of this Session.
        :rtype: Boat
        """
        return self._boat

    @boat.setter
    def boat(self, boat):
        """
        Sets the boat of this Session.


        :param boat: The boat of this Session.
        :type: Boat
        """

        self._boat = boat

    @property
    def timetable_id(self):
        """
        Gets the timetable_id of this Session.


        :return: The timetable_id of this Session.
        :rtype: int
        """
        return self._timetable_id

    @timetable_id.setter
    def timetable_id(self, timetable_id):
        """
        Sets the timetable_id of this Session.


        :param timetable_id: The timetable_id of this Session.
        :type: int
        """

        self._timetable_id = timetable_id

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
