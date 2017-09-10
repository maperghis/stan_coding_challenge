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
from stan_coding_challenge.errors import MyHTTPBadRequest
import os


CWD = os.path.dirname(os.path.realpath(__file__))
RESOURCES_DIR = os.path.join(os.path.dirname(CWD), 'resources')


@pytest.fixture
def client():
    api = get_app()
    return testing.TestClient(api)

def test_post_movies(client):
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
    assert response.status == falcon.HTTP_OK
    data_received = json.loads(response.content)
    assert set(data_received) == set(resp_data)
    for a in data_received['response']:
        print a
    print "------"
    for a in resp_data['response']:
        print a
    assert data_received['response'] == resp_data['response']

# def test_post_movies_invalid_json(client):
#
#     response = client.simulate_post(
#         '/',
#         body='{"movies": ["spiderman", "batman",]}',
#         headers={'content-type': 'application/json'}
#     )
#     assert response.status == falcon.HTTP_400
#     error = "Could not decode request: JSON parsing failed"
#     json_content = json.loads(response.content)
#     assert 'error' in json_content
#     assert json_content['error'] == MyHTTPBadRequest.INVALID_JSON
