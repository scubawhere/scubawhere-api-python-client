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


class Booking(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, reference=None, lead_customer_id=None, agent_id=None, agent_reference=None, source=None, price=None, discount=None, status=None, reserved_until=None, cancellation_fee=None, comment=None, parent_id=None, decimal_price=None, real_decimal_price=None, arrival_date=None, created_at_local=None, lead_customer=None, payments=None, refunds=None):
        """
        Booking - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'reference': 'str',
            'lead_customer_id': 'int',
            'agent_id': 'int',
            'agent_reference': 'str',
            'source': 'str',
            'price': 'int',
            'discount': 'int',
            'status': 'str',
            'reserved_until': 'date',
            'cancellation_fee': 'int',
            'comment': 'str',
            'parent_id': 'int',
            'decimal_price': 'str',
            'real_decimal_price': 'str',
            'arrival_date': 'date',
            'created_at_local': 'date',
            'lead_customer': 'Customer',
            'payments': 'list[Payment]',
            'refunds': 'list[Refund]'
        }

        self.attribute_map = {
            'id': 'id',
            'reference': 'reference',
            'lead_customer_id': 'lead_customer_id',
            'agent_id': 'agent_id',
            'agent_reference': 'agent_reference',
            'source': 'source',
            'price': 'price',
            'discount': 'discount',
            'status': 'status',
            'reserved_until': 'reserved_until',
            'cancellation_fee': 'cancellation_fee',
            'comment': 'comment',
            'parent_id': 'parent_id',
            'decimal_price': 'decimal_price',
            'real_decimal_price': 'real_decimal_price',
            'arrival_date': 'arrival_date',
            'created_at_local': 'created_at_local',
            'lead_customer': 'lead_customer',
            'payments': 'payments',
            'refunds': 'refunds'
        }

        self._id = id
        self._reference = reference
        self._lead_customer_id = lead_customer_id
        self._agent_id = agent_id
        self._agent_reference = agent_reference
        self._source = source
        self._price = price
        self._discount = discount
        self._status = status
        self._reserved_until = reserved_until
        self._cancellation_fee = cancellation_fee
        self._comment = comment
        self._parent_id = parent_id
        self._decimal_price = decimal_price
        self._real_decimal_price = real_decimal_price
        self._arrival_date = arrival_date
        self._created_at_local = created_at_local
        self._lead_customer = lead_customer
        self._payments = payments
        self._refunds = refunds

    @property
    def id(self):
        """
        Gets the id of this Booking.


        :return: The id of this Booking.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Booking.


        :param id: The id of this Booking.
        :type: int
        """

        self._id = id

    @property
    def reference(self):
        """
        Gets the reference of this Booking.


        :return: The reference of this Booking.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference of this Booking.


        :param reference: The reference of this Booking.
        :type: str
        """

        self._reference = reference

    @property
    def lead_customer_id(self):
        """
        Gets the lead_customer_id of this Booking.


        :return: The lead_customer_id of this Booking.
        :rtype: int
        """
        return self._lead_customer_id

    @lead_customer_id.setter
    def lead_customer_id(self, lead_customer_id):
        """
        Sets the lead_customer_id of this Booking.


        :param lead_customer_id: The lead_customer_id of this Booking.
        :type: int
        """

        self._lead_customer_id = lead_customer_id

    @property
    def agent_id(self):
        """
        Gets the agent_id of this Booking.


        :return: The agent_id of this Booking.
        :rtype: int
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this Booking.


        :param agent_id: The agent_id of this Booking.
        :type: int
        """

        self._agent_id = agent_id

    @property
    def agent_reference(self):
        """
        Gets the agent_reference of this Booking.


        :return: The agent_reference of this Booking.
        :rtype: str
        """
        return self._agent_reference

    @agent_reference.setter
    def agent_reference(self, agent_reference):
        """
        Sets the agent_reference of this Booking.


        :param agent_reference: The agent_reference of this Booking.
        :type: str
        """

        self._agent_reference = agent_reference

    @property
    def source(self):
        """
        Gets the source of this Booking.


        :return: The source of this Booking.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Booking.


        :param source: The source of this Booking.
        :type: str
        """

        self._source = source

    @property
    def price(self):
        """
        Gets the price of this Booking.


        :return: The price of this Booking.
        :rtype: int
        """
        return self._price

    @price.setter
    def price(self, price):
        """
        Sets the price of this Booking.


        :param price: The price of this Booking.
        :type: int
        """

        self._price = price

    @property
    def discount(self):
        """
        Gets the discount of this Booking.


        :return: The discount of this Booking.
        :rtype: int
        """
        return self._discount

    @discount.setter
    def discount(self, discount):
        """
        Sets the discount of this Booking.


        :param discount: The discount of this Booking.
        :type: int
        """

        self._discount = discount

    @property
    def status(self):
        """
        Gets the status of this Booking.


        :return: The status of this Booking.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this Booking.


        :param status: The status of this Booking.
        :type: str
        """

        self._status = status

    @property
    def reserved_until(self):
        """
        Gets the reserved_until of this Booking.


        :return: The reserved_until of this Booking.
        :rtype: date
        """
        return self._reserved_until

    @reserved_until.setter
    def reserved_until(self, reserved_until):
        """
        Sets the reserved_until of this Booking.


        :param reserved_until: The reserved_until of this Booking.
        :type: date
        """

        self._reserved_until = reserved_until

    @property
    def cancellation_fee(self):
        """
        Gets the cancellation_fee of this Booking.


        :return: The cancellation_fee of this Booking.
        :rtype: int
        """
        return self._cancellation_fee

    @cancellation_fee.setter
    def cancellation_fee(self, cancellation_fee):
        """
        Sets the cancellation_fee of this Booking.


        :param cancellation_fee: The cancellation_fee of this Booking.
        :type: int
        """

        self._cancellation_fee = cancellation_fee

    @property
    def comment(self):
        """
        Gets the comment of this Booking.


        :return: The comment of this Booking.
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """
        Sets the comment of this Booking.


        :param comment: The comment of this Booking.
        :type: str
        """

        self._comment = comment

    @property
    def parent_id(self):
        """
        Gets the parent_id of this Booking.


        :return: The parent_id of this Booking.
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """
        Sets the parent_id of this Booking.


        :param parent_id: The parent_id of this Booking.
        :type: int
        """

        self._parent_id = parent_id

    @property
    def decimal_price(self):
        """
        Gets the decimal_price of this Booking.


        :return: The decimal_price of this Booking.
        :rtype: str
        """
        return self._decimal_price

    @decimal_price.setter
    def decimal_price(self, decimal_price):
        """
        Sets the decimal_price of this Booking.


        :param decimal_price: The decimal_price of this Booking.
        :type: str
        """

        self._decimal_price = decimal_price

    @property
    def real_decimal_price(self):
        """
        Gets the real_decimal_price of this Booking.


        :return: The real_decimal_price of this Booking.
        :rtype: str
        """
        return self._real_decimal_price

    @real_decimal_price.setter
    def real_decimal_price(self, real_decimal_price):
        """
        Sets the real_decimal_price of this Booking.


        :param real_decimal_price: The real_decimal_price of this Booking.
        :type: str
        """

        self._real_decimal_price = real_decimal_price

    @property
    def arrival_date(self):
        """
        Gets the arrival_date of this Booking.


        :return: The arrival_date of this Booking.
        :rtype: date
        """
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, arrival_date):
        """
        Sets the arrival_date of this Booking.


        :param arrival_date: The arrival_date of this Booking.
        :type: date
        """

        self._arrival_date = arrival_date

    @property
    def created_at_local(self):
        """
        Gets the created_at_local of this Booking.


        :return: The created_at_local of this Booking.
        :rtype: date
        """
        return self._created_at_local

    @created_at_local.setter
    def created_at_local(self, created_at_local):
        """
        Sets the created_at_local of this Booking.


        :param created_at_local: The created_at_local of this Booking.
        :type: date
        """

        self._created_at_local = created_at_local

    @property
    def lead_customer(self):
        """
        Gets the lead_customer of this Booking.


        :return: The lead_customer of this Booking.
        :rtype: Customer
        """
        return self._lead_customer

    @lead_customer.setter
    def lead_customer(self, lead_customer):
        """
        Sets the lead_customer of this Booking.


        :param lead_customer: The lead_customer of this Booking.
        :type: Customer
        """

        self._lead_customer = lead_customer

    @property
    def payments(self):
        """
        Gets the payments of this Booking.


        :return: The payments of this Booking.
        :rtype: list[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments):
        """
        Sets the payments of this Booking.


        :param payments: The payments of this Booking.
        :type: list[Payment]
        """

        self._payments = payments

    @property
    def refunds(self):
        """
        Gets the refunds of this Booking.


        :return: The refunds of this Booking.
        :rtype: list[Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """
        Sets the refunds of this Booking.


        :param refunds: The refunds of this Booking.
        :type: list[Refund]
        """

        self._refunds = refunds

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
