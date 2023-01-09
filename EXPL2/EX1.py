# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# number = float(input())
def CheckNumber(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

def Summary(number):
    sum=0
    for i in number:
        if i.isdigit():
            sum=sum+float(i)
        else:
            continue
    return sum

Number = input("Введите число: ")
if CheckNumber(Number)==False:
    print(f"Не верное значение!")
else:
    print(f"Сумма цифр числа = {Summary(Number)}")