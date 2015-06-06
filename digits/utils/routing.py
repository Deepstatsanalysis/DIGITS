# Copyright (c) 2015, NVIDIA CORPORATION.  All rights reserved.

from flask import request

# Adapted from http://flask.pocoo.org/snippets/45/
def request_wants_json():
    """
    Returns True if the response should be JSON
    """
    if request.base_url.endswith('.json'):
        return True
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    # Some browsers accept on */* and we don't want to deliver JSON to an ordinary browser
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']

