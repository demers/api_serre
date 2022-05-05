#!/bin/bash

#cd ~/api_serre
rm -f nohup.out.bak
mv nohup.out nohup.bak
killall python3
nohup python3 api.py &