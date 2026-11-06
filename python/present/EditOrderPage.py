from datetime import datetime

from PySide6.QtWidgets import *
from PySide6.QtCore import QDate

from python.database.models.Order import Order


class EditOrderPage(QWidget):
    def __init__(self, app_window):
        super().__init__()
        #необходимые пременные
        self.app_window = app_window
        self.order = None
        self.order_controller = self.app_window.order_controller
        #основной контейнер

        self.setStyleSheet("""
            font-family: 'Times New Roman';
            font-size: 17px;
        """)
        layout = QVBoxLayout(self)

        self.page_title = QLabel("")
        self.page_title.setStyleSheet("""
            font-size:25px;
            color: #7FFF00;
        """)
        layout.addWidget(self.page_title)
        #описание заказа
        text_article = QLabel("Артикул:")
        self.article_edit = QLineEdit()
        self.article_edit.setPlaceholderText("Ввесдите артикул...")
        text_status = QLabel("Статус заказа:")
        self.status = QComboBox()
        self.status.addItems([
            "Завершен",
            "Новый"
        ])
        text_address = QLabel("Адрес пункта выдачи(текст):")
        self.address_edit = QLineEdit()
        self.address_edit.setPlaceholderText("Введите адрес пункта выдачи(текст)...")
        text_order_date = QLabel("Дата заказа:")
        self.order_date_edit = QDateEdit()
        self.order_date_edit.setDisplayFormat('yyyy-MM-dd')
        self.order_date_edit.setDate(QDate.currentDate())
        self.order_date_edit.setCalendarPopup(True)
        text_delivery_date = QLabel("Дата доставки:")
        self.delivery_date_edit = QDateEdit()
        self.delivery_date_edit.setDisplayFormat('yyyy-MM-dd')
        self.delivery_date_edit.setDate(QDate.currentDate())
        self.delivery_date_edit.setCalendarPopup(True)

        layout.addWidget(text_article)
        layout.addWidget(self.article_edit)
        layout.addWidget(text_status)
        layout.addWidget(self.status)
        layout.addWidget(text_address)
        layout.addWidget(self.address_edit)
        layout.addWidget(text_order_date)
        layout.addWidget(self.order_date_edit)
        layout.addWidget(text_delivery_date)
        layout.addWidget(self.delivery_date_edit)

        #кнопки Сохранить, Отмеена, Удалить
        btn_save = QPushButton("Сохранить")
        btn_cancel = QPushButton("Отмена")
        self.btn_delete = QPushButton("Удалить")
        btn_save.clicked.connect(self.save_order)
        btn_save.setStyleSheet("border: 7px solid #00FA9A; color:#00FA9A; border-radius: 10px; font-size: 21px;")
        btn_cancel.clicked.connect(self.canel)
        btn_cancel.setStyleSheet("border: 7px solid #00FA9A; color:#00FA9A; border-radius: 10px; font-size: 21px;")
        self.btn_delete.clicked.connect(self.delete_order)
        self.btn_delete.setStyleSheet("border: 7px solid #00FA9A; color:#00FA9A; border-radius: 10px; font-size: 21px;")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(self.btn_delete)
        layout.addLayout(btn_layout)

    #загружаем имеющиеся данные о заказе
    def set_order(self, order: Order):
        self.order = order
        if self.order.order_number:
            self.setWindowTitle("Редактирование заказа")
            self.page_title.setText("Редактирование заказа")
            self.order_date_edit.setDate(order.order_date)
            ids = self.order_controller.get_ids(order)
            articles = self.app_window.product_controller.get_articles_by_ids(ids)
            self.article_edit.setText(", ".join(articles))
            self.delivery_date_edit.setDate(order.delivery_date)
            pickup_point = self.app_window.pickup_point_controller.get_pickup_point_by_id(self.order.pickup_point_code)
            self.address_edit.setText(self.order_controller.get_pickup_point_address(pickup_point))
            self.status.setCurrentText(order.status)
            self.btn_delete.setVisible(True)
        else:
            self.setWindowTitle("Добавление заказа")
            self.page_title.setText("Добавление заказа")
            self.order_date_edit.setDate(QDate.currentDate())
            self.article_edit.setText("")
            self.delivery_date_edit.setDate(QDate.currentDate())
            self.address_edit.setText("")
            self.status.setCurrentText("Новый")
            self.btn_delete.setVisible(False)

    #сохраняем введенные данные о заказе
    def save_order(self):
        is_update_operation = self.order.order_number is not None


        articles = self.article_edit.text()
        ans = self.order_controller.set_articles(articles)
        if not ans:
            self.show_warning("Указан несуществуюший артикул")
            return
        # 1. Формируем словарь данных
        data = {
            "status": self.status.currentText(),
            "delivery_date": datetime.strptime(self.delivery_date_edit.text(), "%Y-%m-%d").date(),
            "order_date": datetime.strptime(self.order_date_edit.text(), "%Y-%m-%d").date(),
            "user_id": self.app_window.current_user.id,
            "receive_code": self.order.receive_code,
        }

        pickup_point_id = self.app_window.pickup_point_controller.get_id_by_address(self.address_edit.text())
        if pickup_point_id is None:
            self.show_warning("Указан несуществуюший адрес(возможно стоит убрать запятые)")
            return
        data['pickup_point_id']=pickup_point_id

        # Вызываем контроллер
        if is_update_operation:
            self.order = self.order_controller.update_order(
                order_number=self.order.order_number,
                new_data=data,
                new_articles=articles,
            )
        else:
            self.order = self.order_controller.add_order(
                new_data=data,
                new_articles=articles

            )

        # Обновление карточки в UI
        order_page = self.app_window.pages.get("orders")
        if order_page:
            order_page.update_single_card(self.order)

        #Переход на страницу заказов
        self.app_window.set_page("orders")

    def show_warning(self, e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Внимание")
        msg.setText("Неккоректный ввод данных:")
        msg.setInformativeText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    #удаление заказа
    def delete_order(self):
        if self.order:
            order_page = self.app_window.pages.get("orders")
            if order_page:
                order_page.delete_card(self.order.order_number)
                self.order_controller.delete_order(self.order.order_number)

            self.app_window.set_page("orders")
    #отмена действия и переход страничку с заками
    def canel(self):
        self.app_window.set_page("orders")