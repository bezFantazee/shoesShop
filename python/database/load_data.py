from python.database.connection import get_session
import pandas as pd
from datetime import datetime

from python.database.models.OrderItem import OrderItem
from python.database.models.PickupPoint import PickupPoint
from python.database.models.Shoe import Shoe
from python.database.models.User import User
from python.database.models.Order import Order


def is_empty_data(table):
    session = get_session()
    if session.query(table).first() is None:
        return True
    else:
        return False

def pickup_address_file():
    df = pd.read_excel("Пункты выдачи_import.xlsx", header=None)

    df.columns = ['address']
    df[['postal_code', 'town', 'street', 'house']] = df["address"].str.split(',', expand=True)
    df[['postal_code', 'town', 'street', 'house']] = df[['postal_code', 'town', 'street', 'house']].apply(lambda col: col.str.strip())
    df['house'] = pd.to_numeric(df['house'], errors='coerce')

    session = get_session()
    try:
        id = 1
        for _, row in df.iterrows():
            point = PickupPoint(
                id=id,
                postal_code=row['postal_code'],
                town=row['town'],
                street=row['street'],
                house=row['house']
            )
            session.add(point)
            id+=1
        session.commit()
    except Exception as e:
        session.rollback()
        print("Ошибка при добавлении пунктов выдачи: {e}")
    finally:
        session.close()


def shoes_file():
    df = pd.read_excel("Tovar.xlsx")
    mapping = {
        "Артикул": "article",
        "Наименование товара": "name",
        "Единица измерения": "unit",
        "Цена": "price",
        "Поставщик": "supplier",
        "Производитель": "manufacturer",
        "Категория товара": "category",
        "Действующая скидка": "discount",
        "Кол-во на складе": "quantity_in_stock",
        "Описание товара": "description",
        "Фото": "image"
    }
    df = df.rename(columns=mapping)

    session = get_session()
    try:
        for _, row in df.iterrows():
            product = Shoe(
                article=row['article'],
                name=row['name'],
                unit=row['unit'],
                price=row['price'],
                supplier=row['supplier'],
                manufacturer=row['manufacturer'],
                category=row['category'],
                discount=row['discount'],
                quantity_in_stock=row['quantity_in_stock'],
                description=row['description'],
                image=row['image']
            )
            session.add(product)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении товаров: {e}")
    finally:
        session.close()

def user_file():
    df = pd.read_excel("user_import.xlsx")

    df[['last_name', 'first_name', 'patronymic']] = df["ФИО"].str.split(' ', expand=True)
    df[['first_name', 'last_name', 'patronymic']] = df[['first_name', 'last_name', 'patronymic']].apply(lambda col: col.str.strip())

    mapping = {
        "Роль сотрудника": "status",
        "Логин": "login",
        "Пароль": "password"
    }
    df = df.rename(columns=mapping)

    session = get_session()
    try:
        for _, row in df.iterrows():
            user = User(
                last_name=row['last_name'],
                first_name=row['first_name'],
                patronymic=row['patronymic'],
                status=row['status'],
                login=row['login'],
                password=row['password']
            )
            session.add(user)
        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Ошибка при добавлении пользователей: {e}")
    finally:
        session.close()


def order_file():
    session = get_session()
    df =  pd.read_excel("Заказ_import.xlsx")

    mapping = {
        "Номер заказа": "order_number",
        "Артикул заказа": "articles",
        "Дата заказа": "order_date",
        "Дата доставки": "delivery_date",
        "Адрес пункта выдачи": "pickup_point_code",
        "ФИО авторизированного клиента": "client_fio",
        "Код для получения": "receive_code",
        "Статус заказа": "status"
    }
    df = df.rename(columns=mapping)

    session = get_session()
    for _, row in df.iterrows():
        client_fio = row['client_fio']
        client = get_client(session, client_fio)
        if client is None:
            print(f"User {client_fio} dont't find")
            continue

        order = Order(
            user_id = client.id,
            receive_code = row["receive_code"],
            status = row["status"],
            pickup_point_code = row["pickup_point_code"],
            order_date=parse_date(row["order_date"]),
            delivery_date=parse_date(row["delivery_date"])
        )
        session.add(order)
        session.flush()

        items = parse_article_quantity(row["articles"])

        for article, qty in items:
            shoe = get_shoe_by_article(session, article)
            if shoe is None:
                print(f"Shoe with article {article} not found")
                continue

            order_item = OrderItem(
                order_number=order.order_number,
                shoe_id=shoe.id,
                quantity=qty
            )
            session.add(order_item)

    session.commit()

def get_shoe_by_article(session,  article):
    return session.query(Shoe).filter(Shoe.article == article).first()

def parse_date(date_str: str):
    if pd.isna(date_str):
        return None
    for fmt in ("%Y-%m-%d %H:%M:%S", "%d.%m.%Y", "%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(str(date_str), fmt).date()
        except ValueError:
            continue

    return None

def get_client(session, client_fio):
    parts = client_fio.strip().split(' ')
    last_name, first_name, patronymic = parts

    return session.query(User).filter(
        User.last_name.ilike(last_name.strip()),
        User.first_name.ilike(first_name.strip()),
        User.patronymic.ilike(patronymic.strip())
    ).first()

def parse_article_quantity(raw_string: str):
    if not raw_string:
        return []
    parts = [p.strip() for p in raw_string.split(',')]
    result = []

    if len(parts) %2 != 0:
        raise ValueError("")

    for i in range(0, len(parts), 2):
        article = parts[i]
        quantity = parts[i+1]
        result.append((article, int(quantity)))

    return result