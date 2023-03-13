'''
Esta clase es la fachada con los métodos a implementar en la lógica
'''
from datetime import date, timedelta
from src.modelo.elemento import Elemento, ElementoConClave, Identificacion, Login, Secreto, Tarjeta
from src.modelo.clave import Clave
from src.modelo.caja_de_seguridad import CajaDeSeguridad
from src.modelo.declarative_base import engine, Base, session

import string
import random

class FachadaCajaDeSeguridad:

    def __init__(self):
        Base.metadata.create_all(engine)

        # Creamos la caja de seguridad si no existe
        caja = session.query(CajaDeSeguridad).first()
        if caja is None:
            caja = CajaDeSeguridad()
            session.add(caja)
            session.commit()
            

    def dar_elementos(self):
        ''' Retorna la lista de elementos de la caja de seguridad
        Retorna:
            (list): La lista con los dict o los objetos de los elementos
        '''
        elementos = session.query(Elemento).all()
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
        claves = session.query(Clave).all()
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
        return session.query(CajaDeSeguridad).first().clave_maestra

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
        self.validar_crear_editar_login(None, nombre, email, usuario, password, url, notas)
        
        if session.query(Clave).filter_by(nombre=password).first() is None:
            raise ValueError("El nombre de clave favorita no existe")

        session.add(Login(tipo="login", nombre=nombre, nota=notas, email=email, usuario=usuario, clave=password, url=url))
        session.commit()

    def validar_parametro_string(self, param):
        ''' Valida que un parámetro sea de tipo string
        Parámetros:
            param (string): El parámetro a validar
        Retorna:
            (bool): True si el parámetro es de tipo string y contiene las subcadenas de caracteres
            en args, False de lo contrario
        '''
        return isinstance(param, str)

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
        nombre_correcto = self.validar_parametro_string(nombre)
        email_correcto = self.validar_parametro_string(email)
        usuario_correcto = self.validar_parametro_string(usuario)
        password_correcto = self.validar_parametro_string(password)
        url_correcto = self.validar_parametro_string(url)
        notas_correcto = self.validar_parametro_string(notas)
        if not (nombre_correcto and email_correcto and usuario_correcto and password_correcto and url_correcto and notas_correcto) or type(id) == str:
                raise TypeError("Los parámetros no son del tipo correcto")

    def editar_login(self, id, nombre, email, usuario, password, url, notas):
        ''' Edita un elemento login
        Parámetros:
            id (int): El id del elemento a editar
            nombre (string): El nombre del elemento
            email (string): El email del elemento
            usuario (string): El usuario del login
            password (string): El nombre de clave favorita del elemento
            url (string): El URL del login
            notas (string): Las notas del elemento
        '''
        self.validar_crear_editar_login(id, nombre, email, usuario, password, url, notas)

        # Verificar que el id exista
        login = session.query(Login).filter_by(id=id).first()
        if login is None:
            raise ValueError("El id no existe")
        
        # Verificar que la clave favorita exista
        if session.query(Clave).filter_by(nombre=password).first() is None:
            raise ValueError("El nombre de clave favorita no existe")

        # Editar el login
        login.nombre = nombre
        login.email = email
        login.usuario = usuario
        login.clave = password
        login.url = url
        login.nota = notas
        session.commit()

    def crear_id(self, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        ''' Crea un elemento identificación
        Parámetros:
            nombre_elemento (string): El nombre del elemento
            numero (integer): El número del elemento
            nombre_completo (string): El nombre completo de la persona en la identificación
            fnacimiento (string): La fecha de nacimiento de la persona en la identificación
            fexpedicion (string): La fecha de expedición en la identificación
            fvencimiento (string): La feha de vencimiento en la identificación
            notas (string): Las notas del elemento
        '''
        self.validar_crear_editar_id(None, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas)
        identificacion = Identificacion(tipo = "Identificacion",
                                        nombre = nombre_elemento,
                                        nota = notas,
                                        numero = numero,
                                        nombreCompleto = nombre_completo,
                                        fechaNacimiento = fnacimiento,
                                        fechaExpedicion = fexpedicion,
                                        fechaVencimiento = fvencimiento)
        session.add(identificacion)
        session.commit()

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
        if not isinstance(nombre_elemento, str) or not isinstance(numero, int) or not isinstance(nombre_completo, str) or not isinstance(fnacimiento, date) or not isinstance(fexpedicion, date) or not isinstance(fvencimiento, date) or not isinstance (notas, str) or (id != None and not type(id) == int):
            raise TypeError("Los parámetros no son del tipo correcto")
        if len(nombre_elemento) < 3 or len(nombre_completo) < 3 or len(notas) < 3:
            raise ValueError("Los parámetros no cumplen con la longitud mínima")
        if len(nombre_elemento) > 255 or len(nombre_completo) > 255 or len(notas) > 512:
            raise ValueError("Los parámetros no cumplen con la longitud máxima")
        if (identificacion:=session.query(Identificacion).filter_by(nombre=nombre_elemento).first()) is not None:
            if id == None:
                raise ValueError("El nombre de la identificación ya existe")
            else:
                if identificacion.id != id:
                    raise ValueError("El nombre de la identificación ya existe")
        if id != None:
            if session.query(Identificacion).filter_by(id=id).first() is None:
                raise ValueError("La identificación no existe")

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
        self.validar_crear_editar_id(id, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas)
        identificacion = session.query(Identificacion).filter_by(id=id).first()
        identificacion.nombre = nombre_elemento
        identificacion.nota = notas
        identificacion.numero = numero
        identificacion.nombreCompleto = nombre_completo
        identificacion.fechaNacimiento = fnacimiento
        identificacion.fechaExpedicion = fexpedicion
        identificacion.fechaVencimiento = fvencimiento
        session.commit()



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
            raise TypeError(error_message)

        clave = Clave(nombre=nombre, clave=clave, pista=pista)
        session.add(clave)
        session.commit()

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

        if not(isinstance(nombre, str) and isinstance(clave, str) and isinstance(pista, str)):
            return "Todos los campos deben ser de tipo string"
        return ""

    def editar_clave(self, id, nombre, clave, pista):
        ''' Edita una clave favorita
        Parámetros:
            id (int): El id de la clave favorita
            nombre (string): El nombre de la clave favorita
            clave (string): El password o clave de la clave favorita
            pista (string): La pista para recordar la clave favorita
        '''
        if not isinstance(clave, str) or not isinstance(pista, str) or not isinstance(nombre, str):
            raise TypeError("Todos los campos deben ser de tipo string")
        if (len(session.query(Clave).filter(Clave.nombre == nombre).all())>0):
            raise ValueError("Ya existe una clave favorita con ese nombre.")
        if (len(nombre) < 3 or len(pista) <3 or len(clave) == 0):
            raise ValueError("El nombre de la clave favorita y la pista deben tener al menos 3 caracteres. Y la longitud de la clave debe ser mayor a 0")
        if (len(session.query(Clave).filter(Clave.id == id).all())==0):
            raise ValueError("La clave favorita referenciada no existe.")
        else: 
            clave_busqueda = session.query(Clave).filter(Clave.id == id).first()
            clave_busqueda.clave = clave
            clave_busqueda.pista = pista
            session.commit()
        

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
        clave = session.query(Clave).filter(Clave.id == id).first()
        if clave == None:
            raise ValueError("No existe una clave favorita con ese id")
        if session.query(ElementoConClave).filter(ElementoConClave.clave == clave.nombre).count() > 0:
            raise ValueError("No se puede eliminar la clave favorita porque está asociada a un elemento")
        session.delete(clave)
        session.commit()
        
    def dar_reporte_seguridad(self):
        ''' Genera la información para el reporte de seguridad
        Retorna:
            (dict): Un mapa con los valores numéricos para las llaves logins, ids, tarjetas,
            secretos, inseguras, avencer, masdeuna y nivel que conforman el reporte
        '''
        reporte = {
            'logins': 0,
            'ids': 0,
            'tarjetas': 0,
            'secretos': 0,
            'inseguras': 0,
            'avencer': 0,
            'masdeuna': 0,
            'nivel': 0
        }
        listaClaves = session.query(Clave).all()
        if len(listaClaves) != 0:
            inseguras = 0
            masdeuna = 0
            for clave in listaClaves:
                if not (any(c.islower() for c in clave.clave) and 
                        any(c.isupper() for c in clave.clave) and 
                        any(c.isdigit() for c in clave.clave) and 
                        any(c in "?-*!@#$()/{}=.,;:" for c in clave.clave) and 
                        ' ' not in clave.clave):
                    inseguras += 1
                if len(clave.elementos) > 1:
                    masdeuna += 1

            # SC: El procentaje de claves que son seguras en la lista de claves
            # SC = (total_claves - claves_inseguras) / total_claves
            sc = (len(listaClaves) - inseguras) / len(listaClaves)

            # Calcular elementos a vencer
            v = 0
            avencer = 0
            if len(session.query(Tarjeta).all()) + len(session.query(Identificacion).all()) != 0:
                
                for tarjeta in session.query(Tarjeta).all():
                    if tarjeta.fecha_vencimiento < date.today() + timedelta(days=30):
                        avencer += 1
                for identificacion in session.query(Identificacion).all():
                    if identificacion.fechaVencimiento < date.today() + timedelta(days=30):
                        avencer += 1
                v = avencer / (len(session.query(Tarjeta).all()) + len(session.query(Identificacion).all()))
            
            r = 1
            tieneMasDeUno = False
            i = 0
            while not tieneMasDeUno and i < len(listaClaves):
                if len(listaClaves[i].elementos) > 1:
                    if len(listaClaves[i].elementos) > 3:
                        r = 0
                    tieneMasDeUno = True
                i += 1
            reporte['logins'] = session.query(Login).count()
            reporte['ids'] = session.query(Identificacion).count()
            reporte['tarjetas'] = session.query(Tarjeta).count()
            reporte['secretos'] = session.query(Secreto).count()
            reporte['inseguras'] = inseguras
            reporte['avencer'] = avencer
            reporte['masdeuna'] = masdeuna
            reporte['nivel'] = sc * 0.5 + v * 0.2 + r * 0.3

        return reporte
