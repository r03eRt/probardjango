# probardjango
aplicacion django pruebas


sudo pip install virtualenv o sudo easy_install virtualenv
virtualenv .
. bin/activate
pip install Django==1.9
./bin/django-admin.py start project probardjango
cd probardjango
./manage.py startapp boletin (añadir a apps en settings.py)
# Añado moldelo
./manage.py makemigrations
./manage.py migrate
# Ejecutar
./manage.py runserver

# Para añadir url se va a views.py,se registra la vista con el contexto, urls.py añadimos la ruta donde esta ese views
# vamos a settings.py y definimos donde están los templates 'DIRS': [os.path.join(BASE_DIR, "templates")],

