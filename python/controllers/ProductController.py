from sqlalchemy import select
from python.database.connection import get_session
from python.database.models.Shoe import Shoe

class ProductController:
    def __init__(self):
        self.session = get_session()

    def get_all_product(self):
        return self.session.query(Shoe).all()

    def get_all_suppliers(self):
        stmt = select(Shoe.supplier).distinct()
        return self.session.execute(stmt).scalars().all()

    def get_all_categories(self):
        stmt = select(Shoe.category).distinct()
        return self.session.execute(stmt).scalars().all()

    def get_all_manufacturers(self):
        stmt = select(Shoe.manufacturer).distinct()
        return self.session.execute(stmt).scalars().all()

    def get_articles_by_ids(self, ids):
        shoes = (self.session.query(Shoe.article).filter(Shoe.id.in_(ids)).all())
        return [s.article for s in shoes]

    def create_empty_product(self):
        return Shoe()

    # def add_product(self, new_product: Shoe):
    #     self.session.add(new_product)
    #     self.session.commit()

    def add_product(self, new_product: Shoe):
        if not new_product.article or new_product.article in ('Не определен', ''):
            last_article_obj = self.session.query(Shoe.article) \
                .filter(Shoe.article != 'Не определен') \
                .order_by(Shoe.id.desc()) \
                .first()

            if last_article_obj:
                last_article = last_article_obj[0]

                digits = ''
                for char in reversed(last_article):
                    if char.isdigit():
                        digits = char + digits
                    else:
                        break

                if digits:
                    new_number = int(digits) + 1
                    base = last_article[:-len(digits)]
                    new_product.article = base + str(new_number)
                else:
                    new_product.article = last_article + "1"
            else:
                new_product.article = "F635R4"

        self.session.add(new_product)
        self.session.commit()

    def update_product(self, product_to_update: Shoe):
        product = self.session.query(Shoe).get(product_to_update.id)
        if not product:
            self.add_product(product_to_update)
            return

        for attr in Shoe.__table__.columns.keys():
            if attr != 'article':
                setattr(product, attr, getattr(product_to_update, attr))

        self.session.commit()

    def delete_product(self, product_id: int):
        product = self.session.query(Shoe).get(product_id)
        if not product:
            raise Exception("Product not found")

        if product.order_items:
            return None
        self.session.delete(product)
        self.session.commit()
        return True

