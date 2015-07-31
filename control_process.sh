#!/bin/bash

PID_FILE="slack-invite.pid"

PRODUCT_NAME="slack-invite"
WSGI_CONF="invite"
APP_OBJECT="app"
PORT=5000

core() {
    gunicorn ${WSGI_CONF}:${APP_OBJECT} \
        --bind 0.0.0.0:${PORT} \
        --pid ${PID_FILE} \
        --log-level INFO \
        --access-logfile=./logs/access.log \
        --error-logfile=./logs/error.log \
        --daemon
}


start() {
    echo "Starting..."
    core
}


stop() {
    echo "Stopping"
    kill -SIGTERM `cat $PID_FILE`
}


restart () {
   stop
   start
}


status() {
    ps aux|grep python|grep gunicorn
}

case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
esac
