import cProfile
import random


# Создание матрицы двумя циклами

def m_create_2_for(range_raw, range_coll):
    matrix = [[random.randint(1, 100) for _ in range(1, range_coll)] for _ in range(1, range_raw)]


cProfile.run('m_create_2_for(10, 10)')
cProfile.run('m_create_2_for(100, 100)')
cProfile.run('m_create_2_for(1000, 1000)')


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

cProfile.run("m_create_1_for(10)")
cProfile.run("m_create_1_for(100)")
cProfile.run("m_create_1_for(1000)")

# Сложность данного алгоритма O(n ** 2)
