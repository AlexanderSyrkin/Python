# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# import os
# os.system('cls')

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res


# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res


# s = input("Введите текст для сжатия: ")
# print()
# print(f"Текст после сжатия: {coding(s)}","\n")
# print(f"Текст после распаковки: {decoding(coding(s))}","\n")

import os
os.system("cls")


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res


def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res

s = write_file('task_024_1.txt', input("Введите текст для кодировки: "))
with open('task_024_1.txt', 'r') as data:
    file1 = (" ".join(data.readlines()))
d = write_file('task_024_2.txt', coding(file1))
with open('task_024_2.txt', 'r') as data:
    file2 = (" ".join(data.readlines()))
print(f"Текст после кодировки: {coding(file1)}")
print(f"Текст после дешифровки: {decoding(coding(file1))}")