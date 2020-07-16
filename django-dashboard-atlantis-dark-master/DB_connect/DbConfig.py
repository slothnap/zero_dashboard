import socket
import pymysql


class DbConfig:
    db_config = {}
    db = None
    cursor = None

    def __init__(self, db_info=None):
        ip = socket.gethostbyname(socket.getfqdn())
        if db_info is not None:
            self.db_config = db_info
        elif ip == '192.168.102.144':  # MDM 운영
            self.db_config = {
                'host': '192.168.102.144'
                , 'user': 'root'
                , 'password': 'wpdltms123!@#'
                , 'db': 'test'
            }
        else:  # MDM 개발
            self.db_config = {
                'host': '192.168.0.63'
                , 'user': 'MDM_Admin'
                , 'password': 'wpdltms123!@#'
                , 'db': 'MDM'
            }

    def setdb(self, db_info):
        self.db_config = db_info

    def getdb(self):
        return self.db_config

    def opendb(self):
        self.db = pymysql.connect(**self.db_config)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def closedb(self):
        self.db.close()

    def select(self, sql):

        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def update(self, sql):
        self.cursor.execute(sql)
        self.db.commit()
