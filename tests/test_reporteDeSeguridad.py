import unittest

from src.modelo.declarative_base import session

from src.modelo.elemento import Login
from src.modelo.clave import Clave

from src.logica.FachadaCajaDeSeguridad import FachadaCajaDeSeguridad

from tests import testing_utils

class ReporteDeSeguridadTestCase(unittest.TestCase):
    listaLogins: "list[Clave]" = []

    def setUp(self) -> None:
        self.fachada = FachadaCajaDeSeguridad()    
        self.session = session   
        self.data_factory = testing_utils.data_factory                 

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


    def tearDown(self) -> None:
        return super().tearDown()
