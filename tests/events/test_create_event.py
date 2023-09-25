import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestCreateEvent(unittest.TestCase):
    def test_create_event_success(self):
        # Define event details in JSON format
        event_data = {
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

        # Make a POST request to create a new event
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the response data contains the expected event details
        response_data = response.json()
        self.assertIn("data", response_data)
        created_event = response_data["data"]
        self.assertEqual(created_event["title"], "New Event")
        self.assertEqual(created_event["description"], "Event Description")
        #self.assertEqual(created_event["thumbnail"], "Event Thumbnail")
        self.assertEqual(created_event["location"], "Event Location")
        self.assertEqual(created_event["creator_id"], "user1_id")
        self.assertEqual(created_event["start_time"], "06:52:10")
        self.assertEqual(created_event["end_time"], "06:57:10")
        self.assertEqual(created_event["start_date"], "2000-07-11")
        self.assertEqual(created_event["end_date"], "1999-06-11")
        self.assertIn("created_at", created_event)
        self.assertIn("updated_at", created_event)

    def test_create_event_missing_data(self):
        # Define event details with missing data (e.g., missing title, creator_id, etc.)
        event_data = {
            "description": "Event Description",
            "thumbnail": "Event Thumbnail",
            "location": "Event Location",
            "start_time": "06:52:10",
            "end_time": "06:57:10",
            "start_date": "2000-07-11",
            "end_date": "1999-06-11"
        }

        # Make a POST request with missing data
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is correct
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertEqual(response_data["message"], "Missing required fields")

    def test_empty_fields(self):
        # Define event details with empty fields (e.g., empty title, creator_id, etc.)
        event_data = {
            "title": "",
            "description": "",
            "thumbnail": "",
            "location": "",
            "creator_id": "",
            "start_time": "",
            "end_time": "",
            "start_date": "",
            "end_date": ""
        }

        # Make a POST request with empty fields
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is correct
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertEqual(response_data["message"], "Missing required fields")

    def test_fields_as_none(self):
        # Define event details with null fields (e.g., null title, creator_id, etc.)
        event_data = {
            "title": None,
            "description": None,
            "thumbnail": None,
            "location": None,
            "creator_id": None,
            "start_time": None,
            "end_time": None,
            "start_date": None,
            "end_date": None
        }

        # Make a POST request with null fields
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is correct
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertEqual(response_data["message"], "Missing required fields")


    def test_long_fields(self):
        # Define event details with long fields (e.g., long title, creator_id, etc.)
        event_data = {
            "title": "a" * 65,
            "description": "T" * 230,
            "thumbnail": "Event Thumbnail",
            "location": "T" * 1030,
            "creator_id": "T" * 65,
            "start_time": "06:52:10",
            "end_time": "06:57:10",
            "start_date": "2000-07-11",
            "end_date": "1999-06-11"
        }

        # Make a POST request with long fields
        response = requests.post(BASE_URI, json=event_data)
        
        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is correct
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertEqual(response_data["message"], "Invalid field length")


    def test_negative_time_duration(self):
        # Define event details with negative time duration
        event_data = {
            "title": "New Event",
            "description": "Event Description",
            "thumbnail": "Event Thumbnail",
            "location": "Event Location",
            "creator_id": "user1_id",
            "start_time": "06:52:10",
            "end_time": "06:51:10",
            "start_date": "2000-07-11",
            "end_date": "1999-06-11"
        }

        # Make a POST request with negative time duration
        response = requests.post(BASE_URI, json=event_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is correct
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertEqual(response_data["message"], "Invalid time duration")


if __name__ == '__main__':
    unittest.main()