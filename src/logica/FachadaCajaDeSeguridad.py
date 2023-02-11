'''
Esta clase es tan sólo un mock con datos para probar la interfaz
'''
class FachadaCajaDeSeguridad:



    def dar_elementos(self):
        raise NotImplementedError("Método no implementado")

    def dar_elemento(self, id_elemento):
        raise NotImplementedError("Método no implementado")

    def dar_claves_favoritas(self):
        raise NotImplementedError("Método no implementado")

    def dar_clave_favorita(self, id_clave):
        raise NotImplementedError("Método no implementado")

    def dar_clave(self, nombre_clave):
        raise NotImplementedError("Método no implementado")

    def eliminar_elemento(self, id):
        raise NotImplementedError("Método no implementado")

    def dar_claveMaestra(self):
        raise NotImplementedError("Método no implementado")

    def crear_login(self, nombre, email, usuario, password, url, notas):
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_login(self, id, nombre, email, usuario, password, url, notas):
        raise NotImplementedError("Método no implementado")

    def editar_login(self, id, nombre, email, usuario, password, url, notas):
        raise NotImplementedError("Método no implementado")

    def crear_id(self, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_id(self, id, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        raise NotImplementedError("Método no implementado")

    def editar_id(self, id,nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        raise NotImplementedError("Método no implementado")

    def crear_tarjeta(self, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_tarjeta(self, id, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        raise NotImplementedError("Método no implementado")

    def editar_tarjeta(self, id, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        raise NotImplementedError("Método no implementado")

    def crear_secreto(self, nombre, secreto, clave, notas):
        raise NotImplementedError("Método no implementado")

    def validar_crear_editar_secreto(self, id, nombre, secreto, clave, notas):
        raise NotImplementedError("Método no implementado")

    def editar_secreto(self, id, nombre, secreto, clave, notas):
        raise NotImplementedError("Método no implementado")

    def crear_clave(self, nombre, clave, pista):
        self.claves_favoritas.append({'nombre': nombre, 'clave': clave, 'pista': pista})

    def validar_crear_editar_clave(self, nombre, clave, pista):
        return True

    def editar_clave(self,id,  nombre, clave, pista):
        raise NotImplementedError("Método no implementado")

    def generar_clave(self):
        raise NotImplementedError("Método no implementado")

    def eliminar_clave(self, id):
        raise NotImplementedError("Método no implementado")

    def dar_reporte_seguridad(self):
        return NotImplementedError("Método no implementado")
