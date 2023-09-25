import unittest
import requests

BASE_URI = "http://spitfire.onrender.com/api/events/"

class TestAllEvents(unittest.TestCase):
    def test_all_events_success(self):
        # Make a GET request to retrieve all events
        response = requests.get(BASE_URI)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response data contains multiple events and veriy their fields
        response_data = response.json()
        self.assertIn("message", response_data)
        self.assertIn("data", response_data)
        all_events = response_data["data"]
        for event in all_events:
            self.assertIn("id", event)
            self.assertIn("title", event)
            self.assertIn("description", event)
            self.assertIn("location", event)
            self.assertIn("start_date", event)
            self.assertIn("start_time", event)
            self.assertIn("end_date", event)
            self.assertIn("end_time", event)
            self.assertIn("created_at", event)
            self.assertIn("updated_at", event)

    def test_all_events_empty(self):
        # Time will come to write this test
        # Let the database breathe.
        pass


if __name__ == '__main__':
    unittest.main()