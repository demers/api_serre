# -*- coding: utf-8 -*-

import mysqldb
from flask import *

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize():
    query = "..."
    getDB().runUpdateQuery(query)

def getTemperatureFromDB(senseur):
    query = "..."
    getDB().runUpdateQuery(query)

def putTemperatureToDB(senseur):
    query = "..."
    getDB().runUpdateQuery(query)


app = Flask('API pour la serre')

def hello():
	return 'Bienvenue!'

@app.route('/')
def welcome():
	return hello()



if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

