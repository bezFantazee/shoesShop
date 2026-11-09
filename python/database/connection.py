import configparser
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


DB_CONNECTION_ERROR = (
    "Не удалось подключиться к базе данных. "
    "Проверьте настройки подключения в файле config.ini."
)

CONFIG_PATH = Path(__file__).resolve().parents[2] / "config.ini"

config = configparser.ConfigParser()

if not config.read(CONFIG_PATH, encoding="utf-8"):
    raise FileNotFoundError(
        "Файл конфигурации config.ini не найден. "
        "Создайте его в корне проекта на основе config.ini.example."
    )

db = config["database"]

DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=db["user"],
    password=db["password"],
    host=db["host"],
    port=int(db["port"]),
    database=db["name"]
)

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(bind=engine)


def get_session():
    return SessionLocal()


def check_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        return True
    except Exception:
        print(DB_CONNECTION_ERROR)
        return False