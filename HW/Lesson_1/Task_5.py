# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

X_1 = int(input("Введите первое значение А по Х: "))
Y_1 = int(input("Введите второе значение А по Y: "))
X_2 = int(input("Введите первое значение В по Х: "))
Y_2 = int(input("Введите первое значение В по Y: "))

dist_in_space = ((X_2-X_1)**2 + (Y_2-Y_1)**2)**0.5
print("A (",(X_1),",",(Y_1),"); ", "B (",(X_2),",",(Y_2),") -> ","%.2f" % dist_in_space, sep="")