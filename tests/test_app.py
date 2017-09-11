#!/usr/bin/env python
"""
:created on: 10-09-2017
:modified on: 10-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import falcon
from falcon import testing
import json
from stan_coding_challenge.app import get_app
import pytest
from stan_coding_challenge.errors import MyHTTPError
import os


CWD = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(os.path.dirname(CWD), 'resources')


@pytest.fixture
def client():
    api = get_app()
    return testing.TestClient(api)

def test_post_movies(client):
    """Test POST valid json"""
    request_file = os.path.join(RESOURCES_DIR, 'request.json')
    with open(request_file) as fd:
        req_data = json.load(fd)
    response_file = os.path.join(RESOURCES_DIR, 'response.json')
    with open(response_file) as fd:
        resp_data = json.load(fd)

    response = client.simulate_post(
        '/',
        body=json.dumps(req_data),
        headers={'content-type': 'application/json'}
    )
    assert response.status == falcon.HTTP_200
    data_received = json.loads(response.content)
    assert set(data_received) == set(resp_data)
    assert data_received['response'] == resp_data['response']

def test_post_movies_invalid_json(client):
    """Test POST invalid json"""
    response = client.simulate_post(
        '/',
        body='{"movies": ["spiderman", "batman",]}',
        headers={'content-type': 'application/json'}
    )
    assert response.status == falcon.HTTP_400
    json_content = json.loads(response.content)
    assert 'error' in json_content
    assert json_content['error'] == MyHTTPError.INVALID_JSON

def test_post_movies_valid_json_not_correct_type(client):
    """Test POST valid json, payload has a dict not a list of movies"""
    response = client.simulate_post(
        '/',
        body='{"payload": [["a", "b"]]}',
        headers={'content-type': 'application/json'}
    )
    assert response.status == falcon.HTTP_200
    json_content = json.loads(response.content)
    assert json_content == {}

def test_post_movies_empty_data(client):
    """Test POST empty data"""
    response = client.simulate_post(
        '/',
        body='{}',
        headers={'content-type': 'application/json'}
    )
    assert response.status == falcon.HTTP_200
    json_content = json.loads(response.content)
    assert json_content == {}

def test_post_movies_unsupported_type(client):
    """Test POST unsupported content type"""
    response = client.simulate_post(
        '/',
        body='{"movies": ["spiderman", "batman",]}',
        headers={'content-type': 'image/png'}
    )
    assert response.status == falcon.HTTP_415
    json_content = json.loads(response.content)
    assert 'error' in json_content
    assert json_content['error'] == MyHTTPError.UNSUPPORTED_MEDIA_TYPE

def test_post_movies_empty_content_type(client):
    """Test POST empty content type"""
    response = client.simulate_post(
        '/',
        body='{"movies": ["spiderman", "batman",]}',
        headers={'content-type': ''}
    )
    assert response.status == falcon.HTTP_400
    json_content = json.loads(response.content)
    assert 'error' in json_content
    assert json_content['error'] == MyHTTPError.NO_MEDIA_TYPE
