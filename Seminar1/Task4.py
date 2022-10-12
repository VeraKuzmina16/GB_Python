n = int(input('Введите номер четверти: '))
if n < 1 or n > 4:
    print('Неверный номер')
elif n == 1:
    print('x > 0 и y > 0')
elif n == 2:
    print('x < 0 и y > 0')
elif n == 3:
    print('x < 0  и y < 0')
elif n == 4:
    print('x > 0 и y < 0')