#!/usr/bin/env bash

#let database to start all scripts
echo "WAITING 30 seconds to start database container"
sleep 30

python manage.py test
python manage.py migrate
python manage.py populate_db
python manage.py runserver 0.0.0.0:8000
