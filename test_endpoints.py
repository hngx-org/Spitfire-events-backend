import requests

base_url = 'http://127.0.0.1:5000'
# post comments without images
data ={
    'user_id': 'dbd0bf30-575b-11ee-a686-40b03417ac57',
    'body': 'I am so excited'
}
comment_response = requests.post(f'{base_url}/api/events/f1544fd0-575c-11ee-a686-40b03417ac57/comments', json=data)
print(f'comment_response: {comment_response.json().get("data")}')

# post comments with images
data['image_url_list'] = [
    'https://www.istockphoto.com/photo/hand-holding-globe-with-young-plant-growing-and-sunshine-in-nature-concept-save-earth-gm1394781341-450126532',
    'https://www.istockphoto.com/photo/small-plant-in-female-hands-gm502816866-82151879'
]
comment_response = requests.post(f'{base_url}/api/events/f1544fd0-575c-11ee-a686-40b03417ac57/comments', json=data)
print(f'comment_response with images: {comment_response.json().get("data")}')