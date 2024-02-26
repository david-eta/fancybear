release: python manage.py collectstatic --noinput
release: ./manage.py migrate --no-input
web: gunicorn fancybear.wsgi:application --log-file -
