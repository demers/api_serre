#/bin/bash

echo "BD est vidé..."
sleep 1
http localhost:8080/initialize
sleep 1
echo "La BD est vide..."
http -f localhost:8080/temperatures
http -f localhost:8080/humidites
http -f localhost:8080/saturations

sleep 1
echo "La température du capteur 45 est à 32.2..."
http -f localhost:8080/temperatures capteur_id=45 temp=32.2
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/temperatures

sleep 1
echo "L'humidité du capteur 45 est à 50.2..."
http -f localhost:8080/humidites capteur_id=45 hum=50.2
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/humidites

sleep 1
echo "La température et l'humidité du capteur 1 est à 30.2 et 100.0..."
http -f localhost:8080/capteur1 temp=30.2 hum=100.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur1

sleep 1
echo "La température et l'humidité du capteur 2 est à 40.2 et 90.0..."
http -f localhost:8080/capteur2 temp=40.2 hum=90.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur2

sleep 1
echo "La température et l'humidité du capteur 3 est à 50.2 et 80.0..."
http -f localhost:8080/saturations capteur=3 sat=50.2
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/saturations

sleep 1
echo "La température et l'humidité du capteur 4 est à 60.2 et 70.0..."
http -f localhost:8080/saturations capteur=4 sat=60.2
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/saturations

