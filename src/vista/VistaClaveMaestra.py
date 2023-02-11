from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class VistaClaveMaestra(QDialog):
    # Ventana clave maestra

    def __init__(self, principal):
        """
        Constructor de la ventana
        """
        super().__init__()

        self.titulo = 'Clave maestra'
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz = principal

        self.width = 400
        self.height = 150
        self.inicializar_GUI()
        self.show()

    def inicializar_GUI(self):
        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_clave = QWidget()
        self.distribuidor_clave = QGridLayout()
        self.widget_clave.setLayout(self.distribuidor_clave)
        self.distribuidor_base.addWidget(self.widget_clave, Qt.AlignTop)
        numero_fila = 0

        etiqueta_clave = QLabel("Ingrese la clave maestra")
        self.distribuidor_clave.addWidget(etiqueta_clave, numero_fila, 0)

        self.texto_clave = QLineEdit(self)
        self.texto_clave.setEchoMode(QLineEdit.Password)
        self.distribuidor_clave.addWidget(self.texto_clave, numero_fila, 1)
        numero_fila + 1

        # Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

        # Creación de los botones con las diferentes operaciones
        self.btn_ok = QPushButton("Confirmar", self)
        self.btn_ok.setFixedSize(120, 40)
        self.btn_ok.setToolTip("Confirmar")
        self.btn_ok.setDefault(True)
        self.distribuidor_botones.addWidget(self.btn_ok, 0, 0, Qt.AlignCenter)
        self.btn_ok.clicked.connect(self.verificar_clave)

    def mostrar_clave(self, clave):
        self.clave = clave
        self.texto_clave.setText('')

    def verificar_clave(self):
        """
        Esta función permite verificar la clave
        """
        if (self.clave == self.texto_clave.text()):
            self.hide()
            self.interfaz.mostrar_vista_lista_elementos()
        else:
            self.error_clave()

    def error_clave(self):
        mensaje_error = QMessageBox()
        mensaje_error.setIcon(QMessageBox.Question)
        mensaje_error.setText("Verifique la clave maestra.")
        mensaje_error.setWindowTitle("Error clave maesra")
        mensaje_error.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
        mensaje_error.setStandardButtons(QMessageBox.Ok)
        respuesta = mensaje_error.exec_()
