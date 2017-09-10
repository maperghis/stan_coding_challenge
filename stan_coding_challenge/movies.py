#!/usr/bin/env python
"""
:created on: 10-09-2017
:modified on: 10-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import falcon
import json


class Resource(object):

    def __init__(self, jsonHandler):
        self._jsonHandler = jsonHandler

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON
        if req.content_length:
            data = req.stream
            doc = self._jsonHandler.filter(data)
            resp.data = json.dumps(doc)


class MovieHandler(object):

    def filter(self, data):
        print data
        try:
            doc = json.load(data)
            return doc
        except ValueError:
            desc = '{"error": "Could not decode request: JSON parsing failed"}'
            raise falcon.HTTPBadRequest(description=desc,
                headers={'content_type': falcon.MEDIA_JSON})
