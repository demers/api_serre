# -*- coding: utf-8 -*-

import mysqldb
from flask import *
import datetime

VERSION = 'Fevrier 2023'

def getDB():
    return mysqldb.MYSQLDB.getInstance()

def dbInitialize(test = True):
    # Initialize the database by deleting the tables and recreating it
    
    if test:
        test_str = '_test'
    else:
        test_str = ''

    # Delete the existing table
    query = "DROP TABLE IF EXISTS Temperature" + test_str + ';'
    getDB().runUpdateQuery(query)
    query = "DROP TABLE IF EXISTS Humidite" + test_str + ';'
    getDB().runUpdateQuery(query)
    query = "DROP TABLE IF EXISTS Saturation" + test_str + ';'
    getDB().runUpdateQuery(query)
    query = "DROP TABLE IF EXISTS Systemes" + test_str + ';'
    getDB().runUpdateQuery(query)


    # Create the table
    query = "CREATE TABLE Temperature" + test_str + " (Temperature_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Temp FLOAT, Date_capteur DATETIME, CONSTRAINT temp_pk PRIMARY KEY (Temperature_id));"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Humidite" + test_str + " (Humidite_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Hum FLOAT, Date_capteur DATETIME, CONSTRAINT hum_pk PRIMARY KEY (Humidite_id));"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Saturation" + test_str + " (Saturation_id INT NOT NULL AUTO_INCREMENT, Capteur INT, Mesure FLOAT, Date_capteur DATETIME, CONSTRAINT sat_pk PRIMARY KEY (Saturation_id));"
    getDB().runUpdateQuery(query)
    query = "CREATE TABLE Systemes" + test_str + " (Systeme_id INT NOT NULL AUTO_INCREMENT, Systeme VARCHAR(10), Etat BOOL, Date DATETIME, CONSTRAINT sys_pk PRIMARY KEY (Systeme_id));"
    getDB().runUpdateQuery(query)


    return 'Temperature' + test_str + ', Humidite' + test_str + ', Saturation' + test_str

def getTemperatureFromDB(test = True, capteur = 0, last = False):
    # capteur < 1  -> Get all temperature from all sensors
    # last = false -> Get all temperature from the sensor
    # last = true  -> Get the last temperature from the sensor

    if test:
        test_str = '_test'
    else:
        test_str = ''

    if last:
        last_str = ' ORDER BY Temperature_id DESC LIMIT 1'
    else:
        last_str = ''

    if capteur < 1:
        query = "SELECT * FROM Temperature" + test_str + last_str  + ';'
    else:
        query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'

    if last:
        return getDB().runSelectOneQuery(query)
    else:
        return getDB().runSelectQuery(query)
"""
def getHistorique24HTempFromDB(test = True, capteur = 0):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # 96 = 24x4 Data des 24 derniere heure aux 15 mins
    last_str = ' ORDER BY Temperature_id DESC LIMIT 96'
    

    if capteur < 1:
        query = "SELECT * FROM Temperature" + test_str + last_str  + ';'
    else:
        query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'

    return getDB().runSelectQuery(query)
"""    
def getHistorique24HTempFromDB(test=True, capteur=0):
    if test:
        test_str = '_test'
    else:
        test_str = ''

    order_str = ' ORDER BY Temperature_id DESC'
    time_filter = " WHERE Date_capteur >= NOW() - INTERVAL 24 HOUR"

    if capteur < 1:
        query = (
            "SELECT * FROM Temperature" + test_str
            + time_filter
            + order_str + ';'
        )
    else:
        query = (
            "SELECT * FROM Temperature" + test_str
            + time_filter
            + " AND Capteur = " + str(capteur)
            + order_str + ';'
        )

    return getDB().runSelectQuery(query)
"""
def getHistorique24HHumFromDB(test = True, capteur = 0):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # 96 = 24x4 Data des 24 derniere heure aux 15 mins
    last_str = ' ORDER BY Humidite_id DESC LIMIT 96'
    

    if capteur < 1:
        query = "SELECT * FROM Humidite" + test_str + last_str  + ';'
    else:
        query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'

    return getDB().runSelectQuery(query)
"""
def getHistorique24HHumFromDB(test = True, capteur = 0):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    
    order_str = ' ORDER BY Humidite_id DESC'
    time_filter = " WHERE Date_capteur >= NOW() - INTERVAL 24 HOUR"

    if capteur < 1:
        query = (
            "SELECT * FROM Humidite" + test_str
            + time_filter
            + order_str + ';'
        )
    else:
        query = (
            "SELECT * FROM Humidite" + test_str
            + time_filter
            + " AND Capteur = " + str(capteur)
            + order_str + ';'
        )
    return getDB().runSelectQuery(query)
