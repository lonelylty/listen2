import tornado.ioloop
import tornado.web
import os,sys
from tornado import httpclient,gen

import configuration.config
import handler.base

class indexHandler(handler.base.BaseHandler):

	@tornado.gen.coroutine
	def get(self):
		url=self.get_argument("url", '', True)
		domain=self.get_argument("domain", '', True)

		if len(url)==0:
			url=configuration.config.common_url
		if len(domain)==0:
			domain=configuration.config.common_domain
		print(url+"\r\n"+self.GetRemoteIP()+" "+self.GetRemoteUA())
			
		try:
			response = yield httpclient.AsyncHTTPClient().fetch(url, headers=self.domain_to_heads(domain))
			if domain=="netease" and "playlist" in url:
				result=response.body
				# result=tornado.escape.to_basestring(response.body[8100:])
			else:
				result=response.body
			self.write(result)
		except httpclient.HTTPError as e:
			print('Exception: %s %s' % (e, url))
			raise gen.Return([])

	@tornado.gen.coroutine
	def post(self):
		url=self.get_argument("url", '', True)
		domain=self.get_argument("domain", '', True)

		# netease search songs arg
		s=self.get_argument("s", '', True)
		offset=self.get_argument("offset", '', True)
		limit=self.get_argument("limit", '', True)
		tye=self.get_argument("type", '', True)

		# netease bootstrap_track/lyric arg
		encSecKey=self.get_argument("encSecKey", '', True)
		params=self.get_argument("params", '', True)

		if len(url)==0:
			url=configuration.config.common_url
		if len(domain)==0:
			domain=configuration.config.common_domain

		if len(s)!=0 or len(offset)!=0 or len(limit)!=0 or len(tye)!=0:
			data ='s='+s+'&offset='+ offset+'&limit='+ limit+'&type='+ tye
		elif len(encSecKey)!=0 or len(params)!=0:
			# tornado.escape.url_unescape(url, encoding='utf-8', plus=True)
			data='encSecKey='+tornado.escape.url_escape(encSecKey, plus=True)+'&params='+tornado.escape.url_escape(params, plus=True)

		print(url+"\r\n"+data)

		try:
			response = yield httpclient.AsyncHTTPClient().fetch(url, method='POST',body=data,headers=self.domain_to_heads(domain))
			result=str(response.body)
			# print(result)
			self.write(result)
		except httpclient.HTTPError as e:
			print('Exception: %s %s' % (e, url))
			raise gen.Return([])

	def domain_to_heads(self,argument):
		switcher = {
		    "netease": configuration.config.netease_request_header,
		    "qq": configuration.config.qq_request_header,
		    "xiami": configuration.config.xiami_request_header
		}
		return switcher.get(argument, "nothing")
	