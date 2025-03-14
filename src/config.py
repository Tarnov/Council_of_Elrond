import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла (если он есть)
load_dotenv()

class Config:
    """Конфигурационный класс с настройками приложения."""

    # Основные параметры API
    APP_NAME = "Council of Elrond"
    HOST = os.getenv("HOST", "127.0.0.1")  # Читаем из .env или ставим значение по умолчанию
    PORT = int(os.getenv("PORT", 8000))  # Преобразуем в число
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"  # Читаем как булево

    # Настройки CORS (разрешённые источники)
    CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

    # Логирование
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# Экземпляр конфигурации, который можно импортировать в других модулях
config = Config()