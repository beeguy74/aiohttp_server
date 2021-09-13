#!/bin/bash
python3 -m venv ENV
source ENV/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py