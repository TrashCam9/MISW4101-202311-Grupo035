from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from functools import partial


class VistaListaElementos(QWidget):
    #Ventana que muestra la lista de autos

    def __init__(self, interfaz):
        """
        Constructor de la ventanas
        """
        super().__init__()
        
        self.interfaz = interfaz
       
        #Se establecen las características de la ventana
        self.title = 'Caja de seguridad'
        self.width = 900
        self.height = 758
        self.inicializar_GUI()

    def inicializar_GUI(self):
        
        #inicializamos la ventana
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
         
        self.distribuidor_base = QVBoxLayout(self)

        #Creación del logo de encabezado
        self.logo=QLabel(self)
        self.pixmap = QPixmap("src/recursos/cajaDeSeguridadLogo.png")
        self.pixmap = self.pixmap.scaled(488,158, Qt.KeepAspectRatio)
        self.logo.setPixmap(self.pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.logo,alignment=Qt.AlignCenter)

        #Creación de las etiquetsa con textos de bienvenida
        self.etiqueta_bienvenida=QLabel("!!Bienvenido a su Caja de Seguridad!!")
        self.etiqueta_bienvenida.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_bienvenida,Qt.AlignCenter)
        
        self.etiqueta_descripcion=QLabel("Con este software podrá administrar sus claves e información de cuentas, tarjetas e identidades")
        self.etiqueta_descripcion.setAlignment(Qt.AlignCenter)
        self.distribuidor_base.addWidget(self.etiqueta_descripcion,Qt.AlignCenter)

        #Creación del espacio de los botones
        self.widget_botones=QWidget()
        self.distribuidor_botones=QGridLayout()
        self.widget_botones.setLayout(self.distribuidor_botones)

        #Creación de los botones

        self.btn_crear_reporte = QPushButton("Reporte de seguridad", self)
        self.btn_crear_reporte.setFixedSize(288, 48)
        self.btn_crear_reporte.setToolTip("Reporte de seguridad")
        self.btn_crear_reporte.setIcon(QIcon("src/recursos/reporte.png"))
        self.btn_crear_reporte.setIconSize(QSize(30, 30))
        self.distribuidor_botones.addWidget(self.btn_crear_reporte, 0, 0, Qt.AlignLeft)
        self.btn_crear_reporte.clicked.connect(self.mostrar_ventana_reporte)

        self.btn_crear_elemento=QPushButton("Crear elemento",self)
        self.btn_crear_elemento.setFixedSize(288,48)
        self.btn_crear_elemento.setToolTip("Crear elemento")
        self.btn_crear_elemento.setIcon(QIcon("src/recursos/006-add.png"))
        self.btn_crear_elemento.setIconSize(QSize(120,120))
        self.distribuidor_botones.addWidget(self.btn_crear_elemento,0,1,Qt.AlignLeft)
        self.btn_crear_elemento.clicked.connect(self.mostrar_ventana_crear_elemento)

        self.btn_ver_claves_favoritas=QPushButton("Claves favoritas",self)
        self.btn_ver_claves_favoritas.setFixedSize(288,48)
        self.btn_ver_claves_favoritas.setToolTip("Claves favoritas")
        self.btn_ver_claves_favoritas.setIcon(QIcon("src/recursos/010-llave.png"))
        self.btn_ver_claves_favoritas.setIconSize(QSize(120,120))
        self.btn_ver_claves_favoritas.clicked.connect(self.mostrar_claves_favoritas)
        self.distribuidor_botones.addWidget(self.btn_ver_claves_favoritas,0,2,Qt.AlignRight)
        self.distribuidor_base.addWidget(self.widget_botones,Qt.AlignCenter)

        #Creación del área con la información de los elementos
        self.tabla_elementos = QScrollArea(self)
        self.tabla_elementos.setWidgetResizable(True)
        self.tabla_elementos.setFixedSize(840, 400)
        self.widget_tabla_elementos = QWidget()
        self.distribuidor_tabla_elementos = QGridLayout()        
        self.widget_tabla_elementos.setLayout(self.distribuidor_tabla_elementos);                
        self.tabla_elementos.setWidget(self.widget_tabla_elementos)
        self.distribuidor_base.addWidget(self.tabla_elementos)

        #Hacemos la ventana visible
        self.show()


    def mostrar_elementos(self, lista_elementos):
        """
        Esta función puebla la tabla con las elementos
        """
        self.elementos = lista_elementos
        numero_fila=0


        self.distribuidor_tabla_elementos.setColumnStretch(0,1)
        self.distribuidor_tabla_elementos.setColumnStretch(1,1)
        self.distribuidor_tabla_elementos.setColumnStretch(2,0)
        self.distribuidor_tabla_elementos.setColumnStretch(3,0)
        self.distribuidor_tabla_elementos.setColumnStretch(4,0)
        self.distribuidor_tabla_elementos.setColumnStretch(5,0)

        #Ciclo para llenar la tabla
        if (self.elementos!= None and len(self.elementos)>0) :
            self.tabla_elementos.setVisible(True)

            #Creación de las etiquetas

            etiqueta_nombre=QLabel("Elemento")
            etiqueta_nombre.setMinimumSize(QSize(0,0))
            etiqueta_nombre.setMaximumSize(QSize(65525,65525))
            etiqueta_nombre.setAlignment(Qt.AlignCenter)
            etiqueta_nombre.setFont(QFont("Times",weight=QFont.Bold)) 
            self.distribuidor_tabla_elementos.addWidget(etiqueta_nombre, 0,0, Qt.AlignLeft)

            etiqueta_nombre = QLabel("Tipo")
            etiqueta_nombre.setMinimumSize(QSize(0, 0))
            etiqueta_nombre.setMaximumSize(QSize(65525, 65525))
            etiqueta_nombre.setAlignment(Qt.AlignCenter)
            etiqueta_nombre.setFont(QFont("Times", weight=QFont.Bold))
            self.distribuidor_tabla_elementos.addWidget(etiqueta_nombre, 0, 1, Qt.AlignLeft)

            etiqueta_acciones=QLabel("Opciones")                      
            etiqueta_acciones.setMinimumSize(QSize(0,0))
            etiqueta_acciones.setMaximumSize(QSize(65525,65525))
            etiqueta_acciones.setAlignment(Qt.AlignCenter)
            etiqueta_acciones.setFont(QFont("Times",weight=QFont.Bold))               
            self.distribuidor_tabla_elementos.addWidget(etiqueta_acciones, 0,2,1,3, Qt.AlignCenter)
       
            for dic_elemento in self.elementos:
                numero_fila=numero_fila+1

                etiqueta_nombre=QLabel(dic_elemento['nombre_elemento'])
                etiqueta_nombre.setWordWrap(True)
                self.distribuidor_tabla_elementos.addWidget(etiqueta_nombre,numero_fila,0)

                etiqueta_nombre = QLabel(dic_elemento['tipo'])
                etiqueta_nombre.setWordWrap(True)
                self.distribuidor_tabla_elementos.addWidget(etiqueta_nombre, numero_fila, 1)

                #Creación de los botones asociados a cada acción

                if dic_elemento['tipo'] !='Identificación':
                    btn_ver_clave=QPushButton("",self)
                    btn_ver_clave.setToolTip("Ver clave")
                    btn_ver_clave.setFixedSize(40,40)
                    btn_ver_clave.setIcon(QIcon("src/recursos/002-eye-variant-with-enlarged-pupil.png"))
                    btn_ver_clave.clicked.connect(partial(self.mostrar_clave,numero_fila -1 ) )
                    self.distribuidor_tabla_elementos.addWidget(btn_ver_clave,numero_fila,2,Qt.AlignCenter)

                btn_editar_elemento=QPushButton("",self)
                btn_editar_elemento.setToolTip("Editar elemento")
                btn_editar_elemento.setFixedSize(40,40)
                btn_editar_elemento.setIcon(QIcon("src/recursos/004-edit-button.png"))
                btn_editar_elemento.clicked.connect(partial(self.mostrar_elemento,numero_fila-1) )
                self.distribuidor_tabla_elementos.addWidget(btn_editar_elemento,numero_fila,3,Qt.AlignCenter)


                btn_eliminar=QPushButton("",self)
                btn_eliminar.setToolTip("Borrar")
                btn_eliminar.setFixedSize(40,40)
                btn_eliminar.setIcon(QIcon("src/recursos/005-delete.png"))
                btn_eliminar.clicked.connect(partial(self.eliminar_elemento,numero_fila -1) )
                self.distribuidor_tabla_elementos.addWidget(btn_eliminar,numero_fila,4,Qt.AlignCenter)

        else:
                self.tabla_elementos.setVisible(False)

        #Elemento para ajustar la forma de la tabla (y evitar que queden muy espaciados)
        self.distribuidor_tabla_elementos.layout().setRowStretch(numero_fila+2, 1)


    def mostrar_clave(self,id_elemento):
        """
        Esta función informa a la interfaz para desplegar la clave del elemento
        """
        self.interfaz.mostrar_clave(self, id_elemento)


    def mostrar_ventana_crear_elemento(self):
        """
        Esta función informa a la interfaz para desplegar la ventana para crear elementos
        """
        self.hide()
        self.interfaz.crear_elemento(self)

    def mostrar_elemento(self, id_elemento):
        """
        Esta función informa a la interfaz para desplegar la ventana del elemento
        """
        self.hide()
        self.interfaz.mostrar_elemento(id_elemento)

    def eliminar_elemento(self, indice):
        """
        Esta función elimina un elemento tras solicitar una confirmación
        """
        mensaje_confirmacion = QMessageBox()
        mensaje_confirmacion.setIcon(QMessageBox.Question)
        mensaje_confirmacion.setText(
            "¿Esta seguro de que desea borrar este elemento?\nRecuerde que esta acción es irreversible")
        mensaje_confirmacion.setWindowTitle("¿Desea borrar este elemento?")
        mensaje_confirmacion.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
        mensaje_confirmacion.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        respuesta = mensaje_confirmacion.exec_()
        if respuesta == QMessageBox.Yes:
            self.interfaz.eliminar_elemento(indice)
            self.hide()
            self.interfaz.mostrar_vista_lista_elementos()

    def mostrar_claves_favoritas(self):
        """
        Esta función informa a la interfaz para desplegar la ventana de la lista de claves favoritas
        """
        self.hide()
        self.interfaz.mostrar_claves_favoritas()


    def mostrar_ventana_reporte(self):
        """
        Esta función informa a la interfaz para desplegar la ventana del reporte de seguridad
        """
        self.hide()
        self.interfaz.mostrar_reporte_seguridad()

        
