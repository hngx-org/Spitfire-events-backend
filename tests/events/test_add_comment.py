import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestAddComments(unittest.TestCase):
    def setUp(self):
        # Create an event to add comments to
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

    def test_add_comment_success(self):
        # Make a POST request to add a comment to an event
        comment_data = {
            "user_id": "user-1",
            "body": "This is a comment"
        }
        response = requests.post(BASE_URI + self.event_id + "/comments", json=comment_data)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)
        self.assertIn("id", response_data["data"])
        self.assertIn("body", response_data["data"])

    def test_add_comment_missing_fields(self):
        # Make a POST request to add a comment to an event with missing fields
        comment_data = {    
            "user_id": "user-1"
        }
        response = requests.post(BASE_URI + self.event_id + "/comments", json=comment_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("error", response_data)

    def test_add_comment_invalid_event_id(self):
        # Make a POST request to add a comment to an invalid event ID
        comment_data = {
            "user_id": "user-1",
            "body": "This is a comment"
        }
        response = requests.post(BASE_URI + "invalid-event-id/comments", json=comment_data)

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

    def test_add_comment_database_error(self):
        # Mock the insert function to raise an exception
        def mock_insert(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").Comments.insert
        __import__("routes").Comments.insert = mock_insert

        # Make a POST request to add a comment to an event
        comment_data = {
            "user_id": "user-1",
            "body": "This is a comment"
        }
        response = requests.post(BASE_URI + self.event_id + "/comments", json=comment_data)

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("error", response_data)

    def test_get_comments_success(self):
        # Make a GET request to get all comments for an event
        response = requests.get(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

    def test_get_comments_invalid_event_id(self):
        # Make a GET request to get comments for an invalid event ID
        response = requests.get(BASE_URI + "invalid-event-id/comments")

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

    def test_get_comments_no_comments(self):
        # Make a GET request to get comments for an event with no comments
        event_data = {
            "title": "Event 2",
            "description": "Event 2 Description",
            "location": "Event 2 Location",
            "start_date": "2023-09-21",
            "start_time": "10:00:00",
            "end_date": "2023-09-22",
            "end_time": "12:00:00",
            "thumbnail": "thumbnail-url-2"
        }
        response = requests.post(BASE_URI, json=event_data)
        event_id = response.json()["data"]["id"]
        response = requests.get(BASE_URI + event_id + "/comments")

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)

        # Delete the event from the database
        delete_uri = BASE_URI + event_id
        requests.delete(delete_uri)

    def test_get_comments_database_error(self):
        # Mock the query_all_filtered function to raise an exception
        def mock_query_all_filtered(*args, **kwargs):
            raise Exception("Database error")

        # Replace the original function with the mock function
        original_function = __import__("routes").query_all_filtered
        __import__("routes").query_all_filtered = mock_query_all_filtered

        # Make a GET request to get all comments for an event
        response = requests.get(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 400 (Bad Request)
        self.assertEqual(response.status_code, 400)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("status", response_data)
        self.assertIn("message", response_data)
        self.assertIn("error", response_data)