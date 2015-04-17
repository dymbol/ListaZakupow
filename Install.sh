python manage.py migrate
echo "Creating superuser:"
python manage.py createsuperuser
python manage.py makemigrations manager
python manage.py migrate
