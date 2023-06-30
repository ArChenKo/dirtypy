# Дан список. Найдите три последовательных элемента в список, сумма которых максимальна.

from random import randint

print(spisok := [randint(0, 20) for _ in range(20)])
max3 = 0
index = 0
for i in range(2, len(spisok)):
    sum3 = spisok[i] + spisok[i - 1] + spisok[i - 2]
    if max3 < sum3:
        index = i
        max3 = sum3
print(f'Сумма э-лтов: {spisok[index-2]}, {spisok[index - 1]} и {spisok[index]} = {max3}')
