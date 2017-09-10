#!/usr/bin/env python
"""
:created on: 10-09-2017
:modified on: 10-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import falcon
import json
from stan_coding_challenge.errors import MyHTTPError
import falcon.status_codes as status


class Resource(object):

    def __init__(self, jsonHandler):
        self._jsonHandler = jsonHandler

    def on_post(self, req, resp):
        if req.content_type != falcon.MEDIA_JSON:
            desc = MyHTTPError.UNSUPPORTED_MEDIA_TYPE
            raise MyHTTPError(errorMsg=desc, status=status.HTTP_415)
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_JSON
        if req.content_length:
            data = req.stream
            doc = self._jsonHandler.filter(data)
            resp.data = json.dumps(doc)


class MovieHandler(object):

    def filter(self, data):
        try:
            data = json.load(data)
            payload = data["payload"]
            return self.processPayload(payload)
        except ValueError:
            desc = MyHTTPError.INVALID_JSON
            raise MyHTTPError(errorMsg=desc)
        except KeyError:
            desc = MyHTTPError.MISSING_PAYLOAD
            raise MyHTTPError(errorMsg=desc)

    def processPayload(self, payload):
        """Process the payload
        :param payload: list of movies
        :type payload: list
        :return: filtered payload
        :rtype: dictionary
        """
        # filter by drm = True
        data = list(filter(lambda mov: mov.get(u'drm') == True, payload))
        # filter again by eps > 0
        data = list(filter(lambda mov: mov.get(u'episodeCount') > 0, data))
        movies = []
        for m in data:
            # image, slug and title in the response
            mv = {}
            if m.get('image'):
                mv['image'] = m.get('image').get('showImage')
            mv['slug'] = m.get('slug')
            mv['title'] = m.get('title')
            movies.append(mv)
        return {u"response": movies}
