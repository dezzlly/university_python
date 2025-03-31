from datetime import datetime, timedelta
from collections import UserDict

def input_error(func):
    """Декоратор для обработки ошибок ввода."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Error: Not enough arguments."
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return "Error: Contact not found."
    return wrapper

class Field:
    """Базовый класс для полей записи."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    """Класс для хранения имени контакта."""
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(name)

class Phone(Field):
    """Класс для хранения и валидации номера телефона."""
    def __init__(self, number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(number)

class Birthday(Field):
    """Класс для хранения и валидации дня рождения."""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    """Класс для хранения информации о контакте."""
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))
    
    def remove_phone(self, phone_number):
        self.phones = [phone for phone in self.phones if phone.value != phone_number]
    
    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return
        raise ValueError("Phone number not found.")
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def show_birthday(self):
        return self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "No birthday set."
    
    def __str__(self):
        phones = ", ".join(p.value for p in self.phones)
        birthday = f", Birthday: {self.show_birthday()}" if self.birthday else ""
        return f"{self.name.value}: {phones}{birthday}"

class AddressBook(UserDict):
    """Класс для управления контактами."""
    def add_record(self, record):
        self.data[record.name.value] = record
    
    def find(self, name):
        return self.data.get(name, None)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []
        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.replace(year=today.year)
                if birthday < today:
                    birthday = birthday.replace(year=today.year + 1)
                if 0 <= (birthday - today).days < 7:
                    upcoming.append(f"{record.name.value}: {record.show_birthday()}")
        return upcoming if upcoming else ["No upcoming birthdays."]

@input_error
def add_birthday(args, book):
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return f"Birthday {date} added for {name}."
    return "Contact not found."

@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    return record.show_birthday() if record else "Contact not found."

@input_error
def birthdays(_, book):
    return "\n".join(book.get_upcoming_birthdays())

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
