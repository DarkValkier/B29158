a = 5
b = 0

try:
    # Часть кода, которая может выдать ошибку
    print(a / b)
except ZeroDivisionError:
    # Реакция на деление на ноль
    print('Делить на ноль нельзя!')
except Exception as error:
    # Реакция на любую ошибку
    print(f'Что-то пошло не так: {error}')
else:
    # Действия в случае отсутствия ошибок
    pass

print('Программа не прервалась')
