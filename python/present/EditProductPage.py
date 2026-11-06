from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import os
import shutil

class EditProductPage(QWidget):
    def __init__(self, app_window):
        super().__init__()
        #необходимые переменные
        self.app_window = app_window
        self.product = None
        self.product_controller = self.app_window.product_controller
        #основные контейнеры
        self.setStyleSheet("""
            font-family: 'Times New Roman';
            font-size: 17px;
        """)
        main_layout = QVBoxLayout(self)
        layout = QHBoxLayout()

        self.page_title = QLabel("")
        self.page_title.setStyleSheet("""
            color: #7FFF00;
            font-size:25px;
        """)

        #картинка
        image_layout = QVBoxLayout()
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_label.setFixedSize(200, 200)
        self.image_label.setScaledContents(True)

        self.file_path = None
        self.upload_image_btn = QPushButton("Загрузка изображения")
        self.upload_image_btn.clicked.connect(self.upload_new_image)
        self.upload_image_btn.setStyleSheet("border: 4px solid #7FFF00; color:#7FFF00; border-radius: 10px;")

        image_layout.addWidget(self.image_label)
        image_layout.addWidget(self.upload_image_btn)
        layout.addLayout(image_layout)
        #описание товара
        self.text_layout = QVBoxLayout()
        self.text_layout.addWidget(self.page_title)
        self.text_id = QLabel()

        text_name = QLabel("Название:")
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("Введите название...")
        text_category = QLabel()
        self.category_edit = QLineEdit()
        text_category = QLabel("Категория:")
        self.category_edit = QComboBox()
        self.category_edit.addItems(self.product_controller.get_all_categories())
        text_description = QLabel("Описание:")
        self.description_edit = QTextEdit()
        self.description_edit.setPlaceholderText("Введите описание...")
        text_manufacturer = QLabel("Производитель:")
        self.manufacturer_edit = QComboBox()
        manufacturers = self.product_controller.get_all_manufacturers()
        self.manufacturer_edit.addItems(manufacturers)
        text_supplier = QLabel("Поставщик:")
        self.supplier_edit = QLineEdit()
        self.supplier_edit.setPlaceholderText("Введите поставщика...")
        text_price = QLabel("Цена:")
        self.price_edit = QLineEdit()
        self.price_edit.setPlaceholderText("Введите цену...")
        text_unit = QLabel("Единица измерения:")
        self.unit_edit = QLineEdit()
        self.unit_edit.setPlaceholderText("Введите единицу измерения...")
        text_count = QLabel("Количество товара на складе:")
        self.count_edit = QLineEdit()
        self.count_edit.setPlaceholderText("Введите количество товара на складе...")
        text_discount = QLabel("Скидка:")
        self.discount_edit = QLineEdit()
        self.discount_edit.setPlaceholderText("Введите скидку...")

        self.text_layout.addWidget(self.text_id)
        self.text_layout.addWidget(text_name)
        self.text_layout.addWidget(self.name_edit)
        self.text_layout.addWidget(text_category)
        self.text_layout.addWidget(self.category_edit)
        self.text_layout.addWidget(text_description)
        self.text_layout.addWidget(self.description_edit)
        self.text_layout.addWidget(text_manufacturer)
        self.text_layout.addWidget(self.manufacturer_edit)
        self.text_layout.addWidget(text_supplier)
        self.text_layout.addWidget(self.supplier_edit)
        self.text_layout.addWidget(text_price)
        self.text_layout.addWidget(self.price_edit)
        self.text_layout.addWidget(text_unit)
        self.text_layout.addWidget(self.unit_edit)
        self.text_layout.addWidget(text_count)
        self.text_layout.addWidget(self.count_edit)
        self.text_layout.addWidget(text_discount)
        self.text_layout.addWidget(self.discount_edit)

        layout.addLayout(self.text_layout)
        main_layout.addLayout(layout)

        #кнопки Сохранить, Отмена, Удалить
        btn_save = QPushButton("Сохранить")
        btn_cancel = QPushButton("Отмена")
        self.btn_delete = QPushButton("Удалить")
        btn_save.clicked.connect(self.save_product)
        btn_save.setStyleSheet("border: 7px solid #00FA9A; color:#00FA9A; border-radius: 10px; font-size: 21px;")
        btn_cancel.clicked.connect(self.canel)
        btn_cancel.setStyleSheet("border: 7px solid #00FA9A; color:#00FA9A; border-radius: 10px; font-size: 21px;")
        self.btn_delete.clicked.connect(self.delete_order)
        self.btn_delete.setStyleSheet("border: 7px solid #00FA9A; color:#00FA9A; border-radius: 10px; font-size: 21px;")

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btn_save)
        btn_layout.addWidget(btn_cancel)
        btn_layout.addWidget(self.btn_delete)
        main_layout.addLayout(btn_layout)

    #устанавливаем уже существующие данные о товаре
    def set_product(self, product):
        self.product = product

        if product.id:
            self.setWindowTitle("Редактирование товара")
            self.page_title.setText("Редактирование товара")
            self.text_id.setText(f"id: {product.id}")
            self.price_edit.setText(f"{product.price:.2f}")
            self.count_edit.setText(str(product.quantity_in_stock))
            self.discount_edit.setText(str(product.discount))
            self.set_image(f"present/images/{product.image}")
            self.name_edit.setText(product.name)
            self.category_edit.setCurrentText(product.category)
            self.description_edit.setText(product.description)
            self.manufacturer_edit.setCurrentText(product.manufacturer)
            self.supplier_edit.setText(product.manufacturer)
            self.unit_edit.setText(product.unit)
            self.btn_delete.setVisible(True)
        else:
            self.setWindowTitle("Добавление товара")
            self.page_title.setText("Добавление товара")
            self.text_id.setText("")
            self.price_edit.setText("")
            self.count_edit.setText("")
            self.discount_edit.setText("")
            self.set_image("")
            self.name_edit.setText("")
            self.category_edit.setCurrentText("")
            self.description_edit.setText("")
            self.manufacturer_edit.setCurrentText("")
            self.supplier_edit.setText("")
            self.unit_edit.setText("")
            self.btn_delete.setVisible(False)

    #КАРТИНКА
    #загрузка изображение добавленного пользователем
    def upload_new_image(self):
        file_dialog = QFileDialog(self)

        filter_str = "Изображения (*.png *.jpg *.jpeg *.gif);;Все файлы (*)"

        source_file_path, _ = file_dialog.getOpenFileName(
            self,
            "Выберете изображение для товара",
            QDir.homePath(),
            filter_str
        )
        self.file_path = self.save_image_to_project(source_file_path)
        self.set_image(self.file_path)

    def save_image_to_project(self, source_path: str):
        if not source_path:
            return None
        destination_dir = "present/images"
        os.makedirs(destination_dir, exist_ok=True)

        file_name = os.path.basename(source_path)
        destination_path = os.path.join(destination_dir, file_name)

        try:
            shutil.copy2(source_path, destination_path)
            return destination_path
        except Exception as e:
            print(f"Ошибка при копировании файла {e}")
            return None

    def delete_image(self, image_name):
        image_dir = 'present/images'

        file_path = os.path.join(image_dir, image_name)
        if os.path.exists(file_path) and image_name not in ['picture.png']:
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Ошибка при удалении файла {file_path}: {e}")

    #установка изображения на экране
    def set_image(self, file_path):
        pixmap = QPixmap(file_path)

        if not pixmap.isNull():
            self.image_label.setPixmap(pixmap)
        else:
            placeholder = QPixmap("present/images/picture.png")
            self.image_label.setPixmap(placeholder)
    #сохраняем товар
    def save_product(self):

        if not self.product:
            self.product = self.product_controller.create_empty_product()

        is_update_operation = self.product.id is not None

        old_image_name = self.product.image

        self.product.name = self.name_edit.text()
        self.product.category = self.category_edit.currentText()
        self.product.description = self.description_edit.toPlainText()
        self.product.supplier = self.manufacturer_edit.currentText()
        self.product.manufacturer = self.supplier_edit.text()
        self.product.unit = self.unit_edit.text()
        if self.file_path: #если пути нет, то будет поставлена заглушка
            self.product.image = os.path.basename(self.file_path)
            print('1',self.product.image)
        if old_image_name and old_image_name != self.product.image:
            self.delete_image(old_image_name)
        try: #валидация данных
            price = float(self.price_edit.text())
            if price<0:
                raise ValueError("Цена не может быть отрицательной")
            self.product.price = price

            count = int(self.count_edit.text())
            if count<0:
                raise ValueError("Количество товара не может быть отрицательным")
            self.product.quantity_in_stock = count

            sale = int(self.discount_edit.text())
            if sale<0:
                raise ValueError("Скидка не может быть отрицательной")
            self.product.discount = sale
        except ValueError as e:
            self.show_warning("Неверный формат данных")
            return
        #сохранение товара в бд
        if is_update_operation:
            self.product_controller.update_product(self.product)
        else:
            self.product_controller.add_product(self.product)
        #обновление данных на страничке с товарами
        product_page = self.app_window.pages.get("products")
        if product_page:
            product_page.update_single_card(self.product)
        #переход на страничку с товарами
        self.app_window.set_page("products")
    #показ оповещения о неправильном формате данных
    def show_warning(self, e):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Внимание")
        msg.setText("Неккоректный ввод данных:")
        msg.setInformativeText(str(e))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    #удаление товара
    def delete_order(self):
        if self.product:
            product_page = self.app_window.pages.get("products")
            if product_page:
                product_page.delete_card(self.product.id)
                res = self.product_controller.delete_product(self.product.id)
                if res is None:
                    self.show_warning("Нельзя удалить товар, который находится в заказах!")
                    return

            self.app_window.set_page("products")
    #отмена действия и преход на страничку с товарами
    def canel(self):
        self.app_window.set_page("products")