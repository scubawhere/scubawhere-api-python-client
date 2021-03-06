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
from swagger_client.apis.course_api import CourseApi


class TestCourseApi(unittest.TestCase):
    """ CourseApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.course_api.CourseApi()

    def tearDown(self):
        pass

    def test_create_course(self):
        """
        Test case for create_course

        Create a new course
        """
        pass

    def test_delete_course(self):
        """
        Test case for delete_course

        Delete a course by ID
        """
        pass

    def test_edit_course(self):
        """
        Test case for edit_course

        Update a course by ID
        """
        pass

    def test_get_all_courses(self):
        """
        Test case for get_all_courses

        Retrieve all courses including any deleted models
        """
        pass

    def test_get_all_with_trashed_courses(self):
        """
        Test case for get_all_with_trashed_courses

        Retrieve all courses including any deleted models
        """
        pass

    def test_get_course(self):
        """
        Test case for get_course

        Retrieve a course by ID
        """
        pass


if __name__ == '__main__':
    unittest.main()
