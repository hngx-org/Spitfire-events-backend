import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestUpdateEventById(unittest.TestCase):
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

    def test_update_event_by_id_success(self):
        # Make a DELETE request to delete the event
        response = requests.delete(BASE_URI + self.event_id)

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["message"], "Event deleted successfully")

        # Check if the event was deleted from the database
        response = requests.delete(BASE_URI + self.event_id)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["error"], "Not found")
        self.assertEqual(response_data["message"], "Event not found")


    def test_update_event_by_id_not_found(self):
        # Make a PUT request to update an event by an invalid id
        updated_data = {
            "title": "Updated Event",
            "description": "Updated Event Description",
            "location": "Updated Event Location"
        }   
        event_id = "invalid-id"
        response = requests.put(BASE_URI + event_id)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertEqual(response_data["error"], "Not found")
        self.assertEqual(response_data["message"], "Event not found")

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