import random

array_length = int(input("Введите длину массива: "))

array = [random.randint(0, 100) for i in range(array_length)]

print(array, "- Первоначальный список")
# Нахожу максимальный и минимальный элемент массива
mx = max(array)
mn = min(array)
# Нахожу индексы максимального и минимального элемента массива
i_mx = array.index(mx)
i_mn = array.index(mn)
# Меняю местами эти элементы
array[i_mx], array[i_mn] = array[i_mn], array[i_mx]


print(array, "- Измененный список")
