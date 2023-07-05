# Напишите программу, которая вводит с клавиатуры непустой список целых чисел, и выводит
# число локальных максимумов (элемент является локальным максимумом, если он не имеет соседей,
# больших, чем он сам).

from random import randint

print(spisok := [randint(0, 50) for _ in range(int(input('Введите длину списка: ')))])
print([spisok[i] for i in range(1, len(spisok)-1) if spisok[i - 1] < spisok[i] > spisok[i + 1]])
