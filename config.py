import os

BOT_TKN = os.environ.get("BOT_TOKEN")  # Получение значения переменной среды BOT_TOKEN
BASE_URL_BACKEND = os.environ.get("BASE_URL_BACKEND")  # Получение значения переменной среды BASE_URL_BACKEND
ANALYTICS_URL_BACKED = os.environ.get("ANALYTICS_URL_BACKEND")

if BOT_TKN:
    print("Значение переменной BOT_TOKEN:", BOT_TKN)
else:
    print("Переменная BOT_TOKEN не установлена.")