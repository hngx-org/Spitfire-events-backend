import unittest
import requests

BASE_URI = "http://localhost:5000/api/events/"

class TestGetEventById(unittest.TestCase):
    def setUp(self):
        # Create some events to be retrieved
        self.event_data = [
            {
                "title": "Event 1",
                "description": "Event 1 Description",
                "location": "Event 1 Location",
                "start_date": "2023-09-21",
                "start_time": "10:00:00",
                "end_date": "2023-09-22",
                "end_time": "12:00:00",
                "thumbnail": "thumbnail-url-1"
            },
            {
                "title": "Event 2",
                "description": "Event 2 Description",
                "location": "Event 2 Location",
                "start_date": "2023-09-23",
                "start_time": "14:00:00",
                "end_date": "2023-09-24",
                "end_time": "16:00:00",
                "thumbnail": "thumbnail-url-2"
            }
        ]
        self.event_ids = []
        for event in self.event_data:
            response = requests.post(BASE_URI, json=event)
            self.event_ids.append(response.json()["data"]["id"])

    def tearDown(self):
        # Delete all events from the database
        for event_id in self.event_ids:
            delete_uri = BASE_URI + event_id
            requests.delete(delete_uri)

    def test_get_event_by_id_success(self):
        # Make a GET request to retrieve an event by id
        event_id = self.event_ids[0]
        response = requests.get(BASE_URI + event_id)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

        # Check if the response data matches the expected event
        expected_event = self.event_data[0]
        returned_event = response_data["data"]
        self.assertEqual(expected_event["title"], returned_event["title"])
        self.assertEqual(expected_event["description"], returned_event["description"])
        self.assertEqual(expected_event["location"], returned_event["location"])
        self.assertEqual(expected_event["start_date"], returned_event["start_date"])
        self.assertEqual(expected_event["start_time"], returned_event["start_time"])
        self.assertEqual(expected_event["end_date"], returned_event["end_date"])
        self.assertEqual(expected_event["end_time"], returned_event["end_time"])
        self.assertEqual(expected_event["thumbnail"], returned_event["thumbnail"])

    def test_get_event_by_id_not_found(self):
        # Make a GET request to retrieve an event by an invalid id
        event_id = "invalid-id"
        response = requests.get(BASE_URI + event_id)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

    def test_get_event_by_id_error(self):
        # Mock the query_by_id function to raise an exception
        def mock_query_by_id(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").query_by_id
        __import__("routes").query_by_id = mock_query_by_id

        # Make a GET request to retrieve an event by id
        event_id = self.event_ids[0]
        response = requests.get(BASE_URI + event_id)

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)