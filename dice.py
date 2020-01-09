import sys
import random

class Die:
    
    def __init__(self, sides):
        self.sides = sides
        
    def roll(self):
        return random.randint(1, self.sides)
        
def checkSnakeEyes(x, y) :
    if (x == 1 and y == 1) :
        return "Snake Eyes!"
    else :
        return
        
def checkCraps(x, y) :
    dice_sum = x + y
    if (dice_sum == 2 or dice_sum == 3 or dice_sum == 12) :
        return "Crapped out!"
    else :
        return
        
def checkBoxCars(x,y) :
    if (x == 6 and y == 6) :
        return "Box Cars!"
    else :
        return
        

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
        result_1 = die_1.roll()
        result_2 = die_2.roll()
        print(str(result_1))
        print(str(result_2))
        
        print(checkSnakeEyes(result_1, result_2))
        print(checkCraps(result_1, result_2))
        print(checkBoxCars(result_1, result_2))
        
        cont = input("Roll again? (y/n)")

if __name__ == '__main__':
    sys.exit(main(sys.argv))
