# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

import os
os.system('cls')
new_num = str(input("Введите число больше нуля: "))
del_point =new_num.replace('.', '')
int_value = int(str(del_point))
if int_value <=0:
    print("Ошибка. Введите число больше нуля.")
else:
    suma = 0
    while int_value > 0:
        digit = int_value % 10
        suma = suma + digit
        int_value = int_value // 10
    print(new_num, "->", suma)








