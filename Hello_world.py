name = input("What is your name? ")
print(f"Hello, {name}!")
from datetime import datetime
# Function to calculate age 

def calculate_age(birth_year):
    current_year = datetime.now().year  
    return current_year - birth_year

birth_year = int(input("What is your birth year?"))
age = calculate_age(birth_year)
print(f"You must be {age} years old!")