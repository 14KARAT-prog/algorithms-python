num = int(input("Введите количество элементов: "))
j = 1
sum = 0  # Сумма элементов

for i in range(num):
    sum = sum + j
    j /= -2

print("Сумма элементов: ", sum)