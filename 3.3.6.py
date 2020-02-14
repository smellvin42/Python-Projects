import random
print('Hello World!')
some_values = ('a', 'b', 3,)
print(some_values[0:2])
values = [1, 2, 3]
print(values[1:])
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

print(random.choice(values))
print(random.randint(5, 8))
print(random.uniform(5, 8))

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


def roll_two_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(dice1 + dice2)


roll_two_dice()


print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')


def guess_letter():
    letter = ('abcdefghijklmnopqrstuvwxyz')
    print(random.choice(letter))


guess_letter()
