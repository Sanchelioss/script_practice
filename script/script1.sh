#!/bin/bash
###
#Variables
FORMATTED_DATE=`date +"%b %d"`
LOG_FILE=/var/log/syslog
LOG_DIR=~/for_syslog
#Check and create target directory
if ! [ -d $LOG_DIR ];
  then
  	mkdir $LOG_DIR
  	echo "target directory created"
fi
#show log dir
ls -la /var/log > ~/for_syslog/show_dir_log.log
#Check syslog and redirecting output to a files
if [ -f $LOG_FILE ];
  then
	echo "starting file operations"
	tail $LOG_FILE > ~/for_syslog/last_10_lines_in_syslog.log
	head $LOG_FILE > ~/for_syslog/first_10_line_in_syslog.log
	head $LOG_FILE | grep -n "FORMATTED_DATE" > ~/for_syslog/first_10_lines_today_in_syslog.log
	tail $LOG_FILE | grep crontab > ~/for_syslog/last_10_lines_of_crontab_in_syslog.log
	echo "done"
  else
  	echo "File not found"
fi
###
#deleting files older than 10 minutes
find ~/for_syslog -mmin +10 -type f -exec rm -fv {} \;