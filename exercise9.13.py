from random import randint


class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


print("Dadu 6 sisi:")
die = Die()
for i in range(10):
    die.roll_die()

print("\nDadu 10 sisi:")
die = Die(10)
for i in range(10):
    die.roll_die()

print("\nDadu 20 sisi:")
die = Die(20)
for i in range(10):
    die.roll_die()