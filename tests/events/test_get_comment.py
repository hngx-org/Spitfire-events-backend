import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestGetComments(unittest.TestCase):
    def setUp(self):
        # Create an event to get comments for
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

        # Create some comments for the event
        self.comment_data = [
            {
                "user_id": "user-1",
                "body": "This is comment 1"
            },
            {
                "user_id": "user-2",
                "body": "This is comment 2"
            },
            {
                "user_id": "user-3",
                "body": "This is comment 3"
            }
        ]
        for comment in self.comment_data:
            response = requests.post(BASE_URI + self.event_id + "/comments", json=comment)

    def tearDown(self):
        # Delete the event and comments from the database
        delete_uri = BASE_URI + self.event_id
        requests.delete(delete_uri)

    def test_get_comments_success(self):
        # Make a GET request to get comments for an event
        response = requests.get(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)
        self.assertIsInstance(response_data["data"], list)
        self.assertEqual(len(response_data["data"]), len(self.comment_data))
        for comment in response_data["data"]:
            self.assertIn("id", comment)
            self.assertIn("user_id", comment)
            self.assertIn("body", comment)

    def test_get_comments_not_found(self):
        # Make a GET request to get comments for a non-existent event
        response = requests.get(BASE_URI + "non-existent-event-id/comments")

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

    def test_get_comments_database_error(self):
        # Mock the query_all_filtered function to raise an exception
        def mock_query_all_filtered(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").query_all_filtered
        __import__("routes").query_all_filtered = mock_query_all_filtered

        # Make a GET request to get comments for an event
        response = requests.get(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("error", response_data)

    def test_get_comments_empty(self):
        # Create a new event with no comments
        event_data = {
            "title": "Event 2",
            "description": "Event 2 Description",
            "location": "Event 2 Location",
            "start_date": "2023-09-23",
            "start_time": "10:00:00",
            "end_date": "2023-09-24",
            "end_time": "12:00:00",
            "thumbnail": "thumbnail-url-2"
        }
        response = requests.post(BASE_URI, json=event_data)
        event_id = response.json()["data"]["id"]

        # Make a GET request to get comments for the new event
        response = requests.get(BASE_URI + event_id + "/comments")

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)
        self.assertIsInstance(response_data["data"], list)
        self.assertEqual(len(response_data["data"]), 0)

        # Delete the new event from the database
        delete_uri = BASE_URI + event_id
        requests.delete(delete_uri)

    def test_get_comments_invalid_event_id(self):
        # Make a GET request to get comments for an invalid event ID
        response = requests.get(BASE_URI + "invalid-event-id/comments")

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

    def test_get_comments_invalid_request_method(self):
        # Make a POST request to get comments for an event
        response = requests.post(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 405 (Method Not Allowed)
        self.assertEqual(response.status_code, 405)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

    def test_get_comments_invalid_content_type(self):
        # Make a GET request to get comments for an event with an invalid content type
        headers = {"Content-Type": "application/xml"}
        response = requests.get(BASE_URI + self.event_id + "/comments", headers=headers)

        # Check if the response status code is 415 (Unsupported Media Type)
        self.assertEqual(response.status_code, 415)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)