"""
def getHistorique24HSystemesFromDB(test = True, systeme = ""):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    # 96 = 24x4 Data des 24 derniere heure aux 15 mins
    last_str = ' ORDER BY Systeme_id DESC LIMIT 96'
    if not isSysteme(systeme):
        systeme = ""

    if systeme == "":
        query = "SELECT * FROM Systemes" + test_str + last_str  + ';'
    else:
        query = "SELECT * FROM Systemes" + test_str + " WHERE Systeme = '" + systeme +"'" + last_str + ';'

    return getDB().runSelectQuery(query)
"""


def getHistorique24HSystemesFromDB(test = True, systeme = ""):
    if test:
        test_str = '_test'
    else:
        test_str = ''
    order_str = ' ORDER BY Systeme_id DESC'
    time_filter = " WHERE Date >= NOW() - INTERVAL 24 HOUR"
    if not isSysteme(systeme):
        systeme = ""

    if systeme == "":
        query = (
            "SELECT * FROM Systemes" + test_str
            + time_filter
            + order_str + ';'
        )
    else:
        query = (
            "SELECT * FROM Systemes" + test_str
            + time_filter
            + " AND Systeme = '" +  systeme +"'" 
            + order_str + ';'
        )
    return getDB().runSelectQuery(query)

def getHumiditeFromDB(test = True, capteur=0, last = False):
    # capteur < 1  -> Get all humidity from all sensors
    # last = false -> Get all humidity from the sensor
    # last = true  -> Get the last humidity from the sensor

    if test:
        test_str = '_test'
    else:
        test_str = ''

    if last:
        last_str = ' ORDER BY Humidite_id DESC LIMIT 1'
    else:
        last_str = ''
    
    if capteur < 1:
        query = "SELECT * FROM Humidite" + test_str + last_str + ';'
    else:
        query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'

    if last:
        return getDB().runSelectOneQuery(query)
    else:
        return getDB().runSelectQuery(query)
def getEtatSystemeFromDB(test = True, systeme = "", last = False):
    if test:
        test_str = '_test'
    else:
        test_str = ''

    if last:
        last_str = ' ORDER BY Systeme_id DESC LIMIT 1'
    else:
        last_str = ''
    
    if not isSysteme(systeme):
        query = "SELECT * FROM Systemes" + test_str + last_str + ';'
    else:
        query = "SELECT * FROM Systemes" + test_str + " WHERE Systeme = " + "'"+str(systeme)+"'" + last_str + ';'

    if last:
        return getDB().runSelectOneQuery(query)
    else:
        return getDB().runSelectQuery(query)

def getSaturationFromDB(test = True, capteur=0, last = False):
    # capteur < 1  -> Get all saturation from all sensors
    # last = false -> Get all saturation from the sensor
    # last = true  -> Get the last saturation from the sensor

    if test:
        test_str = '_test'
    else:
        test_str = ''

    if last:
        last_str = ' ORDER BY Saturation_id DESC LIMIT 1'
    else:
        last_str = ''

    if capteur < 1:
        query = "SELECT * FROM Saturation" + test_str + last_str + ';'
    else:
        query = "SELECT * FROM Saturation" + test_str + " WHERE Capteur = " + str(capteur) + last_str + ';'

    if last:
        return getDB().runSelectOneQuery(query)
    else:
        return getDB().runSelectQuery(query)

def getTemperatureHumiditeFromDB(capteur, test = True):
    # Get the temperature and the humidty of a sensor from the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "SELECT Temperature" + test_str + ".Temperature_id, Temperature" + test_str + ".Capteur, Temperature" + test_str + ".Temp, Humidite" + test_str + ".Hum, Temperature" + test_str + ".Date_capteur FROM Temperature" + test_str + ", Humidite" + test_str + " WHERE Temperature" + test_str + ".Date_capteur = Humidite" + test_str + ".Date_capteur AND Temperature" + test_str + ".Capteur = " + str(capteur) + " AND Humidite" + test_str + ".Capteur = " + str(capteur) + ";"
    return getDB().runSelectQuery(query)

def getTemperatureSenseurFromDB(capteur_id, test = True):
    # Get all the temperature of a sensor from the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "SELECT * FROM Temperature" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putTemperatureToDB(capteur, temperature, date, test = True):
    # Put the temperature of a sensor in the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "INSERT INTO Temperature" + test_str + " (Capteur, Temp, Date_capteur) VALUES (" + capteur + ", " + temperature + ", '" +  date + "');"
    getDB().runUpdateQuery(query)

