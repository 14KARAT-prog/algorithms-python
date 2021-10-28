import random

array_length = int(input("Введите длину массива: "))

array = [random.randint(-100, 0) for j in range(array_length)]
print(array)

i = 0
index = -1

# Ищет в массиве максимальное отрицательное целое число

while i < array_length:
    if array[i] < 0 and index == -1:
        index = i
    elif array[i] < 0 and array[i] > array[index]:
        index = i
    i += 1

print(index, '- Позиция в массиве, значение:', array[index])
