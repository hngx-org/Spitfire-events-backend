"""Just testing this endpoint"""
import requests

BASE_URI = "http://127.0.0.1:5000"

data = requests.post(f'{BASE_URI}/api/users/groups', data={'title': 'Team spitfire'})
res = data.text
print(res)