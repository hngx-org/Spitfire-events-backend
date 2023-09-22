import unittest
import requests
import json

BASE_URI = "http://localhost:5000/api/events/"

class TestCreateNewEvent(unittest.TestCase):
    def test_create_event_success(self):
        # Define event details in JSON format
        event_data = {
            "title": "New Event",
            "description": "Event Description",
            "location": "Event Location",
            "start_date": "2023-09-21",
            "start_time": "10:00:00",
            "end_date": "2023-09-22",
            "end_time": "12:00:00",
            "thumbnail": "thumbnail-url"
        }

        # Make a POST request to create a new event
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the response data contains the expected event details
        response_data = response.json()
        self.assertEqual(response_data["status"], "success")
        self.assertIn("event", response_data)
        created_event = response_data["event"]
        self.assertEqual(created_event["title"], "New Event")
        self.assertEqual(created_event["description"], "Event Description")
        self.assertEqual(created_event["location"], "Event Location")

    def test_create_event_missing_data(self):
        # Define event details with missing data (e.g., missing title)
        event_data = {
            "description": "Event Description",
            "location": "Event Location",
            "start_date": "2023-09-21",
            "start_time": "10:00:00",
            "end_date": "2023-09-22",
            "end_time": "12:00:00",
            "thumbnail": "thumbnail-url"
        }

        # Make a POST request with missing data
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains an error message
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertIn("message", response_data)


if __name__ == '__main__':
    unittest.main()
