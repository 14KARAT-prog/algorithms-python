import random

randNum = random.randint(0, 100)


def goodLuck(num, j):
    num = int(input("Введите число от 0 до 100: "))  # Запрашиваем число

    if num == randNum:  # Если число равно загаданному
        print("Поздравляю вы угадали!")
        return
    elif j == 0:  # Когда все попытки кончаются
        print("Все попытки закончились, загаданое число было:", randNum)
    else:
        j = j - 1  # Уменьшение попыток на 1 с каждой неудачной попыткой отгадать
        print(f"К сожаление вы не угадали, у вас осталось {j} попыток")
        return goodLuck(num, j)


goodLuck(0, 10)
