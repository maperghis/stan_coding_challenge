#!/usr/bin/env python
"""
:created on: 10-09-2017
:modified on: 10-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import falcon
from stan_coding_challenge.handlers import MovieHandler
from stan_coding_challenge.movies import Resource


def create_app(jsonFilter):
    """Create resource and app instances for hosting
    :return: falcon API app
    :rtype: <falcon.api.API>
    """
    movie_resource = Resource(jsonFilter)
    api = falcon.API()
    api.add_route('/', movie_resource)
    return api


def get_app():
    """Configure app for hosting
    :return: falcon API app
    :rtype: <falcon.api.API>
    """
    jsonHandler = MovieHandler()
    return create_app(jsonHandler)
