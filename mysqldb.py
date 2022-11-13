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

    def getConfig(self):
        config = {
            'user': 'serre',
            'password': base64.b64decode(self.ACCESS).decode('UTF-8')[:-1],
            'host': 'localhost',
            'port': '3306',
            'database':'serre'}
        return config

    def __init__(self):
        if MYSQLDB.__instance != None:
            raise Exception("There should only be one instance of Mysql")
        else:
            MYSQLDB.__instance = self
            #self.db = mysql.connector.connect(**getConfig())

    def runUpdateQuery(self, query):
        try:
            conn = mysql.connector.connect(**self.getConfig())
            cursor = conn.cursor()
            print(query, flush=True)
            cursor.execute(query)
            conn.commit()
        except Exception as e:
            print("some exception occurred: " + str(e), flush=True)
        finally:
            if conn.is_connected():
                conn.close()
                cursor.close()

    def runSelectQuery(self, query):
        records = []
        try:
            conn = mysql.connector.connect(**self.getConfig())
            cursor = conn.cursor()
            print(query, flush=True)
            cursor.execute(query)
            records = cursor.fetchall()
            conn.commit()
        except Exception as e:
            print("some exception occurred: " + str(e), flush=True)
        finally:
            if conn.is_connected():
                conn.close()
                cursor.close()
        return records

    def runSelectOneQuery(self, query):
        record = ()
        try:
            conn = mysql.connector.connect(**self.getConfig())
            cursor = conn.cursor()
            print(query, flush=True)
            cursor.execute(query)
            record = cursor.fetchone()
            conn.commit()
        except Exception as e:
            print("some exception occurred: " + str(e), flush=True)
        finally:
            if conn.is_connected():
                conn.close()
                cursor.close()
        return record
