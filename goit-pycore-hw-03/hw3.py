import re


def normalize_phone(phone_number):
    # Remove unnecessary spaces and surrounding characters
    phone_number = phone_number.strip() 

    # Process the phone number depending on its beginning
    if re.match(r'^\+', phone_number):
         # If the number already starts with '+', just remove all non-digit characters except the '+'.
        new_format_phone = '+' + re.sub(r'\D+', '', phone_number[1:])
    elif re.match(r'^38', phone_number):
        # If the number starts with '38', remove all non-digit characters and add a '+'
        new_format_phone = '+' + re.sub(r'\D+', '', phone_number)
    else:
        # For all other numbers, add '+38' and remove non-digit characters
        new_format_phone = '+38' + re.sub(r'\D+', '', phone_number)


    return new_format_phone
         


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
print(sanitized_numbers)