import pytest

from Event import create_app, db


@pytest.fixture()
def app():
    app = create_app("sqlite://")

    with app.app_context():
        db.create_all()
    print("Creating database")
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
