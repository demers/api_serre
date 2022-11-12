# -*- coding: utf-8 -*-

import mysqldb
from flask import *
import datetime

VERSION = 'Novembre 2022'

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize(test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "DROP TABLE IF EXISTS Temperature" + test_str + ';'
    getDB().runUpdateQuery(query)
    query = "DROP TABLE IF EXISTS Humidite" + test_str + ';'
    getDB().runUpdateQuery(query)
    query = "DROP TABLE IF EXISTS Saturation" + test_str + ';'
    getDB().runUpdateQuery(query)
    #query = "CREATE TABLE Temperature (Temperature_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Temp FLOAT, Date_capteur DATETIME, CONSTRAINT temp_pk PRIMARY KEY (Temperature_id));"
    query = "CREATE TABLE Temperature" + test_str + " (Temperature_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Temp FLOAT, Date_capteur DATETIME, CONSTRAINT temp_pk PRIMARY KEY (Temperature_id));"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Humidite" + test_str + " (Humidite_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Hum FLOAT, Date_capteur DATETIME, CONSTRAINT hum_pk PRIMARY KEY (Humidite_id));"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Saturation" + test_str + " (Saturation_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Mesure FLOAT, Date_capteur DATETIME, CONSTRAINT sat_pk PRIMARY KEY (Saturation_id));"
    getDB().runUpdateQuery(query)
    return 'Temperature' + test_str + ', Humidite' + test_str + ', Saturation' + test_str

def getTemperatureFromDB(test = True, capteur=0):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    if capteur < 1:
        query = "SELECT * FROM Temperature" + test_str + ';'
    else:
        query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + str(capteur) + " ;"
    return getDB().runSelectQuery(query)

def getHumiditeFromDB(test = True, capteur=0):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    if capteur < 1:
        query = "SELECT * FROM Humidite" + test_str + ';'
    else:
        query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + str(capteur) + " ;"
    return getDB().runSelectQuery(query)

def getSaturationFromDB(test = True, capteur=0):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    if capteur > 0:
        query = "SELECT * FROM Saturation" + test_str + " WHERE Capteur = " + str(capteur) + " ;"
    else:
        query = "SELECT * FROM Saturation" + test_str + ';'

    return getDB().runSelectQuery(query)

def getTemperatureHumiditeFromDB(test = True, capteur):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    #query = "SELECT Temperature.Temperature_id, Temperature.Capteur, Temperature.Temp, Humidite.Hum, Temperature.Date_capteur FROM Temperature, Humidite WHERE Temperature.Temperature_id = Humidite.Humidite_id and Temperature.Capteur = " + str(capteur) + ";"
    query = "SELECT Temperature" + test_str + ".Temperature_id, Temperature" + test_str + ".Capteur, Temperature" + test_str + ".Temp, Humidite" + test_str + ".Hum, Temperature" + test_str + ".Date_capteur FROM Temperature" + test_str + ", Humidite" + test_str + " WHERE Temperature" + test_str + ".Temperature_id = Humidite" + test_str + ".Humidite_id and Temperature" + test_str + ".Capteur = " + str(capteur) + ";"
    return getDB().runSelectQuery(query)

def getTemperatureSenseurFromDB(test = True, capteur_id):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + capteur_id + ";"
    #query = "SELECT * FROM Temperature WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putTemperatureToDB(test = True, capteur, temperature, date):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # query = "INSERT INTO Temperature (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", NOW());"
    #query = "INSERT INTO Temperature (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", '" +  date + "');"
    query = "INSERT INTO Temperature" + test_str + " (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", '" +  date + "');"
    getDB().runUpdateQuery(query)

def getSaturationSenseurFromDB(test = True, capteur_id):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    #query = "SELECT * FROM Saturation WHERE Capteur = " + capteur_id + ";"
    query = "SELECT * FROM Saturation" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putSaturationToDB(test= True, capteur, mesure, date):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # query = "INSERT INTO Humidite (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", NOW());"
    #query = "INSERT INTO Saturation (Capteur, Mesure, Date_capteur) VALUES (" + capteur + ", " + mesure + ", '" + date + "');"
    query = "INSERT INTO Saturation" + test_str + " (Capteur, Mesure, Date_capteur) VALUES (" + capteur + ", " + mesure + ", '" + date + "');"
    getDB().runUpdateQuery(query)

def getHumiditeSenseurFromDB(test = True, capteur_id):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    #query = "SELECT * FROM Humidite WHERE Capteur = " + capteur_id + ";"
    query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putHumiditeToDB(test = True, capteur, humidite, date):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # query = "INSERT INTO Humidite (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", NOW());"
    #query = "INSERT INTO Humidite (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", '" + date + "');"
    query = "INSERT INTO Humidite" + test_str + " (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", '" + date + "');"
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
	return 'Bienvenue! Version ' + VERSION

@app.route('/')
def welcome():
	return hello()

# TEST
@app.route('/initialize')
def route_initialize():
    reponse = dbInitialize(test = True)
    return jsonify({'Réinitialisation.  Tables recréées ': reponse})

@app.route('/initialize_global')
def route_initialize(test = False):
    reponse = dbInitialize()
    return jsonify({'Réinitialisation des tables test.  Tables recréées ': reponse})


