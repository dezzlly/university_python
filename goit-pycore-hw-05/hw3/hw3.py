import sys
from collections import defaultdict

# Функція для парсингу рядка логу
def parse_log_line(line: str) -> dict:
    parts = line.split(' ', 3)
    date_time = ' '.join(parts[:2])  # Дата та час
    level = parts[2]  # Рівень логування
    message = parts[3]  # Повідомлення
    return {
        'date_time': date_time,
        'level': level,
        'message': message
    }

# Функція для завантаження логів з файлу
def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line.strip()))
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        sys.exit(1)
    return logs

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'].lower() == level.lower()]

# Функція для підрахунку записів за рівнем
def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return dict(counts)

# Функція для відображення підрахунку записів
def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<20} | {'Кількість'}")
    print("-" * 30)
    for level, count in counts.items():
        print(f"{level:<20} | {count}")

# Основна функція для запуску скрипту
def main():
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до лог-файлу.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    logs = load_logs(file_path)

    # Перевірка на другий аргумент для фільтрації за рівнем
    if len(sys.argv) == 3:
        level = sys.argv[2].lower()
        logs = filter_logs_by_level(logs, level)
        display_log_counts(count_logs_by_level(logs))
        print(f"\nДеталі логів для рівня '{level.upper()}':")
        for log in logs:
            print(f"{log['date_time']} - {log['message']}")
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

if __name__ == "__main__":
    main()
