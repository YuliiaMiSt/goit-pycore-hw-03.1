
#Домашне завдання № 1#
from datetime import datetime
 
def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError
    current_date = datetime.today()
    delta = current_date - input_date
    return delta.days

#Домашне завдання № 2#

import random
 
def get_numbers_ticket(minimum, maximum, quantity):
    if minimum < 1 or maximum > 1000 or quantity < minimum or quantity > maximum:
        return []
    unique_numbers = set()
    while len(unique_numbers) < quantity:
        unique_numbers.add(random.randint(minimum, maximum))
    sorted_numbers = sorted(unique_numbers)
 
    return sorted_numbers

#Домашне завдання № 3#

import re
 
def normalize_phone(phone_number):
 
    digits_only = re.sub(r'\D', '', phone_number)
    if digits_only.startswith('+'):
       
        normalized_number = '+38' + digits_only[2:]
    else:
        normalized_number = '+38' + digits_only
 
    return normalized_number
 
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
 
sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

#Домашне завдання № 4#

from datetime import datetime, timedelta
 
def get_upcoming_birthdays(users):
    today = datetime.today().date()
 
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)
        days_until_birthday = (birthday - today).days
 
        if 0 <= days_until_birthday <= 7:
            if birthday.weekday() >= 5:
                next_monday = today + timedelta(days=(7 - today.weekday()) + 1)
                congratulation_date = next_monday.strftime("%Y.%m.%d")
            else:
                congratulation_date = birthday.strftime("%Y.%m.%d")
            upcoming_birthday = {"name": user["name"], "congratulation_date": congratulation_date}
            upcoming_birthdays.append(upcoming_birthday)
 
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)