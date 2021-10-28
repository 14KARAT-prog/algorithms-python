import random

array_length = int(input("Введите длину массива: "))

array = [random.randint(0, 100) for j in range(array_length)]

print(array, '- Массив')
# Находим наименьшие элементы массива
min1 = min(array)
array.remove(min1)
min2 = min(array)

print(min1, min2, sep='\n')
