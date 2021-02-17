#!/bin/zsh
# the script shall assume you have python installed in your computer and only run
check_version=3.0
python_version="$(python -V 2>&1)"
echo "$python_version"

# checks what if version is greater then 3, if so it execute all the comamnds below with one command
if [ -n "$python_version" -a -n "$check_version" ]
then
  pip install pip
  pip intsall -r requirement.txt
  chmod +x ./.runprocess.py #giving process execution permission
  pyhton3 ./.runprocess.py
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  python -m webbrowser http://127.0.0.1:8000/
else
  echo "please update your python version"
fi