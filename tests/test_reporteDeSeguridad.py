import unittest

from src.modelo.declarative_base import session

from src.modelo.elemento import Elemento, ElementoConClave, Login, Identificacion, Secreto, Tarjeta
from src.modelo.clave import Clave

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

from tests import testing_utils

class ReporteDeSeguridadTestCase(unittest.TestCase):
    listaLogins: "list[Login]" = []
    listaClaves: "list[Clave]" = []
    listaIds: "list[Identificacion]" = []
    listaTarjetas: "list[Tarjeta]" = []
    listaSecretos: "list[Secreto]" = []
    clave: "Clave"

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()     
        self.data_factory = testing_utils.data_factory

        if len(session.query(Clave).all()) == 0:
            self.clave = testing_utils.crear_clave()
        else:
            self.clave = session.query(Clave).first()

        if len(session.query(Login).all()) == 0:
            testing_utils.crear_5_logins_aleatorios(self.clave)
        self.listaLogins = session.query(Login).all()

        if len(session.query(Identificacion).all()) == 0:
            testing_utils.crear_5_identificacioens_aleatorias()
        self.listaIds = session.query(Identificacion).all()

        if len(session.query(Tarjeta).all()) == 0:
            testing_utils.crear_5_tarjetas_aleatorias(self.clave)
        self.listaTarjetas = session.query(Tarjeta).all()

        if len(session.query(Secreto).all()) == 0:
            testing_utils.crear_5_secretos_aleatorios(self.clave)
        self.listaSecretos = session.query(Secreto).all()

        self.listaClaves = session.query(Clave).all()
    
    def test_retorna_diccionario(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte, dict)

    def test_llaves_correctas(self):
        llaves = ['logins', 'ids', 'tarjetas', 'secretos', 'inseguras', 'avencer', 'masdeuna', 'nivel']
        reporte = self.fachada.dar_reporte_seguridad()
        for llave in llaves:
            self.assertIn(llave, reporte.keys())

    def test_num_logins(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['logins'], int)
        self.assertEqual(reporte['logins'], len(self.listaLogins))

    def test_num_ids(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['ids'], int)
        self.assertEqual(reporte['ids'], len(self.listaIds))

    def test_num_tarjetas(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['tarjetas'], int)
        self.assertEqual(reporte['tarjetas'], len(self.listaTarjetas))

    def test_num_secretos(self):
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['secretos'], int)
        self.assertEqual(reporte['secretos'], len(self.listaSecretos))

    def test_num_inseguras(self):
        # Crear 3 claves seguras y 2 inseguras si hay menos de 5 claves
        if len(self.listaClaves) < 5:
            for _ in range(3):
                clave = testing_utils.crear_clave(segura=True)
                self.listaClaves.append(clave)
            for _ in range(2):
                clave = testing_utils.crear_clave(segura=False)
                self.listaClaves.append(clave)

        inseguras = 0
        for clave in self.listaClaves:
            if not testing_utils.verificar_clave_segura(str(clave.clave)):
                inseguras += 1

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['inseguras'], int)
        self.assertEqual(reporte['inseguras'], inseguras)

    def test_elementos_avencer(self):
        avencer = 0
        for identificacion in self.listaIds:
            if testing_utils.verificar_vencimiento(identificacion.fechaVencimiento):
                avencer += 1
        for tarjeta in self.listaTarjetas:
            if testing_utils.verificar_vencimiento(tarjeta.fecha_vencimiento):
                avencer += 1

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['avencer'], int)
        self.assertEqual(reporte['avencer'], avencer)

    def test_clave_mas_de_un_elemento(self):
        masdeuna = 0
        for clave in self.listaClaves:
            if len(clave.elementos) > 1:
                masdeuna += 1

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['masdeuna'], int)
        self.assertEqual(reporte['masdeuna'], masdeuna)

    def test_nivel_seguridad(self):
        seguras = 0
        for clave in self.listaClaves:
            if testing_utils.verificar_clave_segura(str(clave.clave)):
                seguras += 1
        porcentajeSeguras = seguras / len(self.listaClaves)
        porcentajeNoVencidas = 0
        for identificacion in self.listaIds:
            if testing_utils.verificar_vencimiento(identificacion.fechaVencimiento):
                porcentajeNoVencidas += 1
        for tarjeta in self.listaTarjetas:
            if testing_utils.verificar_vencimiento(tarjeta.fecha_vencimiento):
                porcentajeNoVencidas += 1
        porcentajeNoVencidas /= (len(self.listaIds) + len(self.listaTarjetas))

        porcentajeR = 1
        tieneMasDeUno = False
        i = 0
        while not tieneMasDeUno and i < len(self.listaClaves):
            if len(self.listaClaves[i].elementos) > 1:
                if len(self.listaClaves[i].elementos) > 3:
                    porcentajeR = 0
                tieneMasDeUno = True
            i += 1

        nivel = porcentajeSeguras * 0.5 + porcentajeNoVencidas * 0.2 + porcentajeR * 0.3

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['nivel'], float)
        self.assertEqual(reporte['nivel'], nivel)

    def tearDown(self) -> None:
        session.query(ElementoConClave).delete()
        session.query(Elemento).delete()
        session.query(Login).delete()
        session.query(Identificacion).delete()
        session.query(Tarjeta).delete()
        session.query(Secreto).delete()
        session.query(Clave).delete()
        session.commit()
        session.close()
