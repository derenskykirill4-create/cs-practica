def parse_record(line: str) -> dict:
    """
    Разбирает строку «город;температура;дата» в словарь.
    Если строка некорректна — возбуждает ValueError.
    """
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")

    city, temp_str, date = parts

    # Проверяем, что город и дата не пустые (после удаления пробелов)
    if not city.strip() or not date.strip():
        raise ValueError("Город и дата не могут быть пустыми данными")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Невозможно преобразовать температуру к числу: '{temp_str}'")

    return {
        "city": city.strip(),
        "temperature": temp,
        "date": date.strip()
    }


