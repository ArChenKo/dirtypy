# Проверьте, содержит ли данный список из n чисел, все числа от 1 до n.

from random import randint

num = int(input('Введите число n: '))
print(spisok := [randint(1, num) for _ in range(num)])

m_spisok=[i for i in range(1,num+1)]
print(m_spisok)
for i in m_spisok:
    if i not in spisok:
        print(i, end=' ')
