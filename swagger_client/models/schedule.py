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


class Schedule(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, weeks=None, schedule=None):
        """
        Schedule - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'weeks': 'str',
            'schedule': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'weeks': 'weeks',
            'schedule': 'schedule'
        }

        self._id = id
        self._weeks = weeks
        self._schedule = schedule

    @property
    def id(self):
        """
        Gets the id of this Schedule.


        :return: The id of this Schedule.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Schedule.


        :param id: The id of this Schedule.
        :type: int
        """

        self._id = id

    @property
    def weeks(self):
        """
        Gets the weeks of this Schedule.


        :return: The weeks of this Schedule.
        :rtype: str
        """
        return self._weeks

    @weeks.setter
    def weeks(self, weeks):
        """
        Sets the weeks of this Schedule.


        :param weeks: The weeks of this Schedule.
        :type: str
        """

        self._weeks = weeks

    @property
    def schedule(self):
        """
        Gets the schedule of this Schedule.


        :return: The schedule of this Schedule.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this Schedule.


        :param schedule: The schedule of this Schedule.
        :type: str
        """

        self._schedule = schedule

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
