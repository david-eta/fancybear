release: python manage.py collectstatic --noinput
web: gunicorn fancybear.wsgi:application --log-file -
