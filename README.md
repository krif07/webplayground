python -m venv venv

retroceder con cd .. para ir hasta la carpeta Django que contiene venv
venv\Scripts\activate
.\venv\Scripts\activate

python manage.py createsuperuser

python manage.py makemigrations
python manage.py makemigrations pages

python manage.py migrate
python manage.py migrate pages