def putEtatSystemToDB(systeme, etat, date, test = True):
    # Put the state of a system in the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "INSERT INTO Systemes" + test_str + " (Systeme, Etat, Date) VALUES ('" + str(systeme) + "', " + etat + ", '" +  date + "');"
    getDB().runUpdateQuery(query)

def getSaturationSenseurFromDB(capteur_id, test = True):
    # Get all the saturation of a sensor from the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    
    query = "SELECT * FROM Saturation" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putSaturationToDB(capteur, mesure, date, test = True):
    # Put the saturation of a sensor in the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "INSERT INTO Saturation" + test_str + " (Capteur, Mesure, Date_capteur) VALUES (" + capteur + ", " + mesure + ", '" + date + "');"
    getDB().runUpdateQuery(query)

def getHumiditeSenseurFromDB(capteur_id, test = True):
    # Get all the humidity of a sensor from the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''

    query = "SELECT * FROM Humidite" + test_str + " WHERE Capteur = " + capteur_id + ";"
    return getDB().runSelectQuery(query)

def putHumiditeToDB(capteur, humidite, date, test = True):
    # Put humudity of a sensor in the DB
    if test:
        test_str = '_test'
    else:
        test_str = ''
    
    query = "INSERT INTO Humidite" + test_str + " (Capteur, Hum, Date_capteur) VALUES (" + capteur + ", " + humidite + ", '" + date + "');"
    getDB().runUpdateQuery(query)

def representsInt(s):
    # Check if 's' can be turn in a Int
    try:
        int(s)
        return True
    except ValueError:
        return False

def representsFloat(s):
    # Check if 's' can be turn in a Float
    try:
        float(s)
        return True
    except ValueError:
        return False
def representsBool(s):
    # Check if 's' can be turn in a bool
    try:
        bool(s)
        return True
    except ValueError:
        return False

def isSysteme(s):
    match s:
        case "fan1":
            return True
        case "fan2":
            return True
        case "porte":
            return True
        case "pompe":
            return True
        case "valve1":
            return True
        case "valve2":
            return True
        case "valve3":
            return True
        case _:
            return False

def hello():
	return 'Bienvenue! Version ' + VERSION

app = Flask('API pour la serre')

# --------------------------------------------------------------------------------------------------------------
#                                     Definitions of routes

@app.route('/')
def welcome():
	return hello()

@app.route('/accueil')
def accueil():
    return render_template("Page_Accueil.html", active_page="accueil")

@app.route("/realtime")
def realtime():
    return render_template("Page_Real_Time.html", active_page="realtime")

@app.route("/graph")
def graph():
    return render_template("Page_Graphiques.html", active_page="graph")

@app.route("/controle")
def controle():
    return render_template("Page_Controle.html", active_page="controle")


# TEST
@app.route('/initialize')
def route_initialize():
    reponse = dbInitialize(True)
    return jsonify({'Reinitialisation des tables tests.  Tables recreees ': reponse})

@app.route('/initialize_global')
def route_initialize_global():
    reponse = dbInitialize(False)
    return jsonify({'Reinitialisation des tables.  Tables recreees ': reponse})


@app.route('/temperatures', methods=['POST'])
def route_temperatures_post():
    capteur_id = request.form.get('capteur_id')
    temperature = request.form.get('temp')
    if (not representsInt(capteur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne representation"})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(capteur_id, temperature, now.strftime('%Y-%m-%d %H:%M:%S'), False)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse


@app.route('/temperatures', methods=['GET'])
def route_temperatures_get():
    reponse_records = getTemperatureFromDB(False, 0, False)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Temperature': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des temperatures': json_return})


@app.route('/humidites', methods=['POST'])
def route_humidites_post():
    capteur_id = request.form.get('capteur_id')
    humidite = request.form.get('hum')
    if (not representsInt(capteur_id)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': "capteur_id ou hum n'ont pas la bonne representation."})
    else:
        now = datetime.datetime.now()
        putHumiditeToDB(capteur_id, humidite, now.strftime('%Y-%m-%d %H:%M:%S'), False)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse


@app.route('/humidites', methods=['GET'])
def route_humidites_get():
    reponse_records = getHumiditeFromDB(False, 0, False)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Humidite': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des humidites': json_return})

# Saturation
@app.route('/saturations', methods=['POST'])
def route_saturations_post():
    capteur_id = request.form.get('capteur_id')
    mesure = request.form.get('sat')
    if (not representsInt(capteur_id)) or (not representsFloat(mesure)):
        reponse = jsonify({'Erreur': "capteur_id ou sat n'ont pas la bonne representation."})
    else:
        now = datetime.datetime.now()
        putSaturationToDB(capteur_id, mesure, now.strftime('%Y-%m-%d %H:%M:%S'), False)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['sat'] = mesure
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
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

