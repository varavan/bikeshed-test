#!/usr/bin/env bash

echo "WAITING 30 seconds to start database container"
sleep 30

python manage.py test