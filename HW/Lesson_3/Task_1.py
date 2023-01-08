# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import os
os.system('cls')

list_length = int(input("Введите длину списка: "))

from random import randint
lst = []
for i in range(list_length):
    lst.append(randint(1, 10))
print(lst, '->', end=' ')

def sum_odd_index(lst):
    s = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            s += lst[i]
    print(f"Сумма элементов на нечетных позициях равна = {s}.")
sum_odd_index(lst)



