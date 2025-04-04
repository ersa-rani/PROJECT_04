# Constant for the speed of light in meters per second
C = 299792458  # m/s

def main():
    # Ask user for mass input
    mass_in_kg = float(input("Enter kilos of mass: "))
    
    # Calculate energy using E = m * c^2
    energy_in_joules = mass_in_kg * (C ** 2)
    
    # Output the result and breakdown
    print("\ne = m * C^2...")
    print(f"m = {mass_in_kg} kg")
    print(f"C = {C} m/s")
    print(f"{energy_in_joules} joules of energy!")

# Required call to the main function
if __name__ == '__main__':
    main()
