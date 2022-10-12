a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
x = lambda a, b: a**2 == b or b**2 == a
print(x(a,b))
 