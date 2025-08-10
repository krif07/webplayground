python -m venv venv

venv\Scripts\activate

python manage.py createsuperuser

python manage.py makemigrations
python manage.py makemigrations pages

python manage.py migrate
python manage.py migrate pages