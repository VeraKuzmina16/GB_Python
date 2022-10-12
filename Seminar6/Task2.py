from math import *
n = int(input("Введите положительное число:  "))
if n < 1:
    print("Неверное число, повторите ввод")
else:
    list = (factorial(i) for i in range(1, n + 1))
    print(list)
