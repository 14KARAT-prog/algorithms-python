num = int(input("Введите число: "))
newNum = 0

while num > 0:
    lastNum = num % 10  # Последняя цифра числа
    num = num // 10  # Удаление последней цифры числа
    newNum = newNum * 10 + lastNum  # Увеличение разрядности "обратного" числа и добавление цифры

print("Обратное число:", newNum)
