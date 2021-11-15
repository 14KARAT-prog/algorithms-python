import random


def bubble_sort(lst):
    n = 1

    while n < len(lst):
        count = 0

        for i in range(len(lst) - 1 - (n - 1)):

            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1

        if count == 0:
            break
        n += 1


SIZE = 11

array = [random.randint(-100, 99) for _ in range(SIZE)]

print('Массив:', array, sep='\n')
bubble_sort(array)
print('После сортировки:', array, sep='\n')
