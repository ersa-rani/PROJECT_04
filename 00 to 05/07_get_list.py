def main():
    lst = []  # Make an empty list to store values

    val = input("Enter a value: ")  # Get an initial value
    while val:  # Loop until the user enters an empty string
        lst.append(val)  # Add value to the list
        val = input("Enter a value: ")  # Prompt for the next value

    print("Here's the list:", lst)


# This provided line is required at the end of the Python file
if __name__ == '__main__':
    main()