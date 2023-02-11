from PyQt5.QtWidgets import QApplication, QMessageBox

from .VistaClaveMaestra import VistaClaveMaestra
from .VistaId import VistaId
from .VistaListaClaves import VistaListaClaves
from .VistaListaElementos import VistaListaElementos
from .VistaLogin import VistaLogin
from .VistaReporteSeguridad import VistaReporteSeguridad
from .VistaSecreto import VistaSecreto
from .VistaSeleccionElemento import VistaSeleccionElemento
from .VistaTarjeta import VistaTarjeta


class App_CajaDeSeguridad(QApplication):
    """
    Clase principal de la interfaz que coordina las diferentes vistas/ventanas de la aplicación
    """

    def __init__(self, sys_argv, logica):
        """
        Constructor de la interfaz. Debe recibir la lógica e iniciar la aplicación en la ventana principal.
        """
        super(App_CajaDeSeguridad, self).__init__(sys_argv)

        self.logica = logica
        self.mostrar_vista_clave_maestra()


    def mostrar_vista_clave_maestra(self):
        """
        Esta función inicializa la ventana de la clave maestra
        """
        self.vista_clave_maestra = VistaClaveMaestra(self)
        self.vista_clave_maestra.mostrar_clave(self.logica.dar_claveMaestra())

    def mostrar_vista_lista_elementos(self):
        """
        Esta función inicializa la ventana de la lista de elementos
        """
        self.vista_lista_elementos = VistaListaElementos(self)
        self.vista_lista_elementos.mostrar_elementos(self.logica.dar_elementos())

    def crear_elemento(self, ventana):
        """
        Esta función crea un elemento en la ventana de elementos
        """

        dialogo = VistaSeleccionElemento()
        dialogo.exec_()
        if dialogo.resultado == "Login":
            self.mostrar_login()
        elif dialogo.resultado == "Id":
            self.mostrar_id()
        elif dialogo.resultado == "Tarjeta":
            self.mostrar_tarjeta()
        elif dialogo.resultado == "Secreto":
            self.mostrar_secreto()
        else:
            self.mostrar_vista_lista_elementos()


    def mostrar_elemento(self, id_elemento=-1):
        """
        Esta función muestra un elemento de acuerdo al tipo de elemento
        """
        self.elemento_actual = id_elemento

        if id_elemento != -1:
            tipo = self.logica.dar_elementos()[id_elemento]['tipo']
            if tipo == "Login":
                self.mostrar_login(id_elemento)
            elif tipo == "Identificación":
                self.mostrar_id(id_elemento)
            elif tipo == "Tarjeta":
                self.mostrar_tarjeta(id_elemento)
            elif tipo == "Secreto":
                self.mostrar_secreto(id_elemento)
            else:
                print("Error tipo")

    def mostrar_login(self, id_elemento=-1):
        """
        Esta función muestra un elemento de tipo login en la ventana de login
        """
        self.elemento_actual = id_elemento
        if id_elemento != -1:
                self.vista_login = VistaLogin(self, self.logica.dar_claves_favoritas())
                self.vista_login.mostrar_login(self.logica.dar_elemento(self.elemento_actual))
        else:
            self.vista_login = VistaLogin(self,self.logica.dar_claves_favoritas())
            self.vista_login.mostrar_login(None)


    def guardar_login(self, nombre, email, usuario, password,url, notas):
        """
        Esta función guarda un nuevo login o los cambios sobre una existente
        """
        validacion = self.logica.validar_crear_editar_login(self.elemento_actual, nombre, email, usuario, password, url, notas)
        if validacion == "":
            if self.elemento_actual == -1:
                self.logica.crear_login(nombre, email, usuario, password, url, notas)
            else:
                self.logica.editar_login(self.elemento_actual, nombre, email, usuario, password, url, notas)
            self.vista_lista_elementos.mostrar_elementos(self.logica.dar_elementos())
        return validacion

    def mostrar_id(self, id_elemento=-1):
        """
            Esta función muestra un elemento de tipo id en la ventana de identificación
        """
        self.elemento_actual = id_elemento
        if id_elemento != -1:
            self.vista_id = VistaId(self)
            self.vista_id.mostrar_id(self.logica.dar_elemento(self.elemento_actual))
        else:
            self.vista_id = VistaId(self)
            self.vista_id.mostrar_id(None)

    def guardar_id(self, nombre_elemento, numero, nombre_completo,fnacimiento,fexpedicion,fvencimiento,notas):
        """
        Esta función guarda un nuevo elemento de indentificación o los cambios sobre uno existente
        """
        validacion = self.logica.validar_crear_editar_id(self.elemento_actual, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas)
        if validacion == "":
            if self.elemento_actual == -1:
                self.logica.crear_id(nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas)
            else:
                self.logica.editar_id(self.elemento_actual, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas)
            self.vista_lista_elementos.mostrar_elementos(self.logica.dar_elementos())
        return validacion

    def mostrar_tarjeta(self, id_elemento=-1):
        """
            Esta función muestra un elemento de tipo tarjeta en la ventana de tarjetas
        """
        self.elemento_actual = id_elemento
        if id_elemento != -1:
            self.vista_tarjeta = VistaTarjeta(self, self.logica.dar_claves_favoritas())
            self.vista_tarjeta.mostrar_tarjeta(self.logica.dar_elemento(self.elemento_actual))
        else:
            self.vista_tarjeta = VistaTarjeta(self,self.logica.dar_claves_favoritas())
            self.vista_tarjeta.mostrar_tarjeta(None)

    def guardar_tarjeta(self, nombre_elemento, numero, titular,fvencimiento, ccv, clave, direccion, telefono, notas):
        """
        Esta función guarda un nuevo elemento de tipo tarjeta o los cambios sobre uno existente
        """
        validacion = self.logica.validar_crear_editar_tarjeta(self.elemento_actual, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas)
        if validacion == "":
            if self.elemento_actual == -1:
                self.logica.crear_tarjeta(nombre_elemento, numero, titular ,fvencimiento, ccv, clave, direccion, telefono, notas)
            else:
                self.logica.editar_tarjeta(self.elemento_actual, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas)
            self.vista_lista_elementos.mostrar_elementos(self.logica.dar_elementos())
        return validacion

    def mostrar_secreto(self, id_elemento=-1):
        """
        Esta función muestra un elemento de tipo secreto en la ventana de secretos
        """
        self.elemento_actual = id_elemento
        if id_elemento != -1:
                self.vista_secreto = VistaSecreto(self, self.logica.dar_claves_favoritas())
                self.vista_secreto.mostrar_secreto(self.logica.dar_elemento(self.elemento_actual))
        else:
            self.vista_secreto = VistaSecreto(self, self.logica.dar_claves_favoritas())
            self.vista_secreto.mostrar_secreto(None)

    def guardar_secreto(self, nombre, secreto, clave, notas):
        """
        Esta función guarda un nuevo secreto o los cambios sobre una existente
        """
        validacion = self.logica.validar_crear_editar_secreto(self.elemento_actual, nombre, secreto, clave, notas)
        if validacion == "":
            if self.elemento_actual == -1:
                self.logica.crear_secreto(nombre, secreto, clave, notas)
            else:
                self.logica.editar_secreto(self.elemento_actual, nombre, secreto, clave, notas)
            self.vista_lista_elementos.mostrar_elementos(self.logica.dar_elementos())
        return validacion

    def eliminar_elemento(self, indice):
        """
        Esta función elimina un elemento
        """
        self.logica.eliminar_elemento(indice)
        self.vista_lista_elementos.mostrar_elementos(self.logica.dar_elementos())

    def mostrar_clave(self, ventana, id_elemento):
        """
        Esta función muestra la clave del elemento
        """
        self.elemento_actual = id_elemento
        clave_elemento = self.logica.dar_elemento(id_elemento)['clave']
        clave = self.logica.dar_clave(clave_elemento)
        QMessageBox.information(ventana, 'Clave elemento',
                                "Nombre clave favorita: " + clave_elemento + "\nClave: " + clave, QMessageBox.Ok)

    def mostrar_clave_favorita(self, ventana, nombre_clave_favorita):
        """
        Esta función muestra la clave favorita con nombre nombre_clave_favorita
        """
        clave = self.logica.dar_clave(nombre_clave_favorita)
        QMessageBox.information(ventana, 'Clave elemento', "Nombre clave favorita: " + nombre_clave_favorita + "\nClave: " + clave, QMessageBox.Ok)

    def mostrar_reporte_seguridad(self):
        """
        Esta función muestra el reporte de seguridad
        """
        datos_reporte = self.logica.dar_reporte_seguridad()
        self.vista_reporte_seguridad = VistaReporteSeguridad(self)
        self.vista_reporte_seguridad.mostrar_datos(datos_reporte)


    def mostrar_claves_favoritas(self):
        """
        Esta función muestra la ventana con la lista de claves favoritas
        """
        self.vista_lista_claves=VistaListaClaves(self)
        self.vista_lista_claves.mostrar_claves(self.logica.dar_claves_favoritas())

    def crear_clave(self, nombre, clave, pista):
        """
        Esta función agregar una nueva clave a la aplicación
        """
        validacion = self.logica.validar_crear_editar_clave(nombre, clave, pista)
        if validacion == "":
            self.logica.crear_clave(nombre, clave, pista)
        else:
            self.vista_lista_claves.error_clave(validacion)
        self.vista_lista_claves.mostrar_claves(self.logica.dar_claves_favoritas())

    def editar_clave(self, id, nombre, clave, pista):
        """
        Esta función permite editar una clave
        """
        validacion = self.logica.validar_crear_editar_clave(nombre, clave, pista)
        if validacion == "":
            self.logica.editar_clave(id, nombre, clave, pista)
        else:
            self.vista_lista_claves.error_clave(validacion)
        self.vista_lista_claves.mostrar_claves(self.logica.dar_claves_favoritas())

    def generar_clave(self):
        """
        Esta función devuelve una clave que cumple con las condiciones de seguridad
        """
        return self.logica.generar_clave()

    def eliminar_clave(self, indice):
        """
        Esta función elimina una clave
        """
        self.logica.eliminar_clave(indice)
        self.vista_lista_claves.mostrar_claves(self.logica.dar_claves_favoritas())

