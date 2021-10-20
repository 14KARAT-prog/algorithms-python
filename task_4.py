import random

num_1, num_2 = map(int, input("Введите диапазон целых чисел ").split())
real_number_1, real_number_2 = map(float, input("Введите диапазон вещественных чисел ").split())
let_1, let_2 = input("Введите диапазон букв английского альфавита от 'a' до 'z' ").split()

print("Рандомное число " + str(random.randint(num_1, num_2)))
print("Рандомное вещественное число " + str(round(random.uniform(real_number_1, real_number_2), 2)))

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = ''
alphabet_new = []
j = 0
while let_1 != i:
    i = alphabet[j]
    j = j + 1
else:
    alphabet_new.append(alphabet[j - 1])

while let_2 != i:
    i = alphabet[j]
    alphabet_new.append(alphabet[j])
    j = j + 1
else:
    print('Рандомный символ "' + str(random.choice(alphabet_new)) + '"')
