def main():
    # Prompt the user for a temperature in Fahrenheit
    try:
        degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        
        # Convert to Celsius
        degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

        # Print the result with proper formatting
        print(f"Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.2f}C")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == '__main__':
    main()
