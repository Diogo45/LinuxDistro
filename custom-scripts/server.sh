#!/bin/sh
case "$1" in
  	start)
  		python /usr/bin/simple_http_server.py&
  		;;
  	stop)
  		exit 1
  		;;
  	*)
  		exit 1
  		;;
  esac
  
exit 0
