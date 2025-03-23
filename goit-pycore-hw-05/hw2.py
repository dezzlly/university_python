import re
from typing import Callable

def generator_numbers(text: str):
    for match in re.findall(r'\d+\.\d+', text):  # looking for a number in the format 123.45
        yield float(match)  # Convert to float and return

def sum_profit(text: str, func: Callable):
    return sum(func(text))  # call the passed generator and sum all its values


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f'Загальний дохід: {total_income:.2f}')  # Round to 2 decimal places