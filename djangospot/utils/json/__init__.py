from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from django.utils import simplejson as json

import uuid

class BetterJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, uuid.UUID):
            return obj.hex
        return super(BetterJSONEncoder, self).default(obj)

def better_decoder(data):
    return data

def dumps(value, **kwargs):
    return json.dumps(value, cls=BetterJSONEncoder, **kwargs)

def loads(value, **kwargs):
    return json.loads(value, object_hook=better_decoder)

class JSONHttpResponse(HttpResponse):
    def __init__(self, data, *args, **kwargs):
        kwargs['mimetype'] = 'application/json'
        super(JSONHttpResponse, self).__init__(dumps(data), *args, **kwargs)