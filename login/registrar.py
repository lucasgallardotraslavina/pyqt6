from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QDialog, QLabel, QPushButton, QLineEdit, QMessageBox, QWidget)
from PyQt6.QtGui import QFont

class RegistrarUsuario(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()

    def generar_formulario(self):
        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle("registrar")

        user_label = QLabel(self)
        user_label.setText("Ususuario")
        user_label.setFont(QFont("Arial", 10))
        user_label.move(20, 44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250, 24)
        self.user_input.move(90, 40)

        password_label = QLabel(self)
        password_label.setText("password:")
        password_label.setFont(QFont("Arial", 10))
        password_label.move(20, 74)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250, 24)
        self.password_input.move(90, 70)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        password_2_label = QLabel(self)
        password_2_label.setText("password:")
        password_2_label.setFont(QFont("Arial", 10))
        password_2_label.move(20, 104)

        self.password_2_input = QLineEdit(self)
        self.password_2_input.resize(250, 24)
        self.password_2_input.move(90, 100)
        self.password_2_input.setEchoMode(QLineEdit.EchoMode.Password)
