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
  (r"/", MainHandler),
  (r"/static/(.*)", tornado.web.StaticFileHandler, {'path': STATIC_PATH}),
])

def run ():
  tornado.log.enable_pretty_logging()
  
  application.listen(8888)
  ioloop = tornado.ioloop.IOLoop.instance()
  tornado.autoreload.start(ioloop)
  ioloop.start()
  