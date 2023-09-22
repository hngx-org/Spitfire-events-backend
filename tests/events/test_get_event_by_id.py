import unittest
import requests

BASE_URI = "http://localhost:5000/api/events/"

class TestGetEventById(unittest.TestCase):
    def test_get_event_by_id(self):
        data = requests.get(BASE_URI + "1", timeout=10)
        self.assertEqual(data.status_code, 500)

if __name__ == '__main__':
    unittest.main()
