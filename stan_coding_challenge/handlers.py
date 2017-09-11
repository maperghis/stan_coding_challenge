#!/usr/bin/env python
"""
:created on: 11-09-2017
:modified on: 11-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import json
from stan_coding_challenge.errors import MyHTTPError


class BaseJsonHandler(object):
    """Base json handler provides the filter method which should be overridden
    to specify how the json data should be filtered"""

    def filter(self, data):
        """Filter the json data"""
        raise NotImplementedError()


class MovieHandler(BaseJsonHandler):
    """Handler for the specific movie json request objects"""

    def filter(self, data):
        """Filter the json data
        :param data: unfiltered data
        :type data: <dict>
        :return: filtered data
        :rtype: <dict>
        """
        try:
            data = json.load(data)
            assert isinstance(data, dict)
            payload = data["payload"]
            return self.processPayload(payload)
        except KeyError:
            desc = MyHTTPError.MISSING_PAYLOAD
            raise MyHTTPError(errorMsg=desc)
        # except (ValueError, AssertionError, AttributeError):
        except Exception:
            desc = MyHTTPError.INVALID_JSON
            raise MyHTTPError(errorMsg=desc)

    def processPayload(self, payload):
        """Process the payload of the data
        :param payload: unfiltered movies
        :type payload: <list>
        :return: filtered movies
        :rtype: <dict>
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
