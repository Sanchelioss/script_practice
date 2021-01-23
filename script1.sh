#!/bin/bash
###
time=date +"%b %d"
#show log dir
ls -la /var/log > ~/for_syslog/show_dir_log.log
#checking file availability
check=/var/log/syslog
if [ -f $check ];
  then
	echo "starting file operations"
	tail $check > ~/for_syslog/last_10_lines_in_syslog.log
	head $check > ~/for_syslog/first_10_line_in_syslog.log
	head $check | grep -n "$time" > ~/for_syslog/first_10_lines_today_in_syslog.log
	tail $check | grep crontab > ~/for_syslog/last_10_lines_of_crontab_in_syslog.log
	echo "done"
  else
  	echo "File not found"
fi
###
