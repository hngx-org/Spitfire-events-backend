import unittest
import requests

BASE_URI = "http://localhost:5000/api/events/"

class TestDeleteEvent(unittest.TestCase):
    def test_delete_event_success(self):
        # Create a new event to be deleted
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
        response = requests.post(BASE_URI, json=event_data)
        created_event = response.json()["event"]

        # Make a DELETE request to delete the event
        delete_uri = BASE_URI + created_event["id"]
        response = requests.delete(delete_uri)

        # Check if the response status code is 204 (No Content)
        self.assertEqual(response.status_code, 204)

        # Check if the event was deleted from the database
        response = requests.get(delete_uri)
        self.assertEqual(response.status_code, 404)

    def test_delete_event_not_found(self):
        # Make a DELETE request with an invalid event ID
        delete_uri = BASE_URI + "invalid-id"
        response = requests.delete(delete_uri)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains an error message
        response_data = response.json()
        self.assertEqual(response_data["error"], "Not Found")
        self.assertIn("message", response_data)

    def test_delete_event_error(self):
        # Mock the query_one_filtered function to raise an exception
        def mock_query_one_filtered(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").query_one_filtered
        __import__("routes").query_one_filtered = mock_query_one_filtered

        # Make a DELETE request with a valid event ID
        delete_uri = BASE_URI + "valid-id"
        response = requests.delete(delete_uri)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains an error message
        response_data = response.json()
        self.assertEqual(response_data["error"], "an error has occured, couldn't complete request")

        # Restore the original function
        __import__("routes").query_one_filtered = original_function

if __name__ == '__main__':
    unittest.main()