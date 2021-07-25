#!/bin/bash

# Voir tutoriel: https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04-fr

sudo apt install mysql-server
sudo mysql_secure_installation
sudo mysql
# CREATE USER 'serre'@'localhost' IDENTIFIED BY 'password';
# Changer "password" par le bon mot de passe.
# GRANT ALL PRIVILEGES ON *.* TO 'serre'@'localhost' WITH GRANT OPTION;
sudo apt install phpmyadmin php-mbstring php-zip php-gd php-json php-curl
sudo apt-get -y install python3-pip
pip install mysql-connector-python
pip install flask
