#!/usr/bin/env bash

#let database to start all scripts
echo "WAITING 30 seconds to start database container"
sleep 30

python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('demo', 'demo@demo.com', 'demo')" | ./manage.py shell
python manage.py runserver 0.0.0.0:8000
