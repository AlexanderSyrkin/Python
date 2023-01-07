# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#    Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

value_X = int(input("Введите значение координаты Х: "))
value_Y = int(input("Введите значение координаты Y: "))

if value_X == 0 or value_Y == 0:
    print("Ошибка. Вы ввели значение = 0. Введите другое значение." )
elif value_X > 0 and value_Y > 0:
    print("x=",value_X,"; y=",value_Y,"-> 1")
elif value_X > 0 and value_Y < 0:
    print("x=",value_X,"; y=",value_Y,"-> 4")
elif value_X < 0 and value_Y < 0:
    print("x=",value_X,"; y=",value_Y,"-> 3")
elif value_X < 0 and value_Y > 0:
    print("x=",value_X,"; y=",value_Y,"-> 2")
    