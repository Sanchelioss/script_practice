#!/bin/bash

get_fibonacci_value () {
    CHECK_VALUE='^[0-9]+$'
    TEMP_VALUE=1
    TEMP_ARRAY=(0 1)
    if ! [[ ( $USER_VALUE =~ $CHECK_VALUE ) || ( $USER_VALUE -eq "0" ) ]]
    then
        echo "Указанно неверное значение"
    elif [[ $USER_VALUE -eq "1" ]]
    then
        echo "Число Фибоначчи с номером 1 равно: 1"
    else
        while [[ $TEMP_VALUE -lt $USER_VALUE ]]
        do
          TEMP_ARRAY_LEN=${#TEMP_ARRAY[@]}
          FIBONACCI_VALUE=$((${TEMP_ARRAY[$TEMP_ARRAY_LEN-1]}+${TEMP_ARRAY[$TEMP_ARRAY_LEN-2]}))
          TEMP_ARRAY+=($FIBONACCI_VALUE)
          (( TEMP_VALUE++ ))
        done
        echo "Число Фибоначчи с номером $USER_VALUE равно: $FIBONACCI_VALUE"
    fi
}


echo 'Номер элемента ряда Фибоначчи:'
read USER_VALUE
get_fibonacci_value $USER_VALUE
