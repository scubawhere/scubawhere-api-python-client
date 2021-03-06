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

# import models into sdk package
from .models.accommodation import Accommodation
from .models.addon import Addon
from .models.agent import Agent
from .models.base_price import BasePrice
from .models.boat import Boat
from .models.boatroom import Boatroom
from .models.booking import Booking
from .models.company import Company
from .models.country import Country
from .models.course import Course
from .models.currency import Currency
from .models.customer import Customer
from .models.date_range import DateRange
from .models.error_model import ErrorModel
from .models.inline_response_200 import InlineResponse200
from .models.inline_response_200_1 import InlineResponse2001
from .models.inline_response_200_10 import InlineResponse20010
from .models.inline_response_200_11 import InlineResponse20011
from .models.inline_response_200_12 import InlineResponse20012
from .models.inline_response_200_13 import InlineResponse20013
from .models.inline_response_200_14 import InlineResponse20014
from .models.inline_response_200_15 import InlineResponse20015
from .models.inline_response_200_16 import InlineResponse20016
from .models.inline_response_200_17 import InlineResponse20017
from .models.inline_response_200_18 import InlineResponse20018
from .models.inline_response_200_19 import InlineResponse20019
from .models.inline_response_200_2 import InlineResponse2002
from .models.inline_response_200_20 import InlineResponse20020
from .models.inline_response_200_21 import InlineResponse20021
from .models.inline_response_200_22 import InlineResponse20022
from .models.inline_response_200_23 import InlineResponse20023
from .models.inline_response_200_24 import InlineResponse20024
from .models.inline_response_200_25 import InlineResponse20025
from .models.inline_response_200_26 import InlineResponse20026
from .models.inline_response_200_27 import InlineResponse20027
from .models.inline_response_200_28 import InlineResponse20028
from .models.inline_response_200_29 import InlineResponse20029
from .models.inline_response_200_3 import InlineResponse2003
from .models.inline_response_200_30 import InlineResponse20030
from .models.inline_response_200_31 import InlineResponse20031
from .models.inline_response_200_32 import InlineResponse20032
from .models.inline_response_200_33 import InlineResponse20033
from .models.inline_response_200_34 import InlineResponse20034
from .models.inline_response_200_35 import InlineResponse20035
from .models.inline_response_200_36 import InlineResponse20036
from .models.inline_response_200_37 import InlineResponse20037
from .models.inline_response_200_38 import InlineResponse20038
from .models.inline_response_200_39 import InlineResponse20039
from .models.inline_response_200_4 import InlineResponse2004
from .models.inline_response_200_40 import InlineResponse20040
from .models.inline_response_200_41 import InlineResponse20041
from .models.inline_response_200_42 import InlineResponse20042
from .models.inline_response_200_42_utilisation import InlineResponse20042Utilisation
from .models.inline_response_200_42_utilisation_totals import InlineResponse20042UtilisationTotals
from .models.inline_response_200_43 import InlineResponse20043
from .models.inline_response_200_44 import InlineResponse20044
from .models.inline_response_200_45 import InlineResponse20045
from .models.inline_response_200_46 import InlineResponse20046
from .models.inline_response_200_47 import InlineResponse20047
from .models.inline_response_200_5 import InlineResponse2005
from .models.inline_response_200_6 import InlineResponse2006
from .models.inline_response_200_7 import InlineResponse2007
from .models.inline_response_200_8 import InlineResponse2008
from .models.inline_response_200_9 import InlineResponse2009
from .models.inline_response_201 import InlineResponse201
from .models.inline_response_201_1 import InlineResponse2011
from .models.inline_response_201_2 import InlineResponse2012
from .models.inline_response_201_3 import InlineResponse2013
from .models.inline_response_201_4 import InlineResponse2014
from .models.inline_response_201_5 import InlineResponse2015
from .models.location import Location
from .models.package import Package
from .models.payment import Payment
from .models.payment_gateway import PaymentGateway
from .models.pickup import Pickup
from .models.refund import Refund
from .models.report_entry import ReportEntry
from .models.report_entry_total import ReportEntryTotal
from .models.schedule import Schedule
from .models.session import Session
from .models.tag import Tag
from .models.ticket import Ticket
from .models.timetable import Timetable
from .models.training import Training
from .models.training_session import TrainingSession
from .models.training_session_manifest import TrainingSessionManifest
from .models.training_session_manifest_capacity import TrainingSessionManifestCapacity
from .models.trip import Trip

# import apis into sdk package
from .apis.accommodation_api import AccommodationApi
from .apis.addon_api import AddonApi
from .apis.agent_api import AgentApi
from .apis.boat_api import BoatApi
from .apis.boatroom_api import BoatroomApi
from .apis.booking_api import BookingApi
from .apis.class_api import ClassApi
from .apis.classsession_api import ClasssessionApi
from .apis.company_api import CompanyApi
from .apis.course_api import CourseApi
from .apis.customer_api import CustomerApi
from .apis.customers_api import CustomersApi
from .apis.location_api import LocationApi
from .apis.locations_api import LocationsApi
from .apis.package_api import PackageApi
from .apis.payment_api import PaymentApi
from .apis.refund_api import RefundApi
from .apis.report_api import ReportApi
from .apis.schedule_api import ScheduleApi
from .apis.session_api import SessionApi
from .apis.ticket_api import TicketApi
from .apis.timetable_api import TimetableApi
from .apis.trip_api import TripApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
