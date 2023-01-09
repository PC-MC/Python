# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# sum = 0
# list = input().split()
# for ind in range(1, len(list), 2):
#     sum  += int(list[ind])
# print(sum)



import random

n = int(input('Введите размер списка:'))
list = []
sum = 0

for i in range(n):
    list.append(random.randint(0,10))
    if i % 2 != 0:
        sum = sum + list[i]
print(list)
print(f'Сумма нечетных элементов списка = {sum}')
