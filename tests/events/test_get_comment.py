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

    def test_empty_comments_success(self):
        # Make a GET request to get comments for an event
        response = requests.get(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

        # Check if the response data is empty
        self.assertEqual(len(response_data["data"]), 0)


    def test_get_comments_success(self):
        for comment in self.comment_data:
            response = requests.post(BASE_URI + self.event_id + "/comments", json=comment)
    
        # Make a GET request to get comments for an event
        response = requests.get(BASE_URI + self.event_id + "/comments")

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains the expected fields
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)

        # Check if the response data contains the expected number of comments
        self.assertEqual(len(response_data["data"]), len(self.comment_data))

        # Check the data inthe comment are same as expected
        for i in range(len(self.comment_data)):
            self.assertEqual(response_data["data"][i]["user_id"], self.comment_data[i]["user_id"])
            self.assertEqual(response_data["data"][i]["body"], self.comment_data[i]["body"])


    def test_get_comments_not_found(self):
        # Make a GET request to get comments for a non-existent event
        response = requests.get(BASE_URI + "non-existent-event-id/comments")

        # Check if the response status code is 404 (Not Found)
        self.assertEqual(response.status_code, 404)

        # Check if the response data contains the expected fields and values
        response_data = response.json()
        self.assertEqual(response_data["error"], "Not found")
        self.assertEqual(response_data["message"], "Event not found")