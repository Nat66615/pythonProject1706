# нужно доделать см. фото

def conc(a, b: int) -> str:
    if type(a) == str or type(b) == str:
        raise TypeError('нужны числа')
    return a + b

# try:
#     result1 = conc('myStr', 1)
#     print('Результат: ', result1)
# except
#
# conc('myStr', 1)



def divide(a, b):
    if a == 0:
        raise ValueError('Деление на 0 запрещено')
    return b / a

try:
    result = divide(0, 10)
    print('Результат: ', result)
except ValueError as ex:
    print('Ошибка: ', str(ex))


