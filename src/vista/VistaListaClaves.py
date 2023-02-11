from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

from functools import partial

from src.vista.VistaCrearClave import VistaCrearClave


class VistaListaClaves(QWidget):
    #Ventana que muestra la lista de claves

    def __init__(self, interfaz):
        """
        Constructor de la ventana
        """
        super().__init__()

        #Se establecen las características de la ventana
        self.titulo = 'Caja de Seguridad - Claves Favoritas'
        self.interfaz=interfaz

        self.width = 400
        self.height = 500
        self.inicializar_GUI()
        self.show()


    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
         
        self.distribuidor_base = QVBoxLayout(self)        

        #Creación del grupo de botones
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())

        #Creación de los botones
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(170, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.btn_volver.clicked.connect(self.volver)

        self.btn_crear_clave=QPushButton("Crear clave favorita", self)
        self.btn_crear_clave.setFixedSize(170, 40)
        self.btn_crear_clave.setToolTip("Crear clave favorita")
        self.btn_crear_clave.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_crear_clave.clicked.connect(self.mostrar_dialogo_crear_clave)

        self.contenedor_tabla = QGroupBox(self)
        self.contenedor_tabla.setLayout(QHBoxLayout())
        self.contenedor_tabla.setTitle('Claves favoritas')
        self.distribuidor_base.addWidget(self.contenedor_tabla)

        #Creación de la tabla con la lista de mantenimientos
        self.tabla_claves = QScrollArea(self)
        self.tabla_claves.setWidgetResizable(True)
        self.tabla_claves.setStyleSheet('QScrollArea{border:none}')
        self.tabla_claves.setFixedSize(300, 300)
        self.widget_tabla_viajeros = QWidget()
        self.distribuidor_tabla_claves = QGridLayout(self.widget_tabla_viajeros)
        self.tabla_claves.setWidget(self.widget_tabla_viajeros)
        self.contenedor_tabla.layout().addWidget(self.tabla_claves)

        self.distribuidor_tabla_claves.setColumnStretch(0, 0)
        self.distribuidor_tabla_claves.setColumnStretch(1, 0)
        self.distribuidor_tabla_claves.setColumnStretch(2, 0)

        self.distribuidor_tabla_claves.setSpacing(0)

        #Creación de las etiquetas de encabezado
        etiqueta_nombre = QLabel("Nombre")
        etiqueta_nombre.setFixedSize(145,40)
        etiqueta_nombre.setFont(QFont("Times",weight=QFont.Bold)) 
        self.distribuidor_tabla_claves.addWidget(etiqueta_nombre, 0, 0, Qt.AlignTop)

        etiqueta_accion = QLabel("Acción")
        etiqueta_accion.setFixedSize(60,40)
        etiqueta_accion.setFont(QFont("Times",weight=QFont.Bold)) 
        etiqueta_accion.setAlignment(Qt.AlignCenter)
        self.distribuidor_tabla_claves.addWidget(etiqueta_accion, 0, 1, 0, 2, Qt.AlignTop | Qt.AlignCenter)
        

        #Se añaden los botones a la caja de botones
        caja_botones.layout().addWidget(self.btn_volver)
        caja_botones.layout().addWidget(self.btn_crear_clave)
        caja_botones.layout().setContentsMargins(0, 0, 0, 0)
        caja_botones.setObjectName("MyBox")
        caja_botones.setStyleSheet("#MyBox{border:3px}")
        self.distribuidor_base.addWidget(caja_botones)



       
    def mostrar_claves(self, lista_claves):
        """
        Esta función muestra la lista de claves
        """
        self.claves = lista_claves
        

        #Ciclo para poblar la tabla
        numero_fila = 0
        for clave in self.claves:

            etiqueta_nombre=QLabel(clave["nombre"])
            etiqueta_nombre.setWordWrap(True)
            etiqueta_nombre.setFixedSize(90,40)
            self.distribuidor_tabla_claves.addWidget(etiqueta_nombre, numero_fila + 1, 0, Qt.AlignTop)

            boton_editar=QPushButton("",self)
            boton_editar.setToolTip("Editar")
            boton_editar.setFixedSize(30,30)
            boton_editar.setIcon(QIcon("src/recursos/004-edit-button.png"))
            boton_editar.clicked.connect(partial(self.mostrar_dialogo_editar_clave, numero_fila))
            self.distribuidor_tabla_claves.addWidget(boton_editar, numero_fila + 1, 1, Qt.AlignTop)


            etiqueta_eliminar=QPushButton("",self)
            etiqueta_eliminar.setToolTip("Borrar")
            etiqueta_eliminar.setFixedSize(30,30)
            etiqueta_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
            etiqueta_eliminar.clicked.connect(partial(self.eliminar_clave, numero_fila))
            self.distribuidor_tabla_claves.addWidget(etiqueta_eliminar, numero_fila + 1, 2, Qt.AlignTop)


            numero_fila=numero_fila+1

        #Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_claves.layout().setRowStretch(numero_fila + 1, 1)

    def mostrar_dialogo_editar_clave(self, id_clave):
        """
        Esta función ejecuta el diálogo para editar una clave
        """    
        dialogo=VistaCrearClave(self.claves[id_clave], self.interfaz)
        dialogo.exec_()
        if dialogo.resultado==1:            
            self.interfaz.editar_clave(id_clave, dialogo.texto_nombre.text(), dialogo.texto_clave.text(),dialogo.texto_pista.text())

    def eliminar_clave(self, indice_clave):
        """
        Esta función informa a la interfaz la clave a eliminar
        """    
        mensaje_confirmacion=QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText("¿Esta seguro de que desea eliminar esta clave?\nRecuerde que esta acción es irreversible")
        mensaje_confirmacion.setWindowTitle("¿Desea borrar esta clave?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No ) 
        respuesta=mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            self.interfaz.eliminar_clave(indice_clave)
            self.hide()
            self.interfaz.mostrar_claves_favoritas()

    def mostrar_dialogo_crear_clave(self):
        """
        Esta función ejecuta el diálogo para crear un nueva clave
        """
        dialogo=VistaCrearClave(None, self.interfaz)
        dialogo.exec_()
        if dialogo.resultado==1:
            self.interfaz.crear_clave(dialogo.texto_nombre.text(), dialogo.texto_clave.text(), dialogo.texto_pista.text())

    def volver(self):
        """
        Esta función permite volver a la ventana de lista de elementos
        """
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()

    def error_clave(self, error):
            mensaje_error=QMessageBox()
            mensaje_error.setIcon(QMessageBox.Question)
            mensaje_error.setText("Error : " + error)
            mensaje_error.setWindowTitle("Error guardar clave")
            mensaje_error.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
            mensaje_error.setStandardButtons(QMessageBox.Ok ) 
            respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()
        event.accept()
    