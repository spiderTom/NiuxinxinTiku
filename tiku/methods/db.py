# -*- coding: utf-8 -*-
import MySQLdb
from common import item


def getAllPractice():
    print "getAllPractice"
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="niu", port=3306,
                           charset="utf8")  # 连接对象
    results = []
    cur = conn.cursor()  # 游标对象
    cur.execute("select * from xinxin")
    data = cur.fetchall()
    for row in data:
        result = item(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        results.append(result)

    return results

def getRightIdForTitle(title):
    print "getRightIdForTitle"
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="niu", port=3306,
                           charset="utf8")  # 连接对象
    results = []
    cur = conn.cursor()  # 游标对象
    cur.execute("select * from xinxin where title=%s" % title)
    data = cur.fetchall()
    for row in data:
        result = item(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        results.append(result)

    return results

def getRightIdForTitleId(id):
    print "getRightIdForTitleId %d" % id
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="niu", port=3306,
                           charset="utf8")  # 连接对象
    results = []
    cur = conn.cursor()  # 游标对象
    cur.execute("select * from xinxin where id=%d" % id)
    data = cur.fetchall()
    for row in data:
        result = item(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        results.append(result)

    return results

def addItem(additem):
    print "addItem"
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="niu", port=3306,
                           charset="utf8")  # 连接对象
    cur = conn.cursor()
    cur.execute("select * from xinxin")
    data = cur.fetchall()
    currentId = len(data) + 1
    command = "INSERT INTO xinxin VALUES ('%d', '%s', '%s', '%s', '%s', '%s', '%s')" % \
          (currentId, additem.title, additem.ansA, additem.ansB, additem.ansC, additem.ansD, additem.rightId)
    #command = "insert into xinxin values(" + str(currentId) + ',' + additem.title + ',' + additem.ansA + ',' + additem.ansB + ',' + \
    #    additem.ansC + ',' + additem.ansD + ',' + additem.rightId + ')'
    print command
    cur.execute(command)
    conn.commit()
    conn.close()

def getTitleNumber():
    print "getTitleNumber"
    conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="niu", port=3306,
                           charset="utf8")  # 连接对象
    results = []
    cur = conn.cursor()  # 游标对象
    cur.execute("select * from xinxin")
    data = cur.fetchall()
    return len(data)