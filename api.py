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

def getTemperatureFromDB(test = True, capteur = 0, last = False):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    if last:
        last_str = ' ORDER BY Temperature_id DESC LIMIT 1'
        #last_str = ' WHERE Temperature_id=(SELECT MAX(Temperature_id) FROM Temperature)'
        #last_str_2 = ' AND Temperature_id=(SELECT MAX(Temperature_id) FROM Temperature)'
    else:
        last_str = ''
        #last_str_2 = ''
    if capteur < 1:
        query = "SELECT * FROM Temperature" + test_str + last_str  + ';'
    else:
        query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'
    if last:
        return getDB().runSelectOneQuery(query)
    else:
        return getDB().runSelectQuery(query)


def getHumiditeFromDB(test = True, capteur=0, last = False):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    if last:
        last_str = ' ORDER BY Humidite_id DESC LIMIT 1'
        #last_str = ' WHERE Humidite_id=(SELECT MAX(Humidite_id) FROM Humidite)'
        #last_str_2 = ' AND Humidite_id=(SELECT MAX(Humidite_id) FROM Humidite)'
    else:
        last_str = ''
        #last_str_2 = ''
    if capteur > 0:
        query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'
    else:
        query = "SELECT * FROM Humidite" + test_str + last_str + ';'
    if last:
        return getDB().runSelectOneQuery(query)
    else:
        return getDB().runSelectQuery(query)

def getSaturationFromDB(test = True, capteur=0, last = False):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    if last:
        last_str = ' ORDER BY Saturation_id DESC LIMIT 1'
        #last_str = ' WHERE Saturation_id=(SELECT MAX(Saturation_id) FROM Saturation)'
        #last_str_2 = ' AND Saturation_id=(SELECT MAX(Saturation_id) FROM Saturation)'
    else:
        last_str = ''
        #last_str_2 = ''

    if capteur > 0:
        query = "SELECT * FROM Saturation" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'
    else:
        query = "SELECT * FROM Saturation" + test_str + last_str + ';'
    return getDB().runSelectQuery(query)

