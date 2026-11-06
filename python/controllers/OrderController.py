from python.database.connection import get_session, engine
from python.database.models.Order import Order
from python.database.models.OrderItem import OrderItem
from python.database.models.PickupPoint import PickupPoint
from python.database.models.Shoe import Shoe


class OrderController:
    def __init__(self):
        self.session = get_session()

    def get_all_orders(self):
        orders = self.session.query(Order).all()
        return orders

    def get_ids(self, order: Order):
        return [item.shoe_id for item in order.order_items]

    def get_pickup_point_address(self, pickup_point: PickupPoint):
        return f"{pickup_point.town} {pickup_point.street} {pickup_point.house}"

    def set_articles(self, articles: str):
        article_list = [x.strip() for x in articles.split(",")]

        if article_list is None:
            return False

        for article  in article_list:
            shoe = self.session.query(Shoe).filter(Shoe.article == article).first()
            if shoe is None:
                return False

        return True

    def add_order(self, new_data: dict, new_articles: str):
        from sqlalchemy.exc import SQLAlchemyError
        new_order = Order(
            order_date=new_data['order_date'],
            delivery_date=new_data['delivery_date'],
            status=new_data['status'],
            pickup_point_code=new_data['pickup_point_id'],
            user_id=new_data['user_id']
        )
        article_list = [x.strip() for x in new_articles.split(",")]

        new_order_items = []

        if article_list:
            shoes = {
                sh.article: sh
                for sh in self.session.query(Shoe).filter(Shoe.article.in_(article_list)).all()
            }

            missing = [a for a in article_list if a not in shoes]
            if missing:
                raise ValueError(f"Товары с артикулом(ами) не найдены: {missing}")

            for art in article_list:
                shoe = shoes[art]
                item = OrderItem(
                    order_number=new_order.order_date,
                    shoe_id=shoe.id,
                    quantity=1
                )
                new_order_items.append(item)

        new_order.order_items.extend(new_order_items)

        try:
            self.session.add(new_order)
            self.session.flush()
            self.session.commit()

            return new_order

        except SQLAlchemyError as e:
            self.session.rollback()
            print("SQLAlchemyError:", e)
            raise

    def update_order(self, order_number: int, new_data: dict, new_articles: str):
        from sqlalchemy.exc import SQLAlchemyError

        order = self.session.get(Order, order_number)
        if not order:
            raise ValueError("Order not found")

        simple_fields = [c.name for c in Order.__table__.columns if c.name != "order_number"]
        for key, val in new_data.items():
            if key in simple_fields:
                setattr(order, key, val)

        article_list = [x.strip() for x in new_articles.split(",")]

        new_items = []
        for art in article_list:
            shoe = self.session.query(Shoe).filter_by(article=art).one_or_none()

            if shoe is None:
                raise ValueError(f"Shoe with article {art} not found")

            item = OrderItem(order_number=order.order_number, shoe_id=shoe.id, quantity=1)
            new_items.append(item)

        try:
            order.order_items[:] = new_items

            self.session.flush()
            self.session.commit()
            return order

        except SQLAlchemyError:
            self.session.rollback()
            raise

    def delete_order(self, order_number: int):
        order = self.session.query(Order).get(order_number)
        if not order:
            raise Exception("Product not found")

        self.session.delete(order)
        self.session.commit()