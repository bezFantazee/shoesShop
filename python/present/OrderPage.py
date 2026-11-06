from PySide6.QtWidgets import *

from python.database.models.Order import Order

#карточка товара
class OrderCard(QWidget):
    def __init__(self, order: Order, app_window):
        super().__init__()
        #необходимые пременные
        self.order = order
        self.app_window = app_window
        self.order_controller = self.app_window.order_controller
        #установка основных контейнеров
        self.setStyleSheet("border: 1px solid black;")
        self.layout = QHBoxLayout(self)

        #описание заказа
        self.text_layout = QVBoxLayout()
        ids = self.order_controller.get_ids(order)
        articles = self.app_window.product_controller.get_articles_by_ids(ids)
        self.order_name = QLabel(f"Артикул заказа: {", ".join(articles)}")
        self.order_name.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.order_name.setStyleSheet("padding: 2px 5px; color: black; font-size: 17px;")
        pickup_point = self.app_window.pickup_point_controller.get_pickup_point_by_id(self.order.pickup_point_code)
        self.order_description = QLabel(f"Статус заказа: {order.status}\n"
                                        f"Адрес пункта выдачи(текст): {self.order_controller.get_pickup_point_address(pickup_point)}\n"
                                        f"Дата заказа: {order.order_date}")

        self.order_description.setStyleSheet("color: #000000; font-size: 17px;")
        self.order_description.setWordWrap(True)
        self.order_description.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.text_layout.addWidget(self.order_name)
        self.text_layout.addWidget(self.order_description)
        self.layout.addLayout(self.text_layout)
        #дата доставки
        self.del_order_layout = QVBoxLayout()
        self.del_order = QLabel(f"{order.delivery_date}")
        self.del_order.setFixedWidth(100)
        self.del_order.setStyleSheet("""
            color: #000000;
            qproperty-alignment: AlignCenter;
            font-size: 17px;
        """)
        self.del_order_layout.addWidget(self.del_order)
        self.layout.addLayout(self.del_order_layout)

        # self.setMinimumSize(200, 100)
    #обновление данных на карточке
    def refresh_ui(self):
        order = self.order
        ids = self.order_controller.get_ids(order)
        articles = self.app_window.product_controller.get_articles_by_ids(ids)
        self.order_name.setText(f"Артикул: {", ".join(articles)}")
        pickup_point = self.app_window.pickup_point_controller.get_pickup_point_by_id(self.order.pickup_point_code)
        self.order_description.setText(f"Статус заказа: {order.status}\n"
                                        f"Адрес пункта выдачи(текст): {self.order_controller.get_pickup_point_address(pickup_point)}\n"
                                        f"Дата заказа: {order.order_date}")

        self.del_order.setText(f"{order.delivery_date}")
        self.update()

