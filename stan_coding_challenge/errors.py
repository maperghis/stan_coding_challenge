#!/usr/bin/env python
"""
:created on: 10-09-2017
:modified on: 10-09-2017
:author: Miranda Aperghis <miranda>
:contact: miranda.aperghis@gmail.com
"""
import falcon
from falcon import HTTPError
import falcon.status_codes as status


class MyHTTPError(HTTPError):

    INVALID_JSON = "Could not decode request: JSON parsing failed"
    MISSING_PAYLOAD = "Could not decode request: JSON missing payload key"
    UNSUPPORTED_MEDIA_TYPE = "Unsupported media type: Only JSON accepted"

    def __init__(self, title=None, description=None, errorMsg=None,
                    status=status.HTTP_400, **kwargs):
        super(MyHTTPError, self).__init__(status, title,
                                                description, **kwargs)
        self.errorMsg = errorMsg

    def to_dict(self, obj_type=dict):
        obj = obj_type()
        if self.errorMsg is not None:
            obj['error'] = self.errorMsg
        return obj
