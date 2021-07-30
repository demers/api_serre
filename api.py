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
    query = "INSERT INTO Temperature (Senseur, Temp, Date_temp) VALUES (" + senseur + ", " + temperature + ", NOW());"
    getDB().runUpdateQuery(query)

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def representsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

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
    senseur_id = request.form.get('senseur_id')
    temperature = request.form.get('temp')
    if (not representsInt(senseur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': 'senseur_id ou temp ne sont pas des entiers.'})
    else:
        putTemperatureToDB(senseur_id, temperature)
        valeurs_enr = dict()
        valeurs_enr['senseur_id'] = senseur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/temperatures', methods=['GET'])
def route_temperatures_get():
    reponse_records = getTemperatureFromDB()
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Senseur ID': row[1],
                               'Température': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des températures': json_return})

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

