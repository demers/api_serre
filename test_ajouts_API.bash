echo "Ajout de l'État True à fan1"
echo Requête: http -f localhost:8080/fan1 etat=1
http -f localhost:8080/fan1 etat=1

sleep 1

echo "Ajout de l'État True à fan2"
echo Requête: http -f localhost:8080/fan2 etat=1
http -f localhost:8080/fan2 etat=1

sleep 1

echo "Ajout de l'État True à porte"
echo Requête: http -f localhost:8080/porte etat=1
http -f localhost:8080/porte etat=1

sleep 1

echo "Ajout de l'État True à pompe"
echo Requête: http -f localhost:8080/pompe etat=1
http -f localhost:8080/pompe etat=1

sleep 1

echo "Ajout de l'État True à valve1"
echo Requête: http -f localhost:8080/valve1 etat=1
http -f localhost:8080/valve1 etat=1

sleep 1

echo "Ajout de l'État True à valve2"
echo Requête: http -f localhost:8080/valve2 etat=1
http -f localhost:8080/valve2 etat=1

sleep 1

echo "Ajout de l'État True à valve3"
echo Requête: http -f localhost:8080/valve3 etat=1
http -f localhost:8080/valve3 etat=1

sleep 1

echo "Les valeurs sont bien dans la BD Mysql..."
echo Requête: http -f localhost:8080/etatsSysteme
http -f localhost:8080/etatsSysteme

sleep 1

echo "Recherche etats fan1"
echo Requête: http -f localhost:8080/fan1
http -f localhost:8080/fan1