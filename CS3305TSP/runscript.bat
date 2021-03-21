#!/bin/bash



    : ' install the dependencies needed for the application to run'
      pip install pip
      pip3 install -r requirement.txt
      pip install -r requirement.txt
      pip intall requirement.txt

      : ' this list all process running manage.py and the following commands kills them '

      ps ax | grep manage.py
      pkill -f manage.py

      : ' makes migrations if need be and runs the server and finally lunches the app on web '
      python manage.py makemigrations dashboard
      python manage.py makemigrations userpages
      python manage.py makemigrations webpages

      python3 manage.py makemigrations dashboard
      python3 manage.py makemigrations userpages
      python3 manage.py makemigrations webpages

      python manage.py migrate
      python manage.py runserver

      python -m webbrowser http://127.0.0.1:8000/


