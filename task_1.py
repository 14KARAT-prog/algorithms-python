numbers = [i for i in range(2, 100)]
divider = [i for i in range(2, 10)]
check = [0, 0, 0, 0, 0, 0, 0, 0]
'''
В диапазоне чисел от 2 до 99, определяем сколько из них
кратны 2, кратны 3, кратны 4 и т.д. до 9
'''

for i in numbers:
    for j in divider:
        if numbers[i - 2] % divider[j-2] == 0:
            check[j - 2] += 1
n = 0
while n < len(check):
    print(f'Числа кратные {n + 2} -', check[n])
    n += 1
