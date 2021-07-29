# -*- coding: utf-8 -*-

import mysql.connector
import base64


class MYSQLDB():
    __instance = None

    ACCESS = 'amNkaTM3MjYK'

    @staticmethod
    def getInstance():
        if MYSQLDB.__instance == None:
            MYSQLDB()
        return MYSQLDB.__instance

    def getConfig():
        config = {
            'user': 'serre',
            # 'password': 'jcdi3726'
            'password': base64.b64decode(ACCESS).decode('UTF-8')[:-1]
            'host': 'localhost'
            'port': '3306'
            'database':'serre'}
        return config

    def __init__(self):
        if MYSQLDB.__instance != None:
            raise Exception("There should only be one instance of SQLiteDB")
        else:
            MYSQLDB.__instance = self
            #self.db = mysql.connector.connect(**getConfig())

    def runUpdateQuery(self, query):
        try:
            conn = mysql.connector.connect(**getConfig())
            cursor = conn.cursor()
            print(query, flush=True)
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print("some exception occurred: " + str(e), flush=True)
        finally:
            cursor.close()
            conn.close()

