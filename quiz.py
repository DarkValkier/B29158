points = 0

print('Какой город является столицей Украины?')
print('а) Днепр')
print('б) Киев')
print('в) Харьков')
print('г) Одесса')

answer = input('Ваш ответ: ').lower()

if answer == 'б':
    print('Верно!')
    points += 1
else:
    print('Неверно!')

print('Правильных ответов', points)

print('На сколько областей делится территория Украины?')
print('а) 20')
print('б) 23')
print('в) 25')
print('г) 19')

answer = input('Ваш ответ: ').lower()

if answer == 'в':
    print('Верно!')
    points += 1
else:
    print('Неверно!')

print('Правильных ответов', points)