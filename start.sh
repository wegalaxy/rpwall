#!/bin/bash

cd ~/rpwall
git pull
source ./venv/bin/activate
python3 main.py
