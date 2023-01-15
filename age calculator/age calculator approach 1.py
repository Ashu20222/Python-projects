from datetime import date

def age_calculator(birth_year,birth_month,birth_day):
    
    # Get current date
    today = date.today()

    # Calculate age
    age = today.year - birth_year
    if today.month < birth_month or (today.month == birth_month and today.day < birth_day):
        age

    # Print age
    print("Your age is: ", age)
