import configparser
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


# Путь к config.ini в корне проекта
CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.ini"

# Чтение конфигурации
config = configparser.ConfigParser()

if not config.read(CONFIG_PATH, encoding="utf-8"):
    raise FileNotFoundError(
        f"Файл конфигурации не найден: {CONFIG_PATH}"
    )

db = config["database"]

# Формирование адреса подключения
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=db["user"],
    password=db["password"],
    host=db["host"],
    port=int(db["port"]),
    database=db["name"]
)

# Создание подключения к базе данных
engine = create_engine(DATABASE_URL, echo=False)

# Создание фабрики сессий
SessionLocal = sessionmaker(bind=engine)


def get_session():
    return SessionLocal()

def check_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        print(
            "Не удалось подключиться к базе данных. "
            "Проверьте настройки подключения в файле config.ini."
        )
        return False