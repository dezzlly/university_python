import random


def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000: # check range
        return print('Numbers should be between 1 and 1000')
    
    if quantity > (max - min + 1): # check quantity
        return print("Error! Quantity is too large for the given range.")
    
    win_numbers = random.sample(range(min, max + 1), quantity) # get random unique numbers
    return sorted(win_numbers)


print(get_numbers_ticket(1, 36, 5))
print(get_numbers_ticket(0, 10, 2))
print(get_numbers_ticket(1, 1001, 2))
print(get_numbers_ticket(1, 10, 11))
print(get_numbers_ticket(1, 10, 10))