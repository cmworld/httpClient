# -*- coding: utf-8 -*-
import base64
import urllib
import httplib
from urlparse import urlparse

try:
    import json
except ImportError:
    import simplejson as json

class httpClient(object):
    _host = ''
    _timeout = 10
    _port = 80
    _user = ''
    _pass = ''

    def __init__(self, hosturl,timeout,username='',password=''):
        o = urlparse(hosturl)
        self._host = o.hostname
        self._port = o.port
        self._timeout = timeout
        self._user = username
        self._pass = password

    def _http_send(self, method, url_path, params):
        conn = httplib.HTTPConnection(self._host,self._port,False,self._timeout)

        headers = {}
        if self._user and self._pass:
            auth = base64.encodestring('%s:%s' % (self._user, self._pass)).replace('\n', '')
            headers = {"Authorization":"Basic %s" % auth}

        method = method.upper()
        str_params = urllib.quote("&".join(k + "=" + str(params[k]) for k in sorted(params.keys())), '')
        conn.request(method, url_path, str_params,headers)
        rsp = conn.getresponse()

        if rsp.status != 200:
            raise ValueError, 'status:%d' % rsp.status

        data = rsp.read()
        conn.close()
        return data

    def open(self, method, url_path, params):
        return self._http_send(method, url_path, params)