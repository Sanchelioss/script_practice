#!/bin/bash

data=date +"%b %d"
#show log dir
ls -la /var/log
#checking file availability
check=/var/log/syslog
if [ -f $check ];
  then
	echo "################### last 10 lines"
	tail $check
	echo "################### first 10 lines"
	head $check
	echo "################### first 10 lines today"
	head $check | grep -n "$data"
	echo "################### last 10 lines of crontab"
	tail $check | grep crontab
  else
  	echo "File not found"
fi