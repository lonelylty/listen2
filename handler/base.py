import tornado.ioloop
import tornado.web
import tornado.httpclient
import datetime
#import requests
#import urllib
import traceback

class BaseHandler(tornado.web.RequestHandler):

    def GetRemoteIP(self):
        # if X-Forward-For is None, then get the remote IP from default location.
        # The reason need to check if X-Forward-For is that production is behind proxy server
        return self.request.headers.get("X-Forward-For") or self.request.remote_ip
    def GetRemoteUA(self):
    	return self.request.headers['User-Agent']


