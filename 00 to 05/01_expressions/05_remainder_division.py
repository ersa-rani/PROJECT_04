def main():
    # Ask the user for the dividend and divisor
    dividend = int(input("Please enter an integer to be divided: "))
    divisor = int(input("Please enter an integer to divide by: "))
    
    # Perform integer division and get the remainder
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    # Output the result
    print("The result of this division is", quotient, "with a remainder of", remainder)

# Required call to run the main function
if __name__ == '__main__':
    main()
