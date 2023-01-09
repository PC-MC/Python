# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

list = input().split()
minn = 1
maxx = 0
for el in list:
    if float(el) % 1 != 0:
        if float(el) % 1 < minn:
            minn = float(el) % 1
        if float(el) % 1 > maxx:
            maxx = float(el) % 1
print(round(maxx - minn, 2))