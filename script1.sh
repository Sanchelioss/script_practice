#!/bin/bash

#show log dir
ls -la /var/log
echo $stdout
#checking file availability
check=/var/log/syslog
if test -f $check;
  then
	echo "################### last 10 lines"
	tail $check
	echo "################### first 10 lines"
	head $check
	echo "################### first 10 lines today"
	cat $check | grep -n 'Jan 22' | head
	echo "################### last 10 lines of crontab"
	cat $check | grep crontab | tail
  else
  	echo "File not found"
fi