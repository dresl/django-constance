#!/bin/bash

virtualenv -p /usr/bin/python2.7 leonardo_venv
cd leonardo_venv
. $PWD/bin/activate

pip install django-leonardo
pip install django-leonardo[themes]
pip install django-leonardo[store]

django-admin startproject --template=https://github.com/django-leonardo/site-template/archive/master.zip myproject

export PYTHONPATH=$PWD/myproject
cd myproject

python manage.py makemigrations --noinput
python manage.py migrate --noinput
python manage.py sync_all

echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'mail@leonardo.cz', 'admin')" | python manage.py shell

python manage.py runserver 0.0.0.0:80
