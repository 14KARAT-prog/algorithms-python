num = int(input("Введите натуральное число: "))
even = []  # Список четных цифр
notEven = []  # Список не четных цифр
i = 0  # Накопитель четных цифр
j = 0  # Накопитель не четных цифр

while num > 0:
    if num % 10 % 2 == 0:
        even.append(num % 10)
        num = num // 10
        i += 1
    else:
        notEven.append(num % 10)
        num = num // 10
        j += 1

print(f"У вас {i} четных цифр:", even, f"и {j} не четных цифр:", notEven)
