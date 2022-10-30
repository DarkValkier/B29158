import random


def make_choice(bot=False):
    if bot:
        return random.choice('rps')
    else:
        return input('Выберите предмет (r, p, s):')