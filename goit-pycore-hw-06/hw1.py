from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value  # Сохраняем значение поля

    def __str__(self):
        return str(self.value)  # Возвращаем строковое представление значения

class Name(Field):
    def __init__(self, name):        
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        super().__init__(name)  # Передаем имя в конструктор Field

class Phone(Field):
    def __init__(self, number):
        if not number.isdigit() or len(number) != 10:
            raise ValueError("Invalid phone number. It must contain only digits and be exactly 10 characters long.")
        super().__init__(number)  # Передаем номер в конструктор Field

class Record:
    def __init__(self, name):
        self.name = Name(name)  # Создаем объект Name для хранения имени
        self.phones = []  # Инициализируем список для хранения номеров телефонов

    def add_phone(self, phone_number):
        """Добавление нового телефона в запись."""
        phone = Phone(phone_number)  # Создаем объект Phone
        self.phones.append(phone)  # Добавляем его в список телефонов

    def remove_phone(self, phone_number):
        """Удаление телефона по номеру."""
        for phone in self.phones:
            if phone.value == phone_number:  # Сравниваем с value
                self.phones.remove(phone)
                return f"Phone number {phone_number} removed."
        return f"Phone number {phone_number} not found."

    def edit_phone(self, old_number, new_number):
        """Редактирование телефона. Заменяем старый номер на новый."""
        for phone in self.phones:
            if phone.value == old_number:  # Сравниваем с value
                phone.value = new_number  # Исправляем номер телефона
                return f"Phone number updated to {new_number}."
        return f"Phone number {old_number} not found."

    def find_phone(self, phone_number):
        """Поиск телефона по номеру."""
        for phone in self.phones:
            if phone.value == phone_number:  # Сравниваем с value
                return f"Phone number {phone_number} found."
        return f"Phone number {phone_number} not found."

    def __str__(self):
        """Возвращаем строковое представление записи (имя и телефоны)."""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    """Класс для хранения всех записей в адресной книге."""
    
    def add_record(self, record):
        """Добавление записи в адресную книгу."""
        self.data[record.name.value] = record  # Добавляем запись в словарь по имени контакта

    def find(self, name):
        """Поиск записи по имени."""
        return self.data.get(name, None)  # Возвращаем запись по имени или None, если не найдено

    def delete(self, name):
        """Удаление записи по имени."""
        if name in self.data:
            del self.data[name]  # Удаляем запись из словаря
            return f"Contact {name} has been removed."
        return f"Contact {name} not found."

# Пример использования:

# Создаем новую адресную книгу
book = AddressBook()

# Создаем запись для Джона
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Добавляем запись Джона в адресную книгу
book.add_record(john_record)

# Создаем и добавляем запись для Джейн
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Выводим все записи в книге
for name, record in book.data.items():
    print(record)

# Поиск и редактирование телефона Джона
john = book.find("John")
if john:
    john.edit_phone("1234567890", "1112223333")
    print(john)  # Вывод: Contact name: John, phones: 1112223333; 5555555555

# Поиск конкретного телефона в записи Джона
found_phone = john.find_phone("5555555555")
print(f"Found phone: {found_phone}")  # Вывод: Found phone: 5555555555

# Удаление записи Джейн
print(book.delete("Jane"))