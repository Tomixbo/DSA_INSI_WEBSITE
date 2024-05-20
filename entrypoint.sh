#!/bin/sh

#python manage.py migrate --no-input
python manage.py collectstatic --no-input
#python manage.py loaddata data.json

gunicorn local_contest.wsgi:application --bind 0.0.0.0:8000