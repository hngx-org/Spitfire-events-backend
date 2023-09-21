"""_summary_
    """
import requests

BASE_URI = "https://.../"


# sample test case
def test_get_all_events():
    """
    test get all events in db
    """
    data = requests.get(BASE_URI, timeout=10)
    res = data.json()
    assert data.status_code == 200
    assert isinstance(res["persons"], list)
    
