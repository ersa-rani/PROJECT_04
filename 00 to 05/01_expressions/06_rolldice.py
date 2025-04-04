"""
Simulate rolling two dice, and print results of each
roll as well as the total.
"""

import random  # Needed to simulate dice rolls

# Constant for the number of sides on each die
NUM_SIDES = 6

def main():
    # Optional: Set a seed for reproducible results
    # random.seed(1)
    
    # Roll each die
    die1 = random.randint(1, NUM_SIDES)
    die2 = random.randint(1, NUM_SIDES)
    
    # Calculate total
    total = die1 + die2
    
    # Print results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Required line to call main
if __name__ == '__main__':
    main()
