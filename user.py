# coding:utf8
class User(object):
    def __init__(self, username, passwd, host):
        self.username = username
        self.passwd = passwd
        self.host = host

    def create(self):
        sql = "CREATE USER '{username}'@'{host}' IDENTIFIED BY '{passwd}';".format(**{
            "host": self.host,
            "username": self.username,
            "passwd": self.passwd,
        })
        return self.cursor.execute(sql)
