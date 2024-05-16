release: python manage.py collectstatic --noinput
release: python manage.py migrate --no-input
web: gunicorn fancybear.wsgi:application --log-file -