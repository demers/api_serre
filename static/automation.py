import requests
from datetime import datetime, time
import time as dtime

from IP_SYS import *


INTERVAL = 10

TEST = True
params = dict(
    tempTresBasse = 17.0,
    tempBasse = 20.0,
    tempMid = 23.0,
    tempHaute = 25.0,
    heureOuverture = time(8,0,0),
    heureFermeture = time(18,0,0)
)

etatSerre = dict(
    tempCapteur1 = 0.0,
    tempCapteur2 = 0.0,
    tempCapteur3 = 0.0,
    humCapteur1 = 0.0,
    heure = time(0,0,0),
    etatFan1 = 0.0,
    etatPorte = False,
)

def getSensorData():
    try:
        r = requests.get(f"{API_BASE}/moniteur", timeout=10)
        r.raise_for_status()
        data = r.json()

        capteurs = data["Temperatures et humidites des capteurs 1, 2 et 3"]
        etatSerre["tempCapteur1"] = capteurs["1"]["Temperature"]
        etatSerre["humCapteur1"] = capteurs["1"]["Humidite"]
        etatSerre["tempCapteur2"] = capteurs["2"]["Temperature"]
        etatSerre["tempCapteur3"] = capteurs["3"]["Temperature"]
        
        date_capteur1 = capteurs["1"]["Date"]
        date = datetime.strptime(date_capteur1, "%a, %d %b %Y %H:%M:%S GMT")
        etatSerre["heure"] = date.time()

        return False
    
    except requests.RequestException as e:
        print(f"[ERREUR] Lecture /moniteur : {e}")
        return True
    
def getEtatSysteme():
    try:
        r = requests.get(f"{API_BASE}/fan1", timeout=10)
        r.raise_for_status()
        etatFan1 = r.json()

        r = requests.get(f"{API_BASE}/porte", timeout=10)
        r.raise_for_status()
        etatPorte = r.json()

        etatSerre["etatFan1"] = etatFan1["Etat"]
        etatSerre["etatPorte"] = etatPorte["Etat"]

        return False
    
    except requests.RequestException as e:
        print(f"[ERREUR] Lecture /fan1 ou /porte : {e}")
        return True
    
def algoDecisions():
    
    if (etatSerre["heure"] > params["heureOuverture"]) and (etatSerre["heure"] < params["heureFermeture"]):
        # Gestion de la porte
        if (etatSerre["tempCapteur3"] >= params["tempTresBasse"]) and (etatSerre["etatPorte"] == False):
            print("Ouverture de la porte")
            if not TEST:
                requests.post(ROUTE_CTRL_PORTE+"ON")

        elif (etatSerre["tempCapteur3"] < params["tempTresBasse"]) and (etatSerre["etatPorte"] == True):
            print("Fermeture de la porte")
            if not TEST:
                requests.post(ROUTE_CTRL_PORTE+"OFF")

        # Gestion du fan
        if etatSerre["tempCapteur3"]<params["tempBasse"]:
            print("Fan a 0%")
            if not TEST:
                requests.post(ROUTE_CTRL_FAN1+"0")
        
        elif (etatSerre["tempCapteur3"] >= params["tempBasse"]) and (etatSerre["tempCapteur3"] < params["tempMid"]):
            print("Fan a 50%")
            if not TEST:
                requests.post(ROUTE_CTRL_FAN1+"50")

        elif (etatSerre["tempCapteur3"] >= params["tempMid"]) and (etatSerre["tempCapteur3"] < params["tempHaute"]):
            # Le fan doit déjà être à 50% pour être augmenter
            if etatSerre["etatFan1"] == 0:
                print("Fan a 50%")
                if not TEST:
                    requests.post(ROUTE_CTRL_FAN1+"50")
            else:
                print("Fan à 75%")
                if not TEST:
                    requests.post(ROUTE_CTRL_FAN1+"75")
        
        elif etatSerre["tempCapteur3"] >= params["tempHaute"]:
            # Le fan doit déjà être à 50% pour être augmenter
            if etatSerre["etatFan1"] == 0:
                print("Fan a 50%")
                if not TEST:
                    requests.post(ROUTE_CTRL_FAN1+"50")
            else:
                print("Fan à 100%")
                if not TEST:
                    requests.post(ROUTE_CTRL_FAN1+"100")
        else:
            print("Erreur logique")
            for key in etatSerre:
                print(f"{key} : {etatSerre[key]}")

    else :
        print("Fermeture porte et fan")
    

def main():
    print(f"[START] Automation démarrée — cycle de {INTERVAL}s")
    while True:
        try:
            print(f"[{datetime.now()}] Lecture des capteurs...")
            if getSensorData():
                print("Erreur : getSensorData()") 
                continue

            if getEtatSysteme():
                print("Erreur : getEtatSysteme()")
                continue
            
            algoDecisions()

        except Exception as e:
            print(f"[ERREUR CRITIQUE] {e}")
        dtime.sleep(INTERVAL)

if __name__ == "__main__":
    main()