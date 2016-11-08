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


class RefundApi(object):
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

    def add_refund(self, booking_id, paymentgateway_id, amount, **kwargs):
        """
        Create a new refund
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_refund(booking_id, paymentgateway_id, amount, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int booking_id:  (required)
        :param int paymentgateway_id:  (required)
        :param float amount:  (required)
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_refund_with_http_info(booking_id, paymentgateway_id, amount, **kwargs)
        else:
            (data) = self.add_refund_with_http_info(booking_id, paymentgateway_id, amount, **kwargs)
            return data

    def add_refund_with_http_info(self, booking_id, paymentgateway_id, amount, **kwargs):
        """
        Create a new refund
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_refund_with_http_info(booking_id, paymentgateway_id, amount, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int booking_id:  (required)
        :param int paymentgateway_id:  (required)
        :param float amount:  (required)
        :return: InlineResponse2012
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['booking_id', 'paymentgateway_id', 'amount']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_refund" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'booking_id' is set
        if ('booking_id' not in params) or (params['booking_id'] is None):
            raise ValueError("Missing the required parameter `booking_id` when calling `add_refund`")
        # verify the required parameter 'paymentgateway_id' is set
        if ('paymentgateway_id' not in params) or (params['paymentgateway_id'] is None):
            raise ValueError("Missing the required parameter `paymentgateway_id` when calling `add_refund`")
        # verify the required parameter 'amount' is set
        if ('amount' not in params) or (params['amount'] is None):
            raise ValueError("Missing the required parameter `amount` when calling `add_refund`")

        resource_path = '/refund/add'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'booking_id' in params:
            query_params['booking_id'] = params['booking_id']
        if 'paymentgateway_id' in params:
            query_params['paymentgateway_id'] = params['paymentgateway_id']
        if 'amount' in params:
            query_params['amount'] = params['amount']

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
                                            response_type='InlineResponse2012',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def filter_refunds(self, **kwargs):
        """
        Retrieve all refunds that match a filter
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.filter_refunds(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date after: Date of the earliest payment
        :param date before: Date of the latest payment to be retrieved
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.filter_refunds_with_http_info(**kwargs)
        else:
            (data) = self.filter_refunds_with_http_info(**kwargs)
            return data

    def filter_refunds_with_http_info(self, **kwargs):
        """
        Retrieve all refunds that match a filter
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.filter_refunds_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param date after: Date of the earliest payment
        :param date before: Date of the latest payment to be retrieved
        :return: InlineResponse20039
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['after', 'before']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filter_refunds" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/refund/filter'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'after' in params:
            query_params['after'] = params['after']
        if 'before' in params:
            query_params['before'] = params['before']

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
                                            response_type='InlineResponse20039',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_all_refunds(self, **kwargs):
        """
        Retrieve all refunds made
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_refunds(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_all_refunds_with_http_info(**kwargs)
        else:
            (data) = self.get_all_refunds_with_http_info(**kwargs)
            return data

    def get_all_refunds_with_http_info(self, **kwargs):
        """
        Retrieve all refunds made
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_all_refunds_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: InlineResponse20038
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_refunds" % key
                )
            params[key] = val
        del params['kwargs']

        resource_path = '/refund/all'.replace('{format}', 'json')
        path_params = {}

        query_params = {}

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
                                            response_type='InlineResponse20038',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))

    def get_refund(self, id, **kwargs):
        """
        Retrieve a refund by ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_refund(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id:  (required)
        :return: InlineResponse20037
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_refund_with_http_info(id, **kwargs)
        else:
            (data) = self.get_refund_with_http_info(id, **kwargs)
            return data

    def get_refund_with_http_info(self, id, **kwargs):
        """
        Retrieve a refund by ID
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_refund_with_http_info(id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int id:  (required)
        :return: InlineResponse20037
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_refund" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_refund`")

        resource_path = '/refund'.replace('{format}', 'json')
        path_params = {}

        query_params = {}
        if 'id' in params:
            query_params['id'] = params['id']

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
                                            response_type='InlineResponse20037',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'))
