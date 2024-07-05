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

        create_button = QPushButton(self)
        create_button.setText("Crear")
        create_button.resize(150,32)
        create_button.move(20,170)
        create_button.clicked.connect(self.crear_usuario)

        cancel_button = QPushButton(self)
        cancel_button.setText("Cancelar")
        cancel_button.resize(150,32)
        cancel_button.move(170,170)
        cancel_button.clicked.connect(self.cancelar_usuario)

    def cancelar_usuario(self):
        self.close()
    
    def crear_usuario(self):
        usuario_text = "usuario.txt"
        usuario = self.user_input.text()
        password1 = self.password_input.text()
        password2 = self.password_2_input.text()

        if password1 == "" or password2 == "" or usuario == "":
            QMessageBox.warning(self,"error",
                                "ingrese datos",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        elif password1 != password2:
            QMessageBox.warning(self,"error",
                                "la contrasenia no es la misma",
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)
        else:
            try:
                with open(usuario_text,"a+") as f:
                    f.write(f"{usuario},{password1}\n")
                QMessageBox.information(self,"creado con exito",
                                        "el usuario se creo con exito",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.close()
                
                
            except FileNotFoundError as e:
                QMessageBox.warning(self,"error",
                                    "ingrese datos",{e},
                                QMessageBox.StandardButton.Close,
                                QMessageBox.StandardButton.Close)