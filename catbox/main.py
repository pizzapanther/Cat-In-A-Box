import os

import tornado.ioloop
import tornado.web
import tornado.log
import tornado.template
import tornado.autoreload

MYDIR = os.path.dirname(__file__)
STATIC_PATH = os.path.join(MYDIR, "static")
TEMPLATE_PATH = os.path.join(MYDIR, "templates")

class MainHandler (tornado.web.RequestHandler):
  def get (self):
    loader = tornado.template.Loader(TEMPLATE_PATH)
    t = loader.load("index.html")
    context = {}
    html = t.generate(**context)
    
    self.write(html)
    
application = tornado.web.Application([
  (r"/favicon.ico", tornado.web.RedirectHandler, {"url": "/static/img/icon-64.png"}),
  (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': STATIC_PATH}),
  (r"/", MainHandler),
])

def run ():
  tornado.log.enable_pretty_logging()
  
  application.listen(8888)
  ioloop = tornado.ioloop.IOLoop.instance()
  tornado.autoreload.start(ioloop)
  ioloop.start()
  