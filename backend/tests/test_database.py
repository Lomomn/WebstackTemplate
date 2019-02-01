import os
import sys
from entry import create_db, drop_db, get_database_uri_string
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists

'''
Test that the database can be connected to
'''

def test_database_exists():
    db_uri = get_database_uri_string(testing=False)
    assert database_exists(db_uri) == True


def test_database_testing_exists():
    db_uri = get_database_uri_string(testing=True)
    assert database_exists(db_uri) == True


