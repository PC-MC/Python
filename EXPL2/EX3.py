# Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input('Введите число n: '))
list = {}
for i in range(1, n + 1):
    list[i] = (1+1/i)**i
print(list)
print(sum(list.values()))