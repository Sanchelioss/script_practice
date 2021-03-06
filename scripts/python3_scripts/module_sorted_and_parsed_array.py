

def get_parsed_array_for(input_array):
	value_limit = 7
	output_array = []

	for i in input_array:
		try:
			array_value_to_integer = int(i)

			if (array_value_to_integer > value_limit):
				output_array.append(array_value_to_integer)
		except:
			print(f'element {i} is string')

	return output_array


def get_parsed_array_while(input_array):
	value_limit = 7
	output_array = []
	i = 0
	while i < len(input_array):
		try:
			array_value_to_integer = int(input_array[i])

			if (array_value_to_integer > value_limit):
				output_array.append(array_value_to_integer)
		except:
			print(f'element {input_array[i]} is string')
		i += 1
	return output_array


def get_sorted_array(output_array):
	output_array_len = len(output_array)

	for i in range (output_array_len):
		for j in range (0, output_array_len-i-1):
			if (output_array[j] > output_array[j+1]):
				temp = output_array[j]
				output_array[j] = output_array[j+1]
				output_array[j+1] = temp
	return output_array
