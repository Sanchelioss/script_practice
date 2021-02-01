#!/bin/bash


get_parsed_array () {
	VALUE_LIMIT=7
	for i in ${INPUT_ARRAY[@]}; do
		if [[ $i -ge $VALUE_LIMIT ]]
        then
			OUTPUT_ARRAY+=($i)
	    fi
	done
}


get_sorted_array () {
OUTPUT_ARRAY_LEN="${#OUTPUT_ARRAY[@]}"
    for (( i=0; i < OUTPUT_ARRAY_LEN; i++ ))
    do
        for (( j = OUTPUT_ARRAY_LEN-1; j > i; j-- ))
        do
            if (( ${OUTPUT_ARRAY[$j-1]} > ${OUTPUT_ARRAY[$j]} ))
            then
                temp=${OUTPUT_ARRAY[$j-1]}
                OUTPUT_ARRAY[$j-1]=${OUTPUT_ARRAY[$j]}
                OUTPUT_ARRAY[$j]=$temp
            fi
        done
    done
}

INPUT_ARRAY=("$@")
get_parsed_array ${INPUT_ARRAY[@]}
get_sorted_array ${OUTPUT_ARRAY[@]}
echo "${OUTPUT_ARRAY[@]}"