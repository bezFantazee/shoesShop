from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import QPixmap, Qt, QIcon

from python.controllers.AuthController import AuthController


class LoginPage(QWidget):
    def __init__(self, app_window):
        super().__init__()
        #необходимые пременные
        self.app_window = app_window
        #заголовок страницы
        # self.window().setWindowIcon(QIcon(QDir.currentPath() + "/present/images/Icon.ico"))
        self.window().setWindowTitle("Авторизация")
        #основной контейнер

        main_layout  = QVBoxLayout(self)
        self.setStyleSheet("font-family: 'Times New Roman';")
        #заголовок
        image_path = QDir.currentPath() + "/present/images/Icon.ico"
        image_path = image_path.replace("\\", "/")
        shop_image = QPixmap(image_path)
        shop_image_label = QLabel()
        shop_image_label.setFixedSize(80, 80)
        shop_image_label.setPixmap(shop_image.scaled(
            shop_image_label.size(),
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        ))
        main_text = QLabel("Авторизация")
        main_text.setStyleSheet("""
            color: #00FA9A;
            font-size: 48px;
            font-weight: bold;
            font-family: 'Times New Roman';
            margin: 10px;
            qproperty-alignment: AlignCenter;
        """)
        #контейнер для полей ввода
        self.input_container = QWidget() #чтобы можно было работать с ним по всему классу
        self.input_container.setStyleSheet("""
            padding: 24px 40px;
            border: 20px solid #7FFF00;
            border-radius: 30px;
            margin: 10px 20px;
        """)

        self.input_container.setFixedSize(700, 450)
        input_layout = QVBoxLayout(self.input_container)
        #поля ввода
        input1_text = QLabel("Логин")
        input1_text.setStyleSheet("""
            border: none;
            color: #000000;
            font-size: 32px;
            font-family: 'Times New Roman';
        """)
        self.input1 = QLineEdit()
        self.input1.setStyleSheet("""
            QLineEdit{
                color: black;
                font-size: 28px;
                background-color: #FFFFFF;
                border-radius: 15px;
                margin: 0 60px;
                border: 2px solid black;
            }
            QLineEdit::placeholder{
                color: grey;
                font-size: 28px;
            }
        """)
        self.input1.setPlaceholderText("Введите логин...")
        input_layout.addWidget(input1_text)
        input_layout.addWidget(self.input1)
        input2_text = QLabel("Пароль")
        input2_text.setStyleSheet("""
            border: none;
            color: #000000;
            font-size: 32px;
        """)
        self.input2 = QLineEdit()
        self.input2.setStyleSheet("""
            QLineEdit{
                color: black;
                font-size: 28px;
                background-color: #FFFFFF;
                border-radius: 15px;
                margin: 0 60px 30px 60px;
                border: 2px solid black;
            }
            QLineEdit::placeholder{
                color: grey;
                font-size: 28px;
            }
        """)
        self.input2.setPlaceholderText("Введите пароль...")
        input_layout.addWidget(input2_text)
        input_layout.addWidget(self.input2)
        #кнопки Войти как гость и Авторизоваться
        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        btn_guest = QPushButton("Войти как гость")
        btn_guest.setStyleSheet("border: 7px solid #00FA9A; font-size: 21px; color: #00FA9A;")
        btn_guest.setFixedWidth(320)
        btn_guest.clicked.connect(lambda: self.go_to_product(is_authenticated=False, user=None))
        btn_auth = QPushButton("Авторизоваться")
        btn_auth.setStyleSheet("border: 7px solid #00FA9A; font-size: 21px; color: #00FA9A;")
        btn_auth.setFixedWidth(320)
        btn_auth.clicked.connect(self.try_login)
        button_layout.addWidget(btn_guest)
        button_layout.addWidget(btn_auth)

        main_layout.addStretch()
        main_layout.addWidget(shop_image_label,  alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(main_text)
        main_layout.addWidget(self.input_container, alignment=Qt.AlignmentFlag.AlignHCenter)
        main_layout.addLayout(button_layout)
        main_layout.addStretch()

        self.setLayout(main_layout)
    #установка пользователя при авторизации
    def try_login(self):
        login = self.input1.text()
        password = self.input2.text()
        if not login or not password:
            self.show_warning("Необходимо указать логин и пароль")
            return
        # user = Authcontroller().login(login, password)
        # user = AuthController().login("tjde7c@yahoo.com", "YOyhfR")
        user = AuthController().login("uth4iz@mail.com", "2L6KZG")
        if user:
            self.app_window.current_user = user
            self.go_to_product(True, user)
        else:
            self.show_warning("Неверный логин или пароль")
    #оповещение о неверном действии
    def show_warning(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Внимание")
        msg.setText("Авторизация не пройдена")
        msg.setInformativeText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()
    #переход на страницу с продуктами
    def go_to_product(self, is_authenticated, user=None):
        self.app_window.set_page("products", user=user, is_authericated=is_authenticated)
