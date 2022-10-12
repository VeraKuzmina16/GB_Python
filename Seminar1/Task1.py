day = int(input('Введите число: '))
if day > 7 or day < 1:
  print('Неверное число')
elif day == 6 or day == 7:
  print("Это выходной")
else:
  print("Это рабочий день")