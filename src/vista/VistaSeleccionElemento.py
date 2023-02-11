from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *


class VistaSeleccionElemento(QDialog):
    #Diálogo para escoger el tipo de elemento que se va a crear

    def __init__(self):
        """
        Constructor del diálogo
        """   
        super().__init__()

        self.setFixedSize(340, 210)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
        self.setModal(True)
        self.setWindowModality(Qt.ApplicationModal)

        self.resultado = ""

        self.widget_dialogo = QListWidget()
        
        distribuidor_dialogo = QGridLayout()
        self.setLayout(distribuidor_dialogo)


        titulo="Crear elemento"

        self.setWindowTitle("Caja de Seguridad - {}".format(titulo))

        etiqueta_mensaje = QLabel("Seleccione el tipo de elemento que desea crear")
        distribuidor_dialogo.addWidget(etiqueta_mensaje, 0, 0)

        #Creación botones de selección

        self.botonLogin = QRadioButton("Login")
        distribuidor_dialogo.addWidget(self.botonLogin, 1, 0)
        self.botonId = QRadioButton("Identificación")
        distribuidor_dialogo.addWidget(self.botonId, 2, 0)
        self.botonTarjeta = QRadioButton("Tarjeta")
        distribuidor_dialogo.addWidget(self.botonTarjeta, 3, 0)
        self.botonSecreto = QRadioButton("Secreto")
        distribuidor_dialogo.addWidget(self.botonSecreto, 4, 0)

        self.botonLogin.setChecked(True)



        #Creación de los botones para guardar o cancelar
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())
        caja_botones.setStyleSheet('''
                QGroupBox{border:none}''')

        self.btn_ok = QPushButton("Ok")
        caja_botones.layout().addWidget(self.btn_ok)
        self.btn_ok.clicked.connect(self.seleccionar)

        self.btn_cancelar = QPushButton("Cancelar")
        caja_botones.layout().addWidget(self.btn_cancelar)
        self.btn_cancelar.clicked.connect(self.cancelar)

        distribuidor_dialogo.addWidget(caja_botones, 5, 0, 1, 2)




    def seleccionar(self):
        """
        Esta función envía la información del boton escogido
        """
        if (self.botonLogin.isChecked()):
            self.resultado = "Login"
        elif (self.botonId.isChecked()):
            self.resultado = "Id"
        elif (self.botonTarjeta.isChecked()):
            self.resultado = "Tarjeta"
        else:
            self.resultado = "Secreto"
        self.close()
        return self.resultado


    def cancelar(self):
        """
        Esta función envía la información de que se ha cancelado la operación
        """   
        self.resultado="Cancelar"
        self.close()
        return self.resultado






