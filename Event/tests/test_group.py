
from Event.models.groups import Groups

def test_create_group(client, app):
    response = client.post("/api/groups/create", json={"title": "five Event"})
    data = response.get_json()
    assert response.status_code == 201
    assert data["message"] == "Group created successfully"
    with app.app_context():
        assert Groups.query.count() == 1
        assert Groups.query.first().title == "five Event"
