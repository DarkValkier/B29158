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