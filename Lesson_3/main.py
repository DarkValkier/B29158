from berserk import Berserk
from Lesson_2.character import Character

player1 = Berserk(name='Volodya', damage=10)
player2 = Character(name='Oleg', damage=15)

print(player1)
print(player2)

while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    player2.attack(player1)

    print(player1)
    print(player2)