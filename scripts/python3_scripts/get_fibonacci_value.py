

def get_fibonacci_value(user_value):

    temp_value = 1
    temp_array = [0, 1]
    while (int(temp_value) < int(user_value)):
        temp_array_len = len(temp_array)
        fibonacci_value = temp_array[temp_array_len-1] + temp_array[temp_array_len-2]
        temp_array.append(fibonacci_value)
        temp_value += 1
    return fibonacci_value


input_value = input('Номер элемента ряда Фибоначчи:')
try:
    user_value = int(input_value)
    if isinstance(user_value, str) or int(user_value) <= 0:
        print ('Указанно неверное значение')
    elif int(user_value) == 1:
        print ('Число Фибоначчи с номером 1 равно: 1')
    else:
        result = get_fibonacci_value(user_value)
        print (f'Число Фибоначчи с номером {user_value} равно: {result}')
except:
    print ('Указанно неверное значение')