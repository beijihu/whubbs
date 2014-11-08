import tornado.ioloop
import tornado.web
import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="index")

class Page1Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("page1.html", title="page1")

class Page2Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("page2.html", title="page2")

class Page3Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("page3.html", title="page3")

class Page4Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("page4.html", title="page4")        

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "public"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "debug": True,
}

application = tornado.web.Application([
    (r"/", IndexHandler),
    (r"/page1", Page1Handler),
    (r"/page2", Page2Handler),
    (r"/page3", Page3Handler),
    (r"/page4", Page4Handler),
], **settings)

if __name__ == "__main__":
    port = 8888
    application.listen(port)
    print "app running at http://localhost: %d" % (port)
    tornado.ioloop.IOLoop.instance().start()