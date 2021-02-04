#!/bin/bash

echo 'Введите Bash или Python:'
read USER_VALUE

case "$USER_VALUE" in
Bash   ) echo "Bash - лучший язык программирования";;
Python ) echo "Python - лучший язык программирования";;
*      ) echo "Указанно неверное значение"
esac