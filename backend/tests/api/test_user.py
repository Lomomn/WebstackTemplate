from flask_sqlalchemy import SQLAlchemy
from flask import request, url_for
from src.api import api
from . import client
import json

db = SQLAlchemy()


def test_users(client):
    with client:
        # Check database is empty
        rv = client.get('/api/users/')
        json_data = rv.get_json()
        assert len(json_data) == 0
        
        # Make new user
        rv = client.post('/api/users/', json={
            "username": "testuser",
            "password": "testpass",
            "email"   : "email@somewhere.com"
        })
        json_data = rv.get_json()
        assert json_data["username"] == "testuser"
        
        # Get token from login
        rv = client.post('/api/users/login/', json={
            "username": "testuser",
            "password": "testpass"
        })
        json_data = rv.get_json()
        assert "token" in json_data
        assert len(json_data["token"]) > 0
