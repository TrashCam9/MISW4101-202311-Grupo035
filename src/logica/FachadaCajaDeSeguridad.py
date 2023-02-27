'''
Esta clase es la fachada con los métodos a implementar en la lógica
'''
from src.modelo.elemento import Elemento
from src.modelo.clave import Clave
from src.modelo.caja_de_seguridad import CajaDeSeguridad
from src.modelo.declarative_base import engine, Base, Session

import string
import random

class FachadaCajaDeSeguridad:

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = Session()

        # Creamos la caja de seguridad si no existe
        caja = self.session.query(CajaDeSeguridad).first()
        if caja is None:
            caja = CajaDeSeguridad()
            self.session.add(caja)
            self.session.commit()
            

    def dar_elementos(self):
        ''' Retorna la lista de elementos de la caja de seguridad
        Retorna:
            (list): La lista con los dict o los objetos de los elementos
        '''
        elementos = self.session.query(Elemento).all()
        return elementos

    def dar_elemento(self, id_elemento):
        ''' Retorna un elemento de la caja de seguridad
        Parámetros:
            id_elemento (int): El identificador del elemento a retornar
        Retorna:
            (dict): El elemento identificado con id_elemento
        '''
        raise NotImplementedError("Método no implementado")

    def dar_claves_favoritas(self):
        ''' Retorna la lita de claves favoritas
        Retorna:
            (list): La lista con los dict o los objetos de las claves favoritas
        '''
        claves = self.session.query(Clave).all()
        return claves

    def dar_clave_favorita(self, id_clave):
        ''' Retorna una clave favoritas
        Parámetros:
            id_clave (int): El identificador de la clave favorita a retornar
        Retorna:
            (dict): La clave favorita identificada con id_clave
        '''
        raise NotImplementedError("Método no implementado")

    def dar_clave(self, nombre_clave):
        ''' Retorna la clave asignada a una clave favorita
        Parámetros:
            nombre_clave (string): El nombre de la clave favorita
        Retorna:
            (string): La clave asignada a la clave favorita del parámetro
        '''
        raise NotImplementedError("Método no implementado")

    def eliminar_elemento(self, id):
        ''' Elimina un elemento de la lista de elementos
        Parámetros:
            id (int): El id del elemento a eliminar_clave
        '''
        raise NotImplementedError("Método no implementado")

    def dar_claveMaestra(self):
        ''' Retorna la clave maestra de la caja de seguridad
        Rertorna:
            (string): La clave maestra de la caja de seguridad
        '''
        return self.session.query(CajaDeSeguridad).first().clave_maestra

    def crear_login(self, nombre, email, usuario, password, url, notas):
        ''' Crea un elemento login
        Parámetros:
            nombre (string): El nombre del elemento
            email (string): El email del elemento
            usuario (string): El usuario del login
            password (string): El nombre de clave favorita del elemento
            url (string): El URL del login
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_login(self, id, nombre, email, usuario, password, url, notas):
        ''' Valida que un login se pueda crear o editar
        Parámetros:
            nombre (string): El nombre del elemento
            email (string): El email del elemento
            usuario (string): El usuario del login
            password (string): El nombre de clave favorita del elemento
            url (string): El URL del login
            notas (string): Las notas del elemento
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la 
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def editar_login(self, id, nombre, email, usuario, password, url, notas):
        ''' Edita un elemento login
        Parámetros:
            nombre (string): El nombre del elemento
            email (string): El email del elemento
            usuario (string): El usuario del login
            password (string): El nombre de clave favorita del elemento
            url (string): El URL del login
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def crear_id(self, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        ''' Crea un elemento identificación
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (string): El número del elemento
            nombre_completo (string): El nombre completo de la persona en la identificación
            fnacimiento (string): La fecha de nacimiento de la persona en la identificación
            fexpedicion (string): La fecha de expedición en la identificación
            fvencimiento (string): La feha de vencimiento en la identificación
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_id(self, id, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        ''' Valida que una identificación se pueda crear o editar
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (string): El número del elemento
            nombre_completo (string): El nombre completo de la persona en la identificación
            fnacimiento (string): La fecha de nacimiento de la persona en la identificación
            fexpedicion (string): La fecha de expedición en la identificación
            fvencimiento (string): La feha de vencimiento en la identificación
            notas (string): Las notas del elemento
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la 
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def editar_id(self, id,nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        ''' Edita un elemento identificación
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (string): El número del elemento
            nombre_completo (string): El nombre completo de la persona en la identificación
            fnacimiento (string): La fecha de nacimiento de la persona en la identificación
            fexpedicion (string): La fecha de expedición en la identificación
            fvencimiento (string): La feha de vencimiento en la identificación
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def crear_tarjeta(self, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        ''' Crea un elemento tarjeta
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (string): El número del elemento
            titular (string): El nombre del titular de la tarjeta
            fvencimiento (string): La feha de vencimiento en la tarjeta
            ccv (string): El código de seguridad en la tarjeta
            clave (string): El nombre de clave favorita del elemento
            direccion (string): La dirección del titular de la tarjeta
            telefono (string): El número de teléfono del titular de la tarjeta
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_tarjeta(self, id, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        ''' Valida que una tarjeta se pueda crear o editar
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (string): El número del elemento
            titular (string): El nombre del titular de la tarjeta
            fvencimiento (string): La feha de vencimiento en la tarjeta
            ccv (string): El código de seguridad en la tarjeta
            clave (string): El nombre de clave favorita del elemento
            direccion (string): La dirección del titular de la tarjeta
            telefono (string): El número de teléfono del titular de la tarjeta
            notas (string): Las notas del elemento
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la 
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def editar_tarjeta(self, id, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        ''' Edita un elemento tarjeta
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (string): El número del elemento
            titular (string): El nombre del titular de la tarjeta
            fvencimiento (string): La feha de vencimiento en la tarjeta
            ccv (string): El código de seguridad en la tarjeta
            clave (string): El nombre de clave favorita del elemento
            direccion (string): La dirección del titular de la tarjeta
            telefono (string): El número de teléfono del titular de la tarjeta
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def crear_secreto(self, nombre, secreto, clave, notas):
        ''' Crea un elemento secreto
        Parámetros:
            nombre (string): El nombre del elemento
            secreto (string): El secreto del elemento
            clave (string): El nombre de clave favorita del elemento
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_secreto(self, id, nombre, secreto, clave, notas):
        ''' Valida que se pueda crear o editar un elemento secreto
        Parámetros:
            nombre (string): El nombre del elemento
            secreto (string): El secreto del elemento
            clave (string): El nombre de clave favorita del elemento
            notas (string): Las notas del elemento
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la 
            validación o una cadena de caracteres vacía si no hay errores.
        '''
        raise NotImplementedError("Método no implementado")

    def editar_secreto(self, id, nombre, secreto, clave, notas):
        ''' Edita un elemento secreto
        Parámetros:
            nombre (string): El nombre del elemento
            secreto (string): El secreto del elemento
            clave (string): El nombre de clave favorita del elemento
            notas (string): Las notas del elemento
        '''
        raise NotImplementedError("Método no implementado")

    def crear_clave(self, nombre, clave, pista):
        ''' Crea una clave favorita
        Parámetros:
            nombre (string): El nombre de la clave favorita
            clave (string): El password o clave de la clave favorita
            pista (string): La pista para recordar la clave favorita
        '''
        if error_message := self.validar_crear_editar_clave(nombre, clave, pista):
            raise ValueError(error_message)

        clave = Clave(nombre=nombre, clave=clave, pista=pista)
        self.session.add(clave)
        self.session.commit()

    def validar_crear_editar_clave(self, nombre, clave, pista):
        ''' Valida que se pueda crear o editar una clave favorita
        Parámetros:
            nombre (string): El nombre de la clave favorita
            clave (string): El password o clae de la clave favorita
            pista (string): La pista para recordar la clave favorita
        Retorna:
            (string): El mensaje de error generado al presentarse errores en la
            validación o una cadena de caracteres vacía si no hay errores.
        '''

        # Validar que los parámetros no sean nulos
        if not nombre or not clave or not pista:
            return "Todos los campos son obligatorios"
        
        # Validar que los parámetros sean de tipo string
        if not(isinstance(nombre, str) and isinstance(clave, str) and isinstance(pista, str)):
            return "Todos los campos deben ser de tipo string"
        return ""

    def editar_clave(self, id, nombre, clave, pista):
        ''' Edita una clave favorita
        Parámetros:
            nombre (string): El nombre de la clave favorita
            clave (string): El password o clae de la clave favorita
            pista (string): La pista para recordar la clave favorita
        '''
        raise NotImplementedError("Método no implementado")

    def generar_clave(self):
        ''' Genera una clave para una clave favorita
        Retorna:
            (string): La clave generada
        '''

        especiales = r"?-*!@#$/(){}=.,;:"
        caracteres = string.ascii_letters + string.digits + especiales
        while True:
            # Generar una cadena aleatoria de longitud 8 o superior
            clave = ''.join(random.choice(caracteres) for _ in range(random.randint(8, 16)))
            # Verificar si la clave cumple los criterios
            if (any(c.islower() for c in clave) and 
                any(c.isupper() for c in clave) and 
                any(c.isdigit() for c in clave) and 
                any(c in "?-*!@#$()/{}=.,;:" for c in clave) and 
                ' ' not in clave):
                return clave

    def eliminar_clave(self, id):
        ''' Elimina una clave favorita
        Parámetros:
            id (int): El id de la clave favorita a borrar
        '''
        raise NotImplementedError("Método no implementado")

    def dar_reporte_seguridad(self):
        ''' Genera la información para el reporte de seguridad
        Retorna:
            (dict): Un mapa con los valores numéricos para las llaves logins, ids, tarjetas,
            secretos, inseguras, avencer, masdeuna y nivel que conforman el reporte
        '''
        return NotImplementedError("Método no implementado")
