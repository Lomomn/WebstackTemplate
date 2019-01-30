import os
import sys
from . import client

def test_client_exists(client):
    assert client != None