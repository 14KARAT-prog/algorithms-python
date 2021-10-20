a = int(input("Введите первое число "))
b = int(input("Введите второе число "))
c = int(input("Введите третье число "))

if ((a > b) & (b > c)) or ((a < b) & (b < c)):
    print("Среднее число 'b'")
elif ((b > a) & (a > c)) or ((b < a) & (a < c)):
    print("Среднее число 'a'")
elif ((a > c) & (c > b)) or ((a < c) & (c < b)):
    print("Среднее число 'c'")
else:
    print("Какие-то или все числа равны")