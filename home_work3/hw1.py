from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')  # check date format
        today = datetime.today()  # get current date
        delta = (today - date).days  # difference of days
        return delta
    except ValueError:
        print("Invalid date format! Please use YYYY-MM-DD.")


print(get_days_from_today('2025-03-01'))
print(get_days_from_today('2025-03-15'))
print(get_days_from_today('3454-45-45'))
print(get_days_from_today('wwww-ee-aa'))
print(get_days_from_today('1234-13-23'))
print(get_days_from_today('hello'))
print(get_days_from_today('20250309'))
print(get_days_from_today('1234-12-32'))
print(get_days_from_today('2023-03-14 00:00:00'))