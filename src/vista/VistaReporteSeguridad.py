from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QWidget


class VistaReporteSeguridad(QWidget):
    #Ventana que muestra el reporte de gastos de un auto

    def __init__(self, interfaz):
        """
        Constructor de la ventana
        """
        super().__init__()

        # Se establecen las características de la ventana
        self.titulo = 'Caja de seguridad - Reporte seguridad'
        self.left = 80
        self.top = 80
        self.width = 400
        self.height = 560

        self.setAttribute(Qt.WA_DeleteOnClose)

        self.interfaz = interfaz

        self.inicializar_GUI()
        self.show()

    def inicializar_GUI(self):

        # inicializamos la ventana
        self.setWindowTitle(self.titulo)
        self.setFixedSize(self.width, self.height)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridadLogo.png"))

        self.distribuidor_base = QVBoxLayout(self)

        # Creación de la tabla datos de cantidad de elementos

        self.tabla_elementos = QScrollArea(self)
        self.tabla_elementos.setWidgetResizable(True)
        self.widget_tabla_elementos = QWidget()
        self.distribuidor_tabla_elementos = QGridLayout(self.widget_tabla_elementos)
        self.tabla_elementos.setWidget(self.widget_tabla_elementos)

        self.distribuidor_tabla_elementos.setColumnStretch(0, 0)
        self.distribuidor_tabla_elementos.setColumnStretch(1, 0)


        self.contenedor_tabla_elementos = QGroupBox(self)
        self.contenedor_tabla_elementos.setLayout(QHBoxLayout())
        self.contenedor_tabla_elementos.setTitle('Elementos')
        self.distribuidor_base.addWidget(self.contenedor_tabla_elementos)


        self.contenedor_tabla_elementos.layout().addWidget(self.tabla_elementos)
        self.tabla_elementos.setStyleSheet('QScrollArea{border:none}')

        # Creación de las etiquetas con los encabezados
        etiqueta_tipo = QLabel("Tipo elemento")
        etiqueta_tipo.setFont(QFont("Times",weight=QFont.Bold))
        self.distribuidor_tabla_elementos.addWidget(etiqueta_tipo, 0, 0, Qt.AlignCenter|Qt.AlignTop)

        etiqueta_cantidad = QLabel("Cantidad")
        etiqueta_cantidad.setFont(QFont("Times",weight=QFont.Bold))
        self.distribuidor_tabla_elementos.addWidget(etiqueta_cantidad, 0, 1, Qt.AlignCenter|Qt.AlignTop)

        # Creación de la tabla datos seguridad

        self.tabla_seguridad = QScrollArea(self)
        self.tabla_seguridad.setWidgetResizable(True)
        self.widget_tabla_seguridad = QWidget()
        self.distribuidor_tabla_seguridad = QGridLayout(self.widget_tabla_seguridad)
        self.tabla_seguridad.setWidget(self.widget_tabla_seguridad)

        self.distribuidor_tabla_seguridad.setColumnStretch(0, 0)
        self.distribuidor_tabla_seguridad.setColumnStretch(1, 0)

        self.contenedor_tabla_seguridad = QGroupBox(self)
        self.contenedor_tabla_seguridad.setLayout(QHBoxLayout())
        self.contenedor_tabla_seguridad.setTitle('Indicadores seguridad')
        self.distribuidor_base.addWidget(self.contenedor_tabla_seguridad)

        self.contenedor_tabla_seguridad.layout().addWidget(self.tabla_seguridad)
        self.tabla_seguridad.setStyleSheet('QScrollArea{border:none}')

        # Creación de las etiquetas con los encabezados
        etiqueta_indicador = QLabel("Indicador")
        etiqueta_indicador.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_indicador, 0, 0, Qt.AlignCenter | Qt.AlignTop)

        etiqueta_valor = QLabel("Valor")
        etiqueta_valor.setFont(QFont("Times", weight=QFont.Bold))
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_valor, 0, 1, Qt.AlignCenter | Qt.AlignTop)

        #Creación de los botones de funciones de la ventana
        self.btn_volver = QPushButton("Volver", self)
        self.btn_volver.setFixedSize(200, 40)
        self.btn_volver.setToolTip("Volver")
        self.btn_volver.setIcon(QIcon("src/recursos/007-back-button.png"))
        self.btn_volver.setIconSize(QSize(120, 120))
        self.btn_volver.clicked.connect(self.volver)
        self.distribuidor_base.addWidget(self.btn_volver)
        self.distribuidor_base.setAlignment(self.btn_volver, Qt.AlignCenter)


    def mostrar_datos(self, datos_reporte):
        """
        Esta función pobla el reporte de seguridad con la información
        """

        #Mostrar cantidades de cada tipo de elementos

        numero_fila = 1

        etiqueta_tipo_elemento = QLabel("Logins")
        etiqueta_tipo_elemento.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_tipo_elemento, numero_fila, 0, Qt.AlignLeft)

        etiqueta_cantidad = QLabel(str(datos_reporte['logins']))
        etiqueta_cantidad.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_cantidad, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila+1

        etiqueta_tipo_elemento = QLabel("Identificaciones")
        etiqueta_tipo_elemento.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_tipo_elemento, numero_fila, 0, Qt.AlignLeft)

        etiqueta_cantidad = QLabel(str(datos_reporte['ids']))
        etiqueta_cantidad.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_cantidad, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_tipo_elemento = QLabel("Tarjetas")
        etiqueta_tipo_elemento.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_tipo_elemento, numero_fila, 0, Qt.AlignLeft)

        etiqueta_cantidad = QLabel(str(datos_reporte['tarjetas']))
        etiqueta_cantidad.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_cantidad, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_tipo_elemento = QLabel("Secretos")
        etiqueta_tipo_elemento.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_tipo_elemento, numero_fila, 0, Qt.AlignLeft)

        etiqueta_cantidad = QLabel(str(datos_reporte['secretos']))
        etiqueta_cantidad.setWordWrap(True)
        self.distribuidor_tabla_elementos.addWidget(etiqueta_cantidad, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila + 1


        # Mostrar datos de seguridad

        numero_fila = 1

        etiqueta_indicador = QLabel("Contraseñas inseguras")
        etiqueta_indicador.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_indicador, numero_fila, 0, Qt.AlignLeft)

        etiqueta_valor = QLabel(str(datos_reporte['inseguras']))
        etiqueta_valor.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_valor, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_indicador = QLabel("Próximos a vencer")
        etiqueta_indicador.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_indicador, numero_fila, 0, Qt.AlignLeft)

        etiqueta_valor = QLabel(str(datos_reporte['avencer']))
        etiqueta_valor.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_valor, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_indicador = QLabel("Contraseñas usadas más de una vez")
        etiqueta_indicador.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_indicador, numero_fila, 0, Qt.AlignLeft)

        etiqueta_valor = QLabel(str(datos_reporte['masdeuna']))
        etiqueta_valor.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_valor, numero_fila, 1, Qt.AlignCenter)
        numero_fila = numero_fila + 1

        etiqueta_indicador = QLabel("Nivel de seguridad")
        etiqueta_indicador.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_indicador, numero_fila, 0, Qt.AlignLeft)

        etiqueta_valor = QLabel("{:.0%}".format(datos_reporte['nivel']))
        etiqueta_valor.setWordWrap(True)
        self.distribuidor_tabla_seguridad.addWidget(etiqueta_valor, numero_fila, 1, Qt.AlignCenter)

        
    def volver(self):
        """
        Esta función permite volver a la ventana de la lista de elementos
        """   
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()

    def closeEvent(self, event):
        self.hide()
        self.interfaz.mostrar_vista_lista_elementos()
        event.accept()
