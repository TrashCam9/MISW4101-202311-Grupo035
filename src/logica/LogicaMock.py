'''
Esta clase es tan sólo un mock con datos para probar la interfaz
'''
from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad


class LogicaMock(FachadaCajaDeSeguridad):


    def __init__(self):
        #Este constructor contiene los datos falsos para probar la interfaz
        self.clave_maestra = 'clave'
        self.elementos = [{'nombre_elemento': 'Correo uniandes', 'tipo': 'Login', 'email': 'jperez@uniandes.edu.co', 'usuario': 'jperez', \
                        'clave':'La de siempre', 'url': 'correo.uniandes.edu.co', 'notas':'Se debe renovar cada 3 meses'},
                          {'nombre_elemento': 'Pasaporte', 'tipo': 'Identificación', 'numero': 'AC2028498','nombre': 'Ricardo José Rodríguez Marín', \
                           'fecha_nacimiento': '1995-01-18', 'fecha_exp': '2018-04-16', 'fecha_venc': '2028-04-16','notas': 'Expedido en Bogotá'},
                          {'nombre_elemento': 'Pasaporte', 'tipo': 'Identificación', 'numero': 'AC2028498','nombre': 'Ricardo José Rodríguez Marín', \
                           'fecha_nacimiento': '1995-01-18', 'fecha_exp': '2018-04-16', 'fecha_venc': '2028-04-16','notas': 'Expedido en Bogotá'},
                          {'nombre_elemento': 'Tarjeta Visa Banco U', 'tipo': 'Tarjeta', 'numero': '0054768934567654','titular': 'Ricardo Rodríguez', \
                           'fecha_venc': '2025-12-07', 'ccv': 234, 'clave': 'Con fechas','direccion': 'Cra 53 45-39','telefono': '+573124353456', 'notas': ''},
                          {'nombre_elemento': 'Números de polizas', 'tipo': 'Secreto', 'secreto': 'poliza de vida Colpatria: 67846838',\
                           'clave': 'Muy segura', 'notas': 'La póliza es valida si muero antes de los 75 años'}]

        self.claves_favoritas = [{'nombre':"La de siempre", 'clave':"miclavedesiempre", 'pista':'mi clave de siempre todo seguido'}, \
                                 {'nombre':"Con fechas", 'clave':"20180519", 'pista':'fecha expedicion de cedula'},\
                                 {'nombre':"Muy segura", 'clave':"Un153gur4!", 'pista':'Una segura con números!'}]

    def dar_elementos(self):
        return self.elementos.copy()

    def dar_elemento(self, id_elemento):
        return self.elementos[id_elemento].copy()

    def dar_claves_favoritas(self):
        return self.claves_favoritas.copy()

    def dar_clave_favorita(self, id_clave):
        return self.claves_favoritas[id_clave].copy()

    def dar_clave(self, nombre_clave):

        i = 0
        while i < len(self.claves_favoritas):
            if self.claves_favoritas[i]['nombre'] == nombre_clave:
                return self.claves_favoritas[i]['clave']
            i=i+1
        return "Error " + nombre_clave


    def eliminar_elemento(self, id):
        del self.elementos[id]

    def dar_claveMaestra(self):
        return self.clave_maestra

    def crear_login(self, nombre, email, usuario, password, url, notas):
        self.elementos.append({'nombre_elemento': nombre, 'tipo': 'login', 'email': email, 'usuario': usuario, \
                        'clave':password, 'url': url, 'notas': notas})

    def validar_crear_editar_login(self, id, nombre, email, usuario, password, url, notas):
        return ""

    def editar_login(self, id, nombre, email, usuario, password, url, notas):
        self.elementos[id]['nombre_elemento'] = nombre
        self.elementos[id]['tipo'] = 'Login'
        self.elementos[id]['email'] = email
        self.elementos[id]['usuario'] = usuario
        self.elementos[id]['clave'] =  password
        self.elementos[id]['url'] = url
        self.elementos[id]['notas'] = notas


    def crear_id(self, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        self.elementos.append({'nombre_elemento': nombre_elemento, 'tipo': 'Identificación', 'numero': numero,'nombre':nombre_completo , \
                           'fecha_nacimiento': fnacimiento, 'fecha_exp': fexpedicion, 'fecha_venc': fvencimiento, 'notas': notas})

    def validar_crear_editar_id(self, id, nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        return ""

    def editar_id(self, id,nombre_elemento, numero, nombre_completo, fnacimiento, fexpedicion, fvencimiento, notas):
        self.elementos[id]['nombre_elemento'] = nombre_elemento
        self.elementos[id]['tipo'] = 'Identificación'
        self.elementos[id]['numero'] = numero
        self.elementos[id]['nombre'] = nombre_completo
        self.elementos[id]['fecha_nacimiento'] =  fnacimiento
        self.elementos[id]['fecha_exp'] = fexpedicion
        self.elementos[id]['fecha_venc'] = fvencimiento
        self.elementos[id]['notas'] = notas

    def crear_tarjeta(self, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        self.elementos.append({'nombre_elemento': nombre_elemento, 'tipo': 'tarjeta', 'numero': numero, 'titular': titular, \
             'fecha_venc': fvencimiento, 'ccv': ccv, 'clave': clave, 'direccion': direccion, 'telefono': telefono,'notas': notas})

    def validar_crear_editar_tarjeta(self, id, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        return ""

    def editar_tarjeta(self, id, nombre_elemento, numero, titular, fvencimiento, ccv, clave, direccion, telefono, notas):
        self.elementos[id]['nombre_elemento'] = nombre_elemento
        self.elementos[id]['tipo'] = 'Tarjeta'
        self.elementos[id]['numero'] = numero
        self.elementos[id]['titular'] = titular
        self.elementos[id]['fecha_venc'] = fvencimiento
        self.elementos[id]['ccv'] = ccv
        self.elementos[id]['clave'] = clave
        self.elementos[id]['direccion'] = direccion
        self.elementos[id]['telefono'] = telefono
        self.elementos[id]['notas'] = notas

    def crear_secreto(self, nombre, secreto, clave, notas):
        self.elementos.append({'nombre_elemento': nombre, 'tipo': 'secreto', 'secreto': secreto, \
                               'clave': clave, 'notas': notas})

    def validar_crear_editar_secreto(self, id, nombre, secreto, clave, notas):
        return ""

    def editar_secreto(self, id, nombre, secreto, clave, notas):
        self.elementos[id]['nombre_elemento'] = nombre
        self.elementos[id]['tipo'] = 'Secreto'
        self.elementos[id]['secreto'] = secreto
        self.elementos[id]['clave'] = clave
        self.elementos[id]['notas'] = notas

    def crear_clave(self, nombre, clave, pista):
        self.claves_favoritas.append({'nombre': nombre, 'clave': clave, 'pista': pista})

    def validar_crear_editar_clave(self, nombre, clave, pista):
        return ""

    def editar_clave(self,id,  nombre, clave, pista):
        self.claves_favoritas[id]['nombre']= nombre
        self.claves_favoritas[id]['clave'] = clave
        self.claves_favoritas[id]['pista'] = pista

    def generar_clave(self):
        """
        Esta función devuelve una clave que cumple con las reglas de seguridad
        """
        return("aM2!9hg90")

    def eliminar_clave(self, id):
        del self.claves_favoritas[id]


    def dar_reporte_seguridad(self):
        return {'logins':10, 'ids':10, 'tarjetas': 5, 'secretos':2, 'inseguras':3, 'avencer': 1, 'masdeuna': 1, 'nivel': 0.6}

