from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    # Get the current date
    current_date = datetime.today().date()

    upcoming_birthdays = []

    for user in users:
        # Convert the user's birthday from string to a date object
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Create a date for the upcoming birthday in the current year
        upcoming_birthday = user_birthday.replace(year=current_date.year)
        
        # If the birthday has already passed this year, adjust to the next year
        if upcoming_birthday < current_date:
            upcoming_birthday = upcoming_birthday.replace(year=current_date.year + 1)

        # Transfer to Monday if birthday falls on a weekend
        if upcoming_birthday.weekday() == 5:  # Saturday
            upcoming_birthday += timedelta(days=2)
        elif upcoming_birthday.weekday() == 6:  # Sunday
            upcoming_birthday += timedelta(days=1)

        # Check if the upcoming birthday is within the next 7 days
        if (upcoming_birthday - current_date).days <= 7:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": upcoming_birthday.strftime("%Y.%m.%d")})

    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.03.17"},
    {"name": "Valera Smith", "birthday": "1990.03.09"},
    {"name": "Jane Smith", "birthday": "1990.03.10"},
    {"name": "Isabele Smith", "birthday": "1990.03.16"},
    {"name": "Donjuan Smith", "birthday": "1990.03.15"},
    {"name": "Illya Smith", "birthday": "1990.03.20"},
]


upcoming_birthdays = get_upcoming_birthdays(users)
print('Список привітань на цьому тижні: ', upcoming_birthdays)