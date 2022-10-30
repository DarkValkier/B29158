while True:
    name = input('Введите своё имя:')

    if len(name):
        print('Привет, ' + name)
        print('Привет, ', name)
        print(f'Привет, {name}!')
    else:
        print('Вы ничего не ввели!')

    print('1. Повторить')
    print('0. Выйти')

    action = input('Выберите действие: ')

    if action == '0':
        break