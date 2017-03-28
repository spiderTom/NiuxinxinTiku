# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop
from tornado.web import Application, url, RequestHandler
from handlers.index import *


app = Application([
    url(r"/", MainHanlder),
    url(r"/niu", NiuHandler, name="niu"),
    url(r"/tom", TomHandler, name="tom"),
    url(r"/add", AddHandler, name="add"),
    url(r"/display", DisplayHandler, name="display"),
])


def main():
    app.listen(9123, "0.0.0.0")
    IOLoop.current().start()

if __name__ == "__main__":
    main()

