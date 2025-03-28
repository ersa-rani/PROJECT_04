def main():
    try:
        # Prompt the user for a number and convert to float
        num = float(input("Type a number to see its square: "))

        # Compute the square
        square = num ** 2

        # Print the result with formatted output
        print(f"{num} squared is {square}")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == '__main__':
    main()
