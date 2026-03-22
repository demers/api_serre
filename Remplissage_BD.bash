#/bin/bash

echo "Vidage des tables"
sleep 1
http localhost:8080/initialize_global
sleep 1
echo "Vérification de l'initialisation..."
http -f localhost:8080/temperatures
http -f localhost:8080/humidites
http -f localhost:8080/saturations
http -f localhost:8080/etatsSysteme

sleep 1
echo "Remplissage de 96 données (24x4= 96 données aux 15 min)"
for ((i=0; i<96; i++)); do
    http -f localhost:8080/capteur1 temp=$i hum=$((96-i))
    http -f localhost:8080/capteur2 temp=$((i*2)) hum=$((96-i))
    http -f localhost:8080/capteur3 temp=$((i*3))

    http -f localhost:8080/fan1 etat=$i

    if ((i%2==0)); then
        http -f localhost:8080/porte etat=1
    else
        http -f localhost:8080/porte etat=0
    fi

    sleep 0.1
done
sleep 1

echo "Lecture des données"
http -f localhost:8080/capteur1