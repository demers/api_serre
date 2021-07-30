#/bin/bash

echo "BD est vidé..."
sleep 1
http localhost:8080/initialize
sleep 1
echo "La BD est vide..."
http -f localhost:8080/temperatures
sleep 1
echo "La température du senseur 45 est à 32.2..."
http -f localhost:8080/temperatures senseur_id=45 temp=32.2
sleep 1
echo "Les valeurs sont bien dans la BD Mysql..."
http -f localhost:8080/temperatures