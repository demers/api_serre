# -*- coding: utf-8 -*-

import mysqldb
from flask import *

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize():
    query = "DROP TABLE IF EXISTS Temperature;"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Temperature (Temperature_id INT NOT NULL AUTO_INCREMENT, Senseur INT, Temp FLOAT, Date_temp DATETIME, CONSTRAINT temp_pk PRIMARY KEY (Temperature_id));"
    getDB().runUpdateQuery(query)
    return 'Temperature'

def getTemperatureFromDB():
    query = "SELECT * FROM Temperature;"
    return getDB().runSelectQuery(query)

def getTemperatureSenseurFromDB(senseur_id):
    query = "SELECT * FROM Temperature WHERE Senseur = " + senseur_id + ";"
    return getDB().runSelectQuery(query)

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
    reponse_sql = getTemperatureFromDB()
    return jsonify({'Requête': str(reponse_sql)})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

