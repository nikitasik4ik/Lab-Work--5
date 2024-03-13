import pytest
import requests
import os

os.environ['TESTING'] = 'True'
os.environ['DATABASE_URL'] = 'sqlite:///:memory:'

from backend.app import app

def test_index():
    flask_app = app.test_client()
    response = flask_app.get('/')
    assert response.status_code == 200, response
    assert response.json == {'Message': 'Pong!'}


def test_get_users():
    flask_app = app.test_client()
    response = flask_app.get('/users')
    assert list(response.json.keys())[0] == 'Users'
    assert response.status_code == 200


def test_post_user():
    flask_app = app.test_client()
    response = flask_app.post('/users', json={
        'username': 'test_user',
        'email': 'test@mail.com',
        'password': 'password',
        'role_id': '1'
    })
    assert response.status_code == 201
    assert list(response.json.keys())[0] == 'Message'
    assert 'User created.' in response.json['Message']


