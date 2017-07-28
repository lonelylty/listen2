import tornado.ioloop
import tornado.web
import tornado.httpclient
import os,sys

import handler.home
import configuration.config

settings = {
    #"cookie_secret": "PYEKcp5FSMmMs9fn9AXJn/4jqHZLOUjEoK3E2lwrP8M=",
    #"login_url": "/login",
    #"static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "page")
}

application = tornado.web.Application([
    (r"/index", handler.home.indexHandler),
    (r"/()$", tornado.web.StaticFileHandler, {'path':'static/listen2.html'}),
    (r"/(.*)", tornado.web.StaticFileHandler, {'path':'static/'}),
    #(r".*", handler.nopage.NotFoundHandler)	
    ],**settings)


if __name__ == "__main__":
    print 'listen2 Web starts at port ' + str(configuration.config.WebServer_Port) + ' ...'

    application.listen(configuration.config.WebServer_Port)
    tornado.ioloop.IOLoop.instance().start()