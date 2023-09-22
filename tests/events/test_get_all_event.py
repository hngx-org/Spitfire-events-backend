import unittest
import requests

BASE_URI = "http://localhost:5000/api/events/"

class TestGetAllEvents(unittest.TestCase):
    # Test if no event is in database

    # Test if one event is in database

    # Test if multiple events are in database
    def test_get_all_events(self):
        data = requests.get(BASE_URI, timeout=10)
        self.assertEqual(data.status_code, 200)

if __name__ == '__main__':
    unittest.main()
