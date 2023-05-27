def format(input_string, settings_dict):
    """
    Функция принимает входную строку и словарь с настройками и возвращает отформатированную строку.

    Аргументы:
    - input_string (str): Входная строка, содержащая плейсхолдеры для замены.
    - settings_dict (dict): Словарь с настройками, где ключи соответствуют плейсхолдерам в строке.

    Возвращает:
    - formatted_string (str): Отформатированная строка, в которой плейсхолдеры заменены значениями из словаря.

    Пример использования:
        input_string = "Ваши настройки:\n{you_name}"
        settings_dict = {"you_name": "Григорий"}
        formatted_string = format_settings_string(input_string, settings_dict)
        print(formatted_string)
    Ваши настройки:
    Григорий
    """
    formatted_string = input_string.format(**settings_dict)
    return formatted_string

import re

import datetime

def unix_time_to_string(unix_time):
    dt = datetime.datetime.fromtimestamp(unix_time)
    return dt.strftime('%Y-%m-%d %H:%M')

def tagsToString( tags, tagsLocalization ):
    string = ""
    for val in tagsLocalization:
        if val in tags:
            string += tagsLocalization[val] + " "
    return string

def validate_email(email):
    # Паттерн для проверки валидности email
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    # Проверка совпадения паттерна с email
    if re.match(pattern, email):
        return True
    else:
        return False

def getEmoj(country):
    if country == 0:
        return "🇷🇺"
    elif country == 1:
        return "🇺🇲"
    elif country == 2:
        return "🇨🇳"
    else:
        return False