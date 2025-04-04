"""
An example program with constants
Converts feet to inches.
"""

INCHES_IN_FOOT = 12  # There are 12 inches in 1 foot

def main():
    # Ask user for the number of feet
    feet = float(input("Enter number of feet: "))
    
    # Convert to inches
    inches = feet * INCHES_IN_FOOT
    
    # Output result
    print("That is", inches, "inches!")

# Required line to run the main function
if __name__ == '__main__':
    main()
