import os

import tornado.ioloop
import tornado.web
import tornado.log
import tornado.template
import tornado.autoreload

class MainHandler (tornado.web.RequestHandler):
  def get(self):
    mydir = os.path.dirname(__file__)
    
    loader = tornado.template.Loader(os.path.join(mydir, "templates"))
    t = loader.load("index.html")
    context = {}
    html = t.generate(**context)
    
    self.write(html)
    
application = tornado.web.Application([
  (r"/", MainHandler),
])

def run ():
  tornado.log.enable_pretty_logging()
  
  application.listen(8888)
  ioloop = tornado.ioloop.IOLoop.instance()
  tornado.autoreload.start(ioloop)
  ioloop.start()
  