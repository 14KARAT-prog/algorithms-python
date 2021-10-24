def calc(num_1, num_2, sign):
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))
    sign = input("Введите знак операции(+, -, *, /) или '0'(если хотите закончить): ")
    if (num_2 == 0) and (sign == '/'):  # Проверка деления на ноль
        print("На ноль делить нельзя!")
        return calc(num_1, num_2, sign)

    if sign == '+':  # Сложение
        print("сумма чисел", num_1 + num_2)
        return calc(num_1, num_2, sign)
    elif sign == '-':  # Вычитание
        print("разность чисел", num_1 - num_2)
        return calc(num_1, num_2, sign)
    elif sign == '*':  # Умножение
        print("произведение чисел", num_1 * num_2)
        return calc(num_1, num_2, sign)
    elif sign == '/':  # Деление
        print("деление чисел", num_1 / num_2)
        return calc(num_1, num_2, sign)
    elif sign == '0':  # Завершение программы ноль '0'
        print("Завершение программы")
    else:  # Если знак введен не верно
        print("Введите корректный знак операции!")
        return calc(num_1, num_2, sign)


calc(4, 2, '+')
