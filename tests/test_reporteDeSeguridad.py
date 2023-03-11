import unittest

from src.modelo.declarative_base import session

from src.modelo.elemento import Login, Identificacion, Secreto, Tarjeta
from src.modelo.clave import Clave

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

from tests import testing_utils

class ReporteDeSeguridadTestCase(unittest.TestCase):
    listaLogins: "list[Clave]" = []
    listaIds: "list[Identificacion]" = []
    listaTarjetas: "list[Tarjeta]" = []
    listaSecretos: "list[Secreto]" = []
    clave: "Clave"

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()    
        self.session = session   
        self.data_factory = testing_utils.data_factory

        if session.query(Clave).count == 0:
            self.clave = testing_utils.crear_clave()
        else:
            self.clave = session.query(Clave).first()

        if session.query(Login).count() == 0:
            testing_utils.crear_5_logins_aleatorios(self.clave)
        self.listaLogins = session.query(Login).all()

        if session.query(Identificacion).count() == 0:
            testing_utils.crear_5_identificacioens_aleatorias()
        self.listaIds = session.query(Identificacion).all()

        if session.query(Tarjeta).count() == 0:
            testing_utils.crear_5_tarjetas_aleatorias(self.clave)
        self.listaTarjetas = session.query(Tarjeta).all()

        if session.query(Secreto).count() == 0:
            testing_utils.crear_5_secretos_aleatorios(self.clave)
        self.listaSecretos = session.query(Secreto).all()

        return super().setUp()
    
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
        if session.query(Clave).count() < 5:
            for _ in range(3):
                testing_utils.crear_clave(segura=True)
            for _ in range(2):
                testing_utils.crear_clave(segura=False)

        listaClaves = session.query(Clave).all()
        inseguras = 0
        print("Claves: ")
        for clave in listaClaves:
            print(clave.clave)
            if not testing_utils.verificar_clave_segura(str(clave.clave)):
                inseguras += 1

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['inseguras'], int)
        self.assertEqual(reporte['inseguras'], inseguras)

    def test_elementos_avencer(self):
        # Identificacions y tarjetas
        listaIds = session.query(Identificacion).all()
        listaTarjetas = session.query(Tarjeta).all()
        avencer = 0
        for identificacion in listaIds:
            if testing_utils.verificar_vencimiento_3_meses(identificacion.fechaVencimiento):
                avencer += 1
        for tarjeta in listaTarjetas:
            if testing_utils.verificar_vencimiento_3_meses(tarjeta.fecha_vencimiento):
                avencer += 1

        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['avencer'], int)
        self.assertEqual(reporte['avencer'], avencer)

    def tearDown(self) -> None:
        return super().tearDown()
