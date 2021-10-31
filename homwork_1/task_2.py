# Создаём массив из кубов нечётных чисел
array_of_cubes = []
for i in range(0, 1000):
    if i % 2 != 0:
        array_of_cubes.append(i**3)

sum_of_numbers_7 = 0 #Сумма чисел, сумма цифр которых делится нацело на 7

#Пробегаемся циклом по всем  элементам массива из кубов нечётных чисел
for k in range(0, len(array_of_cubes)):
    array_element = array_of_cubes[k]
    array_from_array_element = []

    #Создаём массив из составных чисел элемента массива
    while array_element > 0:
        array_from_array_element.append(array_element % 10)
        array_element = array_element // 10

    # Вычисляем сумму сосставных чисел элемента массива
    sum_of_numbers = 0
    for i in range(0, len(array_from_array_element)):
        sum_of_numbers = sum_of_numbers + array_from_array_element[i]

    #Если сумма составных чисел элемента массива делится нацело на 7, то прибавляем элемент массива к sum_of_numbers_7
    if sum_of_numbers % 7 == 0:
        sum_of_numbers_7 = sum_of_numbers_7 + array_of_cubes[k]

print(sum_of_numbers_7)

# Увеличиваем каждый элемент массива из кубов нечетных чисел на 17 и повторяем все наши вычисления
for i in range(0, len(array_of_cubes)):
    array_of_cubes[i] = array_of_cubes[i] + 17

sum_of_numbers_7 = 0

for k in range(0, len(array_of_cubes)):
    array_element = array_of_cubes[k]
    array_from_array_element = []

    while array_element > 0:
        array_from_array_element.append(array_element % 10)
        array_element = array_element // 10

    sum_of_numbers = 0
    for i in range(0, len(array_from_array_element)):
        sum_of_numbers = sum_of_numbers + array_from_array_element[i]

    if sum_of_numbers % 7 == 0:
        sum_of_numbers_7 = sum_of_numbers_7 + array_of_cubes[k]

print(sum_of_numbers_7)








