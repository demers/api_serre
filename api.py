# -*- coding: utf-8 -*-

import mysqldb
from flask import *

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize():
    query = "DROP TABLE IF EXISTS Temperature;"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Temperature (Temperature_id INT NOT NULL AUTO_INCREMENT, Senseur INT, Temp DECIMAL(2, 2), Date_temp DATETIME, CONSTRAINT temp_pk PRIMARY KEY (Temperature_id));"
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
    return jsonify({'Réinitialisation.  Tables recréées ': reponse})

@app.route('/temperatures', methods=['POST'])
def route_temperatures_post():
	return 'post'

@app.route('/temperatures', methods=['GET'])
def route_temperatures_get():
	return 'get'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

