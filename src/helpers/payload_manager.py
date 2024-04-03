# it will help to keep the payload e.g of payload is dictionary
import json




def payload_create_booking():
    payload = {
        "firstname": "Jimmy",
        "lastname": "Brown",
        "totalprice": 4000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-03-11",
            "checkout": "2024-03-14"
        },
        "additionalneeds": "Breakfast with Lunch"
    }
    return payload


def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": faker.last_name(),
        "totalprice": faker.random_int(min=100, max=1000),
        "depositpaid": faker.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "Wifi")),
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload


# def payload_create_booking_data_excel():
#     payload = {
#         "firstname": read_from_excel["fistname"],
#         "lastname": faker.last_name(),
#         "totalprice": faker.random_int(min=100, max=1000),
#         "depositpaid": faker.boolean(),
#         "bookingdates": {
#             "checkin": "2018-01-01",
#             "checkout": "2019-01-01"
#         },
#         "additionalneeds": faker.random_element(elements=("Breakfast", "Parking", "Wifi")),
#     }
#     return payload
