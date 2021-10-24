num = int(input("Введите число: "))
sum = 0
rightEquat = num * (num + 1) / 2
for i in range(num):
    sum = sum + num
    num -= 1
else:
    print("Сумма 1+2+3+...+n равна:", float(sum))
    print("n(n+1)/2 равно:", rightEquat)

if sum == rightEquat:
    print(f"Равенство выполняется {str(sum)} = {str(rightEquat)}")