# Etats Systemes
@app.route('/etatsSysteme', methods=['POST'])
def route_etatSysteme_post():
    systeme_id= request.form.get('systeme_id')
    etat = request.form.get('etat')
    if (not isSysteme(systeme_id)) or (not representsInt(etat)):
        reponse = jsonify({'Erreur': "systeme_id ou etat n'ont pas la bonne representation."})
    else:
        now = datetime.datetime.now()
        putEtatSystemToDB(systeme_id, etat, now.strftime('%Y-%m-%d %H:%M:%S'), False)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = systeme_id
        valeurs_enr['sat'] = etat
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse

# Etats Systemes
@app.route('/etatsSysteme', methods=['GET'])
def route_etatsSysteme_get():
    reponse_records = getEtatSystemeFromDB(False)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Systeme ID': row[1],
                               'Etat': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des etats du systeme': json_return})

@app.route('/moniteur', methods=['GET'])
def route_capteur1_capteur2_capteur3_get():
    # Obtenir les dernières valeurs des capteurs...
    reponse_temp_capteur1 = getTemperatureFromDB(False, 1, True)
    reponse_temp_capteur2 = getTemperatureFromDB(False, 2, True)
    reponse_temp_capteur3 = getTemperatureFromDB(False, 3, True)
    reponse_hum_capteur1 = getHumiditeFromDB(False, 1, True)
    reponse_hum_capteur2 = getHumiditeFromDB(False, 2, True)
    #reponse_hum_capteur3 = getHumiditeFromDB(False, 3, True)
    json_return = dict()
    json_return[1] = {  'Capteur ID': reponse_temp_capteur1[1],
                        'Temperature': reponse_temp_capteur1[2],
                        'Humidite': reponse_hum_capteur1[2],
                        'Date': reponse_temp_capteur1[3] }

    json_return[2] = {  'Capteur ID': reponse_temp_capteur2[1],
                        'Temperature': reponse_temp_capteur2[2],
                        'Humidite': reponse_hum_capteur2[2],
                        'Date': reponse_temp_capteur2[3] }

    json_return[3] = {  'Capteur ID': reponse_temp_capteur3[1],
                        'Temperature': reponse_temp_capteur3[2],
     #                   'Humidite': reponse_hum_capteur3[2],
                        'Date': reponse_temp_capteur3[3] }
    return jsonify({'Temperatures et humidites des capteurs 1, 2 et 3': json_return})

@app.route('/historique24h', methods=['GET'])
def route_hitorique24_get():
    json_return = {}

    # Capteur 1 - Température ET Humidité
    reponse_temp = getHistorique24HTempFromDB(False, 1)
    reponse_hum  = getHistorique24HHumFromDB(False, 1)

    historique_capteur1 = []
    for temp_row, hum_row in zip(reponse_temp, reponse_hum):
        historique_capteur1.append({
            'Capteur ID':  temp_row[1],
            'Temperature': temp_row[2],
            'Humidite':    hum_row[2],
            'Date':        temp_row[3]})
    json_return['Capteur 1'] = historique_capteur1

    # Capteurs 2 et 3 - Température seulement
    for capteur_id in [2, 3]:
        reponse_temp = getHistorique24HTempFromDB(False, capteur_id)

        historique = []
        for temp_row in reponse_temp:
            historique.append({
                'Capteur ID':  temp_row[1],
                'Temperature': temp_row[2],
                'Date':        temp_row[3]})
        json_return[f'Capteur {capteur_id}'] = historique

    # Systemes
    for systeme_id in ["fan1","fan2", "pompe", "porte", "valve1", "valve2", "valve3"]:
        reponse_sys = getHistorique24HSystemesFromDB(False, systeme_id)

        historique = []
        for sys_row in reponse_sys:
            historique.append({
                'Systeme ID': sys_row[1],
                'Etat': sys_row[2],
                'Date': sys_row[3]})
        json_return[f'Systeme {systeme_id}'] = historique

    return jsonify({'Historique des capteurs 1, 2 et 3': json_return})

