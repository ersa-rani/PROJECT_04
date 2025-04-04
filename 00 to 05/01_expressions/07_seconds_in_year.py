# Constants to define time units
DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN = 60

def main():
    # Calculate total seconds in a year
    seconds_in_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    
    # Print result
    print("There are", seconds_in_year, "seconds in a year!")

# Required call to main
if __name__ == '__main__':
    main()
