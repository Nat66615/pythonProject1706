def divide(a, b):
    if a == 0:
        raise ValueError('Деление на 0 запрещено')
    return b / a

try:
    result = divide(0, 10)
    print('Результат: ', result)
except ValueError as ex:
    print('Ошибка: ', str(ex))