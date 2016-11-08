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

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CompanyApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def attach_locations(self, **kwargs):
        """
        Attach a location to a company
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_locations(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: 
        :param str description: 
        :param float latitude: 
        :param float longitude: 
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.attach_locations_with_http_info(**kwargs)
        else:
            (data) = self.attach_locations_with_http_info(**kwargs)
            return data

    def attach_locations_with_http_info(self, **kwargs):
        """
        Attach a location to a company
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.attach_locations_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str name: 
        :param str description: 
        :param float latitude: 
        :param float longitude: 
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['name', 'description', 'latitude', 'longitude']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method attach_locations" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/company/add-location'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'name' in params:
            query_params['name'] = params['name']
        if 'description' in params:
            query_params['description'] = params['description']
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20023',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_locations(self, latitude, longitude, **kwargs):
        """
        Retrieve the locations this Dive Centre uses
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_locations(latitude, longitude, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str latitude:  (required)
        :param str longitude:  (required)
        :param int limit: 
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_locations_with_http_info(latitude, longitude, **kwargs)
        else:
            (data) = self.get_locations_with_http_info(latitude, longitude, **kwargs)
            return data

    def get_locations_with_http_info(self, latitude, longitude, **kwargs):
        """
        Retrieve the locations this Dive Centre uses
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_locations_with_http_info(latitude, longitude, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str latitude:  (required)
        :param str longitude:  (required)
        :param int limit: 
        :return: InlineResponse20024
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['latitude', 'longitude', 'limit']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_locations" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'latitude' is set
        if ('latitude' not in params) or (params['latitude'] is None):
            raise ValueError("Missing the required parameter `latitude` when calling `get_locations`")
        # verify the required parameter 'longitude' is set
        if ('longitude' not in params) or (params['longitude'] is None):
            raise ValueError("Missing the required parameter `longitude` when calling `get_locations`")

        resource_path = '/company/locations'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'latitude' in params:
            query_params['latitude'] = params['latitude']
        if 'longitude' in params:
            query_params['longitude'] = params['longitude']
        if 'limit' in params:
            query_params['limit'] = params['limit']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20024',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_pickup_schedule(self, date, **kwargs):
        """
        Retrieve the pick up schedule for a date
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pickup_schedule(date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date:  (required)
        :return: InlineResponse20025
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_pickup_schedule_with_http_info(date, **kwargs)
        else:
            (data) = self.get_pickup_schedule_with_http_info(date, **kwargs)
            return data

    def get_pickup_schedule_with_http_info(self, date, **kwargs):
        """
        Retrieve the pick up schedule for a date
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_pickup_schedule_with_http_info(date, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str date:  (required)
        :return: InlineResponse20025
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pickup_schedule" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'date' is set
        if ('date' not in params) or (params['date'] is None):
            raise ValueError("Missing the required parameter `date` when calling `get_pickup_schedule`")

        resource_path = '/company/pick-up-schedule'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'date' in params:
            query_params['date'] = params['date']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20025',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def update_company(self, id, **kwargs):
        """
        Update the companies information
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_company(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id:  (required)
        :param str contact: 
        :param str description: 
        :param str name: 
        :param str address_1: 
        :param str address_2: 
        :param str city: 
        :param str county: 
        :param str postcode: 
        :param int country_id: 
        :param int currency_id: 
        :param str business_phone: 
        :param str business_email: 
        :param str vat_number: 
        :param str registration_number: 
        :param str website: 
        :return: InlineResponse20026
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_company_with_http_info(id, **kwargs)
        else:
            (data) = self.update_company_with_http_info(id, **kwargs)
            return data

    def update_company_with_http_info(self, id, **kwargs):
        """
        Update the companies information
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_company_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id:  (required)
        :param str contact: 
        :param str description: 
        :param str name: 
        :param str address_1: 
        :param str address_2: 
        :param str city: 
        :param str county: 
        :param str postcode: 
        :param int country_id: 
        :param int currency_id: 
        :param str business_phone: 
        :param str business_email: 
        :param str vat_number: 
        :param str registration_number: 
        :param str website: 
        :return: InlineResponse20026
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'contact', 'description', 'name', 'address_1', 'address_2', 'city', 'county', 'postcode', 'country_id', 'currency_id', 'business_phone', 'business_email', 'vat_number', 'registration_number', 'website']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_company" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_company`")

        resource_path = '/company/update'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']
        if 'contact' in params:
            query_params['contact'] = params['contact']
        if 'description' in params:
            query_params['description'] = params['description']
        if 'name' in params:
            query_params['name'] = params['name']
        if 'address_1' in params:
            query_params['address_1'] = params['address_1']
        if 'address_2' in params:
            query_params['address_2'] = params['address_2']
        if 'city' in params:
            query_params['city'] = params['city']
        if 'county' in params:
            query_params['county'] = params['county']
        if 'postcode' in params:
            query_params['postcode'] = params['postcode']
        if 'country_id' in params:
            query_params['country_id'] = params['country_id']
        if 'currency_id' in params:
            query_params['currency_id'] = params['currency_id']
        if 'business_phone' in params:
            query_params['business_phone'] = params['business_phone']
        if 'business_email' in params:
            query_params['business_email'] = params['business_email']
        if 'vat_number' in params:
            query_params['vat_number'] = params['vat_number']
        if 'registration_number' in params:
            query_params['registration_number'] = params['registration_number']
        if 'website' in params:
            query_params['website'] = params['website']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'POST',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='InlineResponse20026',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))