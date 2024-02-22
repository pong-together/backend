#!/bin/sh
cd /code
chmod +x manage.py
python3 manage.py loaddata dummy_data.json
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
