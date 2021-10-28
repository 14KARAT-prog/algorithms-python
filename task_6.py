import random

array_length = int(input("Введите длину массива: "))

array = [random.randint(0, 100) for j in range(array_length)]

print(array, '- Массив')

min_id = array.index(min(array))
max_id = array.index(max(array))

if max_id > max_id:
    min_id, max_id = max_id, min_id

summ = 0
for i in range(min_id + 1, max_id):
    summ += array[i]

print(summ, "- Сумма чисел между максимальным и минимальным")