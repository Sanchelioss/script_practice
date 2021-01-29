

def get_parsed_array(input_array):
	value_limit = 7
	output_array = []
	i = 0
	while i < len(input_array):
		try:
			a = int(input_array[i])

			if (a > value_limit):
				output_array.append(a)
		except:
			print(f'element {input_array[i]} is string')
		i += 1
	return output_array


def get_sort_array(output_array):
	output_array_len = len(output_array)

	for i in range (output_array_len):
		for j in range (0, output_array_len-i-1):
			if (output_array[j] > output_array[j+1]):
				temp = output_array[j]
				output_array[j] = output_array[j+1]
				output_array[j+1] = temp
	return output_array


input_array = list(input('Введите значения массива через пробел ').split())

output_array = get_parsed_array(input_array)

sort_array = get_sort_array(output_array)

print(sort_array)