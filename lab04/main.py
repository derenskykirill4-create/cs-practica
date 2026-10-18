import sys
from stats import average_by_city, read_valid, warmest_city, parse_record


def main():
    # Читаем все строки из стандартного ввода
    lines = sys.stdin.read().splitlines()

    # Подсчитываем строки с ошибками (исключая пустые)
    errors_count = 0
    for line in lines:
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            errors_count += 1

    # Получаем только корректные записи
    valid_records = read_valid(lines)

    # Вычисляем аналитику
    averages = average_by_city(valid_records)
    best_city = warmest_city(valid_records)

    # Определяем среднюю температуру самого теплого города (0.0 если данных нет)
    best_temp = averages.get(best_city, 0.0)

    # Вывод строго 3 строк по ТЗ
    print(len(valid_records))
    print(errors_count)
    print(f"{best_temp:.1f}")


if __name__ == "__main__":
    main()
