# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.

number = int(input("Введите номер дня недели:"))
if number == 6 or number == 7:
    print("Выходной день")
elif number > 0 and number < 6:
    print("Рабочий день")
elif number < 1 or number > 7:
    print("Вы выбрали не верный день")
