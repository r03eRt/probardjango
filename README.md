# probardjango
aplicacion django pruebas


sudo pip install virtualenv o sudo easy_install virtualenv
virtualenv .
. bin/activate
pip install Django==1.9
./bin/django-admin.py start project probardjango
cd probardjango
./manage.py startapp boletin
./manage.py makemigrations
./manage.py migrate
./manage.py runserver
