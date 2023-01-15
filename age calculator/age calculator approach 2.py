from datetime import date

def age_calculator():
    # Get birthdate from user
    birth_year = int(input("Enter your birth year: "))
    birth_month = int(input("Enter your birth month: "))
    birth_day = int(input("Enter your birth day: "))

    # Get current date
    today = date.today()

    # Calculate age
    age = today.year - birth_year
    if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
        age

    # Print age
    print("Your age is: ", age)
