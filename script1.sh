#!/bin/bash

ls -la /var/log
echo $stdout
ls -la /var/log | awk '{print $3,$9}'
echo $stdout