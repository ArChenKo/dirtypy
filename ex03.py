# Заполните список случайным образом нулями и единицами так, чтобы количество единиц было больше количества нулей.

from random import randint
num = int(input('Введите длину списка: '))
spisok = [0 for _ in range(num)]
len_1 = num//2+randint(1, num//3-1)
count = 0
while count < len_1:
    n = randint(0, num-1)
    if spisok[n] == 0:
        spisok[n] = 1
        count += 1
print(spisok)
