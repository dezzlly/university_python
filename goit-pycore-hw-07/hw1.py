from collections import UserDict
from datetime import datetime, timedelta

class Field:
    """
    Базовый класс для полей записи. Хранит значение и определяет общий метод __str__.
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    """
    Класс для хранения имени контакта. Обязательное поле.
    """
    def __init__(self, name):        
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(name)
    
class Phone(Field):
    """
    Класс для хранения номера телефона. Проверяет, что номер состоит из 10 цифр.
    """
    def __init__(self, number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Invalid phone number. It must contain exactly 10 digits.")
        super().__init__(number)

class Birthday(Field):
    """
    Класс для хранения дня рождения. Дата должна быть в формате DD.MM.YYYY.
    """
    def __init__(self, value):
        try:
            self.date = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")
        super().__init__(value)

class Record:
    """
    Класс для хранения информации о контакте. 
    Содержит имя, список телефонов и день рождения.
    """
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        """Добавляет новый номер телефона."""
        phone = Phone(phone_number)
        self.phones.append(phone)
    
    def remove_phone(self, phone_number):
        """Удаляет номер телефона из списка, если он есть."""
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return f"Phone number {phone_number} removed."
        return f"Phone number {phone_number} not found."
    
    def edit_phone(self, old_number, new_number):
        """Редактирует существующий номер телефона."""
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return f"Phone number updated to {new_number}."
        return f"Phone number {old_number} not found."
    
    def find_phone(self, phone_number):
        """Ищет номер телефона в списке телефонов."""
        for phone in self.phones:
            if phone.value == phone_number:
                return f"Phone number {phone_number} found."
        return f"Phone number {phone_number} not found."
    
    def add_birthday(self, birthday):
        """Добавляет день рождения контакта."""
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        phones = '; '.join(p.value for p in self.phones)
        birthday = f", birthday: {self.birthday.value}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {phones}{birthday}"

class AddressBook(UserDict):
    """
    Класс для управления адресной книгой. Наследуется от UserDict.
    """
    def add_record(self, record):
        """Добавляет новый контакт в адресную книгу."""
        self.data[record.name.value] = record
    
    def find(self, name):
        """Ищет контакт по имени."""
        return self.data.get(name, None)
    
    def delete(self, name):
        """Удаляет контакт по имени, если он есть в книге."""
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self):
        """Возвращает список контактов, у которых день рождения на следующей неделе."""
        upcoming_birthdays = []
        today = datetime.today().date()
        next_week = today + timedelta(days=7)
        
        for record in self.data.values():
            if record.birthday:
                birthday_date = record.birthday.date.replace(year=today.year)
                if today <= birthday_date <= next_week:
                    upcoming_birthdays.append(record.name.value)
        
        return upcoming_birthdays


# Создаем адресную книгу
book = AddressBook()

# Добавляем контакт с телефонами и днем рождения
record = Record("John")
record.add_phone("1234567890")
record.add_phone("0987654321")
record.add_birthday("15.04.1990")
book.add_record(record)

# Добавляем еще один контакт
record2 = Record("Jane")
record2.add_phone("1112223333")
record2.add_birthday("10.04.1995")
book.add_record(record2)

# Выводим все контакты
for name, rec in book.data.items():
    print(rec)

# Ищем ближайшие дни рождения
print("Upcoming birthdays:", book.get_upcoming_birthdays())