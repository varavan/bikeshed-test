#!/usr/bin/env bash

python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('demo', 'demo@demo.com', 'demo')" | ./manage.py shell
python manage.py runserver 0.0.0.0:8000
