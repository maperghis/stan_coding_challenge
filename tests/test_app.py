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


@pytest.fixture
def client():
    api = get_app()
    return testing.TestClient(api)


def test_post_movies(client):
    doc = {"movie": "spiderman"}

    response = client.simulate_post(
        '/',
        body=json.dumps(doc),
        headers={'content-type': 'application/json'}
    )
    assert response.status == falcon.HTTP_CREATED
    assert json.loads(response.body) == doc