def getTemperatureHumiditeFromDB(capteur, test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    #query = "SELECT Temperature.Temperature_id, Temperature.Capteur, Temperature.Temp, Humidite.Hum, Temperature.Date_capteur FROM Temperature, Humidite WHERE Temperature.Temperature_id = Humidite.Humidite_id and Temperature.Capteur = " + str(capteur) + ";"
    query = "SELECT Temperature" + test_str + ".Temperature_id, Temperature" + test_str + ".Capteur, Temperature" + test_str + ".Temp, Humidite" + test_str + ".Hum, Temperature" + test_str + ".Date_capteur FROM Temperature" + test_str + ", Humidite" + test_str + " WHERE Temperature" + test_str + ".Temperature_id = Humidite" + test_str + ".Humidite_id and Temperature" + test_str + ".Capteur = " + str(capteur) + ";"
    return getDB().runSelectQuery(query)

def getTemperatureSenseurFromDB(capteur_id, test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + capteur_id + ";"
    #query = "SELECT * FROM Temperature WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putTemperatureToDB(capteur, temperature, date, test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # query = "INSERT INTO Temperature (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", NOW());"
    #query = "INSERT INTO Temperature (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", '" +  date + "');"
    query = "INSERT INTO Temperature" + test_str + " (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", '" +  date + "');"
    getDB().runUpdateQuery(query)

def getSaturationSenseurFromDB(capteur_id, test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    #query = "SELECT * FROM Saturation WHERE Capteur = " + capteur_id + ";"
    query = "SELECT * FROM Saturation" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putSaturationToDB(capteur, mesure, date, test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # query = "INSERT INTO Humidite (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", NOW());"
    #query = "INSERT INTO Saturation (Capteur, Mesure, Date_capteur) VALUES (" + capteur + ", " + mesure + ", '" + date + "');"
    query = "INSERT INTO Saturation" + test_str + " (Capteur, Mesure, Date_capteur) VALUES (" + capteur + ", " + mesure + ", '" + date + "');"
    getDB().runUpdateQuery(query)

def getHumiditeSenseurFromDB(capteur_id, test = True):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    #query = "SELECT * FROM Humidite WHERE Capteur = " + capteur_id + ";"
    query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putHumiditeToDB(capteur, humidite, date, test = True):
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
    reponse = dbInitialize(True)
    return jsonify({'Réinitialisation des tables tests.  Tables recréées ': reponse})

@app.route('/initialize_global')
def route_initialize_global():
    reponse = dbInitialize(False)
    return jsonify({'Réinitialisation des tables test.  Tables recréées ': reponse})


@app.route('/temperatures', methods=['POST'])
def route_temperatures_post():
    capteur_id = request.form.get('capteur_id')
    temperature = request.form.get('temp')
    if (not representsInt(capteur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne représentation"})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'), False)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/temperatures', methods=['GET'])
def route_temperatures_get():
    reponse_records = getTemperatureFromDB(False, 0, False)
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
        putHumiditeToDB(capteur_id, humidite, now.strftime('%Y-%m-%d %H:%M:%S'), False)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse


@app.route('/humidites', methods=['GET'])
def route_humidites_get():
    reponse_records = getHumiditeFromDB(False, 0, False)
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
        putSaturationToDB(capteur_id, mesure, now.strftime('%Y-%m-%d %H:%M:%S'), False)
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
    # Obtenir les dernières valeurs des capteurs...
    reponse_temp_capteur1 = getTemperatureFromDB(False, 1, True)
    reponse_temp_capteur2 = getTemperatureFromDB(False, 2, True)
    reponse_hum_capteur1 = getHumiditeFromDB(False, 1, True)
    reponse_hum_capteur2 = getHumiditeFromDB(False, 2, True)
    json_return = dict()
    json_return[1] = {  'Capteur ID': reponse_temp_capteur1[1],
                        'Température': reponse_temp_capteur1[2],
                        'Humidité': reponse_hum_capteur1[2],
                        'Date': reponse_temp_capteur1[3] }

    json_return[2] = {  'Capteur ID': reponse_temp_capteur2[1],
                        'Température': reponse_temp_capteur2[2],
                        'Humidité': reponse_hum_capteur2[2],
                        'Date': reponse_temp_capteur2[3] }
    return jsonify({'Températures et humidités des capteurs 1 et 2': json_return})

def route_capteur_hum_temp_post(capteur_id, test = True):
    temperature = request.form.get('temp')
    humidite = request.form.get('hum')
    if (not representsFloat(temperature)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne représentation."})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(str(capteur_id), temperature, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        putHumiditeToDB(str(capteur_id), humidite, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = str(capteur_id)
        valeurs_enr['temp'] = temperature
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse

def route_capteur_gen_sat_post(capteur_id, test = True):
    mesure = request.form.get('sat')
    if not representsFloat(mesure):
        reponse = jsonify({'Erreur': "sat n'a pas la bonne représentation."})
    else:
        now = datetime.datetime.now()
        putSaturationToDB(str(capteur_id), mesure, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = str(capteur_id)
        valeurs_enr['sat'] = mesure
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse

def route_capteur_hum_temp_get(capteur_id, test = True):
    reponse_records = getTemperatureHumiditeFromDB(capteur_id, test)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Température': row[2],
                               'Humidité': row[3],
                               'Date': row[4] }
    return jsonify({'Liste des températures et humidités': json_return})


def route_capteur_gen_sat_get(capteur_id, test = True):
    reponse_records = getSaturationFromDB(test, capteur_id)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Mesure': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des mesures': json_return})

def route_capteur_gen_temp_get(capteur_id, test = True):
    reponse_records = getTemperatureFromDB(test, capteur_id, False)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Température': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des températures': json_return})

def route_capteur_gen_temp_post(capteur_id, test = True):
    temperature = request.form.get('temp')
    if (not representsInt(capteur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne représentation"})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardées': valeurs_enr})
    return reponse



@app.route('/capteur1', methods=['POST'])
def route_capteur1_post():
    return route_capteur_hum_temp_post(1, False)

@app.route('/capteur1', methods=['GET'])
def route_capteur1_get():
    return route_capteur_hum_temp_get(1, False)

@app.route('/capteur2', methods=['POST'])
def route_capteur2_post():
    return route_capteur_hum_temp_post(2, False)

@app.route('/capteur2', methods=['GET'])
def route_capteur2_get():
    return route_capteur_hum_temp_get(2, False)

@app.route('/capteur3', methods=['POST'])
def route_capteur3_post():
    #return route_capteur_gen_sat_post(3)
    return route_capteur_gen_temp_post(3, False)

@app.route('/capteur3', methods=['GET'])
def route_capteur3_get():
    #return route_capteur_gen_sat_get(3)
    return route_capteur_gen_temp_get(3, False)

@app.route('/capteur4', methods=['POST'])
def route_capteur4_post():
    return route_capteur_gen_sat_post(4, False)

@app.route('/capteur4', methods=['GET'])
def route_capteur4_get():
    return route_capteur_gen_sat_get(4, False)

@app.route('/capteur5', methods=['POST'])
def route_capteur5_post():
    return route_capteur_gen_sat_post(5, False)

@app.route('/capteur5', methods=['GET'])
def route_capteur5_get():
    return route_capteur_gen_sat_get(5, False)

@app.route('/capteur6', methods=['POST'])
def route_capteur6_post():
    return route_capteur_gen_sat_post(6, False)

@app.route('/capteur6', methods=['GET'])
def route_capteur6_get():
    return route_capteur_gen_sat_get(6, False)

@app.route('/capteur7', methods=['POST'])
def route_capteur7_post():
    return route_capteur_gen_sat_post(7, False)

@app.route('/capteur7', methods=['GET'])
def route_capteur7_get():
    return route_capteur_gen_sat_get(7, False)

@app.route('/capteur8', methods=['POST'])
def route_capteur8_post():
    return route_capteur_gen_sat_post(8, False)

@app.route('/capteur8', methods=['GET'])
def route_capteur8_get():
    return route_capteur_gen_sat_get(8, False)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

