# coding:utf8
import pymysql


class Connection(object):
    def __init__(self, host, port, user, passwd, autocommit=True):
        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            passwd=passwd,
            autocommit=autocommit,
        )
        self.cursor = self.conn.cursor()

    def databases(self):
        self.cursor.execute("show databases;")
        databases = self.cursor.fetchall()
        return [x[0] for x in databases]

    def tables(self, db):
        self.cursor.execute("use {}".format(db))
        self.cursor.execute("show tables;")
        tables = self.cursor.fetchall()
        return [x[0] for x in tables]
