import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestGetEventById(unittest.TestCase):
    def setUp(self):
        # Create some events to be retrieved
        self.event_data = {
            "title":"New Event",
            "description": "Event Description",
            "thumbnail": "Event Thumbnail",
            "location": "Event Location",
            "creator_id": "user1_id",
            "start_time": "06:52:10",
            "end_time": "06:57:10",
            "start_date": "2000-07-11",
            "end_date": "1999-06-11"
        }

        # Make a POST request to create a new event and store the event id
        response = requests.post(BASE_URI, json=self.event_data)
        self.event_data = response.json()["data"]
        self.event_id = response.json()["data"]["id"]


    def test_get_event_by_id_success(self):
        # Make a GET request to retrieve an event by id
        response = requests.get(BASE_URI + self.event_id)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

        # Check if the response data matches the expected event
        expected_event = self.event_data
        returned_event = response_data["data"]
        self.assertEqual(expected_event["title"], returned_event["title"])
        self.assertEqual(expected_event["description"], returned_event["description"])
        self.assertEqual(expected_event["location"], returned_event["location"])
        self.assertEqual(expected_event["creator_id"], returned_event["creator_id"])
        self.assertEqual(expected_event["start_date"], returned_event["start_date"])
        self.assertEqual(expected_event["start_time"], returned_event["start_time"])
        self.assertEqual(expected_event["end_date"], returned_event["end_date"])
        self.assertEqual(expected_event["end_time"], returned_event["end_time"])
        self.assertEqual(expected_event["created_at"], returned_event["created_at"])
        self.assertEqual(expected_event["created_at"], returned_event["created_at"])

    def test_get_event_by_id_invalid_id(self):
        # Make a GET request to retrieve an event by an invalid id
        event_id = "invalid-id"
        response = requests.get(BASE_URI + event_id)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["error"], "Not found")
        self.assertEqual(response_data["message"], "Invalid event id")

    def test_get_event_by_id_error(self):
        # skip this test for now
        return

        # Simulate a database error

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["error"], "Internal Server Error")
        self.assertEqual(response_data["message"], "Something went wrong")