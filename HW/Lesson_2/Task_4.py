# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import os
os.system('cls')

a = [] 
n = int(input("Введите число N: "))  
m = -1*n
for i in range(m,n+1):  
    new_element = i
    a.append(new_element)
print(a)

sourceList = a
filterObj = filter(lambda x: x !=0, sourceList)
filteredList = list(filterObj)

from functools import reduce
from operator import mul 
spisok = filteredList 
result = reduce(mul, filteredList)
print("Произведение элементов = ", f'{result:,.2f}'.replace(',', ' '))

MyList = ("".join(map(str, a)))
MyFile=open('file.txt', 'w')

for line in MyList:
    MyFile.write(line)
    MyFile.write('\n')
MyFile.close()




