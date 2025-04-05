import pickle
from datetime import datetime, timedelta
from collections import UserDict

def input_error(func):
    """Декоратор для обробки помилок вводу."""
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
    """Базовий клас для полів запису."""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)

class Name(Field):
    """Клас для зберігання імені контакту."""
    def __init__(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(name)

class Phone(Field):
    """Клас для зберігання та валідації номера телефону."""
    def __init__(self, number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(number)

class Birthday(Field):
    """Клас для зберігання та валідації дня народження."""
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    """Клас для зберігання інформації про контакт."""
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
    """Клас для управління контактами."""
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

# Функції для серіалізації та десеріалізації

def save_data(book, filename="addressbook.pkl"):
    """Зберігає дані адресної книги у файл."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    """Завантажує дані адресної книги з файлу, або повертає нову книгу, якщо файл не знайдено."""
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

# Обробка команд

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

@input_error
def add(args, book):
    """Додає новий контакт з іменем і номером телефону."""
    name, phone = args
    record = book.find(name)
    if record:
        record.add_phone(phone)
        return f"Phone {phone} added to {name}."
    else:
        record = Record(name)
        record.add_phone(phone)
        book.add_record(record)
        return f"Contact {name} with phone {phone} added."

@input_error
def phone(args, book):
    """Показує номери телефонів для вказаного контакту."""
    name = args[0]
    record = book.find(name)
    if record:
        phones = ", ".join(phone.value for phone in record.phones)
        return f"{name}'s phones: {phones}"
    return "Contact not found."

@input_error
def change(args, book):
    """Змінює існуючий номер телефону на новий."""
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        result = record.edit_phone(old_phone, new_phone)
        return result
    return "Contact not found."

# Головна функція

def main():
    book = load_data()  # Завантаження даних при запуску програми
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            save_data(book)  # Збереження даних перед виходом
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add(args, book))
        elif command == "phone":
            print(phone(args, book))
        elif command == "change":
            print(change(args, book))
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
