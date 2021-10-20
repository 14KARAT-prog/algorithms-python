let_1, let_2 = input("Введите диапазон букв английского альфавита от 'a' до 'z' ").split()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = ''
alphabet_new = []
j = 0
k = 0
while let_1 != i:
    i = alphabet[j]
    j = j + 1
else:
    alphabet_new.append(alphabet[j - 1])
    print("Порядковый номер в алфавите первой буквы " + str(j))

while let_2 != i:
    i = alphabet[k]
    alphabet_new.append(alphabet[k])
    k = k + 1
else:
    print("Порядковый номер в алфавите второй буквы " + str(k))
    print("Число букв между первой буквой и второй " + str(k - j - 1))