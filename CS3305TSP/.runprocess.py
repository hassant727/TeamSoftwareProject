from subprocess import Popen
from signal import SIGINT

# start the process
p = Popen(['python', 'manage.py', 'runserver'])

# now stop the process
p.send_signal(SIGINT)
p.wait()