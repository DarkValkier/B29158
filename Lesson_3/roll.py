import random

success = 0
for i in range(100):
    if random.randint(1, 100) <= 99:
        print('Прокнуло')
        success += 1
    else:
        print('Не прокнуло')

print(f'Удачных бросков {success}.')