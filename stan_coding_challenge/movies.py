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

    def __init__(self):
        pass

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_OK
        if req.content_length:
            doc = json.load(req.stream)
            resp.data = json.dumps(doc)
        resp.content_type = falcon.MEDIA_JSON
