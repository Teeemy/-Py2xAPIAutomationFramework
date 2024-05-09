# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.


from src.constants.api_constants import APIConstants
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verification import *
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Util

import pytest
import requests
import allure


class TestCreateBooking(object):
    @pytest.mark.positive
    @allure.title("Verify FirstName is updated")
    @allure.description("Creating a booking and verifying FirstName is updated ")
    def create_token(self):
        url = "https://restful-booker.herokuapp.com/auth"
        headers = {"Content-Type": "application/json"}
        json_payload = {
            "username": "admin",
            "password": "password123"
        }
        response = requests.post(url=url, headers=headers, json=json_payload)
        data = response.json()
        token = data["token"]
        print(token)
        return token

    def test_create_booking_with_patch_request(self):
        # URL,Payload,Headers
        URL = "https://restful-booker.herokuapp.com/booking"
        headers = {"Content-Type": "application/json"}
        json_payload = {
            "firstname": "Mariam",
            "lastname": "Smith",
            "totalprice": 111,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = requests.post(url=URL, headers=headers, json=json_payload)
        print(type(URL))
        print(type(headers))
        print(type(json_payload))
        # Assertions
        assert response.status_code == 200
        data = response.json()
        booking_id = data["booking"]
        return booking_id

# Test for the Single Req
# 1. Response
# 2. Status Code
# 3. Headers

# Assertions will always (negative)
