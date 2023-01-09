# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

n = int(input())
strr = ''
while n > 0:
    strr = str(n % 2) + strr
    n //= 2
print(strr)