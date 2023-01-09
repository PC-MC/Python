# адайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def CheckEnteredNumber(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def PrimeFactors(number):
    primeFactorsList=[]
    primeFactorsList.append(1) # добавляем 1 по умолчанию,т.к. единица будет простым множителем для любого числа 
    tempPrimeFactor=2 # задаем следующего "претендента" на простого множителя для введенного числа 
    divisionResult=number
    while divisionResult>1: # выполняем действия пока от введенного числа не останеться единица в результате деления
            if (divisionResult%tempPrimeFactor)==0: # если число делиться нацело на текущего "претендента" на простой множитель, то делим на него.
                primeFactorsList.append(tempPrimeFactor)
                divisionResult=divisionResult/tempPrimeFactor
            else:
                tempPrimeFactor=tempPrimeFactor+1 #иначе увеличиваем "претендена" на единицу 
    return primeFactorsList

mineNumber = input("Enter your integer number: ")
if CheckEnteredNumber(mineNumber)==False:
    print(f"Wrong format of the entered number {mineNumber}! Check your input, the number should be integer!")
elif int(mineNumber)==0:
    print("The entered number must NOT be zero!")
else:
    mineNumber=int(mineNumber)
    result=PrimeFactors(mineNumber)
    print(f"The entered number {mineNumber} has the following prime factors: {result}.")