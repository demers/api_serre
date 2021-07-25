# -*- coding: utf-8 -*-


import mysql.connector
from flask import *

app = Flask('API pour la serre')

def hello():
	return 'Bienvenue!'

@app.route('/')
def welcome():
	return hello()

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port = 8080)

