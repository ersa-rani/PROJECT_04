import math  # For square root function

def main():
    # Ask the user to enter the two perpendicular side lengths
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))
    
    # Use the Pythagorean theorem: hypotenuse^2 = ab^2 + ac^2
    bc = math.sqrt(ab**2 + ac**2)
    
    # Display the result
    print("The length of BC (the hypotenuse) is:", bc)

# Required line to call main
if __name__ == '__main__':
    main()
