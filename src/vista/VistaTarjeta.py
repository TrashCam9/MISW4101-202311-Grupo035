from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from functools import partial
from datetime import datetime


class VistaTarjeta(QWidget):
    #Ventana de elemento logitn

    def __init__(self,principal, claves):
        """
        Constructor de la ventana
        """   
        super().__init__()

        self.titulo = 'Caja de seguridad - Tarjeta'
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz=principal
        self.claves = claves

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

        self.widget_tarjeta = QWidget()
        self.distribuidor_tarjeta = QGridLayout()
        self.widget_tarjeta.setLayout(self.distribuidor_tarjeta)
        self.distribuidor_base.addWidget(self.widget_tarjeta, Qt.AlignTop)
        numero_fila = 0

        etiqueta_nombre_elemento=QLabel("Nombre tarjeta")
        self.distribuidor_tarjeta.addWidget(etiqueta_nombre_elemento, numero_fila, 0)

        self.texto_nombre_elemento=QLineEdit(self)
        self.distribuidor_tarjeta.addWidget(self.texto_nombre_elemento, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_numero=QLabel("Número")
        self.distribuidor_tarjeta.addWidget(etiqueta_numero, numero_fila, 0)

        self.texto_numero=QLineEdit(self)
        self.distribuidor_tarjeta.addWidget(self.texto_numero, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_titular=QLabel("Titular")
        self.distribuidor_tarjeta.addWidget(etiqueta_titular, numero_fila, 0)

        self.texto_titular=QLineEdit(self)
        self.distribuidor_tarjeta.addWidget(self.texto_titular, numero_fila, 1)
        numero_fila=numero_fila+1


        etiqueta_fvencimiento = QLabel("Fecha vencimiento")
        self.distribuidor_tarjeta.addWidget(etiqueta_fvencimiento, numero_fila, 0)

        self.fvencimiento = QDateEdit(self)
        self.fvencimiento.setDisplayFormat("yyyy-MM-dd")
        self.fvencimiento.setDate(datetime.now())
        self.distribuidor_tarjeta.addWidget(self.fvencimiento, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_ccv = QLabel("Código de seguridad(CCV)")
        self.distribuidor_tarjeta.addWidget(etiqueta_ccv, numero_fila, 0)

        self.texto_ccv = QLineEdit(self)
        self.distribuidor_tarjeta.addWidget(self.texto_ccv, numero_fila, 1)
        numero_fila = numero_fila + 1


        etiqueta_clave = QLabel("Clave favorita")
        self.distribuidor_tarjeta.addWidget(etiqueta_clave, numero_fila, 0)

        self.combobox_claves = QComboBox(self)
        for clave in self.claves:
            self.combobox_claves.addItem(clave["nombre"])
        self.combobox_claves.setCurrentIndex(0)
        self.distribuidor_tarjeta.addWidget(self.combobox_claves, numero_fila, 1, 1, 2)

        btn_ver_clave = QPushButton("", self)
        btn_ver_clave.setToolTip("Ver clave")
        btn_ver_clave.setFixedSize(40, 40)
        btn_ver_clave.setIcon(QIcon("src/recursos/002-eye-variant-with-enlarged-pupil.png"))
        btn_ver_clave.clicked.connect(partial(self.mostrar_clave_favorita))
        self.distribuidor_tarjeta.addWidget(btn_ver_clave, numero_fila, 4, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_direccion = QLabel("Dirección")
        self.distribuidor_tarjeta.addWidget(etiqueta_direccion, numero_fila, 0)

        self.texto_direccion= QLineEdit(self)
        self.distribuidor_tarjeta.addWidget(self.texto_direccion, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_telefono = QLabel("Telefono")
        self.distribuidor_tarjeta.addWidget(etiqueta_telefono, numero_fila, 0)

        self.texto_telefono = QLineEdit(self)
        self.distribuidor_tarjeta.addWidget(self.texto_telefono, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_notas=QLabel("Notas")
        self.distribuidor_tarjeta.addWidget(etiqueta_notas, numero_fila, 0)

        self.texto_notas=QTextEdit(self)
        self.texto_notas.setMinimumHeight(100)
        self.distribuidor_tarjeta.addWidget(self.texto_notas, numero_fila, 1)
        numero_fila=numero_fila+1

        #Creación de la caja con los botones
        self.widget_botones = QWidget()
        self.distribuidor_botones = QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)
        self.distribuidor_base.addWidget(self.widget_botones, Qt.AlignTop)

       #Creación de los botones con las diferentes operaciones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(150, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.distribuidor_botones.addWidget(self.btn_volver, 0, 0, Qt.AlignCenter)
        self.btn_volver.clicked.connect(self.volver)

        self.btn_guardar_tarjeta = QPushButton("Guardar Tarjeta", self)
        self.btn_guardar_tarjeta.setFixedSize(150, 40)
        self.btn_guardar_tarjeta.setToolTip("Guardar tarjeta")
        self.btn_guardar_tarjeta.setIcon(QIcon("src/recursos/floppy-disk.png"))
        self.distribuidor_botones.addWidget(self.btn_guardar_tarjeta, 0, 2, Qt.AlignCenter)
        self.btn_guardar_tarjeta.clicked.connect(self.guardar_cambios)

    def mostrar_tarjeta(self, elemento):
        self.elemento=elemento
        if (self.elemento!=None):
            self.texto_nombre_elemento.setText(self.elemento["nombre_elemento"])
            self.texto_numero.setText(self.elemento["numero"])
            self.texto_titular.setText(self.elemento["titular"])
            self.fvencimiento.setDate(QtCore.QDate.fromString(str(self.elemento["fecha_venc"]), "yyyy-MM-dd"))
            self.texto_ccv.setText(str(self.elemento["ccv"]))
            indice_clave = self.combobox_claves.findText(self.elemento["clave"])
            self.combobox_claves.setCurrentIndex(indice_clave)
            self.texto_direccion.setText(self.elemento["direccion"])
            self.texto_telefono.setText(self.elemento["telefono"])
            self.texto_notas.setText(str(self.elemento["notas"]))

    def volver(self):
        """
        Esta función permite volver a la lista de elementos
        """    
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()

    def guardar_cambios(self):
        """
        Esta función guarda los cambios al elemento tipo tarjeta (editando o guardando las nuevas tarjeta)
        """
        resultado = self.interfaz.guardar_tarjeta(self.texto_nombre_elemento.text(), self.texto_numero.text(), self.texto_titular.text(),\
                                self.fvencimiento.text(), self.texto_ccv.text(), self.combobox_claves.currentText(), \
                                self.texto_direccion.text(), self.texto_telefono.text(), self.texto_notas.toPlainText())
        if resultado == "":
            self.hide()
            self.interfaz.mostrar_vista_lista_elementos()
        else:
            self.error_tarjeta(resultado)

    def mostrar_clave_favorita(self):
        """
        Esta función solicita mostrar la clave asociada a la clave favorita seleccionada
        """
        self.interfaz.mostrar_clave_favorita(self, self.combobox_claves.currentText())

    def error_tarjeta(self, error):
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

