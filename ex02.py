# Создать список, который одинаково читается как слева направо, так и справа налево.

num = int(input('Введите размер списка: '))
mid = num//2
spisok = [i for i in range(1, mid)]+[i for i in range(mid, 0, -1)]
print(spisok)
