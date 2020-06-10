import random

class Dice():
    def __init__(self, sides):
        self.sides = sides
        self.rolls = []
    
    def roll(self):
        roll = random.randint(1,self.sides)
        print("You rolled a : %s " % roll)
        self.rolls.append(roll)
    
    def get_average():
        length = len(self.rolls)
        avg = (sum(self.rolls) / length)
        print("The average roll is: %s across %s rolls." % (avg, length))
        input("Press Enter To Continue: \n")

    my_dice = {
        "d6" : Dice(6),
        "d12" : Dice(12),
        "d20" : Dice(20)
    }

dice["d6"].roll()

    def choose_dice():
        for d in dice:
            print(f{d})
        
    
    def start():
        playing = True
        while playing:
    