#страница с карточками заказов
class OrderPage(QWidget):
    def __init__(self, app_window):
        super().__init__()
        #необходимые пременные
        self.app_window = app_window
        self.user = None
        self.order_controller = self.app_window.order_controller
        self.cards = []
        self.user_data = None

        #заголовок страницы
        self.window().setWindowTitle("Каталог заказов")
        #основной контейнер
        self.setStyleSheet("""
            font-family: 'Times New Roman';
        """)
        self.setWindowTitle("Каталог заказов")
        self.main_layout = QVBoxLayout(self)
        #верхняя часть экрана
        tittle_layout = QHBoxLayout()
        shop_title = QLabel("Каталог заказов")
        shop_title.setStyleSheet("""
            font-size:48px;
            color: #7FFF00;
        """)
        tittle_layout.addWidget(shop_title)
        self.main_layout.addLayout(tittle_layout)

        self.top_layout = QHBoxLayout()
        self.btn_back = QPushButton("Назад")
        self.btn_back.setFixedWidth(100)
        self.btn_back.setStyleSheet("border: 4px solid #7FFF00; color: #7FFF00; border-radius: 10px;")
        self.btn_back.clicked.connect(self.go_back)
        self.top_layout.addWidget(self.btn_back)
        self.top_layout.addStretch()
        self.main_layout.addLayout(self.top_layout)

        #карточки
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.cards_container = QWidget()
        self.cards_layout = QVBoxLayout()
        self.cards_container.setLayout(self.cards_layout)

        self.load_orders(self.order_controller.get_all_orders())
        self.scroll_area.setWidget(self.cards_container)
        self.main_layout.addWidget(self.scroll_area)

        self.update_view()

        #кнопка добавить и удалить заказ
        self.add_order_button = QPushButton("Добавить заказ")
        self.add_order_button.clicked.connect(lambda event: self.edit_order_card(event, order=Order()))
        self.add_order_button.setStyleSheet("border: 7px solid #00FA9A; font-size: 21px; color:#00FA9A; border-radius: 10px;")
        self.add_order_button.setFixedWidth(300)
        self.main_layout.addWidget(self.add_order_button)

        self.setLayout(self.main_layout)

    #переходы на страницы
    def go_back(self):
        self.app_window.set_page("products")

    def edit_order_card(self, event, order=Order()):
        self.app_window.set_page("edit_order_card", order=order)

    #установка функционала соответсвующего статусу пользователя
    def set_user(self, user):  #запускается MainWindow
        self.user = user
        self.setup_ui()
        if not self.user_data:
            self.user_data = QLabel(f"{self.user.first_name} {self.user.last_name} {self.user.patronymic}")
            self.user_data.setStyleSheet("font-size: 17px;")
            self.top_layout.addWidget(self.user_data)

    def setup_ui(self):
        if self.user.status == "Администратор":
            self.add_order_button.setVisible(True)
            for card in self.cards:
                card.setEnabled(True)
                card.mousePressEvent = lambda event, p=card.order: self.edit_order_card(event, p)
        else:
            self.add_order_button.setVisible(False)
            for card in self.cards:
                card.setEnabled(True)
                card.mousePressEvent = self.show_warning

    #преедупреждение о недопустимом действии
    def show_warning(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Внимание")
        msg.setText("Выбрано недопустимое действие")
        msg.setInformativeText("Действие недоступно")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    #обновление данных после добавления или удаления заказа
    def update_view(self):
        #Удаление всех существующих виджетов из макета
        while self.cards_layout.count():
            item = self.cards_layout.takeAt(0)
            widget = item.widget()

            # Освобождаем виджет
            if widget is not None:
                widget.setParent(None)

        # Добавление всех карточек из основного списка обратно в макет
        for card in self.cards:
            self.cards_layout.addWidget(card)

        # Добавление растягивающего элемента, чтобы прижать карточки к верху
        self.cards_layout.addStretch()

        # Принудительное обновление макета
        self.cards_layout.update()

    #загружаем данные на карточки
    def load_orders(self, order_list):
        #удаляем старые данные
        for i in reversed(range(self.cards_layout.count())):
            widget_to_remove = self.cards_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)
        self.cards.clear()

        #добавляем новые данные
        for order in order_list:
            card = OrderCard(order, self.app_window)
            self.cards.append(card)
            card.mousePressEvent = lambda event, r=card.order: self.edit_order_card(event, r)
            self.cards_layout.addWidget(card)

        #заполняем свободное место чтобы сместить карточки вверх
        self.cards_layout.addStretch()

    #обновление, добавление и кдаление карточек
    def find_card_by_id(self, order_id):
        for card in self.cards:
            if card.order.order_number == order_id:
                return card
        return None

    def update_single_card(self, updated_order):
        card_to_update = self.find_card_by_id(updated_order.order_number)
        if card_to_update:
            card_to_update.order = updated_order
            card_to_update.refresh_ui()
        else:
            card = OrderCard(updated_order, self.app_window)
            card.mousePressEvent = lambda event, r=card.order: self.edit_order_card(event, r)
            self.cards_layout.addWidget(card)
            self.cards.append(card)
            self.update_view()

    def delete_card(self, id_card):
        card_to_delete = self.find_card_by_id(id_card)
        self.cards.remove(card_to_delete)
        self.update_view()






