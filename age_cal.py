import datetime

monthMap = {
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
currentMonth = datetime.datetime.now().month
currentYear = datetime.datetime.now().year

def get_valid_year():
    while True:
        birth_year = input('Enter Your Birth Year: ')
        
        if birth_year.isdigit() is False:
            print('Please Enter a Valid Year')
            continue
        if int(birth_year) < currentYear - 100:
            print('Maybe you are a spirit? Please Enter a Valid Year')
            continue
        if int(birth_year) > currentYear:
            print('Your Dad will work on it, Please Enter a Valid Year')
            continue
        return int(birth_year)
    
def get_valid_month(birth_year):
    while True:
        birth_month = monthMap.get(input('Enter Your Birth Month: ').lower())
        
        if birth_month is None:
            print('Please Enter a Valid Month')
            continue
        if birth_month > currentMonth and (birth_year) == currentYear:
            print('You have not been born yet!')
            continue
        return birth_month
def calculate_age(birth_year, birth_month):
    ageYear = currentYear - int(birth_year)
    ageMonth = currentMonth - int(birth_month)
    if ageMonth < 0:
        ageYear -= 1
        ageMonth += 12
    if ageYear == 0:
        print('You are less than a year old!') 
    return ageYear, ageMonth
birth_year = get_valid_year()
birth_month = get_valid_month(birth_year)
ageYear, ageMonth = calculate_age(birth_year, birth_month)
if ageYear > 0:
    print(f'You are {ageYear} years {ageMonth} months old.')