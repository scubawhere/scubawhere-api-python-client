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
from swagger_client.apis.company_api import CompanyApi


class TestCompanyApi(unittest.TestCase):
    """ CompanyApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.company_api.CompanyApi()

    def tearDown(self):
        pass

    def test_attach_locations(self):
        """
        Test case for attach_locations

        Attach a location to a company
        """
        pass

    def test_get_locations(self):
        """
        Test case for get_locations

        Retrieve the locations this Dive Centre uses
        """
        pass

    def test_get_pickup_schedule(self):
        """
        Test case for get_pickup_schedule

        Retrieve the pick up schedule for a date
        """
        pass

    def test_update_company(self):
        """
        Test case for update_company

        Update the companies information
        """
        pass


if __name__ == '__main__':
    unittest.main()