def route_capteur_hum_temp_post(capteur_id, test = True):
    temperature = request.form.get('temp')
    humidite = request.form.get('hum')
    if (not representsFloat(temperature)) or (not representsFloat(humidite)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne representation."})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(str(capteur_id), temperature, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        putHumiditeToDB(str(capteur_id), humidite, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = str(capteur_id)
        valeurs_enr['temp'] = temperature
        valeurs_enr['hum'] = humidite
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse

def route_capteur_gen_sat_post(capteur_id, test = True):
    mesure = request.form.get('sat')
    if not representsFloat(mesure):
        reponse = jsonify({'Erreur': "sat n'a pas la bonne representation."})
    else:
        now = datetime.datetime.now()
        putSaturationToDB(str(capteur_id), mesure, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = str(capteur_id)
        valeurs_enr['sat'] = mesure
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse

def route_capteur_hum_temp_get(capteur_id, test = True):
    reponse_records = getTemperatureHumiditeFromDB(capteur_id, test)
    json_return = dict()
    for row in reponse_records:
        json_return[row[0]] = { 'Capteur ID': row[1],
                               'Temperature': row[2],
                               'Humidite': row[3],
                               'Date': row[4] }
    return jsonify({'Liste des temperatures et humidites': json_return})


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
                               'Temperature': row[2],
                               'Date': row[3] }
    return jsonify({'Liste des temperatures': json_return})

def route_capteur_gen_temp_post(capteur_id, test = True):
    temperature = request.form.get('temp')
    if (not representsInt(capteur_id)) or (not representsFloat(temperature)):
        reponse = jsonify({'Erreur': "capteur_id ou temp n'ont pas la bonne representation"})
    else:
        now = datetime.datetime.now()
        putTemperatureToDB(str(capteur_id), temperature, now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['capteur_id'] = capteur_id
        valeurs_enr['temp'] = temperature
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse

def route_systeme_gen_etat_post(systeme_id, test = True):
    etat = request.form.get('etat')
    if (not isSysteme(systeme_id)) or (not representsInt(etat)):
        reponse = jsonify({'Erreur': "systeme_id ou etat n'ont pas la bonne representation"})
    else:
        now = datetime.datetime.now()
        putEtatSystemToDB(str(systeme_id), str(etat), now.strftime('%Y-%m-%d %H:%M:%S'), test)
        valeurs_enr = dict()
        valeurs_enr['systeme_id'] = systeme_id
        valeurs_enr['etat'] = etat
        reponse = jsonify({'Valeurs sauvegardees': valeurs_enr})
    return reponse

def route_systeme_gen_etat_get(systeme_id, test = True):
    reponse_records = getEtatSystemeFromDB(test, systeme_id, True)
    
    json_return = dict()

    json_return = { 'Systeme ID': reponse_records[1],
                    'Etat': reponse_records[2],
                    'Date': reponse_records[3] }
    return jsonify(json_return)

# ------------- Routes des états des systèmes -------------
@app.route('/fan1', methods=['POST'])
def route_fan1_post():
    return route_systeme_gen_etat_post("fan1", False)

@app.route('/fan1', methods=['GET'])
def route_fan1_get():
    return route_systeme_gen_etat_get("fan1", False)

@app.route('/fan2', methods=['POST'])
def route_fan2_post():
    return route_systeme_gen_etat_post("fan2", False)

@app.route('/fan2', methods=['GET'])
def route_fan2_get():
    return route_systeme_gen_etat_get("fan2", False)

@app.route('/porte', methods=['POST'])
def route_porte_post():
    return route_systeme_gen_etat_post("porte", False)

@app.route('/porte', methods=['GET'])
def route_porte_get():
    return route_systeme_gen_etat_get("porte", False)

@app.route('/pompe', methods=['POST'])
def route_pompe_post():
    return route_systeme_gen_etat_post("pompe", False)

@app.route('/pompe', methods=['GET'])
def route_pompe_get():
    return route_systeme_gen_etat_get("pompe", False)

@app.route('/valve1', methods=['POST'])
def route_valve1_post():
    return route_systeme_gen_etat_post("valve1", False)

@app.route('/valve1', methods=['GET'])
def route_valve1_get():
    return route_systeme_gen_etat_get("valve1", False)

@app.route('/valve2', methods=['POST'])
def route_valve2_post():
    return route_systeme_gen_etat_post("valve2", False)

@app.route('/valve2', methods=['GET'])
def route_valve2_get():
    return route_systeme_gen_etat_get("valve2", False)

@app.route('/valve3', methods=['POST'])
def route_valve3_post():
    return route_systeme_gen_etat_post("valve3", False)

@app.route('/valve3', methods=['GET'])
def route_valve3_get():
    return route_systeme_gen_etat_get("valve3", False)

# ------------- Routes des capteurs -------------

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
    return route_capteur_gen_temp_post(3, False)
    # return route_capteur_hum_temp_post(3, False)

@app.route('/capteur3', methods=['GET'])
def route_capteur3_get():
    return route_capteur_gen_temp_get(3, False)
    # return route_capteur_hum_temp_get(3, False)

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

