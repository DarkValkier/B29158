from character import Character

player1 = Character(name='Vasya', health=30, damage=5, defence=1)
player2 = Character(name='Petya', health=30, damage=2, defence=4)

print(player1)
print(player2)

player1.attack(player2)
player2.attack(player1)

print(player1)
print(player2)