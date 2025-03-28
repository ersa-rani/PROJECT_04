def main():
    print("This program adds two numbers.")

    # Get user input and convert to integers
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        # Compute sum
        total = num1 + num2

        # Display result
        print(f"The total is {total}.")
    
    except ValueError:
        print("Invalid input! Please enter integers only.")

if __name__ == '__main__':
    main()
