import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestUpdateEventById(unittest.TestCase):
    def setUp(self):
        # Create some events to be retrieved
        self.event_data = {
            "title":"New Event",
            "description": "Event Description",
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

    def test_update_event_by_id_success(self):
        # Make a PUT request to update an event by id
        updated_data = {
            "title":"Updated Event",
            "description": "Updated Event Description",
            "location": "Updated Event Location",
            "creator_id": "user1_id",
            "start_time": "14:00:00",
            "end_time": "16:00:00",
            "start_date": "2023-09-23",
            "end_date": "2023-09-24"
        }
        response = requests.put(BASE_URI + self.event_id, json=updated_data)

        # Check if the response status code is 201 (Created)
        self.assertEqual(response.status_code, 201)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertIn("Event_id", response_data)
        self.assertIn("data", response_data)

        # Check if the response data matches the updated event
        expected_event = {**self.event_data, **updated_data}
        returned_event = response_data["data"]
        self.assertEqual(expected_event["title"], returned_event["title"])
        self.assertEqual(expected_event["description"], returned_event["description"])
        self.assertEqual(expected_event["location"], returned_event["location"])
        self.assertEqual(expected_event["start_date"], returned_event["start_date"])
        self.assertEqual(expected_event["start_time"], returned_event["start_time"])
        self.assertEqual(expected_event["end_date"], returned_event["end_date"])
        self.assertEqual(expected_event["end_time"], returned_event["end_time"])


    def test_update_event_by_id_not_found(self):
        # Make a PUT request to update an event by an invalid id
        updated_data = {
            "title": "Updated Event",
            "description": "Updated Event Description",
            "location": "Updated Event Location"
        }   
        event_id = "invalid-id"
        response = requests.put(BASE_URI + event_id, json=updated_data)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["error"], "Not found")
        self.assertEqual(response_data["message"], "Event not found")


    def test_empty_fields(self):
        # Define event details with empty fields (e.g., empty title, creator_id, etc.)
        event_data = {
            "title": "",
            "description": "",
            "location": "",
            "creator_id": "",
            "start_time": "",
            "end_time": "",
            "start_date": "",
            "end_date": ""
        }

        # Make a POST request with empty fields
        response = requests.put(BASE_URI, json=event_data)

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
            "location": None,
            "creator_id": None,
            "start_time": None,
            "end_time": None,
            "start_date": None,
            "end_date": None
        }

        # Make a POST request with null fields
        response = requests.put(BASE_URI, json=event_data)

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
            "location": "T" * 1030,
            "creator_id": "T" * 65,
            "start_time": "06:52:10",
            "end_time": "06:57:10",
            "start_date": "2000-07-11",
            "end_date": "1999-06-11"
        }

        # Make a POST request with long fields
        response = requests.put(BASE_URI, json=event_data)
        
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
            "location": "Event Location",
            "creator_id": "user1_id",
            "start_time": "06:52:10",
            "end_time": "06:51:10",
            "start_date": "2000-07-11",
            "end_date": "1999-06-11"
        }

        # Make a POST request with negative time duration
        response = requests.put(BASE_URI, json=event_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the error message is correct
        response_data = response.json()
        self.assertEqual(response_data["error"], "Bad Request")
        self.assertEqual(response_data["message"], "Invalid time duration")


    def test_update_event_by_id_error(self):
        # skip this test for now
        return

        # Simulate a database error

        # Check if the response status code is 500 (Internal Server Error)
        self.assertEqual(response.status_code, 500)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["error"], "Internal Server Error")
        self.assertEqual(response_data["message"], "Something went wrong")


if __name__ == '__main__':
    unittest.main()
