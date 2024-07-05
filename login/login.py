import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QLabel, QWidget, 
                             QLineEdit, QPushButton, QMessageBox, 
                             QCheckBox)
from PyQt6.QtGui import QFont, QPixmap
from registrar import RegistrarUsuario
from main import mainWindow

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()

    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("login")
        self.generar_formulario()
        self.show()
    
    def generar_formulario(self):
        self.is_logged = False

        user_label = QLabel(self)
        user_label.setText("Ususuario")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,54)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,50)

        password_label = QLabel(self)
        password_label.setText("Password")
        password_label.setFont(QFont("Arial",10))
        password_label.move(20,86)

        self.password_input = QLineEdit(self)
        self.password_input.resize(250,24)
        self.password_input.move(90,82)
        self.password_input.setEchoMode(
            QLineEdit.EchoMode.Password
        )
        self.check_view_password = QCheckBox(self)
        self.check_view_password.setText("ver contrasenia")
        self.check_view_password.move(90,110)
        self.check_view_password.clicked.connect(self.mostrar_contrasenia)

        login_button = QPushButton(self)
        login_button.setText("login")
        login_button.resize(320,34)
        login_button.move(20,140)
        login_button.clicked.connect(self.iniciar_main)

        regisrer_button = QPushButton(self)
        regisrer_button.setText("registrar")
        regisrer_button.resize(320,34)
        regisrer_button.move(20,180)
        regisrer_button.clicked.connect(self.registrar_usuario)

    def mostrar_contrasenia(self):
        if self.check_view_password.isChecked():
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
    
    def iniciar_main(self):
        usuario = []
        usuario_text = "usuario.txt"

        try:
            with open(usuario_text, "r") as z:
                for linea in z:
                    usuario.append(linea.strip("\n"))
            login_informacion = f"{self.user_input.text()},{self.password_input.text()}"
            if login_informacion in usuario:
                QMessageBox.information(self,"inicio de sesion",
                                        "inicio de sesion",
                                        QMessageBox.StandardButton.Ok,
                                        QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.open_main_window()
            
            else:
                QMessageBox.warning(self,"error",
                                    "credenciales incorrectas",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
                QMessageBox.warning(self,"error",
                                    "usuario no registrado",{e},
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
        except Exception as e:
            QMessageBox.warning(self,"error",
                                    "error en nose donde",{e},
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)


    def registrar_usuario(self):
        self.usuario = RegistrarUsuario()
        self.usuario.show()

    def open_main_window(self):
        self.main_window = mainWindow()
        self.main_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec())
