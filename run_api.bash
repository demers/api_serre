#!/bin/bash

cd ~/serre/api_serre || exit 1

# Activer le venv
source venv/bin/activate

# Gestion des logs nohup
rm -f nohup.out.bak
[ -f nohup.out ] && mv nohup.out nohup.bak

# ⚠️ Éviter de tuer TOUS les python3 du système
# killall python3   ❌ MAUVAIS

# Option plus sûre : tuer seulement ton API
pkill -f "api.py"

# Lancer l'API avec le python du venv
nohup python api.py &

#cd ~/api_serre
#rm -f nohup.out.bak
#mv nohup.out nohup.bak
#killall python3

#nohup python3 api.py &