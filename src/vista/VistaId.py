from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from datetime import datetime


class VistaId(QWidget):
    #Ventana de elemento logitn

    def __init__(self,principal):
        """
        Constructor de la ventana
        """   
        super().__init__()

        self.titulo = 'Caja de seguridad - Identificación'
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz=principal

        self.width = 500
        self.height = 450
        self.inicializar_GUI()
        self.show()
       

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_id = QWidget()
        self.distribuidor_id = QGridLayout()
        self.widget_id.setLayout(self.distribuidor_id)
        self.distribuidor_base.addWidget(self.widget_id, Qt.AlignTop)
        numero_fila = 0

        etiqueta_nombre_elemento=QLabel("Nombre identificación")
        self.distribuidor_id.addWidget(etiqueta_nombre_elemento, numero_fila, 0)

        self.texto_nombre_elemento=QLineEdit(self)
        self.distribuidor_id.addWidget(self.texto_nombre_elemento, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_numero=QLabel("Número")
        self.distribuidor_id.addWidget(etiqueta_numero, numero_fila, 0)

        self.texto_numero=QLineEdit(self)
        self.distribuidor_id.addWidget(self.texto_numero, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_nombre_completo=QLabel("Nombre completo")
        self.distribuidor_id.addWidget(etiqueta_nombre_completo, numero_fila, 0)

        self.texto_nombre_completo=QLineEdit(self)
        self.distribuidor_id.addWidget(self.texto_nombre_completo, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_fnacimiento=QLabel("Fecha nacimiento")
        self.distribuidor_id.addWidget(etiqueta_fnacimiento, numero_fila, 0)

        self.fnacimiento = QDateEdit(self)
        self.fnacimiento.setDisplayFormat("yyyy-MM-dd")
        self.fnacimiento.setDate(datetime.now())
        self.distribuidor_id.addWidget(self.fnacimiento, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_fexpedicion = QLabel("Fecha expedición")
        self.distribuidor_id.addWidget(etiqueta_fexpedicion, numero_fila, 0)

        self.fexpedicion = QDateEdit(self)
        self.fexpedicion.setDisplayFormat("yyyy-MM-dd")
        self.fexpedicion.setDate(datetime.now())
        self.distribuidor_id.addWidget(self.fexpedicion, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_fvencimiento = QLabel("Fecha vencimiento")
        self.distribuidor_id.addWidget(etiqueta_fvencimiento, numero_fila, 0)

        self.fvencimiento = QDateEdit(self)
        self.fvencimiento.setDisplayFormat("yyyy-MM-dd")
        self.fvencimiento.setDate(datetime.now())
        self.distribuidor_id.addWidget(self.fvencimiento, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_notas=QLabel("Notas")
        self.distribuidor_id.addWidget(etiqueta_notas, numero_fila, 0)

        self.texto_notas=QTextEdit(self)
        self.texto_notas.setMinimumHeight(150)
        self.distribuidor_id.addWidget(self.texto_notas, numero_fila, 1)
        numero_fila = numero_fila + 1

        #Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

       #Creación de los botones con las diferentes operaciones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(120, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_botones.addWidget(self.btn_volver, 0, 0, Qt.AlignCenter)
        self.btn_volver.clicked.connect(self.volver)

        self.btn_guardar_id = QPushButton("Guardar id", self)
        self.btn_guardar_id.setFixedSize(120, 40)
        self.btn_guardar_id.setToolTip("Guardar id")
        self.btn_guardar_id.setIcon(QIcon("src/recursos/floppy-disk.png"))
        self.distribuidor_botones.addWidget(self.btn_guardar_id, 0, 2, Qt.AlignCenter)
        self.btn_guardar_id.clicked.connect(self.guardar_cambios)

    def mostrar_id(self, elemento):
        self.elemento=elemento
        if (self.elemento!=None):
            self.texto_nombre_elemento.setText(self.elemento["nombre_elemento"])
            self.texto_numero.setText(self.elemento["numero"])
            self.texto_nombre_completo.setText(self.elemento["nombre"])
            self.fnacimiento.setDate(QtCore.QDate.fromString(str(self.elemento["fecha_nacimiento"]), "yyyy-MM-dd"))
            self.fvencimiento.setDate(QtCore.QDate.fromString(str(self.elemento["fecha_venc"]), "yyyy-MM-dd"))
            self.fexpedicion.setDate(QtCore.QDate.fromString(str(self.elemento["fecha_exp"]), "yyyy-MM-dd"))
            self.texto_notas.setText(str(self.elemento["notas"]))

    def volver(self):
        """
        Esta función permite volver a la lista de elementos
        """    
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()

    def guardar_cambios(self):
        """
        Esta función guarda los cambios al elemento tipo id (editando o guardando los nuevos id)
        """
        resultado = self.interfaz.guardar_id(self.texto_nombre_elemento.text(), self.texto_numero.text(), self.texto_nombre_completo.text(),\
                                              self.fnacimiento.text(),self.fexpedicion.text(),self.fvencimiento.text(), self.texto_notas.toPlainText())
        if resultado == "":
            self.hide()
            self.interfaz.mostrar_vista_lista_elementos()
        else:
            self.error_id(resultado)
    
    def error_id(self, error):
        mensaje_error=QMessageBox()
        mensaje_error.setIcon(QMessageBox.Question)
        mensaje_error.setText("Error: " + error)
        mensaje_error.setWindowTitle("Error al guardar")
        mensaje_error.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
        mensaje_error.setStandardButtons(QMessageBox.Ok ) 
        respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()
        event.accept()

