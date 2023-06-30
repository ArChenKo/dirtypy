# Найти количество чисел в списке, которые делятся на 3, но не делятся на 7.

from random import randint

spisok = [randint(0, 100) for _ in range(int(input('Введите длину списка: ')))]
print(spisok)
count = 0
for i in spisok:
    if i % 3 == 0 and i % 7 != 0:
        print(i, end=', ')
        count += 1
print(f'Количество чисел в списке кратных 3, но не кратных 7 = {count}')
