import sys
import random

class Die:
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self):
        return random.randint(1, self.sides)
        

def main(args):
    print("Welcome to Krieg's Casino!")
    sides = input("How many sides should each die have? ")
    sides = int(sides)
    die_1 = Die(sides)
    die_2 = Die(sides)
    cont = "y"
    counter = 0
    while (cont == "y") :
        counter += 1
        print("Roll " + str(counter) + ": ")
        print(die_1.roll())
        print(die_2.roll())
        cont = input("Roll again? (y/n)")

if __name__ == '__main__':
    sys.exit(main(sys.argv))
