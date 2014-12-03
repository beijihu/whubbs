#!/usr/bin/env python
#coding=utf-8

import tornado.ioloop
import tornado.web
import os

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", title="index")

class ChildClassHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("childClass.html", title="childClass")

class TopicsListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("topicsList.html", title="topicsList")   

class TopicViewHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("topicView.html", title="topicView")

class TopicEditHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("topicEdit.html", title="topicEdit") 

class SettingHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("setting.html", title="setting") 

class MessageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("message.html", title="message")    

settings = {
    "static_path": os.path.join(os.path.dirname(__file__), "public"),
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "debug": True,
}

application = tornado.web.Application([
    #首页九大板块——已完成（+7、wxc、mty）
    (r"/", IndexHandler),

    #首页下一层--版块子分类——已完成（可以优化==），就是主版页面，改成跟二级页面一样的样式（mty）
    (r"/childClass", ChildClassHandler),

    #版块子分类的下一层--帖子列表  二级页面
    (r"/topicsList", TopicsListHandler),

    #帖子列表的下一层--帖子详情页面  三级页面——完成度60%（mty）
    (r"/topicView", TopicViewHandler),

    #帖子编辑页面
    (r"/topicEdit", TopicEditHandler),

    #设置页面
    (r"/setting", SettingHandler),

    #私信页面
    (r"/message", MessageHandler),

], **settings)

if __name__ == "__main__":
    port = 9999
    application.listen(port)
    print "app running at http://localhost: %d" % (port)
    tornado.ioloop.IOLoop.instance().start()