@app.route('/temperatures', methods=['POST'])
def route_temperatures_post():
    capteur_id = request.form.get('capteur_id')
    temperature = request.form.get('temp')
    if (not representsInt(capteur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne représentation"})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/temperatures', methods=['GET'])
def route_temperatures_get():
    reponse_records = getTemperatureFromDB(False)
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
        reponse = jsonify({'Erreur': "capteur_id ou hum n'ont pas la bonne représentation."})
    else:
        now = datetime.datetime.now()
        putHumiditeToDB(capteur_id, humidite, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/humidites', methods=['GET'])
def route_humidites_get():
    reponse_records = getHumiditeFromDB(False)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Humidité': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des humidités': json_return})

# Saturation
@app.route('/saturations', methods=['POST'])
def route_saturations_post():
    capteur_id = request.form.get('capteur_id')
    mesure = request.form.get('sat')
    if (not representsInt(capteur_id)) or (not representsFloat(mesure)):
        reponse = jsonify({'Erreur': "capteur_id ou sat n'ont pas la bonne représentation."})
    else:
        now = datetime.datetime.now()
        putSaturationToDB(False, capteur_id, mesure, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['sat'] = mesure
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse

# Saturation
@app.route('/saturations', methods=['GET'])
def route_saturations_get():
    reponse_records = getSaturationFromDB(False)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Saturation': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des saturations': json_return})

@app.route('/moniteur', methods=['GET'])
def route_capteur1_capteur2_get():
    reponse_records_capteur1 = getTemperatureFromDB(False, 1)
    reponse_records_capteur2 = getTemperatureFromDB(False, 2)
    json_return = dict()
    json_return = { 'Capteur ID': reponse_records_capteur1[0][1],
                        'Température': reponse_records_capteur1[0][2],
                        'Date': reponse_records_capteur1[0][3] }
                        'Capteur ID': reponse_records_capteur2[0][1],
                        'Humidité': reponse_records_capteur2[0][2],
                        'Date': reponse_records_capteur2[0][3] }
    return jsonify({'Liste des températures et humidités': json_return})

def route_capteur_hum_temp_post(test = True, capteur_id):
    temperature = request.form.get('temp')
    humidite = request.form.get('hum')
    if (not representsFloat(temperature)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne représentation."})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(test, str(capteur_id), temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        putHumiditeToDB(test, str(capteur_id), humidite, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = str(capteur_id)
        valeurs_enr['temp'] = temperature
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse

def route_capteur_gen_sat_post(test = True, capteur_id):
    mesure = request.form.get('sat')
    if not representsFloat(mesure):
        reponse = jsonify({'Erreur': "sat n'a pas la bonne représentation."})
    else:
        now = datetime.datetime.now()
        putSaturationToDB(test, str(capteur_id), mesure, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = str(capteur_id)
        valeurs_enr['sat'] = mesure
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse

def route_capteur_hum_temp_get(test = True, capteur_id):
    reponse_records = getTemperatureHumiditeFromDB(test, capteur_id)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Température': row[2],
                               'Humidité': row[3],
                               'Date': row[4] }
    return jsonify({'Liste des températures et humidités': json_return})


def route_capteur_gen_sat_get(test = True, capteur_id):
    reponse_records = getSaturationFromDB(test, capteur_id)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Mesure': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des mesures': json_return})

def route_capteur_gen_temp_get(test = True, capteur_id):
    reponse_records = getTemperatureFromDB(test, capteur_id)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Température': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des températures': json_return})

def route_capteur_gen_temp_post(test = True, capteur_id):
    temperature = request.form.get('temp')
    if (not representsInt(capteur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne représentation"})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(test, capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'))
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse



@app.route('/capteur1', methods=['POST'])
def route_capteur1_post():
    return route_capteur_hum_temp_post(1)

@app.route('/capteur1', methods=['GET'])
def route_capteur1_get():
    return route_capteur_hum_temp_get(1)

@app.route('/capteur2', methods=['POST'])
def route_capteur2_post():
    return route_capteur_hum_temp_post(2)

@app.route('/capteur2', methods=['GET'])
def route_capteur2_get():
    return route_capteur_hum_temp_get(2)

@app.route('/capteur3', methods=['POST'])
def route_capteur3_post():
    #return route_capteur_gen_sat_post(3)
    return route_capteur_hum_temp_post(3)

@app.route('/capteur3', methods=['GET'])
def route_capteur3_get():
    #return route_capteur_gen_sat_get(3)
    return route_capteur_hum_temp_get(3)

@app.route('/capteur4', methods=['POST'])
def route_capteur4_post():
    return route_capteur_gen_sat_post(4)

@app.route('/capteur4', methods=['GET'])
def route_capteur4_get():
    return route_capteur_gen_sat_get(4)

@app.route('/capteur5', methods=['POST'])
def route_capteur5_post():
    return route_capteur_gen_sat_post(5)

@app.route('/capteur5', methods=['GET'])
def route_capteur5_get():
    return route_capteur_gen_sat_get(5)

@app.route('/capteur6', methods=['POST'])
def route_capteur6_post():
    return route_capteur_gen_sat_post(6)

@app.route('/capteur6', methods=['GET'])
def route_capteur6_get():
    return route_capteur_gen_sat_get(6)

@app.route('/capteur7', methods=['POST'])
def route_capteur7_post():
    return route_capteur_gen_sat_post(7)

@app.route('/capteur7', methods=['GET'])
def route_capteur7_get():
    return route_capteur_gen_sat_get(7)

@app.route('/capteur8', methods=['POST'])
def route_capteur8_post():
    return route_capteur_gen_sat_post(8)

@app.route('/capteur8', methods=['GET'])
def route_capteur8_get():
    return route_capteur_gen_sat_get(8)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

