from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, Qt

from python.database.models.Shoe import Shoe


#карточка продукта
class ProductCard(QWidget):
    def __init__(self, product: Shoe):
        super().__init__()
        #нужные переменные
        self.product = product

        #основные контейнеры
        self.setStyleSheet("""
            border: 1px solid black;
            font-family: 'Times New Roman';
        """)
        self.layout = QHBoxLayout(self)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.MinimumExpanding
        )

        #картинка
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(200, 200)
        self.image_label.setScaledContents(True)
        self.set_image(self.product.image)
        self.image_label.setStyleSheet("border: 1px solid black;")

        self.layout.addWidget(self.image_label)

        #ОПИСАНИЕ продукта
        text_wd = QWidget()
        text_wd.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        text_wd.setStyleSheet("border: 1px solid black; padding: 10px; color: black; font-size: 17px;")
        self.text_layout = QVBoxLayout(text_wd)
        self.text_layout.setContentsMargins(0, 0, 0, 0)
        self.text_layout.setSpacing(0)
        #название
        self.product_name = QLabel(f"{product.category} | {product.name}")
        self.product_name.setStyleSheet("color: black; border: none; font-weight: bold;")
        self.product_name.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        #описание
        self.product_description = QLabel(f"Описание товара: {product.description}")
        self.manufacturer = QLabel(f"Производитель: {product.manufacturer}")
        self.supplier = QLabel(f"Поставщик: {product.supplier}")
        self.product_description.setStyleSheet("color: black; border: none;")
        self.product_description.setWordWrap(True)
        self.product_description.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.manufacturer.setStyleSheet("color: black; border: none;")
        self.manufacturer.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.supplier.setStyleSheet("color: black; border: none;")
        self.supplier.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.price_container = QWidget()
        self.price_container.setStyleSheet("border: none; padding: 0px; margin-left: 8px;")
        self.price_container_layout = QVBoxLayout(self.price_container)
        self.price_container_layout.setContentsMargins(0, 0, 0, 0)
        self.price_container_layout.setSpacing(0)
        self.price_container.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )

        self.product_unit = QLabel(f"Единица измерения: {product.unit}")
        self.product_quantity_in_stock = QLabel(f"Количество на складе: {product.quantity_in_stock}")
        self.product_quantity_in_stock.setStyleSheet("color: black; border: none;")
        self.is_empty_stock()
        self.product_quantity_in_stock.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.product_unit.setStyleSheet("color: black; border: none;")
        self.product_unit.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Preferred
        )
        self.text_layout.addWidget(self.product_name)
        self.text_layout.addWidget(self.product_description)
        self.text_layout.addWidget(self.manufacturer)
        self.text_layout.addWidget(self.supplier)
        self.text_layout.addWidget(self.price_container)
        #цена со скидкой
        if self.product.discount>0:
            self.set_sale(self.product.price, self.product.discount)
        else:
            self.current_price_label = QLabel(f"Цена: {product.price:.2f} руб.")
            self.current_price_label.setStyleSheet("color: black; border: none;")
            self.price_container_layout.addWidget(self.current_price_label)

        self.text_layout.addWidget(self.product_unit)
        self.text_layout.addWidget(self.product_quantity_in_stock)
        self.layout.addWidget(text_wd)
        #скидка
        self.sales_layout = QVBoxLayout()
        self.sales = QLabel(f"{product.discount}%")
        self.sales.setFixedWidth(80)
        self.sales.setStyleSheet("""
            color: #000000;
            qproperty-alignment: AlignCenter;
            font-size: 20px;
        """)
        self.is_big_sales() #изменение цвета фона если скидка >15%
        self.sales_layout.addWidget(self.sales)
        self.layout.addLayout(self.sales_layout)

    def is_empty_stock(self):
        if self.product.quantity_in_stock == 0: # изменение отображения в зависимости от количества
            self.product_quantity_in_stock.setStyleSheet("color: blue; border: none;")

    #отрисовка странички
    def set_image(self, image_name, placeholder_path="present/images/picture.png"):
        image_path = QDir.currentPath() + "/present/images/" + image_name
        image_path = image_path.replace("\\", "/")
        if QFileInfo(image_path):
            target_pimax = QPixmap(image_path)
        else:
            target_pimax = QPixmap()

        placeholder_pixmap = None

        if not target_pimax.isNull():
            self.image_label.setPixmap(target_pimax)
        else:
            if QFileInfo(placeholder_path).exists():
                placeholder_pixmap = QPixmap(placeholder_path)
            self.image_label.setPixmap(placeholder_pixmap)


    def set_sale(self, price, sale):
        self.clear_layout(self.price_container_layout)

        new_price = price * (1 - sale/100)

        price_widget = QWidget()
        price_widget.setStyleSheet("border: none;  padding: 0px;")
        price_layout = QHBoxLayout(price_widget)
        price_layout.setSpacing(1)
        price_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        price_layout.setContentsMargins(0, 0, 0, 0)

        price_label = QLabel("Цена:")
        price_label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )
        price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignCenter)
        price_label.setStyleSheet("color: #000000; border: none;")
        old_price_label = QLabel(f"{price:.2f} руб.")
        old_price_label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )
        old_price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignCenter)
        old_price_label.setStyleSheet("""
            border: none;
            color: red;
            text-decoration: line-through;
        """)
        sale_price_label = QLabel(f"{new_price:.2f} руб.")
        sale_price_label.setSizePolicy(
            QSizePolicy.Policy.Maximum,
            QSizePolicy.Policy.Maximum
        )
        sale_price_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignCenter)
        sale_price_label.setStyleSheet("color: #000000; border: none;")
        price_layout.addWidget(price_label)
        price_layout.addWidget(old_price_label)
        price_layout.addWidget(sale_price_label)
        self.price_container_layout.addWidget(price_widget)

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clear_layout(item.layout())

    def is_big_sales(self):
        if(self.product.discount>=15):
            self.sales.setStyleSheet("""
                background-color: #2E8B57;
                color: #000000;
                qproperty-alignment: AlignCenter;
                font-size: 20px;
            """)

    #фильтрация и сортировка
    def matches_filter(self, text: str):
        text = text.strip().lower()
        if not text:
            return True
        search_terms = text.split()

        product_data = (
            self.product.name.lower()+""+
            self.product.description.lower()+""+
            self.product.category.lower()+""+
            self.product.supplier.lower()+""+
            self.product.manufacturer.lower()
        )
        for term in search_terms:
            if term in product_data:
                return True
        return False

    def suppliers_filter(self, manufacturer: str):
        manufacturer = manufacturer.lower()
        return self.product.supplier.lower() == manufacturer

    #обновление карточки
    def refresh_ui(self):
        product = self.product

        self.set_image(product.image)

        self.product_name.setText(f"{product.category} | {product.name}")
        self.product_description.setText(f"Описание товара: {product.description}")
        self.manufacturer.setText(f"Производитель: {product.manufacturer}")
        self.supplier.setText(f"Поставщик: {product.supplier}")
        self.clear_layout(self.price_container_layout)

        if product.discount>0:
            self.set_sale(product.price, product.discount)
        else:
            self.current_price_label = QLabel(f"Цена: {product.price} руб.")
            self.current_price_label.setStyleSheet("color: black; border: none;")
            self.price_container_layout.addWidget(self.current_price_label)
        self.product_unit.setText(f"Единица измерения: {product.unit}")
        self.product_quantity_in_stock.setText(f"Количество на складе: {product.quantity_in_stock}")
        self.is_empty_stock()
        self.sales.setText(f"{product.discount}%")
        self.is_big_sales()
        self.update()


