# -*- coding: utf-8 -*-

import mysqldb
from flask import *
import datetime

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize():
    query = "DROP TABLE IF EXISTS Temperature;"
    getDB().runUpdateQuery(query)
    query = "DROP TABLE IF EXISTS Humidite;"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Temperature (Temperature_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Temp FLOAT, Date_capteur DATETIME, CONSTRAINT temp_pk PRIMARY KEY (Temperature_id));"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Humidite (Humidite_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Hum FLOAT, Date_capteur DATETIME, CONSTRAINT hum_pk PRIMARY KEY (Humidite_id));"
    getDB().runUpdateQuery(query)
    return 'Temperature, Humidite'

def getTemperatureFromDB():
    query = "SELECT * FROM Temperature;"
    return getDB().runSelectQuery(query)

def getHumiditeFromDB():
    query = "SELECT * FROM Humidite;"
    return getDB().runSelectQuery(query)

def getTemperatureSenseurFromDB(capteur_id):
    query = "SELECT * FROM Temperature WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putTemperatureToDB(capteur, temperature, date):
    # query = "INSERT INTO Temperature (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", NOW());"
    query = "INSERT INTO Temperature (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", " +  date + ");"
    getDB().runUpdateQuery(query)

def getHumiditeSenseurFromDB(capteur_id):
    query = "SELECT * FROM Humidite WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putHumiditeToDB(capteur, humidite, date):
    # query = "INSERT INTO Humidite (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", NOW());"
    query = "INSERT INTO Humidite (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", " + date + ");"
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
    capteur_id = request.form.get('capteur_id')
    temperature = request.form.get('temp')
    if (not representsInt(senseur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': 'capteur_id ou temp ne sont pas des entiers.'})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(senseur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/temperatures', methods=['GET'])
def route_temperatures_get():
    reponse_records = getTemperatureFromDB()
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Température': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des températures': json_return})


@app.route('/humidites', methods=['POST'])
def route_humidites_post():
    capteur_id = request.form.get('capteur_id')
    humidite = request.form.get('hum')
    if (not representsInt(capteur_id)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': 'capteur_id ou hum ne sont pas des entiers.'})
    else:
        now = datetime.datetime.now()
        putHumiditeToDB(capteur_id, humidite, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['hum'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/humidites', methods=['GET'])
def route_humidites_get():
    reponse_records = getHumiditeFromDB()
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Humidité': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des humidités': json_return})


@app.route('/capteur1', methods=['POST'])
def route_temperatures_post():
    temperature = request.form.get('temp')
    humidite = request.form.get('hum')
    capteur_id = '1'
    if (not representsFloat(temperature)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': 'capteur_id ou temp ne sont pas des entiers.'})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        putHumiditeToDB(capteur_id, humidite, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/capteur2', methods=['POST'])
def route_temperatures_post():
    temperature = request.form.get('temp')
    humidite = request.form.get('hum')
    capteur_id = '2'
    if (not representsFloat(temperature)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': 'capteur_id ou temp ne sont pas des entiers.'})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        putHumiditeToDB(capteur_id, humidite, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

