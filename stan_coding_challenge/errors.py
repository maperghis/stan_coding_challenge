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
    """Type of HTTPError which takes an error message when creating an
    instance of this error and overrides the to_dict method to display the
    given error"""

    INVALID_JSON = "Could not decode request: JSON parsing failed"
    UNSUPPORTED_MEDIA_TYPE = "Could not decode request: Unsupported media type, only JSON accepted"

    def __init__(self, title=None, description=None, errorMsg=None,
                    status=status.HTTP_400, **kwargs):
        super(MyHTTPError, self).__init__(status, title,
                                                description, **kwargs)
        self.errorMsg = errorMsg

    def to_dict(self, obj_type=dict):
        """Override the to_dict method to return only the error key
        :return: error message
        :rtype: <dict>
        """
        obj = obj_type()
        if self.errorMsg is not None:
            obj['error'] = self.errorMsg
        return obj
