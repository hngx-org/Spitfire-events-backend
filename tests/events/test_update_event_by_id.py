import unittest
import requests

BASE_URI = "http://localhost:5000/api/events/"

class TestUpdateEventById(unittest.TestCase):
    def setUp(self):
        # Create an event to be updated
        self.event_data = {
            "title": "Event 1",
            "description": "Event 1 Description",
            "location": "Event 1 Location",
            "start_date": "2023-09-21",
            "start_time": "10:00:00",
            "end_date": "2023-09-22",
            "end_time": "12:00:00",
            "thumbnail": "thumbnail-url-1"
        }
        response = requests.post(BASE_URI, json=self.event_data)
        self.event_id = response.json()["data"]["id"]

    def tearDown(self):
        # Delete the event from the database
        delete_uri = BASE_URI + self.event_id
        requests.delete(delete_uri)

    def test_update_event_by_id_success(self):
        # Make a PUT request to update an event by id
        updated_data = {
            "title": "Updated Event",
            "description": "Updated Event Description",
            "location": "Updated Event Location",
            "start_date": "2023-09-23",
            "start_time": "14:00:00",
            "end_date": "2023-09-24",
            "end_time": "16:00:00",
            "thumbnail": "updated-thumbnail-url"
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
        self.assertEqual(expected_event["thumbnail"], returned_event["thumbnail"])

    def test_update_event_by_id_not_found(self):
        # Make a PUT request to update an event by an invalid id
        updated_data = {
            "title": "Updated Event",
            "description": "Updated Event Description",
            "location": "Updated Event Location",
            "start_date": "2023-09-23",
            "start_time": "14:00:00",
            "end_date": "2023-09-24",
            "end_time": "16:00:00",
            "thumbnail": "updated-thumbnail-url"
        }
        event_id = "invalid-id"
        response = requests.put(BASE_URI + event_id, json=updated_data)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("message", response_data)

    def test_update_event_by_id_error(self):
        # Mock the query_one_filtered function to raise an exception
        def mock_query_one_filtered(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").query_one_filtered
        __import__("routes").query_one_filtered = mock_query_one_filtered

        # Make a PUT request to update an event by id
        updated_data = {
            "title": "Updated Event",
            "description": "Updated Event Description",
            "location": "Updated Event Location",
            "start_date": "2023-09-23",
            "start_time": "14:00:00",
            "end_date": "2023-09-24",
            "end_time": "16:00:00",
            "thumbnail": "updated-thumbnail-url"
        }
        response = requests.put(BASE_URI + self.event_id, json=updated_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("error", response_data)