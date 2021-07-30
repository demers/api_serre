# -*- coding: utf-8 -*-

import mysqldb
from flask import *

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize():
    query = "DROP TABLE IF EXISTS Temperature;"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Temperature (TemperatureID INT AUTO_INCREMENT, Senseur INT, Temp DECIMAL(2, 2), Date_temp DATETIME);"
    getDB().runUpdateQuery(query)
    return 'Temperature'

def getTemperatureFromDB(senseur):
    query = "..."
    getDB().runUpdateQuery(query)

def putTemperatureToDB(senseur, temperature):
    query = "INSERT INTO Temperature (Senseur, Temp, Date_temp) VALUES (" + str(senseur) + ", " + str(temperature) + ", NOW());"
    getDB().runUpdateQuery(query)


app = Flask('API pour la serre')

def hello():
	return 'Bienvenue!'

@app.route('/')
def welcome():
	return hello()

@app.route('/initialize')
def route_initialize():
    reponse = dbInitialize()
    return jsonify({'Tables recréées ': reponse})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

