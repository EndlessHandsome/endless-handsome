#!/bin/bash
set -e
DJANGODIR=/home/endless-handsome
#DJANGO_SETTINGS_MODULE=app.settings.prod

LOGFILE=/var/log/gunicorn/guni-app.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2

# user/group to run as
#USER=ubuntu
#GROUP=ubuntu

cd /home/endless-handsome
source /home/venv/bin/activate

#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn endlesshandsome.wsgi:application -b 45.78.51.172:80 -w $NUM_WORKERS \
  #--user=$USER --group=$GROUP 
  --log-level=debug \
  --log-file=$LOGFILE -b 2>>$LOGFILE
