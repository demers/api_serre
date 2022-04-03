#/bin/bash

echo "BD est vidé..."
sleep 1
http localhost:8080/initialize
sleep 1
echo "La BD est vide..."
http -f localhost:8080/temperatures
http -f localhost:8080/humidites

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
http -f localhost:8080/capteur3 temp=50.2 hum=80.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur3

sleep 1
echo "La température et l'humidité du capteur 4 est à 60.2 et 70.0..."
http -f localhost:8080/capteur4 temp=60.2 hum=70.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur4

sleep 1
echo "La température et l'humidité du capteur 5 est à 70.2 et 60.0..."
http -f localhost:8080/capteur5 temp=70.2 hum=60.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur5

sleep 1
echo "La température et l'humidité du capteur 6 est à 80.2 et 50.0..."
http -f localhost:8080/capteur6 temp=80.2 hum=50.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur6

sleep 1
echo "La température et l'humidité du capteur 7 est à 90.2 et 40.0..."
http -f localhost:8080/capteur7 temp=90.2 hum=40.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur7

sleep 1
echo "La température et l'humidité du capteur 8 est à 100.2 et 30.0..."
http -f localhost:8080/capteur8 temp=100.2 hum=30.0
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/capteur8

