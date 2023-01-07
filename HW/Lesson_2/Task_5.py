# Реализуйте алгоритм перемешивания списка/

import os
os.system('cls')

a = [] 
n = int(input("Введите число N: "))  
for i in range(n):  
    new_element = i
    a.append(new_element)
print(a)

from random import sample
 
if __name__ == '__main__':
    nums = range(n)
    print (sample(nums, len(nums)))


