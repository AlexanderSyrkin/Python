 #Напишите программу, удаляющую из текста все слова, содержащие "абв".

import os
os.system('cls')

text = "впывап абв пврврыц купарвва sdfsdf fвп вапрвdgf абв 123 545ыва 9784а 785абв77".split()
print("Условие:",text, "\n")

abc = list(filter(lambda x: "абв" in x, text))
del_=[text.remove(item) for item in abc]

print("Результат:",text, "\n")
print("Удаленные слова:",abc, "\n")

