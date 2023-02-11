from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from functools import partial


class VistaLogin(QWidget):
    #Ventana de elemento logitn

    def __init__(self,principal, claves):
        """
        Constructor de la ventana
        """   
        super().__init__()

        self.titulo = 'Caja de seguridad - Login'
        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz=principal
        self.claves = claves

        self.width = 500
        self.height = 400
        self.inicializar_GUI()
        self.show()
       

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        self.widget_login = QWidget()
        self.distribuidor_login = QGridLayout()
        self.widget_login.setLayout(self.distribuidor_login)
        self.distribuidor_base.addWidget(self.widget_login, Qt.AlignTop)
        numero_fila = 0

        etiqueta_nombre=QLabel("Nombre login")
        self.distribuidor_login.addWidget(etiqueta_nombre, numero_fila, 0)

        self.texto_nombre=QLineEdit(self)
        self.distribuidor_login.addWidget(self.texto_nombre, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_email=QLabel("email")
        self.distribuidor_login.addWidget(etiqueta_email, numero_fila, 0)

        self.texto_email=QLineEdit(self)
        self.distribuidor_login.addWidget(self.texto_email, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_usuario=QLabel("Usuario")
        self.distribuidor_login.addWidget(etiqueta_usuario, numero_fila, 0)

        self.texto_usuario=QLineEdit(self)
        self.distribuidor_login.addWidget(self.texto_usuario, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_password=QLabel("Password")
        self.distribuidor_login.addWidget(etiqueta_password, numero_fila, 0)

        self.combobox_claves = QComboBox(self)
        for clave in self.claves:
            self.combobox_claves.addItem(clave["nombre"])
        self.combobox_claves.setCurrentIndex(0)
        self.distribuidor_login.addWidget(self.combobox_claves, numero_fila, 1, 1, 2)

        btn_ver_clave = QPushButton("", self)
        btn_ver_clave.setToolTip("Ver clave")
        btn_ver_clave.setFixedSize(40, 40)
        btn_ver_clave.setIcon(QIcon("src/recursos/002-eye-variant-with-enlarged-pupil.png"))
        btn_ver_clave.clicked.connect(partial(self.mostrar_clave_favorita))
        self.distribuidor_login.addWidget(btn_ver_clave, numero_fila, 4, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_url=QLabel("URL")
        self.distribuidor_login.addWidget(etiqueta_url, numero_fila, 0)

        self.texto_url=QLineEdit(self)
        self.distribuidor_login.addWidget(self.texto_url, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_notas=QLabel("Notas")
        self.distribuidor_login.addWidget(etiqueta_notas, numero_fila, 0)

        self.texto_notas = QTextEdit(self)
        self.texto_notas.setMinimumHeight(150)
        self.distribuidor_login.addWidget(self.texto_notas, numero_fila, 1)
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

        self.btn_guardar_login = QPushButton("Guardar login", self)
        self.btn_guardar_login.setFixedSize(150, 40)
        self.btn_guardar_login.setToolTip("Guardar login")
        self.btn_guardar_login.setIcon(QIcon("src/recursos/floppy-disk.png"))
        self.distribuidor_botones.addWidget(self.btn_guardar_login, 0, 2, Qt.AlignCenter)
        self.btn_guardar_login.clicked.connect(self.guardar_cambios)

    def mostrar_login(self, elemento):
        self.elemento=elemento
        if (self.elemento!=None):
            self.texto_nombre.setText(self.elemento["nombre_elemento"])
            self.texto_email.setText(self.elemento["email"])
            self.texto_usuario.setText(self.elemento["usuario"])
            indice_clave = self.combobox_claves.findText(self.elemento["clave"])
            self.combobox_claves.setCurrentIndex(indice_clave)
            self.texto_url.setText(self.elemento["url"])
            self.texto_notas.setText(str(self.elemento["notas"]))

    def volver(self):
        """
        Esta función permite volver a la lista de elementos
        """    
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()

    def guardar_cambios(self):
        """
        Esta función guarda los cambios al elemento tipo login (editando o guardando los nuevos login)
        """
        resultado = self.interfaz.guardar_login(self.texto_nombre.text(), self.texto_email.text(), self.texto_usuario.text(), self.combobox_claves.currentText(),\
                                                self.texto_url.text(), self.texto_notas.toPlainText())
        if resultado == "" :
            self.hide()
            self.interfaz.mostrar_vista_lista_elementos()
        else:
            self.error_login(resultado)

    def mostrar_clave_favorita(self):
        """
        Esta función solicita mostrar la clave asociada a la clave favorita seleccionada
        """
        self.interfaz.mostrar_clave_favorita(self, self.combobox_claves.currentText())
    
    def error_login(self, error):
        mensaje_error=QMessageBox()
        mensaje_error.setIcon(QMessageBox.Question)
        mensaje_error.setText("Error: " + str(error))
        mensaje_error.setWindowTitle("Error al guardar")
        mensaje_error.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))
        mensaje_error.setStandardButtons(QMessageBox.Ok ) 
        respuesta=mensaje_error.exec_()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()
        event.accept()