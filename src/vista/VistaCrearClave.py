from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *


class VistaCrearClave(QDialog):
    #Diálogo para crear o editar un mantenimiento

    def __init__(self,clave,interfaz):
        """
        Constructor del diálogo
        """   
        super().__init__()

        self.interfaz = interfaz

        self.setFixedSize(400, 300)
        self.setWindowIcon(QIcon("src/recursos/cajaDeSeguridad.png"))

        self.resultado = ""

        self.widget_dialogo = QListWidget()
        
        distribuidor_dialogo = QGridLayout()
        self.setLayout(distribuidor_dialogo)
        numero_fila=0
        
        #Si se va a crear un nueva clave o se va a editar, usamos el mismo diálogo

        titulo=""
        if(clave==None):
            titulo="Nueva clave"
        else:
            titulo="Editar clave"

        self.setWindowTitle("Caja de Seguridad - {}".format(titulo))
       
        #Creación de las etiquetas y los campos de texto

        etiqueta_nombre=QLabel("Nombre clave")
        distribuidor_dialogo.addWidget(etiqueta_nombre,numero_fila,0)                

        self.texto_nombre=QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_nombre,numero_fila,1)
        numero_fila=numero_fila+1

        etiqueta_clave=QLabel("Clave")
        distribuidor_dialogo.addWidget(etiqueta_clave,numero_fila,0)

        self.texto_clave=QLineEdit(self)
        self.texto_clave.setEchoMode(QLineEdit.Password)
        distribuidor_dialogo.addWidget(self.texto_clave, numero_fila, 1)
        numero_fila=numero_fila+1

        etiqueta_confirmar_clave = QLabel("Confirmar clave")
        distribuidor_dialogo.addWidget(etiqueta_confirmar_clave, numero_fila, 0)

        self.texto_confirmar_clave = QLineEdit(self)
        self.texto_confirmar_clave.setEchoMode(QLineEdit.Password)
        distribuidor_dialogo.addWidget(self.texto_confirmar_clave, numero_fila, 1)
        numero_fila = numero_fila + 1

        etiqueta_pista = QLabel("Pista")
        distribuidor_dialogo.addWidget(etiqueta_pista, numero_fila, 0)

        self.texto_pista = QLineEdit(self)
        distribuidor_dialogo.addWidget(self.texto_pista, numero_fila, 1)
        numero_fila = numero_fila + 1

        #Creación de los botones para guardar o cancelar
        caja_botones = QGroupBox()
        caja_botones.setLayout(QHBoxLayout())
        caja_botones.setStyleSheet('''
                QGroupBox{border:none}''')

        self.btn_guardar = QPushButton("Guardar")
        caja_botones.layout().addWidget(self.btn_guardar)
        self.btn_guardar.clicked.connect(self.guardar)

        self.btn_generar = QPushButton("Generar")
        caja_botones.layout().addWidget(self.btn_generar)
        self.btn_generar.clicked.connect(self.generar)

        self.btn_cancelar = QPushButton("Cancelar")
        caja_botones.layout().addWidget(self.btn_cancelar)
        self.btn_cancelar.clicked.connect(self.cancelar)

        distribuidor_dialogo.addWidget(caja_botones, numero_fila, 0, 1, 2)

        #Si el diálogo se va a usar para editar, se pone la información correspondiente en los campos de texto

        if (clave!=None):
            self.texto_nombre.setText(clave["nombre"])
            self.texto_clave.setText(clave["clave"])
            self.texto_confirmar_clave.setText(clave["clave"])
            self.texto_pista.setText(clave["pista"])



    def generar(self):
        """
        Esta función solicita generar una clave y la coloca en los campos de clave y confirmación de clave
        """
        clave_segura = self.interfaz.generar_clave()
        self.texto_clave.setText(clave_segura)
        self.texto_confirmar_clave.setText(clave_segura)

    def guardar(self):
        """
        Esta función envía la información de que se han solicitado guardar los cambios
        Verifica si la clave y la confirmación son iguales
        """

        if (self.texto_clave.text() == self.texto_confirmar_clave.text()):
            self.resultado=1
            self.close()
            return self.resultado
        else:
            QMessageBox.information(self, 'Crear clave', "La clave y la confirmación deben ser iguales", QMessageBox.Ok)




    def cancelar(self):
        """
        Esta función envía la información de que se ha cancelado la operación
        """   
        self.resultado=0
        self.close()
        return self.resultado


