# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system('cls')
num = int(input("Введите число 'n'= "))
if num < 0 or num == 0:
     print("Ошибка. Введите число больше нуля.")
else:
    a_dic = {}
    key = 1
    a_dic[key] = 1
    total = 0
    while key < num + 1:
        my_value = (1+1/key)**key
        a_dic[key] = round(my_value,2)
        key = key + 1
        total = total + my_value
    print("Для n =",num,":",a_dic, end=" ")
    print("Сумма значений =", round(total,2)) 