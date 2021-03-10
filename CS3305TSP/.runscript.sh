#!/bin/zsh
#!/bin/bash
#!/bin/sh

: ' the script shall assume you have python installed in your computer and os is either windows or unix
  if you we wish to try it on other version we can just expand the if statement
'


os_=""

: ' checking what type of OS'
case "$OSTYPE" in
  solaris*) os_="SOLARIS" ;;
  darwin*)  os_="OSX" ;;
  linux*)   os_="LINUX" ;;
  bsd*)     os_="BSD" ;;
  msys*)    os_="WINDOWS" ;;
  *)        os_="unknown: $OSTYPE" ;;
esac
echo $os_
: ' defining function to to execute the commands '
commands () {
  check_version=3.0
  python_version="$(python -V 2>&1)"
  echo "$python_version"

  commandsFunction () {
    : ' install the dependencies needed for the application to run'
      pip install pip
      pip3 install -r requirement.txt

      : ' gives permission for the execution file and runs it '
      chmod +x ./.runprocess.py #giving process execution permission
      python3 ./.runprocess.py

      : ' this list all process running manage.py and the following commands kills them '

      ps ax | grep manage.py
      pkill -f manage.py

      : ' makes migrations if need be and runs the server and finally lunches the app on web '
      python manage.py makemigrations dashboard
      python manage.py makemigrations userpages
      python manage.py makemigrations webpages

      python manage.py migrate
      python manage.py runserver

      python -m webbrowser http://127.0.0.1:8000/


  }

  : ' checks if version is greater then 3, if so it execute all the commands below with one command '
  : ' shellcheck disable=SC1073 '
  if [ -n "$python_version" -a -n "$check_version" ]
    then
      commandsFunction
  else
      commandsFunction
  fi

}


: ' checks what version os it is and execute based on os '

# shellcheck disable=SC2170
if [[ $os_ == "OSX" ]] || [[ $os_ == $"LINUX" ]]
  then
    #!/bin/zsh || #!/bin/sh
    commands
    : ' the commands calls the function commands () which then execute all the code within it or u can just change the
        file extension --> im not using windows but i think itll be something like --> ren ".runscript.sh" ".runscript.bat"'
elif [[ $os_ == $"WINDOWS" ]]
  then
    #!/bin/bash
    commands

else
  echo "add condition to check any other os version"
fi




