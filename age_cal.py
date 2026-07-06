import datetime

# this is dictionary to map month names to their corresponding numbers

month_map = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}

# This is to get the current date, month and year

current = datetime.datetime.now()

# This function is to get the valid year from the user. It checks if the input is a digit, if it is within a reasonable range (not more than 100 years ago and not in the future), and returns the valid year.

def get_valid_year():
    while True:
        birth_year = input('Enter Your Birth Year: ')
        
        # Check if the input is a digit
        if birth_year.isdigit() is False:
            print('Please Enter a Valid Year')
            continue
        
        birth_year = int(birth_year)
        # Check if the year is within a reasonable range (not more than 100 years ago and not in the future)
        if birth_year < current.year - 100:
            print('Maybe you are a spirit? Please Enter a Valid Year')
            continue
        
        # Check if the year is not in the future
        if birth_year > current.year:
            print('Your Dad will work on it, Please Enter a Valid Year')
            continue
        
        return birth_year

# This function is to get the valid month from the user. It checks if the input is a valid month name, if the birth month is not in the future (if the birth year is the current year), and returns the valid month number.

def get_valid_month(birth_year):
    while True:
        birth_month = input('Enter Your Birth Month: ')
        if birth_month.isdigit():
            birth_month = int(birth_month)
            if birth_month < 1 or birth_month > 12:
                print('Please Enter a Valid Month')
                continue
        
        else:
            birth_month = month_map.get(birth_month.lower())
            if birth_month is None:
                print('Please Enter a Valid Month')
                continue
        
        # Check if the birth month is not in the future (if the birth year is the current year)
        if birth_month > current.month and birth_year == current.year:
            print('You have not been born yet!')
            continue
        
        return birth_month

# This function is to get the valid day from the user. It checks if the input is a digit, if it is within a reasonable range (1-31), if it is valid for the given month (taking into account leap years for February), and if the birth date is not in the future (if the birth year and month are the current year and month). It returns the valid day.

def get_valid_day(birth_year, birth_month):
    while True:
        birth_day = input('Enter Your Birth Day: ')
        
        # Check if the input is a digit
        if birth_day.isdigit() is False:
            print('Please Enter a Valid Day')
            continue
        birth_day = int(birth_day)
        # Check if the day is within a reasonable range (1-31)
        if birth_day < 1 or birth_day > 31:
            print('Please Enter a Valid Day')
            continue
        
        # Check if the day is valid for the given month (taking into account leap years for February)
        if birth_month == 2 and leap_year and birth_day > 29:
            print('February has at most 29 days. Please Enter a Valid Day')
            continue
        elif birth_month == 2 and not leap_year and birth_day > 28:
            print('February has at most 28 days. Please Enter a Valid Day')
            continue

        # Check if the day is valid for the given month
        if birth_month in [4, 6, 9, 11] and birth_day > 30:
            print(f'{birth_month} has at most 30 days. Please Enter a Valid Day')
            continue
        
        # Check if the day is valid for the given month
        if birth_month in [1, 3, 5, 7, 8, 10, 12] and birth_day > 31:
            print(f'{birth_month} has at most 31 days. Please Enter a Valid Day')
            continue
        # Check if the birth date is not in the future (if the birth year and month are the current year and month)
        if birth_year == current.year and birth_month == current.month and birth_day > current.day:
            print('You have not been born yet!')
            continue
        
        return birth_day

# This function calculates the age based on the birth date and the current date. It takes into account the differences in years, months, and days, and adjusts for cases where the day or month difference is negative. It also handles leap years for February.

def calculate_age(birth_year, birth_month, birth_day, current_year,current_month, current_day):
    
    # Calculate the differences in years, months, and days
    age_year = current_year - birth_year
    age_month = current_month - birth_month
    age_day = current_day - birth_day

    # Adjust for cases where the day or month difference is negative
    if age_day < 0:
        age_month -= 1
        if birth_month in [1, 3, 5, 7, 8, 10, 12]:
            age_day += 31
        elif birth_month in [4, 6, 9, 11]:
            age_day += 30
        elif birth_month == 2:
            if leap_year:
                age_day += 29
            else:
                age_day += 28

    # Adjust for cases where the month difference is negative
    if age_month < 0:
        age_year -= 1
        age_month += 12
    # Handle the case where the age is less than a year old
    if age_year == 0:
        print('You are less than a year old!') 
    
    return age_year, age_month, age_day

# This is the main part of the program that calls the functions to get the valid birth date from the user, calculates the age, and prints it.

birth_year = get_valid_year()

leap_year = (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0)

birth_month = get_valid_month(birth_year)

birth_day = get_valid_day(birth_year, birth_month)

age_year, age_month, age_day = calculate_age(birth_year, birth_month, birth_day, current.year, current.month, current.day)

print(f'You are {age_year} years {age_month} months {age_day} days old.')