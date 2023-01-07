# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system('cls')
a = [] 
n = int(input("Введите число N: "))  
m = 1
while m < n:
    for i in range(n):  
        import math
        new_element = math.factorial(m)
        a.append(new_element)
        m = m + 1
print("Пусть N =", n, "тогда ->", a)


        
        

        
   
   
   
    
  