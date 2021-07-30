#!/bin/bash

cd ~/api_serre
killall python3
nohup python3 api.py &