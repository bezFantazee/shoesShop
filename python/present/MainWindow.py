from PySide6.QtWidgets import *
from PySide6.QtCore import *

from python.controllers.OrderController import OrderController
from python.controllers.PickupPointController import PickupPointController
from python.controllers.ProductController import ProductController
from python.present.EditOrderPage import EditOrderPage
from python.present.EditProductPage import EditProductPage
from python.present.LoginPage import LoginPage
from python.present.OrderPage import OrderPage
from python.present.ProductPage import ProductPage
from PySide6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("present/images/Icon.ico"))
        #необходимые переменные
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        self.current_user = None
        self.product_controller = ProductController()
        self.order_controller = OrderController()
        self.pickup_point_controller = PickupPointController()
        #список страниц приложения
        self.pages = {
            "login": LoginPage(self),
            "products": ProductPage(self),
            "edit_product_card": EditProductPage(self),
            "orders": OrderPage(self),
            "edit_order_card": EditOrderPage(self)
        }
        #отрисовка сттраниц
        for page in self.pages.values():
            self.stack.addWidget(page)
        #показ первой странички входа
        self.set_page("login")
    #логика перехода между страничками
    def set_page(self, name, user=None, product=None, order=None, is_authericated=True):
        page = self.pages[name]
        #передача необходимых данных междлу страничками
        if user is not None and hasattr(page, 'set_user'):
            self.current_user = user
            page.set_user(user)
        if not is_authericated and hasattr(page, 'set_user'):
            page.set_user(user)
        if product is not None and hasattr(page, 'set_product'):
            page.set_product(product)
        if order is not None and hasattr(page, 'set_order'):
            page.set_order(order)
        self.stack.setCurrentWidget(page)
        self.setWindowTitle(page.windowTitle())

        if self.window() is not None:
            self.window().setWindowTitle(page.windowTitle())

