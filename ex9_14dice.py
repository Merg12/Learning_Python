from random import randint

x = randint(1,6)

class Die():
    def __init__(self, sides = 6):
        self.sides = sides
        
    def roll_die(self):
        n = 0
        while n <= 10:
            print(randint(1, self.sides))
            n += 1

game = Die()

game.roll_die()