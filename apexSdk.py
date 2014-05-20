# -*- coding:utf-8 -*-
try:
    import json
except ImportError:
    import simplejson as json

from httpClient import httpClient

OPEN_HTTP_TRANSLATE_ERROR = 1801

class ApexServ(object):

    _api = None
    _hosturl = ""
    _timeout = 5
    _user = 'apex'
    _pass = 'apex'

    def __init__(self,hosturl):
        self._api = httpClient(hosturl, self._timeout,self._user,self._pass)

    def call(self, url_path, params, method='post'):

        try:
            data = self._api.open(method, url_path, params)
        except Exception, e:
            return {'error':OPEN_HTTP_TRANSLATE_ERROR, 'ret':str(e)}

        try:
            ret = json.loads(data)
        except:
            return data
        else:
            return ret
