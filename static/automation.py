import time
import requests
from datetime import datetime

API_BASE = "http://localhost"
INTERVAL = 300

def get_sensor_data():
    try:
        r = requests.get(f"{API_BASE}/moniteur", timeout=10)
        r.raise_for_status()
        data = r.json()

        capteurs = data["Temperatures et humidites des capteurs 1, 2 et 3"]
        return capteurs
    except requests.RequestException as e:
        print(f"[ERREUR] Lecture /moniteur : {e}")
        return None
    
def algo_decisions(capteurs):
    temp_capteur1 = capteurs["1"].Temperature
    hum_capteur1 = capteurs["1"].Humidite
    temp_capteur2 = capteurs["2"].Temperature
    temp_capteur3 = capteurs["3"].Temperature
    date_capteur1 = capteurs["1"].Date

    date = datetime.strptime(date_capteur1, "%a, %d %b %Y %H:%M:%S GMT")
    heure = date.time()

    

def main():
    print(f"[START] Automation démarrée — cycle de {INTERVAL}s")
    while True:
        try:
            print(f"[{datetime.now()}] Lecture des capteurs...")
            capteurs = get_sensor_data()
            prendre_decisions(capteurs)
        except Exception as e:
            print(f"[ERREUR CRITIQUE] {e}")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()