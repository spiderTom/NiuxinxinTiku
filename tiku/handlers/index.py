# -*- coding: utf-8 -*-
from tornado.ioloop import IOLoop
from tornado.web import Application, url, RequestHandler
from tornado.httpclient import AsyncHTTPClient
from tornado.web import asynchronous, RequestHandler
from tornado.gen import coroutine
import MySQLdb
import sys
sys.path.append("..")
from methods.db import *
#from methods.MySQL import *

class MainHanlder(RequestHandler):
    def get(self):
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123/niu">牛鑫鑫答题库</a>')
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123/tom">管理员界面</a>')

class NiuHandler(RequestHandler):
    def get(self):
        print "enter get"
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123">回到首页</a>')
        self.write('<br> ')
        self.results = getAllPractice()
        count = 0
        self.write('<form action="/niu" method="POST">')
        for item in self.results:
            count += 1
            name = "Title" + str(count)
            print name
            self.write('\n%d' % item.id)
            self.write('  %s' % item.title)
            self.write('<br> ')
            self.write('<input type="radio" name=%s value="ansA">' % name)
            self.write('%s' % item.ansA)
            self.write('<br>')
            self.write('<input type="radio" name=%s value="ansB">' % name)
            self.write('%s' % item.ansB)
            self.write('<br>')
            self.write('<input type="radio" name=%s value="ansC">' % name)
            self.write('%s' % item.ansC)
            self.write('<br>')
            self.write('<input type="radio" name=%s value="ansD">' % name)
            self.write('%s' % item.ansD)
            self.write('<br>')
        self.write('<input type="submit">')
        self.write('</form>')


    def post(self):
        #self.set_header("Content-Type", "text/plain")
        print "enter post"
        print(self.request.arguments)
        print "--------------"
        count = len(self.request.arguments)
        print "count is %d" % count
        print "--------------"

        for key in self.request.arguments.keys():
            value = self.get_body_argument(key)
            print "===key ===  value==="
            print key, value
            titleId = int(key[5])
            rightAnswer = getRightIdForTitleId(titleId)
            print "===titleId ===  rightAnswer[0]==="
            print titleId, rightAnswer[0].title
            index = ord(rightAnswer[0].rightId[3]) - ord('A')
            print index
            if (len(rightAnswer) == 1 and rightAnswer[0].rightId == value):
                self.write("你猜对了！！！！" )
                self.write('<br>')
                self.write(rightAnswer[0].title)
                self.write("答案是：")
            else:
                self.write("你猜错了。。。。")
                self.write('<br>')
                self.write(rightAnswer[0].title)
                self.write("答案不是：")

            self.write('<br> ')
            if index == 1:
                self.write(rightAnswer[0].ansA)
            elif index == 2:
                self.write(rightAnswer[0].ansB)
            elif index == 3:
                self.write(rightAnswer[0].ansC)
            else:
                self.write(rightAnswer[0].ansD)
            self.write('<br> ')
            self.write('<br> ')


class TomHandler(RequestHandler):
    def get(self):
        print "user entered tom page!!!"
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123/add">编辑题库</a>')
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123/display">查看题库</a>')
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123">回到首页</a>')
        self.write('<br> ')



class AddHandler(RequestHandler):
    def get(self):
        print "user enter add database page"
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123">回到首页</a>')
        self.write('<br> ')

        self.write('<html><body><form action="/add" method="POST">'
            '<input type="text" name="title">'
            '<input type="text" name="ansA">'
            '<input type="text" name="ansB">'
            '<input type="text" name="ansC">'
            '<input type="text" name="ansD">'
            '<input type="text" name="rightId">'
            '<input type="submit" value="addtodatabase">'
            '</form></body></html>')

    def post(self):
        additem = item(0, '', '', '', '', '', '')
        additem.title = self.get_body_argument("title")
        additem.ansA = self.get_body_argument("ansA")
        additem.ansB = self.get_body_argument("ansB")
        additem.ansC = self.get_body_argument("ansC")
        additem.ansD = self.get_body_argument("ansD")
        additem.rightId = self.get_body_argument("rightId")
        addItem(additem)
        print "数据添加成功！！"
        self.write("数据添加成功！！")
        self.write('<br> ')
        self.write("点击下面的链接查看更新后的数据库：")
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123/display">查看题库</a>')


class DisplayHandler(RequestHandler):
    def get(self):
        self.write('<br> ')
        self.write('<a href="http://10.140.30.172:9123">回到首页</a>')
        self.write('<br> ')
        results = getAllPractice()
        print "display table, and the col is %d" % len(results)
        for item in results:
            self.write('\n%d' % item.id)
            self.write('  %s\n' % item.title)
            self.write('<br> ')
            self.write('  %s\n' % item.ansA)
            self.write('<br> ')
            self.write('  %s\n' % item.ansB)
            self.write('<br> ')
            self.write('  %s\n' % item.ansC)
            self.write('<br> ')
            self.write('  %s\n' % item.ansD)
            self.write('<br> ')
            self.write('  %s\n' % item.rightId)
            self.write('<br> ')
            self.write("==========================\n")
            self.write('<br> ')