#экран карточек товаров
class ProductPage(QWidget):
    def __init__(self, app_window):
        super().__init__()
        #нужные переменные
        self.app_window = app_window
        self.user = None
        self.cards = []
        self.filtered_cards = []
        self.user_data = None
        product_controller = self.app_window.product_controller
        self.suppliers = product_controller.get_all_suppliers()

        #заголовок страницы
        self.window().setWindowTitle("Каталог товаров")
        #основной контейнер
        self.main_layout = QVBoxLayout(self)
        self.setStyleSheet("font-family: 'Times New Roman';")
        #верхняя часть экрана
        tittle_layout = QHBoxLayout()

        shop_title = QLabel("Каталог товаров")
        shop_title.setStyleSheet("""
            font-size:48px;
            color: #7FFF00;
        """)
        tittle_layout.addWidget(shop_title)
        self.main_layout.addLayout(tittle_layout)

        self.top_layout = QHBoxLayout()
        self.btn_back = QPushButton("Назад")
        self.btn_back.setFixedWidth(100)
        self.btn_back.setStyleSheet("border: 4px solid #7FFF00; color:#7FFF00; border-radius: 10px;")
        self.btn_back.clicked.connect(self.go_back)
        self.top_layout.addWidget(self.btn_back)
        self.top_layout.addStretch()
        self.main_layout.addLayout(self.top_layout)
        #посик сортировка и фильтрация
        self.search_place = QLineEdit()
        self.search_place.setPlaceholderText("Поиск...")
        self.search_place.textChanged.connect(self.update_view)
        self.main_layout.addWidget(self.search_place)

        self.sort_container = QHBoxLayout()
        self.sort_text = QLabel("Сортировать по количеству товара на складе:")
        self.sort_container.addWidget(self.sort_text)
        self.sort_box = QComboBox()
        self.sort_box.addItems([
            "Без сортировки",
            "По возрастанию",
            "По убыванию"
        ])
        self.current_sort = None
        self.sort_box.currentTextChanged.connect(lambda mode: (self.apply_sort(mode), self.update_view()))
        self.sort_container.addWidget(self.sort_box)
        self.main_layout.addLayout(self.sort_container)

        self.filter_container = QHBoxLayout()
        self.filter_text=QLabel("Отфильтровать по поставщику: ")
        self.filter = QComboBox()
        self.filter.addItem("Все поставщики")
        self.filter.addItems(self.suppliers)
        self.current_filter = None
        self.filter.currentTextChanged.connect(lambda mode: (self.apply_filter(mode), self.update_view()))

        self.filter_container.addWidget(self.filter_text)
        self.filter_container.addWidget(self.filter)
        self.main_layout.addLayout(self.filter_container)

        #карточки
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.cards_container = QWidget()
        self.cards_layout = QVBoxLayout()
        self.cards_container.setLayout(self.cards_layout)

        self.load_products(product_controller.get_all_product())
        self.scroll_area.setWidget(self.cards_container)
        self.main_layout.addWidget(self.scroll_area)

        self.update_view()

        #кнопка добавить товар и прейти на станицу заказов
        self.button_layout = QHBoxLayout()

        self.add_product_button = QPushButton("Добавить товар")
        self.add_product_button.clicked.connect(lambda event: self.edit_product_card(event, product=Shoe()))
        self.add_product_button.setStyleSheet("border: 7px solid #00FA9A; font-size: 21px; color:#00FA9A; border-radius: 10px;")
        self.add_product_button.setFixedWidth(300)
        self.button_layout.addWidget(self.add_product_button)

        self.go_orders_page_button = QPushButton("Перейти к заказам")
        self.go_orders_page_button.clicked.connect(self.go_orders_page)
        self.go_orders_page_button.setStyleSheet("border: 7px solid #00FA9A; font-size: 21px; color:#00FA9A; border-radius: 10px;")
        self.go_orders_page_button.setFixedWidth(300)
        self.button_layout.addWidget(self.go_orders_page_button)
        self.main_layout.addLayout(self.button_layout)

        #ставим функционал соответствующий статусу пользователя
        self.setup_ui()

        self.setLayout(self.main_layout)
    #переходы на другие страницы
    def go_orders_page(self):
        self.app_window.set_page("orders", user=self.user)

    def go_back(self):
        self.app_window.set_page("login")

    def edit_product_card(self, event, product=Shoe()):
        self.app_window.set_page("edit_product_card", product=product)

    #установка функционала соответсвующего статусу пользователя
    def set_user(self, user): #запускается MainWindow
        self.user = user
        self.setup_ui()
        if self.user and not self.user_data:
            self.user_data = QLabel(f"{self.user.first_name} {self.user.last_name} {self.user.patronymic}")
            self.user_data.setStyleSheet("font-size: 17px;")
            self.top_layout.addWidget(self.user_data)

    def setup_ui(self):
        if self.user and self.user.status != 'Авторизированный клиент':
            if self.user_data:
                self.user_data.setText(f"{self.user.first_name} {self.user.last_name} {self.user.patronymic}")
            self.search_place.setVisible(True)
            self.sort_text.setVisible(True)
            self.sort_box.setVisible(True)
            self.filter.setVisible(True)
            self.go_orders_page_button.setVisible(True)
            if self.user.status == "Администратор":
                self.add_product_button.setVisible(True)
                for card in self.cards:
                    card.setEnabled(True)
                    card.mousePressEvent = lambda event, p=card.product: self.edit_product_card(event, p)
        else:
            if self.user_data and self.user is None:
                self.user_data.setText("")
            elif self.user_data:
                self.user_data.setText(f"{self.user.first_name} {self.user.last_name} {self.user.patronymic}")
            self.go_orders_page_button.setVisible(False)
            self.search_place.setVisible(False)
            self.sort_text.setVisible(False)
            self.sort_box.setVisible(False)
            self.filter.setVisible(False)
            self.add_product_button.setVisible(False)
            for card in self.cards:
                card.setEnabled(True)
                card.mousePressEvent = self.show_warning
        self.update_view()
    #предупреждение о недопустимом действии
    def show_warning(self, event):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Внимание")
        msg.setText("Выбрано недопустимое действие")
        msg.setInformativeText("Действие недоступно")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()

    #поиск сортировка и фильтрация
    def apply_filter(self, mode): #определяем статус фильтрации
        if mode == "Все поставщики":
            self.current_filter = None
        else:
            self.current_filter = mode

    def apply_sort(self, mode): #определяем статус сортировки

        if mode == "Без сортировки":
            self.current_sort = None
        elif mode == "По возрастанию":
            self.current_sort = False
        elif mode == "По убыванию":
            self.current_sort = True


    def update_view(self):
        text = self.search_place.text().strip().lower()
        #поиск
        if text:
            self.filtered_cards = [c for c in self.cards  if c.matches_filter(text)]
        else:
            self.filtered_cards = self.cards.copy()
        #фильтрация
        if self.current_filter:
            self.filtered_cards = [c for c in self.filtered_cards if c.suppliers_filter(self.current_filter)]
        #сортировка
        if self.current_sort is not None:
            self.filtered_cards.sort(
                key=lambda c: c.product.quantity_in_stock,
                reverse=self.current_sort
            )

        #обновление списка карточек
        while self.cards_layout.count(): #удаление
            item = self.cards_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)

        for card in self.filtered_cards: #добавление
            self.cards_layout.addWidget(card)
            if self.user and self.user.status == 'Администратор':
                card.mousePressEvent = lambda event, p=card.product: self.edit_product_card(event, p)

        self.cards_layout.addStretch()
        self.cards_layout.update()

    #загрузка данных на карточки
    def load_products(self, product_list):
        #удаляем старые данные
        for i in reversed(range(self.cards_layout.count())):
            widget_to_remove = self.cards_layout.itemAt(i).widget()
            if widget_to_remove is not None:
                widget_to_remove.setParent(None)
        self.cards.clear()

        #добавляем новые данные
        for product in product_list:
            card = ProductCard(product)
            self.cards.append(card)
            self.cards_layout.addWidget(card)

        #заполняем свободное место чтобы сместить карточки вверх
        self.cards_layout.addStretch()

    #добавление, обновление и удаление карточек
    def find_card_by_id(self, product_id):
        for card in self.cards:
            if card.product.id == product_id:
                return card
        return None

    def update_single_card(self, updated_product):
        card_to_update = self.find_card_by_id(updated_product.id)
        if card_to_update:
            card_to_update.product = updated_product
            card_to_update.refresh_ui()
        else:
            card = ProductCard(updated_product)
            card.set_image(updated_product.image)
            card.setEnabled(True)
            card.mousePressEvent = lambda event, p=card.product: self.edit_product_card(event, p)
            self.cards.append(card)
            self.update_view()

    def delete_card(self, id_card):
        card_to_delete = self.find_card_by_id(id_card)
        self.cards.remove(card_to_delete)
        self.update_view()




