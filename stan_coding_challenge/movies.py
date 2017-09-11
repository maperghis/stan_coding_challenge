#!/usr/bin/env python
"""
:created on: 10-09-2017
:modified on: 10-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import falcon
import falcon.status_codes as status
import json
from stan_coding_challenge.errors import MyHTTPError
from stan_coding_challenge.handlers import BaseJsonHandler


class Resource(object):
    """Resource which takes a BaseJsonHandler, defining how the incoming json
    data on a post should be filtered"""

    def __init__(self, jsonHandler):
        assert isinstance(jsonHandler, BaseJsonHandler)
        self._jsonHandler = jsonHandler

    def on_post(self, req, resp):
        """Post method
        :param req: HTTP request
        :param resp: HTTP response
        """
        if 'application/json' not in req.content_type:
            desc = MyHTTPError.UNSUPPORTED_MEDIA_TYPE
            raise MyHTTPError(errorMsg=desc, status=status.HTTP_415)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON
        try:
            raw = req.stream.read(req.content_length or 0)
        except Exception as exc:
            desc = MyHTTPError.INVALID_JSON
            raise MyHTTPError(errorMsg=desc)
        doc = self._jsonHandler.filter(raw)
        resp.data = json.dumps(doc, encoding='utf-8')
