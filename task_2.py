import random

array_length = int(input("Введите длину массива: "))
# Создание рандомного массива с длинной указанной пользователем
array_1 = [random.randint(0, 100) for i in range(array_length)]
print(array_1, '- рандомный массив чисел')

array_2 = []
# Следующий цикл помещяет в пустой массив индексы четных элементов первого массива
for i in range(0, array_length):
    if array_1[i] % 2 == 0:
        array_2.append(i)

print(array_2, '- индексы четных элементов первого массива')