from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QMessageBox
from PyQt6.QtGui import QPixmap

class mainWindow(QWidget):
    
    def __init__(self,):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,500,500)
        self.setWindowTitle("ventana principal")
        self.generar_contenido()

    def generar_contenido(self):
        image = "login/t.png"

        try:
            with open(image):
                image_label = QLabel(self)
                image_label.setPixmap(QPixmap(image))

        except FileNotFoundError:
                QMessageBox.warning(self,"error",
                                    "imagen no encontrada",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
        except Exception:
            QMessageBox.warning(self,"error",
                                    "error en nose donde",
                                    QMessageBox.StandardButton.Close,
                                    QMessageBox.StandardButton.Close)
