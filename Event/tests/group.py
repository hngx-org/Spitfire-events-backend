import unittest
from Event import db
from run import app  # Import your Flask app and db instance

class TestGroupEndpoints(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_user_to_group(self):
        # Test the /api/groups/<groupId>/members/<userId> POST endpoint
        response = self.app.post('/api/groups/1/members/2')
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertTrue(data['success'])
        self.assertIn('id', data)
        self.assertEqual(data['message'], 'User added to Group')

    def test_update_group(self):
        # Test the /api/groups/<int:group_id> PUT endpoint
        response = self.app.put('/api/groups/1', json={"title": "Updated Group Title"})
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Group updated successfully')
        self.assertIn('group', data)

    def test_get_group_details(self):
        # Test the /api/groups/<int:group_id> GET endpoint
        response = self.app.get('/api/groups/1')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('title', data)  # Assuming 'title' is a key in the group details

    def test_remove_group_member(self):
        # Test the /api/groups/<group_id>/members/<user_id> DELETE endpoint
        response = self.app.delete('/api/groups/1/members/2')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'User removed from group successfully')

    def test_create_group(self):
        # Test the /api/groups/ POST endpoint
        response = self.app.post('/api/groups', json={"title": "New Group"})
        data = response.get_json()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['message'], 'Group created successfully')
        self.assertIn('group', data)  # Assuming 'group' is a key in the group details


