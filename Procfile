release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py collectstatic --noinput

web: gunicorn Todo_drf.wsgi