import random
from sys import getsizeof


# ------------------------------1---------------------------------
# Создание матрицы двумя циклами
def m_create_2_for(range_raw, range_coll):
    matrix = [[random.randint(1, 100) for _ in range(1, range_coll)] for _ in range(1, range_raw)]


# cProfile.run('m_create_2_for(10, 10)')
print(getsizeof(m_create_2_for(10, 10)))  # 16 байт

# cProfile.run('m_create_2_for(100, 100)')
print(getsizeof(m_create_2_for(100, 100)))  # 16 байт

# cProfile.run('m_create_2_for(1000, 1000)')
print(getsizeof(m_create_2_for(1000, 1000)))  # 16 байт


# Сложность данного алгоритма O(n ** 2)

# Создание матрицы 1 циклом
def m_create_1_for(size_matrix):
    matrix = []
    temp_array = []

    for i in range(1, (size_matrix ** 2) + 1):
        val = random.randint(1, 100)

        if i % size_matrix == 0:
            temp_array.append(val)
            matrix.append(temp_array)
            temp_array = []
        else:
            temp_array.append(val)
    print(matrix)


# cProfile.run("m_create_1_for(10)")
print(getsizeof(m_create_1_for(10)))  # 16 байт

# cProfile.run("m_create_1_for(100)")
print(getsizeof(m_create_1_for(100)))  # 16 байт

# cProfile.run("m_create_1_for(1000)")
print(getsizeof(m_create_1_for(1000)))  # 16 байт

# ------------------------------2---------------------------------
array_length = int(input("Введите длину массива: "))
print(getsizeof(array_length))  # 28 байт

# Создание рандомного массива с длинной указанной пользователем
array_1 = [random.randint(0, 100) for i in range(array_length)]
print(array_1, '- рандомный массив чисел')
print(getsizeof(array_1))  # 88 байт и больше

array_2 = []
# Следующий цикл помещяет в пустой массив индексы четных элементов первого массива
for i in range(0, array_length):
    if array_1[i] % 2 == 0:
        array_2.append(i)

print(array_2, '- индексы четных элементов первого массива')
print(getsizeof(array_2))  # 56 байт и больше

#  Python version 3.9.1
#  Операционная система Windows 10 Pro, 64-разрядная
