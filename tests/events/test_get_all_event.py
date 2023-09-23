import unittest
import requests

BASE_URI = "http://localhost:5000/api/events/"

class TestAllEvents(unittest.TestCase):
    def test_all_events_success(self):
        # Create some events to be retrieved
        event_data = [
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
        for event in event_data:
            response = requests.post(BASE_URI, json=event)

        # Make a GET request to retrieve all events
        response = requests.get(BASE_URI)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

        # Check if the response data contains the expected events
        expected_events = [event["title"] for event in event_data]
        returned_events = [event["title"] for event in response_data["data"]]
        self.assertCountEqual(expected_events, returned_events)

    def test_all_events_empty(self):
        # Delete all events from the database
        response = requests.get(BASE_URI)
        all_events = response.json()["data"]
        for event in all_events:
            delete_uri = BASE_URI + event["id"]
            response = requests.delete(delete_uri)

        # Make a GET request to retrieve all events
        response = requests.get(BASE_URI)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

        # Check if the response data is empty
        self.assertEqual(len(response_data["data"]), 0)

    def test_all_events_error(self):
        # Mock the query_all function to raise an exception
        def mock_query_all(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").query_all
        __import__("routes").query_all = mock_query_all

        # Make a GET request to retrieve all events
        response = requests.get(BASE_URI)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains an error message
        response_data = response.json()
        self.assertEqual(response_data["error"], "an error has occured, couldn't complete request")

        # Restore the original function
        __import__("routes").query_all = original_function

if __name__ == '__main__':
    unittest.main()