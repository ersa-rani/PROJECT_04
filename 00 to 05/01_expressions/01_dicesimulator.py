"""
Program: dicesimulator
----------------------
Simulate rolling two dice, three times. Prints
the results of each die roll. This program is used
to show how variable scope works.
"""

import random

# Number of sides on each die
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    total = die1 + die2
    print("Rolled dice: {} + {} = {}".format(die1, die2, total))

def main():
    die1 = 10  # Local variable in main to demonstrate scope
    print("die1 in main() starts as:", die1)
    
    # Roll the dice three times
    roll_dice()
    roll_dice()
    roll_dice()
    
    print("die1 in main() is still:", die1)

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
