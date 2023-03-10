import unittest

from src.modelo.declarative_base import session

from src.modelo.elemento import Login, Identificacion
from src.modelo.clave import Clave

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

from tests import testing_utils

class ReporteDeSeguridadTestCase(unittest.TestCase):
    listaLogins: "list[Clave]" = []
    listaIds: "list[Identificacion]" = []

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()    
        self.session = session   
        self.data_factory = testing_utils.data_factory
        self.clave: Clave

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
        listaLogins = session.query(Login).all()
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['logins'], int)
        self.assertEqual(reporte['logins'], len(listaLogins))

    def test_num_ids(self):
        listaIds = session.query(Identificacion).all()
        reporte = self.fachada.dar_reporte_seguridad()
        self.assertIsInstance(reporte['ids'], int)
        self.assertEqual(reporte['ids'], len(listaIds))

    def tearDown(self) -> None:
        return super().tearDown()
