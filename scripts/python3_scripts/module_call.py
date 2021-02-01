
import module_sorted_and_parsed_array

input_array = list(input('Введите значения массива через пробел ').split())

#output_array = module_sorted_and_parsed_array.get_parsed_array_for(input_array)

output_array = module_sorted_and_parsed_array.get_parsed_array_while(input_array)

result = module_sorted_and_parsed_array.get_sorted_array(output_array)

print(result)