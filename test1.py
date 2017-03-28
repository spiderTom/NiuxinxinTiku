#!/usr/bin/env python
# -*- coding: utf-8 -*-
# hello_get_post.py tornadohelloworld案例  orangleliu@2014.03.02
# 这里是一个简单的页面，get一个表单页面，使用post处理请求,没有使用模板就是
# 直接用字符拼出来的html

import tornado.ioloop
import tornado.web


# handler request请求
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<html><body>' +
                   '<form action="/" method="post">' +
                   '<input type="text" name="message">' +
                   '<input type="submit" value"提交">' +
                   '</form>' +
                   '</body></html>')

    def post(self):
        # 获取参数
        message = self.get_argument("message", None)
        self.write('Form input is :<h1>' + message + '</h1>')


        # url router


application = tornado.web.Application([
    (r'/', MainHandler),
])

# web server
if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()