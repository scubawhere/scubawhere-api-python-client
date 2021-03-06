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

from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.customer_api import CustomerApi


class TestCustomerApi(unittest.TestCase):
    """ CustomerApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.customer_api.CustomerApi()

    def tearDown(self):
        pass

    def test_create_customer(self):
        """
        Test case for create_customer

        Create a new customer
        """
        pass

    def test_delete_customer(self):
        """
        Test case for delete_customer

        Delete a customer by ID
        """
        pass

    def test_edit_customer(self):
        """
        Test case for edit_customer

        Update a customer by ID
        """
        pass

    def test_get_all_customers(self):
        """
        Test case for get_all_customers

        Retrieve all customers
        """
        pass

    def test_get_customer(self):
        """
        Test case for get_customer

        Retrieve a customer by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
