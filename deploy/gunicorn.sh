#!/bin/bash

NAME="Trabajos_sccot"
DJANGODIR=$(dirname $(cd `dirname $0` && pwd))
SOCKFILE=/tmp/gunicorn-trabajos.sock
LOGDIR=${DJANGODIR}/logs/gunicorn.log
USER=wilmer
GROUP=wilmer
NUM_WORKERS=5
DJANGO_WSGI_MODULE=Trabajos.wsgi

rm -frv $SOCKFILE

echo $DJANGODIR

cd $DJANGODIR

exec ${DJANGODIR}/env/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=$LOGDIR
